from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from Parameters import *
from logistics_functions import *
from LCA_urine_model import LCA_urine_model, LCA_collection
from logistics_model import logistics_model

def Run_LCA_model(path, n_regen, n_collection, schedule, logistics):

	Logistics = logistics_model(path, n_regen, n_collection, logistics)
	distance_regeneration, distance_collection = Logistics.logistics_distances()

	Total_Energy = pd.DataFrame()
	Total_GHG = pd.DataFrame()
	Total_COST = pd.DataFrame()

	for index, row in distance_regeneration.iterrows():
	    number_of_people_per_facility= row['num_people']
	    distance_regen = row['total_dist_m']
	    truck_num = int(row['trucks_num'])
	    ENERGY, GHG, COST= LCA_urine_model(number_of_people_per_facility, distance_regen, truck_num)
	    Total_Energy=Total_Energy.append(ENERGY)
	    Total_GHG=Total_GHG.append(GHG)
	    Total_COST=Total_COST.append(COST)

	Total_Energy_regen = Total_Energy.sum()
	Total_Energy_regen=pd.DataFrame(Total_Energy_regen).T
	Total_GHG_regen = Total_GHG.sum()
	Total_GHG_regen=pd.DataFrame(Total_GHG_regen).T
	Total_COST_regen = Total_COST.sum()
	Total_COST_regen=pd.DataFrame(Total_COST_regen).T
	Total_people = distance_regeneration['num_people'].sum()

	Total_Energy_collect, Total_GHG_collect, Total_COST_collect = LCA_collection(Total_people, distance_collection)
	Total_Energy_total = Total_Energy_regen
	Total_GHG_total = Total_GHG_regen
	Total_COST_total = Total_COST_regen
	Total_Energy_total['Logistics_collect'] = Total_Energy_collect
	Total_GHG_total['Logistics_collect'] = Total_GHG_collect
	Total_COST_total['Logistics_collect'] = Total_COST_collect
	urine_total = urine_production_scaled/1000
	Total_Energy_m3=Total_Energy_total/(urine_total*365*Total_people)
	Total_Energy_m3['n_facilities'] = n_regen
	Total_GHG_m3 = Total_GHG_total/(urine_total*365*Total_people)
	Total_GHG_m3['n_facilities'] = n_regen
	Total_COST_m3 = Total_COST_total/(urine_total*365*Total_people)
	Total_COST_m3['n_facilities'] = n_regen

	return Total_Energy_m3, Total_GHG_m3, Total_COST_m3