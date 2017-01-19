from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from utils.LCA_class import resin, catridge, flow_equalization_plastic, pump_flow, regeneration, logistics, trucks, regeneration_facility, bottling


def LCA_urine_model(number_of_people_per_facility, distance_regen, truck_num, Parameters, acid_type):

	Resin = resin(number_of_people_per_facility, Parameters)

	Catridge=catridge(Parameters.catridge_diameter, Resin.mass_resin_household(), number_of_people_per_facility, Parameters)

	Flow_equalization=flow_equalization_plastic(number_of_people_per_facility, Parameters)

	Pump = pump_flow(Catridge.diameter, Catridge.catridge_length(), number_of_people_per_facility, Parameters)

	Regeneration = regeneration(Resin.mass_resin_household(), number_of_people_per_facility, Parameters, acid_type)

	Bottling = bottling(number_of_people_per_facility, Regeneration.mass_sulphuric_facility(), Parameters)

	tons = (Resin.mass_resin_household()*number_of_people_per_facility*Parameters.percent_served/Parameters.household_size + Catridge.mass_PVC())/(1000*truck_num)

	Logistics_regen = logistics(tons, distance_regen, Parameters)

	trucking = trucks(truck_num, Parameters)

	Facility_regen = regeneration_facility(number_of_people_per_facility, Parameters)

	Resin_energy_transport, Resin_GHG_transport, Resin_COST_transport = Resin.resin_transport()
	Cartridge_energy_transport, Cartridge_GHG_transport, Cartridge_COST_transport = Catridge.cartridge_transport()
	Tank_energy_transport, Tank_GHG_transport, Tank_COST_transport = Flow_equalization.tank_transport()
	Pump_energy_transport, Pump_GHG_transport, Pump_COST_transport = Pump.pump_transport()
	Acid_energy_transport, Acid_GHG_transport, Acid_COST_transport = Regeneration.acid_transport()
	Bottling_energy_transport, Bottling_GHG_transport, Bottling_COST_transport = Bottling.bottle_transport()

	Material_transport_energy = Resin_energy_transport+Cartridge_energy_transport+Tank_energy_transport+Pump_energy_transport+Acid_energy_transport+Bottling_energy_transport
	Material_transport_GHG = Resin_GHG_transport+Cartridge_GHG_transport+Tank_GHG_transport+Pump_GHG_transport+Acid_GHG_transport+Bottling_GHG_transport
	Material_transport_cost = Resin_COST_transport+Cartridge_COST_transport+Tank_COST_transport+Pump_COST_transport+Acid_COST_transport+Bottling_COST_transport

	Total_ENERGY=[Resin.resin_energy(),Catridge.PVC_energy(), Flow_equalization.plastic_energy(), Pump.pump_operating_energy(),
              Pump.pump_embodied_energy(), Regeneration.sulphuric_energy(), Logistics_regen.transportation_energy(), trucking.total_energy(), Bottling.plastic_energy(), Material_transport_energy]

	Total_GHG=[Resin.resin_GHG(), Catridge.PVC_GHG(), Flow_equalization.plastic_GHG(), Pump.pump_operating_GHG(), 
				Pump.pump_embodied_GHG(), Regeneration.sulphuric_GHG(), Logistics_regen.transportation_GHG(), trucking.total_GHG(), Bottling.plastic_GHG(), Material_transport_GHG]

	Total_COST = [Resin.resin_cost(), Catridge.PVC_cost(), Flow_equalization.plastic_cost(), Pump.pump_operating_cost(),
	           Pump.pump_embodied_cost(), Regeneration.sulphuric_cost(), Logistics_regen.transportation_cost(), trucking.total_cost(), Facility_regen.total_cost(), Bottling.plastic_cost(), Material_transport_cost]


	Total_ENERGY=pd.DataFrame(Total_ENERGY)
	Total_ENERGY_plot=Total_ENERGY.transpose()
	Total_GHG=pd.DataFrame(Total_GHG)
	Total_GHG_plot=Total_GHG.transpose()
	Total_COST=pd.DataFrame(Total_COST)
	Total_COST_plot=Total_COST.transpose()

	Total_ENERGY_plot.columns=['Resin manufacturing', 'Catridge manufacturing', 'Tank manufacturing', 'Pump operation', 'Pump manufacturing', 
	                          'Acid manufacturing', 'Logistics_regen', 'trucks manufacturing', 'Bottling', 'Material transport']

	Total_GHG_plot.columns=['Resin manufacturing', 'Catridge manufacturing', 'Tank manufacturing', 'Pump operation', 'Pump manufacturing', 
	                          'Acid manufacturing', 'Logistics_regen', 'trucks manufacturing', 'Bottling', 'Material transport']

	Total_COST_plot.columns=['Resin manufacturing', 'Catridge manufacturing', 'Tank manufacturing', 'Pump operation', 'Pump manufacturing', 
	                          'Acid manufacturing', 'Logistics_regen', 'trucks manufacturing', 'facility space', 'Bottling', 'Material transport']

	return Total_ENERGY_plot, Total_GHG_plot, Total_COST_plot


def LCA_collection(number_of_people_total, distance_collection, Parameters, acid_type):
	Resin = resin(number_of_people_total, Parameters)
	Regeneration = regeneration(Resin.mass_resin_household(), number_of_people_total, Parameters, acid_type)
	Bottling = bottling(number_of_people_total, Regeneration.mass_sulphuric_facility(), Parameters)
	tons = (Bottling.volume_ferilizer()*Parameters.fertilizer_density)/(Parameters.collection_times_per_year*1000)
	num_trucks = tons/10
	ton_truck = tons/num_trucks
	distance = distance_collection*num_trucks
	Logistics_collect = logistics(ton_truck, distance, Parameters)
	logistics_collect_energy = Logistics_collect.transportation_energy()
	logistics_collect_GHG = Logistics_collect.transportation_GHG()
	logistics_collect_cost = Logistics_collect.transportation_cost()

	return logistics_collect_energy, logistics_collect_GHG, logistics_collect_cost
