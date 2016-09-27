from __future__ import division

scaling_factor = 1
catridge_diameter = 100 #mm
PVC_lifetime = 50 #years
resin_density = 750 #g/L
resin_cost = 32 #$/kg
resin_energy_MJ_kg = 31 #MJ/kg ion exchange resin WEST
resin_GHG_kg_kg= 1 #kg/kg ion exchange resin WEST
resin_transport = 320 #miles WEST
hydraulic_conductivity = 0.00253 #m/s
resin_lifetime = 10 #years

N_urine = 7.5 #gN/L
adsorption_density = 4.9 #mmolN/g resin
molar_mass_N = 14 #g/mol

time_between_catridge_regeneration = 7 #days
urine_production = 1 #L/person-day
household_size = 4 #people
urine_production_scaled = urine_production/scaling_factor

flow_equalization_retention_time = 1  #day
tank_height = 0.5 #m
tank_thickness = 0.002 #m
steel_GHG = 1.3 #kgCO2/kg
steel_energy = 17.5 #MJ/kg
steel_sheet_mass = 186.9 #kg
steel_sheet_area = 3.72 #m2
steel_lifetime = 50 #years

transport_energy_MJ_mile=13 #MJ/km
transport_GHG_kg_mile= 1 #kgCo2/km
miles = 60 #km

truck_manuf_energy = 0.89 #MJ/$
truck_manuf_GHG = 0.06 #kgCO2/$
truck_milage = 1500000
truck_cost = 100000 # $
truck_milage_y = 20000 #miles/y
truck_manufacturing_energy = truck_manuf_energy*truck_cost/(truck_milage/truck_milage_y)
truck_manufacturing_GHG = truck_manuf_GHG*truck_cost/(truck_milage/truck_milage_y)

plastic_energy = 14.8 #MJ/$  EIOLCA plastics manufacturing
plastic_GHG = 0.904 #kg/$ EIOLCA plastics manufacturing
plastic_cost = 300  #$/m3 alibaba
plastic_density = 20 #kg/m3
plastic_lifetime = 50 #years

plastic_energy_MJ_kg = plastic_energy*plastic_cost/plastic_density
plastic_GHG_kg_kg = plastic_GHG*plastic_cost/plastic_density

motor_efficiency = 0.95 
electricity_EF = 0.083 #kgCO2/kWh
specific_weight = 1 #kN/m3
pump_lifetime = 10

sulphuric_acid_energy = 0.67 #MJ/kg Ecoinvent
sulphuric_acid_GHG = 0.12 #kg/kg Ecoinvent
acid_per_resin = 0.01 #kg/kg

collection_times_per_year = 12

