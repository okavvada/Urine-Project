from sklearn.cluster import  MiniBatchKMeans, KMeans, DBSCAN
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import pandas as pd
import math
from pylab import *
from scipy.spatial.distance import cdist
from mpl_toolkits.mplot3d import Axes3D

from logistics_functions import *


class logistics_model():
	def __init__(self, path, n_regen, n_collection):
		self.path =path
		self.n_regen = n_regen
		self.n_collection = n_collection
		self.k_means_labels_regen, self.k_means_cluster_centers_regen = self.clustering_regen()
		self.k_means_labels_collection, self.k_means_cluster_centers_collection = self.clustering_collection()

	def return_dataframe_buildings(self):
		building_virtual_buildings_df = get_virtual_buildings(self.path)
		building_SF_points=building_virtual_buildings_df[['lat_lat','lon_lon']]
		return building_SF_points


	def clustering_regen(self):
		k_means_labels_regen, k_means_cluster_centers_regen = clustering(self.return_dataframe_buildings(), self.n_regen)
		return k_means_labels_regen, k_means_cluster_centers_regen

	def clustering_collection(self):
		k_means_labels_collection, k_means_cluster_centers_collection = clustering(self.k_means_cluster_centers_regen, self.n_collection)
		return k_means_labels_collection, k_means_cluster_centers_collection

	def logistics_distances(self):
		building_virtual_buildings_df = get_virtual_buildings(self.path)
		distance_regeneration = find_distance_regeneration_scheduled(building_virtual_buildings_df, self.k_means_labels_regen)/1000

		distance_collection = find_distance_collection(self.k_means_cluster_centers_regen)/1000
		return distance_regeneration, distance_collection
