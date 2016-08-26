from sklearn.cluster import  MiniBatchKMeans, KMeans, DBSCAN
import pandas as pd
import numpy as np
import math
from scipy.spatial.distance import cdist
from math import radians, cos, sin, asin, sqrt
import doctest
from itertools import permutations
from scipy.spatial.distance import cdist


def read_buildings(path):
    building_SF = pd.read_csv(path)
    return building_SF

def get_virtual_buildings(path):
    building_SF = read_buildings(path)
    building_SF['num_people_int']=building_SF.num_people.round()
    building_SF_array=np.array(building_SF)

    building_virtual_buildings=[]
    for row in building_SF_array:
        for i in range(int(row[-1])):
            building_virtual_buildings.append(row)

    columns=['gid', 'fid_buildi', 'objname', 'numfaces', 'num_floor',
       'fid_landus', 'blklot', 'block_num', 'lot_num', 'resunits',
       'landuse', 'bldgsqft', 'yrbuilt', 'area_m2', 'county',
       'fid_tabblo', 'tractce10', 'housing10', 'lat', 'lon',
       'num_people', 'pop10', 'lat_lat', 'lon_lon', 'num_people_int']

    building_virtual_buildings_df=pd.DataFrame(building_virtual_buildings, columns=columns)
    return building_virtual_buildings_df

def find_unique(data, field):
    data_not_null=data[data[field].notnull()]
    duplicate_index=data_not_null.duplicated(field)
    unique=data_not_null[~duplicate_index]
    return unique


def clustering(dataframe, n):
    k_means = KMeans(init='k-means++', n_clusters=n)
    k_means.fit(dataframe)

    k_means_labels = k_means.labels_
    k_means_cluster_centers = k_means.cluster_centers_
    k_means_labels_unique = np.unique(k_means_labels)
    ft = (k_means_labels, k_means_cluster_centers)
    return k_means_labels, k_means_cluster_centers
    

def find_distance_regeneration(dataframe, k_means_labels, k_means_cluster_centers):
    size_all= []
    for i in range (k_means_labels.max()):
        my_members = k_means_labels==i
        unique = find_unique(dataframe[my_members],'gid')
        size_all.append(unique)

    size_all_distance=[[] for i in range(k_means_labels.max())]
    for i in range (k_means_labels.max()):
        for index, row in size_all[i].iterrows():
            harv=haversine(row['lat'],row['lon'], k_means_cluster_centers[i][0], k_means_cluster_centers[i][1])
            row['eu_dist'] = harv
            size_all_distance[i].append(row)

    total_dist_all=[]
    for i in range (k_means_labels.max()):
        df = pd.DataFrame(size_all_distance[i])
        total_dist = df['eu_dist'].sum()
        total_peop = df['num_people_int'].sum()
        all_totals = (i, total_peop, total_dist)
        total_dist_all.append(all_totals)
    totals_all_df = pd.DataFrame(total_dist_all, columns=['cluster', 'num_people', 'total_dist_m'])
    return totals_all_df


def find_distance_regeneration_scheduled(dataframe, k_means_labels):
    size_all= []
    for i in range (k_means_labels.max()):
        my_members = k_means_labels==i
        unique = find_unique(dataframe[my_members],'gid')
        size_all.append(unique)

    size_all_distance=[]
    cluster_center_meters = [[] for i in range(k_means_labels.max())]
    for i in range (k_means_labels.max()):
        for index, row in size_all[i].iterrows():
            meters = merc(row['lat_lat'], row['lon_lon'])
            cluster_center_meters[i].append(meters)
        total_distance_schedule = total_distance(optimized_travelling_salesman(cluster_center_meters[i]))
        total_peop = size_all[i]['num_people_int'].sum()
        totals = (i, total_peop, total_distance_schedule)
        size_all_distance.append(totals)
    return totals_all_df


def find_distance_collection(k_means_cluster_centers):
    cluster_center_meters = []
    for item in k_means_cluster_centers:
        meters = merc(item[0], item[1])
        cluster_center_meters.append(meters)

    collection_distance = total_distance(optimized_travelling_salesman(cluster_center_meters))
    return collection_distance


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def distance(point1, point2):
    """
    # Returns the Euclidean distance of two points in the Cartesian Plane.
    """
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5


def total_distance(points):
    """
    Returns the length of the path passing throught
    all the points in the given order.
    """
    return sum([distance(point, points[index + 1]) for index, point in enumerate(points[:-1])])


def travelling_salesman(points, start=None):
    """
    Finds the shortest route to visit all the cities by bruteforce.
    Time complexity is O(N!), so never use on long lists.
    """
    if start is None:
        start = points[0]
    return min([perm for perm in permutations(points) if perm[0] == start], key=total_distance)


def optimized_travelling_salesman(points, start=None):
    """
    As solving the problem in the brute force way is too slow,
    this function implements a simple heuristic: always
    go to the nearest city.
    Time complexity is O(N^2).
    """
    if start is None:
        start = points[0]
    must_visit = points
    path = [start]
    must_visit.remove(start)
    while must_visit:
        nearest = min(must_visit, key=lambda x: distance(path[-1], x))
        path.append(nearest)
        must_visit.remove(nearest)
    return path



def merc(lat, lon):
	"""
    Converts lat lon coordinates to mercator projection
    """
	r_major = 6378137.000
	x = r_major * math.radians(lon)
	scale = x/lon
	y = 180.0/math.pi * math.log(math.tan(math.pi/4.0 + lat * (math.pi/180.0)/2.0)) * scale
	return (x, y)