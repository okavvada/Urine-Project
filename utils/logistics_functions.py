from sklearn.cluster import  MiniBatchKMeans, KMeans, DBSCAN
import pandas as pd
import numpy as np
import math
from scipy.spatial.distance import cdist
from math import radians, cos, sin, asin, sqrt
import doctest
from itertools import permutations
from scipy.spatial.distance import cdist
import random
import warnings
from geopy.distance import vincenty


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
    k_means = MiniBatchKMeans(init='k-means++', n_clusters=n)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        k_means.fit(dataframe)

    k_means_labels = k_means.labels_
    k_means_cluster_centers = k_means.cluster_centers_
    k_means_labels_unique = np.unique(k_means_labels)
    ft = (k_means_labels, k_means_cluster_centers)
    return k_means_labels, k_means_cluster_centers
    

def find_distance_regeneration_scheduled(dataframe, k_means_labels):
    size_all= []
    for i in range (k_means_labels.max()+1):
        my_members = k_means_labels==i
        unique = find_unique(dataframe[my_members],'gid')
        size_all.append(unique)

    size_all_distance=[]
    cluster_center_meters = [[] for i in range(k_means_labels.max()+1)]
    for i in range (k_means_labels.max()+1):
        trucks = 1
        total_distance_schedule = 0
        buildings_subset = subset_buildings(size_all[i], 5)
        for index, row in buildings_subset.iterrows():
            point = (row['lat_lat'], row['lon_lon'])
            cluster_center_meters[i].append(point)
        if len(size_all[i]) != 0:
            trucks = len(cluster_center_meters[i])/100
            if trucks > 1:
                for j in range (0, len(cluster_center_meters[i]), 100):
                    total_distance_truck = total_distance(optimized_travelling_salesman(cluster_center_meters[i][j:j+100]))/1000
                    total_distance_schedule = total_distance_schedule + total_distance_truck
            else:
                total_distance_schedule = total_distance(optimized_travelling_salesman(cluster_center_meters[i]))/1000

        total_peop = size_all[i]['num_people_int'].sum()
        trucks_num = int(trucks)
        totals = (i, total_peop, trucks, total_distance_schedule)
        size_all_distance.append(totals)
    totals_all_df = pd.DataFrame(size_all_distance, columns=['cluster', 'num_people', 'trucks_num' ,'total_dist_m'])   
    return totals_all_df


def find_distance_collection(k_means_cluster_centers):
    cluster_center_meters = []
    for item in k_means_cluster_centers:
        meters = (item[0], item[1])
        cluster_center_meters.append(meters)

    collection_distance = total_distance(optimized_travelling_salesman(cluster_center_meters))/1000
    return collection_distance

def subset_buildings(dataframe, value):
    buildings_subset = []
    i = 0
    for index, row in dataframe.iterrows():
        if i%value == 0:
            buildings_subset.append(row)
            i = i + 1
        else:
            i = i + 1
    buildings_subset_df = pd.DataFrame(buildings_subset)
    return buildings_subset_df

def make_grid_points(nx, ny):
    bounding_box = [37.731273, 37.783931, -122.39532, -122.500386]
    Xgrid = make_grid(bounding_box, nx, ny)
    grid_coord=[]

    for row in Xgrid:
        xgrid=row[0]
        ygrid=row[1]
        grid_coords = (xgrid, ygrid)
        grid_coord.append(grid_coords)
    return grid_coord


def make_random_points(n_regen):
    bounding_box = [37.731273, 37.783931, -122.39532, -122.500386]
    AB = bounding_box[1] - bounding_box[0]
    BC = bounding_box[2] - bounding_box[3]
    count = 0
    random_points = []
    while count <= n_regen:
        Px = bounding_box[3] + BC*random.random()
        Py = bounding_box[0] + AB*random.random()
        random_points.append((Py, Px))
        count = count + 1
    return random_points


def make_grid(bounding_box, xcell, ycell):
    xmax, xmin, ymax, ymin = bounding_box
    xgrid = np.linspace(xmin, xmax, xcell)
    ygrid = np.linspace(ymin, ymax, ycell)
    mX, mY = np.meshgrid(xgrid, ygrid)
    ngridX = mX.reshape(xcell*ycell, 1);
    ngridY = mY.reshape(xcell*ycell, 1);
    return np.concatenate((ngridX, ngridY), axis=1)


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


def distance_lat_lon(point1, point2):
    distance = vincenty(point1, point2).meters
    return distance


def total_distance(points):
    """
    Returns the length of the path passing throught
    all the points in the given order.
    """
    return sum([distance_lat_lon(point, points[index + 1]) for index, point in enumerate(points[:-1])])


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

# Define a function that calculates the cost based on the facility size. Assumes linear increase with size.
def facility_manufacturing_curve_linear(houses):
    cost = 1.55*houses+196898
    return cost

def facility_manufacturing_curve_power(houses):
    required_area = 10+houses*0.004/1
    cost = min_facility_cost*(required_area/10)**0.6
    return cost

def facility_manufacturing_curve(houses,a):
    required_area = 10+houses*0.004/1
    cost = (a*required_area)*12
    return cost #$/y

def pareto_frontier(Xs, Ys, maxX = True, maxY = True):
# Sort the list in either ascending or descending order of X
    myList = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxX)
# Start the Pareto frontier with the first value in the sorted list
    p_front = [myList[0]]    
# Loop through the sorted list
    for pair in myList[1:]:
        if maxY: 
            if pair[1] <= p_front[-1][1]: # Look for higher values of Y…
                p_front.append(pair) # … and add them to the Pareto frontier
# Turn resulting pairs back into a list of Xs and Ys
    p_frontX = [pair[0] for pair in p_front]
    p_frontY = [pair[1] for pair in p_front]
    return p_frontX, p_frontY