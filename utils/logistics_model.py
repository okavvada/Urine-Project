from sklearn.cluster import  MiniBatchKMeans, KMeans, DBSCAN
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import pandas as pd
import math
from pylab import *
from scipy.spatial.distance import cdist
from scipy import spatial
from mpl_toolkits.mplot3d import Axes3D
import time

from utils.logistics_functions import *
from utils.Parameters_class import Parameters_values

Parameters = Parameters_values()

class logistics_model():
	def __init__(self, path, n_regen, n_collection, logistics):
		self.path =path
		self.n_regen = n_regen
		self.n_collection = n_collection
		self.logistics = logistics

	def return_dataframe_buildings(self):
		building_virtual_buildings_df = pd.read_csv(self.path)
		building_SF_points=building_virtual_buildings_df[['lat_lat','lon_lon']]
		return building_SF_points

	def clustering_regen(self):
		k_means_labels_regen, k_means_cluster_centers_regen = clustering(self.return_dataframe_buildings(), self.n_regen)
		return k_means_labels_regen, k_means_cluster_centers_regen

	def clustering_regen_grid(self):
		building_SF_points = self.return_dataframe_buildings()
		nx = int(sqrt(self.n_regen))
		ny = int(ceil(self.n_regen/nx))
		cluster_centers_regen = make_grid_points(self.n_regen, nx, ny)
		cluster_centers_regen_df=pd.DataFrame(cluster_centers_regen, columns=['lat', 'lon'])
		tree = spatial.KDTree(list(zip(cluster_centers_regen_df['lat'], cluster_centers_regen_df['lon'])))
		building_SF_points_array = list(zip(building_SF_points['lat_lat'],building_SF_points['lon_lon']))
		k_means_labels_regen = tree.query(building_SF_points_array)[1]

		return k_means_labels_regen, cluster_centers_regen

	def clustering_regen_random(self):
		building_SF_points = self.return_dataframe_buildings()
		cluster_centers_regen = make_random_points(self.n_regen)
		cluster_centers_regen_df=pd.DataFrame(cluster_centers_regen, columns=['lat', 'lon'])
		tree = spatial.KDTree(list(zip(cluster_centers_regen_df['lat'], cluster_centers_regen_df['lon'])))
		building_SF_points_array = list(zip(building_SF_points['lat_lat'],building_SF_points['lon_lon']))
		k_means_labels_regen = tree.query(building_SF_points_array)[1]

		return k_means_labels_regen, cluster_centers_regen

	def clustering_collection(self, k_means_cluster_centers_regen):
		k_means_labels_collection, k_means_cluster_centers_collection = clustering(k_means_cluster_centers_regen, self.n_collection)
		return k_means_labels_collection, k_means_cluster_centers_collection

	def logistics_distances(self):
		building_virtual_buildings_df = pd.read_csv(self.path)

		if self.logistics == 'optimal':
			k_means_labels_regen, k_means_cluster_centers_regen = self.clustering_regen()

		elif self.logistics == 'grid':
			k_means_labels_regen, k_means_cluster_centers_regen = self.clustering_regen_grid()

		elif self.logistics == 'random':
			k_means_labels_regen, k_means_cluster_centers_regen = self.clustering_regen_random()

		else:
			print ("Error type of logistics was not specified")

		time_now = time.time()

		print ("Start calculating distances...")
		distance_regeneration = find_distance_regeneration_scheduled(building_virtual_buildings_df, k_means_labels_regen)
		distance_regeneration['total_dist_m'] = distance_regeneration['total_dist_m']*365/Parameters.time_between_catridge_regeneration
		time_end = time.time() - time_now
		print ("calc distances took time %s" %time_end)


		k_means_labels_collection, k_means_cluster_centers_collection = self.clustering_collection(k_means_cluster_centers_regen)

		distance_collection = find_distance_collection(k_means_cluster_centers_regen)*Parameters.collection_times_per_year
		print ('dist collec = {}'.format(distance_collection))
		return distance_regeneration, distance_collection

