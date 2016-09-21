from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from Parameters import *
from LCA_class import resin, catridge, flow_equalization_plastic,pump_flow, regeneration, logistics, trucks

def LCA_urine_model(number_of_people_per_facility, distance_regen, truck_num):

	Resin = resin(number_of_people_per_facility)
	resin_energy = Resin.total_energy()
	resin_GHG = Resin.total_GHG()

	Catridge=catridge(catridge_diameter, Resin.mass_resin_household(), number_of_people_per_facility)
	catridge_energy = Catridge.total_energy()
	catridge_GHG = Catridge.total_GHG()

	Flow_equalization=flow_equalization_plastic(number_of_people_per_facility)
	flow_equalization_energy = Flow_equalization.total_energy()
	flow_equalization_GHG = Flow_equalization.total_GHG()

	Pump = pump_flow(Catridge.diameter, Catridge.catridge_length(), number_of_people_per_facility)
	pump_energy = Resin.total_energy()
	pump_GHG = Resin.total_GHG()

	Regeneration = regeneration(Resin.mass_resin_household(), acid_per_resin, number_of_people_per_facility)
	regeneration_energy = Regeneration.total_energy()
	regeneration_GHG = Regeneration.total_GHG()

	Logistics_regen = logistics(distance_regen)
	logistics_energy = Logistics_regen.total_energy()
	logistics_GHG = Logistics_regen.total_GHG()

	trucking = trucks(truck_num)
	trucking_energy = trucking.total_energy()
	trucking_GHG = trucking.total_GHG()


	Total_ENERGY=[Resin.resin_energy(),Resin.transportation_energy(),Catridge.PVC_energy(),Catridge.transportation_energy(),
              Flow_equalization.plastic_energy(),Flow_equalization.transportation_energy(),Pump.pump_operating_energy(),
              Pump.pump_embodied_energy(),Pump.transportation_energy(), Regeneration.sulphuric_energy(), 
              Regeneration.transportation_energy(), Logistics_regen.transportation_energy(), trucking.total_energy()]

	Total_GHG=[Resin.resin_GHG(),Resin.transportation_GHG(),Catridge.PVC_GHG(),Catridge.transportation_GHG(),
	           Flow_equalization.plastic_GHG(),Flow_equalization.transportation_GHG(),Pump.pump_operating_GHG(),
	           Pump.pump_embodied_GHG(),Pump.transportation_GHG(), Regeneration.sulphuric_GHG(), 
	              Regeneration.transportation_GHG(), Logistics_regen.transportation_GHG(), trucking.total_GHG()]


	Total_ENERGY=pd.DataFrame(Total_ENERGY)
	Total_ENERGY_plot=Total_ENERGY.transpose()
	Total_GHG=pd.DataFrame(Total_GHG)
	Total_GHG_plot=Total_GHG.transpose()

	Total_ENERGY_plot.columns=['Resin manufacturing','Resin transport', 'Catridge manufacturing', 'Catridge transport', 
	                           'Tank manufacturing', 'Tank transport', 'Pump operation', 'Pump manufacturing', 'Pump transport', 
	                          'Acid manufacturing', 'Acid transport', 'Logistics_regen', 'trucks manufacturing']
	Total_GHG_plot.columns=['Resin manufacturing','Resin transport', 'Catridge manufacturing', 'Catridge transport', 
	                        'Tank manufacturing', 'Tank transport', 'Pump operation', 'Pump manufacturing', 'Pump transport',
	                       'Acid manufacturing', 'Acid transport', 'Logistics_regen', 'trucks manufacturing']

	return Total_ENERGY_plot, Total_GHG_plot


def LCA_collection(number_of_people_total, distance_collection):
	Logistics_collect = logistics(distance_collection)
	logistics_collect_energy = Logistics_collect.total_energy()
	logistics_collect_GHG = Logistics_collect.total_GHG()

	Total_ENERGY = logistics_collect_energy
	Total_GHG=logistics_collect_GHG
	return Total_ENERGY, Total_GHG
