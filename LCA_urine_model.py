from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from Parameters import *
from LCA_class import resin, catridge, flow_equalization_plastic,pump_flow, regeneration, logistics

def LCA_urine_model(number_of_houses_per_facility, distance_regen, distance_collection):
	
	distance_logistics_regen = (distance_regen)*365/time_between_catridge_regeneration
	distance_logistics_collection = distance_collection*collection_times_per_year

	Resin = resin(household_size, number_of_houses_per_facility)
	resin_energy = Resin.total_energy()
	resin_GHG = Resin.total_GHG()

	Catridge=catridge(catridge_diameter, Resin.mass_resin_household(), number_of_houses_per_facility)
	catridge_energy = Catridge.total_energy()
	catridge_GHG = Catridge.total_GHG()

	Flow_equalization=flow_equalization_plastic(household_size, number_of_houses_per_facility)
	flow_equalization_energy = Flow_equalization.total_energy()
	flow_equalization_GHG = Flow_equalization.total_GHG()

	Pump = pump_flow(household_size, Catridge.diameter, Catridge.catridge_length(), number_of_houses_per_facility)
	pump_energy = Resin.total_energy()
	pump_GHG = Resin.total_GHG()

	Regeneration = regeneration(Resin.mass_resin_household(), acid_per_resin)
	regeneration_energy = Regeneration.total_energy()
	regeneration_GHG = Regeneration.total_GHG()

	Logistics_regen = logistics(distance_logistics_regen)
	logistics_energy = Logistics_regen.total_energy()
	logistics_GHG = Logistics_regen.total_GHG()

	Logistics_collect = logistics(distance_logistics_collection)
	logistics_collect_energy = Logistics_collect.total_energy()
	logistics_collect_GHG = Logistics_collect.total_GHG()


	Total_ENERGY=[Resin.resin_energy(),Resin.transportation_energy(),Catridge.PVC_energy(),Catridge.transportation_energy(),
              Flow_equalization.plastic_energy(),Flow_equalization.transportation_energy(),Pump.pump_operating_energy(),
              Pump.pump_embodied_energy(),Pump.transportation_energy(), Regeneration.sulphuric_energy(), 
              Regeneration.transportation_energy(), Logistics_regen.transportation_energy(), Logistics_collect.transportation_energy()]

	Total_GHG=[Resin.resin_GHG(),Resin.transportation_GHG(),Catridge.PVC_GHG(),Catridge.transportation_GHG(),
	           Flow_equalization.plastic_GHG(),Flow_equalization.transportation_GHG(),Pump.pump_operating_GHG(),
	           Pump.pump_embodied_GHG(),Pump.transportation_GHG(), Regeneration.sulphuric_GHG(), 
	              Regeneration.transportation_GHG(), Logistics_regen.transportation_GHG(), Logistics_collect.transportation_GHG()]


	Total_ENERGY=pd.DataFrame(Total_ENERGY)
	Total_ENERGY = Total_ENERGY/(household_size*urine_production_scaled*365*number_of_houses_per_facility)
	Total_ENERGY_plot=Total_ENERGY.transpose()
	Total_GHG=pd.DataFrame(Total_GHG)
	Total_GHG=Total_GHG/(household_size*urine_production_scaled*365*number_of_houses_per_facility)
	Total_GHG_plot=Total_GHG.transpose()
	Total_ENERGY_plot.columns=['Resin manufacturing','Resin transport', 'Catridge manufacturing', 'Catridge transport', 
	                           'Tank manufacturing', 'Tank transport', 'Pump operation', 'Pump manufacturing', 'Pump transport', 
	                          'Acid manufacturing', 'Acid transport', 'Logistics_regen', 'Logistics_collect']
	Total_GHG_plot.columns=['Resin manufacturing','Resin transport', 'Catridge manufacturing', 'Catridge transport', 
	                        'Tank manufacturing', 'Tank transport', 'Pump operation', 'Pump manufacturing', 'Pump transport',
	                       'Acid manufacturing', 'Acid transport', 'Logistics_regen', 'Logistics_collect']

	return Total_ENERGY_plot, Total_GHG_plot
