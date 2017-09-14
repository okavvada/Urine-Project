from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from utils.Parameters_class import Parameters_values
from utils.logistics_functions import *
from utils.LCA_urine_model import LCA_urine_model, LCA_collection, fertilizer_offset
from utils.logistics_model import logistics_model

def Run_LCA_model(path, n_regen, n_collection, logistics, analysis, acid_type, scenario, parameter = None, direction = None):
	Parameters = Parameters_values()

	if analysis == 'Normal':
		Logistics = logistics_model(path, n_regen, n_collection, logistics, scenario)
		distance_regeneration, distance_collection = Logistics.logistics_distances()

	if analysis == 'Uncertainty':
		distance_regeneration = pd.read_csv('results//distance_regeneration_20.csv')
		distance_collection = 502
		perturb = Parameters.uncertainty()
		Parameters = perturb
	if analysis == 'Sensitivity':
		distance_regeneration = pd.read_csv('results//distance_regeneration_20.csv')
		distance_collection = 502
		perturb = Parameters.sensitivity(parameter, direction)
		Parameters = perturb

	Total_Energy = pd.DataFrame()
	Total_GHG = pd.DataFrame()
	Total_COST = pd.DataFrame()

	trucks = 0

	for index, row in distance_regeneration.iterrows():
	    number_of_people_per_facility = row['num_people']
	    distance_regen = row['total_dist_m_y']
	    truck_num = np.ceil(row['trucks_num'])
	    ENERGY, GHG, COST = LCA_urine_model(number_of_people_per_facility, distance_regen, truck_num, Parameters, acid_type, scenario)
	    Total_Energy = Total_Energy.append(ENERGY)
	    Total_GHG = Total_GHG.append(GHG)
	    Total_COST = Total_COST.append(COST)
	    trucks += truck_num

	Total_Energy_regen = Total_Energy.sum()
	Total_Energy_regen=pd.DataFrame(Total_Energy_regen).T
	Total_GHG_regen = Total_GHG.sum()
	Total_GHG_regen=pd.DataFrame(Total_GHG_regen).T
	Total_COST_regen = Total_COST.sum()
	Total_COST_regen=pd.DataFrame(Total_COST_regen).T
	Total_people = distance_regeneration['num_people'].sum()
	Total_people_served = Total_people*Parameters.percent_served

	if scenario == 'Resin':

		Total_Energy_collect, Total_GHG_collect, Total_COST_collect = LCA_collection(Total_people_served, distance_collection, Parameters, acid_type)
		energy_offset, GHG_offset, Cost_offset = fertilizer_offset(Total_people_served, Parameters, acid_type)

		Total_Energy_total = Total_Energy_regen
		Total_GHG_total = Total_GHG_regen
		Total_COST_total = Total_COST_regen

		Total_Energy_total['Fertilizer transport'] = Total_Energy_collect
		Total_GHG_total['Fertilizer transport'] = Total_GHG_collect
		Total_COST_total['Fertilizer transport'] = Total_COST_collect

		Total_Energy_total['Fertilizer offset'] = energy_offset
		Total_GHG_total['Fertilizer offset'] = GHG_offset
		Total_COST_total['Fertilizer offset'] = Cost_offset

	if scenario == 'Urine':

		Total_Energy_total = Total_Energy_regen
		Total_GHG_total = Total_GHG_regen
		Total_COST_total = Total_COST_regen

	employee_number_per_facility = employees_number(Total_people_served, n_regen)

	Total_COST_total['Labor'] = trucks*Parameters.wages_truck*200 + n_regen*employee_number_per_facility*Parameters.wages_facility*200
	Total_COST_total['Labor_trucks'] = trucks*Parameters.wages_truck*200
	Total_COST_total['Labor_facility'] = n_regen*employee_number_per_facility*Parameters.wages_facility*200

	Total_Energy_m3=Total_Energy_total/(3.6*Parameters.urine_production*365*Total_people_served/1000)
	Total_Energy_m3['n_facilities'] = n_regen
	Total_GHG_m3 = Total_GHG_total/(Parameters.urine_production*365*Total_people_served/1000)
	Total_GHG_m3['n_facilities'] = n_regen
	Total_COST_m3 = Total_COST_total/(Parameters.urine_production*365*Total_people_served/1000)
	Total_COST_m3['n_facilities'] = n_regen

	return Total_Energy_m3, Total_GHG_m3, Total_COST_m3, Parameters
