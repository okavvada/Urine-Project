from __future__ import division

scaling_factor = 1
catridge_diameter = 100 #mm
PVC_lifetime = 50 #years
resin_density = 750 #g/L
resin_cost_kg = 3.2 #$/kg #### CHECK with Will
resin_energy_MJ_kg = 31 #MJ/kg ion exchange resin WEST
resin_GHG_kg_kg= 1 #kg/kg ion exchange resin WEST
resin_transport = 3862 #km WEST
hydraulic_conductivity = 0.00253 #m/s
resin_lifetime = 10 #years ### CHECK with Will

N_urine = 7.5 #gN/L
adsorption_density = 4.9 #mmolN/g resin
molar_mass_N = 14 #g/mol

time_between_catridge_regeneration = 7 #days
time_for_regeneration = 1.5 #h/day
urine_production = 1 #L/person-day
household_size = 4 #people

flow_equalization_retention_time = 1  #day
tank_height = 0.5 #m
tank_thickness = 0.002 #m
steel_GHG = 1.3 #kgCO2/kg
steel_energy = 17.5 #MJ/kg
steel_sheet_mass = 186.9 #kg
steel_sheet_area = 3.72 #m2
steel_lifetime = 50 #years

transport_energy_MJ_km=13 #MJ/km
transport_GHG_kg_km= 1 #kgCo2/km
diesel_cost = 2.2 #$/gal (EIA)
truck_mpg = 10 
transport_cost_km = diesel_cost/(truck_mpg*1.6) # $/km
km = 60 #km

truck_manuf_energy = 0.89 #MJ/$
truck_manuf_GHG = 0.06 #kgCO2/$
truck_milage = 1500000
truck_cost = 70000 # $
truck_milage_y = 20000 #miles/y
truck_manufacturing_energy = truck_manuf_energy*truck_cost/(truck_milage/truck_milage_y) #MJ/y
truck_manufacturing_GHG = truck_manuf_GHG*truck_cost/(truck_milage/truck_milage_y) #kg/y
truck_cost_y = truck_cost/(truck_milage/truck_milage_y) #$/y

plastic_energy = 14.8 #MJ/$  EIOLCA plastics manufacturing
plastic_GHG = 0.904 #kg/$ EIOLCA plastics manufacturing
plastic_cost = 300  #$/m3 alibaba
plastic_density = 20 #kg/m3
plastic_lifetime = 50 #years

plastic_energy_MJ_kg = plastic_energy*plastic_cost/plastic_density
plastic_GHG_kg_kg = plastic_GHG*plastic_cost/plastic_density
plastic_cost_kg = plastic_cost/plastic_density

motor_efficiency = 0.95 
electricity_EF = 0.083 #kgCO2/kWh
electricity_cost = 0.1 # $/kWh
specific_weight = 1 #kN/m3
pump_lifetime = 10

sulphuric_acid_energy = 0.67 #MJ/kg Ecoinvent
sulphuric_acid_GHG = 0.12 #kg/kg Ecoinvent
acid_per_resin = 0.01#kg/kg ### CHECK
# acid_per_resin = acid_per_solution*solution_per_resin*acid_density/(resin_density)
acid_per_solution = 0.0065  #L/L #### CHECK with Will
solution_per_resin = 1  #L/L #### CHECK with Will
sulphuric_acid_cost = 0.5 #$/kg  #### CHECK with Will
acid_flow_rate = 360 # ml/min
acid_flow_rate_m3_s = acid_flow_rate/(60*1000*1000) #m3/s
acid_transport = 193 #km WEST
acid_density = 1840 #g/L

collection_times_per_year = 12

facility_manufacturing_energy = 0 #MJ
facility_manufacturing_GHG = 0 #kg
facility_lifetime = 50 # y

# Define a function that calculates the cost based on the facility size. Assumes linear increase with size.
def facility_manufacturing_curve(houses):
	cost = 1.55*houses+196898
	return cost

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

