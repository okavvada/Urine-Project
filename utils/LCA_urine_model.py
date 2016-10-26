from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from utils.LCA_class import resin, catridge, flow_equalization_plastic, pump_flow, regeneration, logistics, trucks, regeneration_facility, material_transport, bottling


def LCA_urine_model(number_of_people_per_facility, distance_regen, truck_num, Parameters):

	Resin = resin(number_of_people_per_facility, Parameters)

	Catridge=catridge(Parameters.catridge_diameter, Resin.mass_resin_household(), number_of_people_per_facility, Parameters)

	Flow_equalization=flow_equalization_plastic(number_of_people_per_facility, Parameters)

	Pump = pump_flow(Catridge.diameter, Catridge.catridge_length(), number_of_people_per_facility, Parameters)

	Regeneration = regeneration(Resin.mass_resin_household(), number_of_people_per_facility, Parameters)

	Bottling = bottling(Regeneration.mass_sulphuric_facility(), Parameters)

	Logistics_regen = logistics(distance_regen, Parameters)

	trucking = trucks(truck_num, Parameters)

	Facility_regen = regeneration_facility(number_of_people_per_facility, Parameters)


	Total_ENERGY=[Resin.resin_energy(),Catridge.PVC_energy(), Flow_equalization.plastic_energy(), Pump.pump_operating_energy(),
              Pump.pump_embodied_energy(), Regeneration.sulphuric_energy(), Logistics_regen.transportation_energy(), trucking.total_energy(), Bottling.plastic_energy()]

	Total_GHG=[Resin.resin_GHG(), Catridge.PVC_GHG(), Flow_equalization.plastic_GHG(), Pump.pump_operating_GHG(), 
				Pump.pump_embodied_GHG(), Regeneration.sulphuric_GHG(), Logistics_regen.transportation_GHG(), trucking.total_GHG(), Bottling.plastic_GHG()]

	Total_COST = [Resin.resin_cost(), Catridge.PVC_cost(), Flow_equalization.plastic_cost(), Pump.pump_operating_cost(),
	           Pump.pump_embodied_cost(), Regeneration.sulphuric_cost(), Logistics_regen.transportation_cost(), trucking.total_cost(), Facility_regen.total_cost(), Bottling.plastic_cost()]


	Total_ENERGY=pd.DataFrame(Total_ENERGY)
	Total_ENERGY_plot=Total_ENERGY.transpose()
	Total_GHG=pd.DataFrame(Total_GHG)
	Total_GHG_plot=Total_GHG.transpose()
	Total_COST=pd.DataFrame(Total_COST)
	Total_COST_plot=Total_COST.transpose()

	Total_ENERGY_plot.columns=['Resin manufacturing', 'Catridge manufacturing', 'Tank manufacturing', 'Pump operation', 'Pump manufacturing', 
	                          'Acid manufacturing', 'Logistics_regen', 'trucks manufacturing', 'Bottling']

	Total_GHG_plot.columns=['Resin manufacturing', 'Catridge manufacturing', 'Tank manufacturing', 'Pump operation', 'Pump manufacturing', 
	                          'Acid manufacturing', 'Logistics_regen', 'trucks manufacturing', 'Bottling']

	Total_COST_plot.columns=['Resin manufacturing', 'Catridge manufacturing', 'Tank manufacturing', 'Pump operation', 'Pump manufacturing', 
	                          'Acid manufacturing', 'Logistics_regen', 'trucks manufacturing', 'facility space', 'Bottling']

	return Total_ENERGY_plot, Total_GHG_plot, Total_COST_plot


def LCA_collection(number_of_people_total, distance_collection, Parameters):
	Logistics_collect = logistics(distance_collection, Parameters)
	logistics_collect_energy = Logistics_collect.transportation_energy()
	logistics_collect_GHG = Logistics_collect.transportation_GHG()
	logistics_collect_cost = Logistics_collect.transportation_cost()

	return logistics_collect_energy, logistics_collect_GHG, logistics_collect_cost


def material_transportation(transport_dist, lifetime, Parameters):
	transport = material_transport(transport_dist, lifetime, Parameters)
	transport_energy = transport.transportation_energy()
	transport_GHG = transport.transportation_GHG()
	transport_cost = transport.transportation_cost()

	return transport_energy, transport_GHG, transport_cost
