from __future__ import division
import numpy as np


class Parameters_values():
    def __init__(self):
        self.percent_served = 0.5 #percent of pop served
        self.catridge_diameter = 12 #cm
        self.catridge_thickness = 0.005 #m
        self.catridge_lifetime = 10
        self.PVC_lifetime = 50 #years
        self.resin_density = 750 #g/L
        self.resin_cost_kg = 2 #$/kg #### CHECK with Will
        self.resin_energy_MJ_kg = 30 #MJ/kg ion exchange resin EcoInvent
        self.resin_GHG_kg_kg= 1 #kg/kg ion exchange resin Econinvent
        self.resin_transport = 300 #km 
        self.porosity = 0.61
        self.hydraulic_conductivity = 0.00253 #m/s
        self.resin_lifetime = 5 #years ### CHECK with Will
        self.N_urine = 7.5 #gN/L
        self.urine_density = 1 #kg/L
        self.adsorption_density = 4.9 #mmolN/g resin
        self.molar_mass_N = 14.0067 #g/mol
        self.time_between_catridge_regeneration = 7 #days
        self.time_between_catridge_regeneration_2 = 7
        self.time_for_regeneration = 1.5 #h/day
        self.urine_production = 1.42 #L/person-day
        self.household_size = 2.54/1.5#people/cartridge
        self.flow_equalization_retention_time = 1  #day
        self.tank_height = 0.5 #m
        self.tank_thickness = 0.002 #m
        self.steel_GHG = 1.3 #kgCO2/kg
        self.steel_energy = 17.5 #MJ/kg
        self.steel_sheet_mass = 186.9 #kg
        self.steel_sheet_area = 3.72 #m2
        self.steel_lifetime = 50 #years
        self.diesel_cost = 2.3 #$/gal (EIA)
        self.truck_mpg = 10 
        self.truck_payload = 4.7 #tons
        self.transport_cost_km = 0.08 # $/ton-km
        self.km = 60 #km
        self.transport_GHG_kg_km= 0.410 #kgCo2/ton-km Taptich
        self.carbon_content = 10 #kgco2/gal d (EIA)
        self.energy_content = 46.8 #MJ/kgd (EIA)
        self.diesel_density = 0.832 #kg/L
        #self.transport_energy_MJ_km = 2.7 #MJ/ton-km #Mathews
        self.transport_energy_MJ_km = self.transport_GHG_kg_km/self.carbon_content*3.6*self.energy_content*self.diesel_density #MJ/ton-km
        self.truck_manuf_energy = 0.89 #MJ/$
        self.truck_manuf_GHG = 0.06 #kgCO2/$
        self.truck_milage = 1500000
        self.truck_cost = 70000 # $
        self.truck_milage_y = 20000 #miles/y
        self.truck_manufacturing_energy = self.truck_manuf_energy*self.truck_cost/(self.truck_milage/self.truck_milage_y) #MJ/y
        self.truck_manufacturing_GHG = self.truck_manuf_GHG*self.truck_cost/(self.truck_milage/self.truck_milage_y) #kg/y
        self.truck_cost_y = self.truck_cost/(self.truck_milage/self.truck_milage_y) #$/y
        self.truck_payload = 3.5 #tons
        self.train_energy_MJ_km = 0.3 #MJ/ton-km #Mathews
        self.train_GHG_kg_km = 0.025 #kgCo2/ton-km
        self.train_cost_km = 0.01 # $/ton-km
        self.plastic_energy = 14.8 #MJ/$  EIOLCA plastics manufacturing
        self.plastic_GHG = 0.904 #kg/$ EIOLCA plastics manufacturing
        self.plastic_cost = 300  #$/m3 alibaba
        self.plastic_density = 20 #kg/m3
        self.plastic_lifetime = 50 #years
        self.fiberglass_density = 1.5 #kg/L
        self.fiberglass_lifetime = 10 #years
        self.plastic_energy_MJ_kg = self.plastic_energy*self.plastic_cost/self.plastic_density
        self.plastic_GHG_kg_kg = self.plastic_GHG*self.plastic_cost/self.plastic_density
        self.plastic_cost_kg = self.plastic_cost/self.plastic_density
        self.fiberglass_energy_MJ_kg = 36 #Ecoinvent
        self.fiberglass_GHG_kg_kg = 2.9 #Ecoinvent
        self.fiberglass_cost = 1955 # $/m3 Boyer
        self.fiberglass_cost_kg = self.fiberglass_cost/(1000*self.fiberglass_density)
        self.motor_efficiency = 0.95 
        self.electricity_EF = 0.083 #kgCO2/kWh
        self.electricity_cost = 0.1 # $/kWh
        self.specific_weight = 1 #kN/m3
        self.pump_lifetime = 10

        self.sulphuric_acid_energy = 1.7 #MJ/kg Ecoinvent
        self.sulphuric_acid_GHG = 0.12 #kg/kg Ecoinvent
        self.acid_density = 1840 #g/L
        self.acid_per_resin_L_g = 0.000135  #L/g 
        self.acid_per_resin = self.acid_per_resin_L_g*self.acid_density #g/g
        self.sulphuric_acid_cost = 0.27 #$/kg
        self.acid_flow_rate = 22.5 # mL/min
        self.acid_flow_rate_m3_s = self.acid_flow_rate/(60*1000*1000) #m3/s
        
        self.Nitricacid_density = 1510 #g/L
        self.Nitricacid_per_resin_L_L = 0.23 # L/L
        self.Nitricacid_per_resin = self.Nitricacid_per_resin_L_L*self.Nitricacid_density/self.resin_density #g/g
        self.Nitric_acid_energy = 12.6 #MJ/kg Ecoinvent
        self.Nitric_acid_GHG = 3.1 #kg/kg Ecoinvent
        self.Nitric_acid_cost = 0.2867 #$/kg 

        self.Hydrochloricacid_density = 1000 #g/L
        self.Hydrochloricacid_per_resin_L_L = 0.3 # L/L
        self.Hydrochloricacid_per_resin = self.Hydrochloricacid_per_resin_L_L*self.Hydrochloricacid_density/self.resin_density #g/g
        self.Hydrochloric_acid_energy = 11.2 #MJ/kg Ecoinvent
        self.Hydrochloric_acid_GHG = 0.82 #kg/kg Ecoinvent
        self.Hydrochloric_acid_cost = 0.285 #$/kg 

        self.Sodiumchloride_per_resin_g_L = 214 # g/L
        self.Sodiumchloride_per_resin = self.Sodiumchloride_per_resin_g_L/self.resin_density #g/g
        self.Sodiumchloride_energy = 2.1 #MJ/kg Ecoinvent
        self.Sodiumchloride_GHG = 0.18 #kg/kg Ecoinvent
        self.Sodiumchloride_cost = 0.0695 #$/kg 

        self.acid_transport = 193 #km WEST
        self.volume_fertilizer_per_acid = 1 #L/L 
        self.mass_N_per_cartridge = 0.12849 #kgN per cartridge
        self.fertilizer_density = 1.8 #kg/L 
        self.volume_bottle = 1 #L
        self.bottle_height = 0.3
        self.bottle_thickness = 0.001 #m
        self.bottle_lifetime = 10 #y
        self.collection_times_per_year = 52
        self.facility_manufacturing_energy = 0 #MJ
        self.facility_manufacturing_GHG = 0 #kg
        self.facility_lifetime = 50 # y
        self.min_facility_cost = 100000
        self.facility_cost_regression = 220.2
        self.trucks_serving = 200

        self.ureafertilizer_molar_mass = 0.132 #kg/mol
        self.conventional_fertilizer_molar_mass = 0.080 #kg/mol
        self.fertilizer_energy = 55 #MJ/kgN Ecoinvent ammonium nitrate
        self.fertilizer_GHG = 8.5 #kg/kgN Ecoinvent ammonium nitrate
        self.fertilizer_cost = 1.7 #$/kgN  #https://www.noble.org/news/publications/ag-news-and-views/2012/june/summer-nitrogen-sources---which-is-best/
        self.kgN_per_kg_fertilizer = 0.35  #
        self.wages_truck = 128 #$/day
        self.wages_facility = 296 #$/day
        self.num_employees = 2 #per facility


    def max_min(self):
        maxmin = {
        'percent_served_max': 80,
        'percent_served_min':30,
        'PVC_lifetime_max': 80,
        'PVC_lifetime_min': 20,
        'resin_cost_kg_max': 1.2*self.resin_cost_kg,
        'resin_cost_kg_min': 0.8*self.resin_cost_kg ,
        'resin_energy_MJ_kg_max': 1.2*self.resin_energy_MJ_kg,
        'resin_energy_MJ_kg_min': 0.8*self.resin_energy_MJ_kg ,
        'resin_GHG_kg_kg_max': 1.2*self.resin_GHG_kg_kg,
        'resin_GHG_kg_kg_min': 0.8*self.resin_GHG_kg_kg,
        'resin_transport_max':1.2*self.resin_transport,
        'resin_transport_min': 0.8*self.resin_transport,
        'N_urine_max':9,  
        'N_urine_min':4, 
        'hydraulic_conductivity_max': 0.00289,
        'hydraulic_conductivity_min': 0.00172,
        'resin_lifetime_max': 1.2*self.resin_lifetime,
        'resin_lifetime_min': 0.8*self.resin_lifetime,
        'adsorption_density_max':5.0,
        'adsorption_density_min': 3.8,
        'time_between_catridge_regeneration_max':8,
        'time_between_catridge_regeneration_min': 6,
        'time_for_regeneration_max': 1.83,
        'time_for_regeneration_min': 1.16,
        'urine_production_max': 2.4,
        'urine_production_min': 0.8,
        'household_size_max': 1.2*self.household_size,
        'household_size_min': 0.8*self.household_size,
        'flow_equalization_retention_time_max': 1.2,
        'flow_equalization_retention_time_min': 0.8,
        'tank_thickness_max': 1.2*self.tank_thickness,
        'tank_thickness_min': 0.8*self.tank_thickness ,
        'steel_GHG_max': 1.2*self.steel_GHG,
        'steel_GHG_min': 0.8*self.steel_GHG ,
        'steel_energy_max': 1.2*self.steel_energy,
        'steel_energy_min': 0.8*self.steel_energy ,
        'steel_sheet_mass_max':1.2*self.steel_sheet_mass,
        'steel_sheet_mass_min': 0.8*self.steel_sheet_mass, 
        'steel_lifetime_max':1.2*self.steel_lifetime,
        'steel_lifetime_min': 0.8*self.steel_lifetime  ,
        'transport_energy_MJ_km_max':1.2*self.transport_energy_MJ_km,
        'transport_energy_MJ_km_min': 0.8*self.transport_energy_MJ_km,
        'transport_GHG_kg_km_max':1.2*self.transport_GHG_kg_km,
        'transport_GHG_kg_km_min': 0.8*self.transport_GHG_kg_km,
        'diesel_cost_max': 1.2*self.diesel_cost,
        'diesel_cost_min': 0.8*self.diesel_cost ,
        'truck_mpg_max': 1.2*self.truck_mpg,
        'truck_mpg_min': 0.8*self.truck_mpg ,
        'transport_cost_km_max':1.2*self.transport_cost_km,
        'transport_cost_km_min': 0.8*self.transport_cost_km  ,
        'train_energy_MJ_km_max' : 1.2*self.train_energy_MJ_km,
        'train_GHG_kg_km_max': 1.2*self.train_GHG_kg_km ,
        'train_cost_km_max' : 1.2*self.train_cost_km ,
        'train_energy_MJ_km_min' : 0.8*self.train_energy_MJ_km,
        'train_GHG_kg_km_min': 0.8*self.train_GHG_kg_km,
        'train_cost_km_min' : 0.8*self.train_cost_km,
        'km_max':1.2*self.km , 
        'km_min': 0.8*self.km  ,
        'truck_manuf_energy_max': 1.2*self.truck_manuf_energy,
        'truck_manuf_energy_min': 0.8*self.truck_manuf_energy ,
        'truck_manuf_GHG_max':1.2*self.truck_manuf_GHG,
        'truck_manuf_GHG_min': 0.8*self.truck_manuf_GHG , 
        'truck_milage_max': 1.2*self.truck_milage,
        'truck_milage_min': 0.8*self.truck_milage ,
        'truck_cost_max':1.2*self.truck_cost  ,
        'truck_cost_min': 0.8*self.truck_cost  ,
        'truck_milage_y_max':1.2*self.truck_milage_y  ,
        'truck_milage_y_min': 0.8*self.truck_milage_y, 
        'truck_manufacturing_energy_max':1.2*self.truck_manufacturing_energy  ,
        'truck_manufacturing_energy_min': 0.8*self.truck_manufacturing_energy , 
        'truck_manufacturing_GHG_max':1.2*self.truck_manufacturing_GHG  ,
        'truck_manufacturing_GHG_min': 0.8*self.truck_manufacturing_GHG  ,
        'truck_cost_y_max':1.2*self.truck_cost_y  ,
        'truck_cost_y_min': 0.8*self.truck_cost_y  ,
        'plastic_energy_max': 1.2*self.plastic_energy, 
        'plastic_energy_min': 0.8*self.plastic_energy ,
        'plastic_GHG_max': 1.2*self.plastic_GHG,
        'plastic_GHG_min': 0.8*self.plastic_GHG,
        'plastic_cost_max': 1.2*self.plastic_cost, 
        'plastic_cost_min': 0.8*self.plastic_cost ,
        'fiberglass_energy_max': 1.2*self.fiberglass_energy_MJ_kg, 
        'fiberglass_energy_min': 0.8*self.fiberglass_energy_MJ_kg ,
        'fiberglass_GHG_max': 1.2*self.fiberglass_GHG_kg_kg,
        'fiberglass_GHG_min': 0.8*self.fiberglass_GHG_kg_kg,
        'fiberglass_cost_max': 1.2*self.fiberglass_cost, 
        'fiberglass_cost_min': 0.8*self.fiberglass_cost ,
        'plastic_density_max': 1.2*self.plastic_density , 
        'plastic_density_min': 0.8*self.plastic_density ,
        'plastic_lifetime_max': 1.2*self.plastic_lifetime,  
        'plastic_lifetime_min': 0.8*self.plastic_lifetime ,
        'plastic_energy_MJ_kg_max': 1.2*self.plastic_energy_MJ_kg , 
        'plastic_energy_MJ_kg_min': 0.8*self.plastic_energy_MJ_kg ,
        'plastic_GHG_kg_kg_max': 1.2*self.plastic_GHG_kg_kg  ,
        'plastic_GHG_kg_kg_min': 0.8*self.plastic_GHG_kg_kg ,
        'plastic_cost_kg_max': 1.2*self.plastic_cost_kg  ,
        'plastic_cost_kg_min': 0.8*self.plastic_cost_kg ,
        'motor_efficiency_max': 1.2*self.motor_efficiency,  
        'motor_efficiency_min': 0.8*self.motor_efficiency ,
        'electricity_EF_max': 1.2*self.electricity_EF  ,
        'electricity_EF_min': 0.8*self.electricity_EF  ,
        'electricity_cost_max': 1.2*self.electricity_cost,  
        'electricity_cost_min': 0.8*self.electricity_cost ,
        'specific_weight_max': 1.2*self.specific_weight  ,
        'specific_weight_min': 0.8*self.specific_weight  ,
        'pump_lifetime_max': 1.2*self.pump_lifetime  ,
        'pump_lifetime_min': 0.8*self.pump_lifetime ,
        'sulphuric_acid_energy_max': 1.2*self.sulphuric_acid_energy,  
        'sulphuric_acid_energy_min': 0.8*self.sulphuric_acid_energy , 
        'sulphuric_acid_GHG_max': 1.2*self.sulphuric_acid_GHG  ,
        'sulphuric_acid_GHG_min': 0.8*self.sulphuric_acid_GHG  ,
        'acid_density_max': 1.2*self.acid_density,
        'acid_density_min': 0.8*self.acid_density,
        'acid_per_resin_L_kg_max': 0.0001426,
        'acid_per_resin_L_kg_min': 0.00009613,
        'acid_per_resin_max': 1.2*self.acid_per_resin,
        'acid_per_resin_min': 0.8*self.acid_per_resin  , 
        'sulphuric_acid_cost_max': 1.2*self.sulphuric_acid_cost,
        'sulphuric_acid_cost_min':0.8*self.sulphuric_acid_cost,   
        'acid_flow_rate_max': 20.2,
        'acid_flow_rate_min': 24.7,
        'acid_flow_rate_m3_s_max': 1.2*self.acid_flow_rate_m3_s ,
        'acid_flow_rate_m3_s_min': 0.8*self.acid_flow_rate_m3_s, 
        'acid_transport_max': 1.2*self.acid_transport , 
        'acid_transport_min': 0.8*self.acid_transport , 
        'volume_fertilizer_per_acid_max': 1.2*self.volume_fertilizer_per_acid  ,
        'volume_fertilizer_per_acid_min': 0.8*self.volume_fertilizer_per_acid ,
        'volume_bottle_max': 1.2*self.volume_bottle  ,
        'volume_bottle_min': 0.8*self.volume_bottle  ,
        'bottle_thickness_max': 1.2*self.bottle_thickness,  
        'bottle_thickness_min': 0.8*self.bottle_thickness ,
        'bottle_lifetime_max': 1.2*self.bottle_lifetime  ,
        'bottle_lifetime_min': 0.8*self.bottle_lifetime  ,
        'collection_times_per_year_max': 1.2*self.collection_times_per_year , 
        'collection_times_per_year_min': 0.8*self.collection_times_per_year , 
        'facility_manufacturing_energy_max': 1.2*self.facility_manufacturing_energy,  
        'facility_manufacturing_energy_min': 0.8*self.facility_manufacturing_energy,  
        'facility_manufacturing_GHG_max': 1.2*self.facility_manufacturing_GHG , 
        'facility_manufacturing_GHG_min': 0.8*self.facility_manufacturing_GHG ,
        'facility_lifetime_max': 1.2*self.facility_lifetime  ,
        'facility_lifetime_min': 0.8*self.facility_lifetime,  
        'min_facility_cost_max': 1.2*self.min_facility_cost,  
        'min_facility_cost_min': 0.8*self.min_facility_cost,
        'facility_cost_regression_min': 0.8*self.facility_cost_regression,
        'facility_cost_regression_max': 1.2*self.facility_cost_regression}
        return maxmin

    def uncertainty(self):
        new_params = Parameters_values()
        maxmin = self.max_min()
        new_params.percent_served = np.random.uniform(maxmin['percent_served_min'],maxmin['percent_served_max'])
        new_params.PVC_lifetime = np.random.uniform(maxmin['PVC_lifetime_min'],maxmin['PVC_lifetime_max'])
        new_params.resin_cost_kg = np.random.uniform(maxmin['resin_cost_kg_min'],maxmin['resin_cost_kg_max'])
        new_params.resin_energy_MJ_kg = np.random.uniform(maxmin['resin_energy_MJ_kg_min'],maxmin['resin_energy_MJ_kg_max'])
        new_params.resin_GHG_kg_kg = np.random.uniform(maxmin['resin_GHG_kg_kg_min'],maxmin['resin_GHG_kg_kg_max'])
        new_params.resin_transport = np.random.uniform(maxmin['resin_transport_min'],maxmin['resin_transport_max'])
        new_params.hydraulic_conductivity = np.random.uniform(maxmin['hydraulic_conductivity_min'],maxmin['hydraulic_conductivity_max'])
        new_params.resin_lifetime = np.random.uniform(maxmin['resin_lifetime_min'],maxmin['resin_lifetime_max'])
        new_params.N_urine = np.random.uniform(maxmin['N_urine_min'],maxmin['N_urine_max'])
        new_params.adsorption_density = np.random.uniform(maxmin['adsorption_density_min'],maxmin['adsorption_density_max'])
        new_params.time_between_catridge_regeneration = np.random.uniform(maxmin['time_between_catridge_regeneration_min'],maxmin['time_between_catridge_regeneration_max'])
        new_params.time_for_regeneration = np.random.uniform(maxmin['time_for_regeneration_min'],maxmin['time_for_regeneration_max'])
        new_params.urine_production = np.random.uniform(maxmin['urine_production_min'],maxmin['urine_production_max'])
        new_params.household_size = np.random.uniform(maxmin['household_size_min'],maxmin['household_size_max'])
        new_params.flow_equalization_retention_time = np.random.uniform(maxmin['flow_equalization_retention_time_min'],maxmin['flow_equalization_retention_time_max'])
        new_params.tank_thickness = np.random.uniform(maxmin['tank_thickness_min'],maxmin['tank_thickness_max'])
        new_params.steel_GHG = np.random.uniform(maxmin['steel_GHG_min'],maxmin['steel_GHG_max'])
        new_params.steel_energy = np.random.uniform(maxmin['steel_energy_min'],maxmin['steel_energy_max'])
        new_params.steel_sheet_mass = np.random.uniform(maxmin['steel_sheet_mass_min'],maxmin['steel_sheet_mass_max'])
        new_params.steel_lifetime = np.random.uniform(maxmin['steel_lifetime_min'],maxmin['steel_lifetime_max'])
        new_params.transport_energy_MJ_km = np.random.uniform(maxmin['transport_energy_MJ_km_min'],maxmin['transport_energy_MJ_km_max'])
        new_params.transport_GHG_kg_km = np.random.uniform(maxmin['transport_GHG_kg_km_min'],maxmin['transport_GHG_kg_km_max'])
        new_params.diesel_cost = np.random.uniform(maxmin['diesel_cost_min'],maxmin['diesel_cost_max'])
        new_params.truck_mpg = np.random.uniform(maxmin['truck_mpg_min'],maxmin['truck_mpg_max'])
        new_params.km = np.random.uniform(maxmin['km_min'],maxmin['km_max'])
        new_params.truck_manuf_energy = np.random.uniform(maxmin['truck_manuf_energy_min'],maxmin['truck_manuf_energy_max'])
        new_params.truck_manuf_GHG = np.random.uniform(maxmin['truck_manuf_GHG_min'],maxmin['truck_manuf_GHG_max'])
        new_params.truck_milage = np.random.uniform(maxmin['truck_milage_min'],maxmin['truck_milage_max'])
        new_params.truck_cost = np.random.uniform(maxmin['truck_cost_min'],maxmin['truck_cost_max'])
        new_params.truck_milage_y = np.random.uniform(maxmin['truck_milage_y_min'],maxmin['truck_milage_y_max'])
        new_params.train_energy_MJ_km = np.random.uniform(maxmin['train_energy_MJ_km_min'],maxmin['train_energy_MJ_km_max'])
        new_params.train_GHG_kg_km = np.random.uniform(maxmin['train_GHG_kg_km_min'],maxmin['train_GHG_kg_km_max'])
        new_params.train_cost_km = np.random.uniform(maxmin['train_cost_km_min'],maxmin['train_cost_km_max'])
        new_params.plastic_energy = np.random.uniform(maxmin['plastic_energy_min'],maxmin['plastic_energy_max'])
        new_params.plastic_GHG = np.random.uniform(maxmin['plastic_GHG_min'],maxmin['plastic_GHG_max'])
        new_params.plastic_cost = np.random.uniform(maxmin['plastic_cost_min'],maxmin['plastic_cost_max'])
        new_params.fiberglass_energy_MJ_kg = np.random.uniform(maxmin['fiberglass_energy_min'],maxmin['fiberglass_energy_max'])
        new_params.fiberglass_GHG_kg_kg = np.random.uniform(maxmin['fiberglass_GHG_min'],maxmin['fiberglass_GHG_max'])
        new_params.fiberglass_cost = np.random.uniform(maxmin['fiberglass_cost_min'],maxmin['fiberglass_cost_max'])
        new_params.plastic_density = np.random.uniform(maxmin['plastic_density_min'],maxmin['plastic_density_max'])
        new_params.plastic_lifetime = np.random.uniform(maxmin['plastic_lifetime_min'],maxmin['plastic_lifetime_max'])
        new_params.motor_efficiency = np.random.uniform(maxmin['motor_efficiency_min'],maxmin['motor_efficiency_max']) 
        new_params.electricity_EF = np.random.uniform(maxmin['electricity_EF_min'],maxmin['electricity_EF_max'])
        new_params.electricity_cost = np.random.uniform(maxmin['electricity_cost_min'],maxmin['electricity_cost_max'])
        new_params.specific_weight = np.random.uniform(maxmin['specific_weight_min'],maxmin['specific_weight_max'])
        new_params.pump_lifetime = np.random.uniform(maxmin['pump_lifetime_min'],maxmin['pump_lifetime_max'])
        new_params.sulphuric_acid_energy = np.random.uniform(maxmin['sulphuric_acid_energy_min'],maxmin['sulphuric_acid_energy_max'])
        new_params.sulphuric_acid_GHG = np.random.uniform(maxmin['sulphuric_acid_GHG_min'],maxmin['sulphuric_acid_GHG_max'])
        new_params.acid_density = np.random.uniform(maxmin['acid_density_min'],maxmin['acid_density_max'])
        new_params.acid_per_resin_L_kg = np.random.uniform(maxmin['acid_per_resin_L_kg_min'],maxmin['acid_per_resin_L_kg_max'])
        new_params.sulphuric_acid_cost = np.random.uniform(maxmin['sulphuric_acid_cost_min'],maxmin['sulphuric_acid_cost_max'])
        new_params.acid_flow_rate = np.random.uniform(maxmin['acid_flow_rate_min'],maxmin['acid_flow_rate_max'])
        new_params.acid_transport = np.random.uniform(maxmin['acid_transport_min'],maxmin['acid_transport_max'])
        new_params.volume_fertilizer_per_acid = np.random.uniform(maxmin['volume_fertilizer_per_acid_min'],maxmin['volume_fertilizer_per_acid_max'])
        new_params.volume_bottle = np.random.uniform(maxmin['volume_bottle_min'],maxmin['volume_bottle_max'])
        new_params.bottle_thickness = np.random.uniform(maxmin['bottle_thickness_min'],maxmin['bottle_thickness_max'])
        new_params.bottle_lifetime = np.random.uniform(maxmin['bottle_lifetime_min'],maxmin['bottle_lifetime_max'])
        new_params.collection_times_per_year = np.random.uniform(maxmin['collection_times_per_year_min'],maxmin['collection_times_per_year_max'])
        new_params.facility_manufacturing_energy = np.random.uniform(maxmin['facility_manufacturing_energy_min'],maxmin['facility_manufacturing_energy_max'])
        new_params.facility_manufacturing_GHG = np.random.uniform(maxmin['facility_manufacturing_GHG_min'],maxmin['facility_manufacturing_GHG_max'])
        new_params.facility_lifetime = np.random.uniform(maxmin['facility_lifetime_min'],maxmin['facility_lifetime_max'])
        new_params.min_facility_cost = np.random.uniform(maxmin['min_facility_cost_min'],maxmin['min_facility_cost_max'])
        new_params.facility_cost_regression = np.random.uniform(maxmin['facility_cost_regression_min'],maxmin['facility_cost_regression_max'])
        return new_params

    def sensitivity(self, parameter, direction):
        new_params = Parameters_values()
        maxmin = self.max_min()
        if parameter == 'percent_served':  
            if direction == 'minus':  
                new_params.percent_served = self.percent_served - (maxmin['percent_served_max'] - maxmin['percent_served_min'])/10 
            if direction == 'plus':
                new_params.percent_served = self.percent_served + (maxmin['percent_served_max'] - maxmin['percent_served_min'])/10 
        if parameter == 'PVC_lifetime':  
            if direction == 'minus':  
                new_params.PVC_lifetime = self.PVC_lifetime - (maxmin['PVC_lifetime_max'] - maxmin['PVC_lifetime_min'])/10 
            if direction == 'plus':
                new_params.PVC_lifetime = self.PVC_lifetime + (maxmin['PVC_lifetime_max'] - maxmin['PVC_lifetime_min'])/10 
        if parameter == 'resin_cost_kg': 
            if direction == 'minus':   
                new_params.resin_cost_kg = self.resin_cost_kg - (maxmin['resin_cost_kg_max'] - maxmin['resin_cost_kg_min'])/10 
            if direction == 'plus':
                new_params.resin_cost_kg = self.resin_cost_kg + (maxmin['resin_cost_kg_max'] - maxmin['resin_cost_kg_min'])/10 
        if parameter == 'resin_energy_MJ_kg':
            if direction == 'minus':
                new_params.resin_energy_MJ_kg = self.resin_energy_MJ_kg - (maxmin['resin_energy_MJ_kg_max'] -  maxmin['resin_energy_MJ_kg_min'])/10
            if direction == 'plus': 
                new_params.resin_energy_MJ_kg = self.resin_energy_MJ_kg + (maxmin['resin_energy_MJ_kg_max'] -  maxmin['resin_energy_MJ_kg_min'])/10
        if parameter == 'resin_GHG_kg_kg':
            if direction == 'minus':
                new_params.resin_GHG_kg_kg = self.resin_GHG_kg_kg - (maxmin['resin_GHG_kg_kg_max'] -  maxmin['resin_GHG_kg_kg_min'])/10 
            if direction == 'plus':
                new_params.resin_GHG_kg_kg = self.resin_GHG_kg_kg + (maxmin['resin_GHG_kg_kg_max'] -  maxmin['resin_GHG_kg_kg_min'])/10 
        if parameter == 'resin_transport':
            if direction == 'minus':
                new_params.resin_transport = self.resin_transport - (maxmin['resin_transport_max'] -  maxmin['resin_transport_min'])/10 
            if direction == 'plus':
                 new_params.resin_transport = self.resin_transport + (maxmin['resin_transport_max'] -  maxmin['resin_transport_min'])/10 
        if parameter == 'hydraulic_conductivity':
            if direction == 'minus':
                new_params.hydraulic_conductivity = self.hydraulic_conductivity - (maxmin['hydraulic_conductivity_max'] -  maxmin['hydraulic_conductivity_min'])/10
            if direction == 'plus': 
                new_params.hydraulic_conductivity = self.hydraulic_conductivity + (maxmin['hydraulic_conductivity_max'] -  maxmin['hydraulic_conductivity_min'])/10
        if parameter == 'resin_lifetime':
            if direction == 'minus':
                new_params.resin_lifetime = self.resin_lifetime - (maxmin['resin_lifetime_max'] -  maxmin['resin_lifetime_min'])/10 
            if direction == 'plus':
                new_params.resin_lifetime = self.resin_lifetime + (maxmin['resin_lifetime_max'] -  maxmin['resin_lifetime_min'])/10 
        if parameter == 'N_urine':
            if direction == 'minus':
                new_params.N_urine = self.N_urine - (maxmin['N_urine_max'] -  maxmin['N_urine_min'])/10
            if direction == 'plus': 
                new_params.N_urine = self.N_urine + (maxmin['N_urine_max'] -  maxmin['N_urine_min'])/10
        if parameter == 'adsorption_density':
            if direction == 'minus':
                new_params.adsorption_density = self.adsorption_density - (maxmin['adsorption_density_max'] -  maxmin['adsorption_density_min'])/10
            if direction == 'plus': 
                new_params.adsorption_density = self.adsorption_density + (maxmin['adsorption_density_max'] -  maxmin['adsorption_density_min'])/10
        if parameter == 'time_between_catridge_regeneration':
            if direction == 'minus':
                new_params.time_between_catridge_regeneration = self.time_between_catridge_regeneration - (maxmin['time_between_catridge_regeneration_max'] -  maxmin['time_between_catridge_regeneration_min'])/10 
            if direction == 'plus':
                new_params.time_between_catridge_regeneration = self.time_between_catridge_regeneration + (maxmin['time_between_catridge_regeneration_max'] -  maxmin['time_between_catridge_regeneration_min'])/10
        if parameter == 'time_for_regeneration':
            if direction == 'minus':
                new_params.time_for_regeneration = self.time_for_regeneration - (maxmin['time_for_regeneration_max'] -  maxmin['time_for_regeneration_min'])/10 
            if direction == 'plus':
                new_params.time_for_regeneration = self.time_for_regeneration + (maxmin['time_for_regeneration_max'] -  maxmin['time_for_regeneration_min'])/10 
        if parameter == 'urine_production':
            if direction == 'minus':
                new_params.urine_production = self.urine_production - (maxmin['urine_production_max'] -  maxmin['urine_production_min'])/10 
            if direction == 'plus':
                new_params.urine_production = self.urine_production + (maxmin['urine_production_max'] -  maxmin['urine_production_min'])/10 
        if parameter == 'household_size':
            if direction == 'minus':
                new_params.household_size = self.household_size - (maxmin['household_size_max'] -  maxmin['household_size_min'])/10 
            if direction == 'plus':
                new_params.household_size = self.household_size + (maxmin['household_size_max'] -  maxmin['household_size_min'])/10 
        if parameter == 'flow_equalization_retention_time':
            if direction == 'minus':
                new_params.flow_equalization_retention_time = self.flow_equalization_retention_time - (maxmin['flow_equalization_retention_time_max'] -  maxmin['flow_equalization_retention_time_min'])/10 
            if direction == 'plus':
                new_params.flow_equalization_retention_time = self.flow_equalization_retention_time + (maxmin['flow_equalization_retention_time_max'] -  maxmin['flow_equalization_retention_time_min'])/10 
        if parameter == 'tank_thickness':
            if direction == 'minus':
                new_params.tank_thickness = self.tank_thickness - (maxmin['tank_thickness_max'] -  maxmin['tank_thickness_min'])/10 
            if direction == 'plus':
                new_params.tank_thickness = self.tank_thickness + (maxmin['tank_thickness_max'] -  maxmin['tank_thickness_min'])/10 
        if parameter == 'steel_GHG':
            if direction == 'minus':
                new_params.steel_GHG = self.steel_GHG - (maxmin['steel_GHG_max'] -  maxmin['steel_GHG_min'])/10 
            if direction == 'plus':
                new_params.steel_GHG = self.steel_GHG + (maxmin['steel_GHG_max'] -  maxmin['steel_GHG_min'])/10 
        if parameter == 'steel_energy':
            if direction == 'minus':
                new_params.steel_energy = self.steel_energy - (maxmin['steel_energy_max'] -  maxmin['steel_energy_min'])/10 
            if direction == 'plus':
                new_params.steel_energy = self.steel_energy + (maxmin['steel_energy_max'] -  maxmin['steel_energy_min'])/10 
        if parameter == 'steel_sheet_mass':
            if direction == 'minus':
                new_params.steel_sheet_mass = self.steel_sheet_mass - (maxmin['steel_sheet_mass_max'] -  maxmin['steel_sheet_mass_min'])/10 
            if direction == 'plus':
                new_params.steel_sheet_mass = self.steel_sheet_mass + (maxmin['steel_sheet_mass_max'] -  maxmin['steel_sheet_mass_min'])/10 
        if parameter == 'steel_lifetime':
            if direction == 'minus':
                new_params.steel_lifetime = self.steel_lifetime - (maxmin['steel_lifetime_max'] -  maxmin['steel_lifetime_min'])/10 
            if direction == 'plus':
                new_params.steel_lifetime = self.steel_lifetime + (maxmin['steel_lifetime_max'] -  maxmin['steel_lifetime_min'])/10 
        if parameter == 'transport_energy_MJ_km':
            if direction == 'minus':
                new_params.transport_energy_MJ_km = self.transport_energy_MJ_km - (maxmin['transport_energy_MJ_km_max'] -  maxmin['transport_energy_MJ_km_min'])/10 
            if direction == 'plus':
                new_params.transport_energy_MJ_km = self.transport_energy_MJ_km + (maxmin['transport_energy_MJ_km_max'] -  maxmin['transport_energy_MJ_km_min'])/10 
        if parameter == 'transport_GHG_kg_km':
            if direction == 'minus':
                new_params.transport_GHG_kg_km = self.transport_GHG_kg_km - (maxmin['transport_GHG_kg_km_max'] -  maxmin['transport_GHG_kg_km_min'])/10 
            if direction == 'plus':
                new_params.transport_GHG_kg_km = self.transport_GHG_kg_km + (maxmin['transport_GHG_kg_km_max'] -  maxmin['transport_GHG_kg_km_min'])/10 
        if parameter == 'diesel_cost':
            if direction == 'minus':
                new_params.diesel_cost = self.diesel_cost - (maxmin['diesel_cost_max'] -  maxmin['diesel_cost_min'])/10 
            if direction == 'plus':
                new_params.diesel_cost = self.diesel_cost + (maxmin['diesel_cost_max'] -  maxmin['diesel_cost_min'])/10 
        if parameter == 'truck_mpg':
            if direction == 'minus':
                new_params.truck_mpg = self.truck_mpg - (maxmin['truck_mpg_max'] -  maxmin['truck_mpg_min'])/10 
            if direction == 'plus':
                new_params.truck_mpg = self.truck_mpg + (maxmin['truck_mpg_max'] -  maxmin['truck_mpg_min'])/10 
        if parameter == 'km':
            if direction == 'minus':
                new_params.km = self.km - (maxmin['km_max'] -  maxmin['km_min'])/10 
            if direction == 'plus':
                new_params.km = self.km + (maxmin['km_max'] -  maxmin['km_min'])/10 
        if parameter == 'truck_manuf_energy':
            if direction == 'minus':
                new_params.truck_manuf_energy = self.truck_manuf_energy - (maxmin['truck_manuf_energy_max'] -  maxmin['truck_manuf_energy_min'])/10 
            if direction == 'plus':
                new_params.truck_manuf_energy = self.truck_manuf_energy + (maxmin['truck_manuf_energy_max'] -  maxmin['truck_manuf_energy_min'])/10 
        if parameter == 'truck_manuf_GHG':
            if direction == 'minus':
                new_params.truck_manuf_GHG = self.truck_manuf_GHG - (maxmin['truck_manuf_GHG_max'] -  maxmin['truck_manuf_GHG_min'])/10 
            if direction == 'plus':
                new_params.truck_manuf_GHG = self.truck_manuf_GHG +(maxmin['truck_manuf_GHG_max'] -  maxmin['truck_manuf_GHG_min'])/10 
        if parameter == 'truck_milage':
            if direction == 'minus':
                new_params.truck_milage = self.truck_milage - (maxmin['truck_milage_max'] -  maxmin['truck_milage_min'])/10 
            if direction == 'plus':
                new_params.truck_milage = self.truck_milage + (maxmin['truck_milage_max'] -  maxmin['truck_milage_min'])/10
        if parameter == 'truck_cost':
            if direction == 'minus':
                new_params.truck_cost = self.truck_cost - (maxmin['truck_cost_max'] -  maxmin['truck_cost_min'])/10 
            if direction == 'plus':
                new_params.truck_cost = self.truck_cost + (maxmin['truck_cost_max'] -  maxmin['truck_cost_min'])/10 
        if parameter == 'truck_milage_y':
            if direction == 'minus':
                new_params.truck_milage_y = self.truck_milage_y - (maxmin['truck_milage_y_max'] -  maxmin['truck_milage_y_min'])/10 
            if direction == 'plus':
                new_params.truck_milage_y = self.truck_milage_y + (maxmin['truck_milage_y_max'] -  maxmin['truck_milage_y_min'])/10 
        if parameter == 'plastic_energy':
            if direction == 'minus':
                new_params.plastic_energy = self.plastic_energy - (maxmin['plastic_energy_max'] -  maxmin['plastic_energy_min'])/10 
            if direction == 'plus':
                new_params.plastic_energy = self.plastic_energy + (maxmin['plastic_energy_max'] -  maxmin['plastic_energy_min'])/10 
        if parameter == 'plastic_GHG':
            if direction == 'minus':
                new_params.plastic_GHG = self.plastic_GHG - (maxmin['plastic_GHG_max'] -  maxmin['plastic_GHG_min'])/10 
            if direction == 'plus':
                new_params.plastic_GHG = self.plastic_GHG + (maxmin['plastic_GHG_max'] -  maxmin['plastic_GHG_min'])/10 
        if parameter == 'fiberglass_energy_MJ_kg':
            if direction == 'minus':
                new_params.fiberglass_energy_MJ_kg = self.fiberglass_energy_MJ_kg - (maxmin['fiberglass_energy_max'] -  maxmin['fiberglass_energy_min'])/10 
            if direction == 'plus':
                new_params.fiberglass_energy_MJ_kg = self.fiberglass_energy_MJ_kg + (maxmin['fiberglass_energy_max'] -  maxmin['fiberglass_energy_min'])/10 
        if parameter == 'fiberglass_GHG_kg_kg':
            if direction == 'minus':
                new_params.fiberglass_GHG_kg_kg = self.fiberglass_GHG_kg_kg - (maxmin['fiberglass_GHG_max'] -  maxmin['fiberglass_GHG_min'])/10 
            if direction == 'plus':
                new_params.fiberglass_GHG_kg_kg = self.fiberglass_GHG_kg_kg + (maxmin['fiberglass_GHG_max'] -  maxmin['fiberglass_GHG_min'])/10 
        if parameter == 'fiberglass_cost':  
            if direction == 'minus':  
                new_params.fiberglass_cost = self.fiberglass_cost - (maxmin['fiberglass_cost_max'] -  maxmin['fiberglass_cost_min'])/10 
            if direction == 'plus':
                new_params.fiberglass_cost = self.fiberglass_cost + (maxmin['fiberglass_cost_max'] -  maxmin['fiberglass_cost_min'])/10 
        if parameter == 'plastic_cost':  
            if direction == 'minus':  
                new_params.plastic_cost = self.plastic_cost - (maxmin['plastic_cost_max'] -  maxmin['plastic_cost_min'])/10 
            if direction == 'plus':
                new_params.plastic_cost = self.plastic_cost + (maxmin['plastic_cost_max'] -  maxmin['plastic_cost_min'])/10 
        if parameter == 'plastic_density':
            if direction == 'minus':
                new_params.plastic_density = self.plastic_density - (maxmin['plastic_density_max'] -  maxmin['plastic_density_min'])/10 
            if direction == 'plus':
                new_params.plastic_density = self.plastic_density + (maxmin['plastic_density_max'] -  maxmin['plastic_density_min'])/10 
        if parameter == 'plastic_lifetime':
            if direction == 'minus':
                new_params.plastic_lifetime = self.plastic_lifetime - (maxmin['plastic_lifetime_max'] -  maxmin['plastic_lifetime_min'])/10 
            if direction == 'plus':
                new_params.plastic_lifetime = self.plastic_lifetime + (maxmin['plastic_lifetime_max'] -  maxmin['plastic_lifetime_min'])/10
        if parameter == 'motor_efficiency': 
            if direction == 'minus':   
                new_params.motor_efficiency = self.motor_efficiency - (maxmin['motor_efficiency_max'] -  maxmin['motor_efficiency_min'])/10 
            if direction == 'plus':
                new_params.motor_efficiency = self.motor_efficiency + (maxmin['motor_efficiency_max'] -  maxmin['motor_efficiency_min'])/10 
        if parameter == 'electricity_EF':
            if direction == 'minus':
                new_params.electricity_EF = self.electricity_EF - (maxmin['electricity_EF_max'] -  maxmin['electricity_EF_min'])/10 
            if direction == 'plus':
                new_params.electricity_EF = self.electricity_EF + (maxmin['electricity_EF_max'] -  maxmin['electricity_EF_min'])/10 
        if parameter == 'electricity_cost':
            if direction == 'minus':
                new_params.electricity_cost = self.electricity_cost - (maxmin['electricity_cost_max'] -  maxmin['electricity_cost_min'])/10 
            if direction == 'plus':
                new_params.electricity_cost = self.electricity_cost + (maxmin['electricity_cost_max'] -  maxmin['electricity_cost_min'])/10 
        if parameter == 'specific_weight':
            if direction == 'minus':
                new_params.specific_weight = self.specific_weight - (maxmin['specific_weight_max'] -  maxmin['specific_weight_min'])/10 
            if direction == 'plus':
                new_params.specific_weight = self.specific_weight + (maxmin['specific_weight_max'] -  maxmin['specific_weight_min'])/10 
        if parameter == 'pump_lifetime':
            if direction == 'minus':
                new_params.pump_lifetime = self.pump_lifetime - (maxmin['pump_lifetime_max'] -  maxmin['pump_lifetime_min'])/10 
            if direction == 'plus':
                new_params.pump_lifetime = self.pump_lifetime + (maxmin['pump_lifetime_max'] -  maxmin['pump_lifetime_min'])/10 
        if parameter == 'sulphuric_acid_energy':
            if direction == 'minus':
                new_params.sulphuric_acid_energy = self.sulphuric_acid_energy - (maxmin['sulphuric_acid_energy_max'] -  maxmin['sulphuric_acid_energy_min'])/10 
            if direction == 'plus':
                new_params.sulphuric_acid_energy = self.sulphuric_acid_energy + (maxmin['sulphuric_acid_energy_max'] -  maxmin['sulphuric_acid_energy_min'])/10
        if parameter == 'sulphuric_acid_GHG':
            if direction == 'minus':
                new_params.sulphuric_acid_GHG = self.sulphuric_acid_GHG - (maxmin['sulphuric_acid_GHG_max'] -  maxmin['sulphuric_acid_GHG_min'])/10 
            if direction == 'plus':
                new_params.sulphuric_acid_GHG = self.sulphuric_acid_GHG + (maxmin['sulphuric_acid_GHG_max'] -  maxmin['sulphuric_acid_GHG_min'])/10 
        if parameter == 'acid_density':
            if direction == 'minus':
                new_params.acid_density = self.acid_density - (maxmin['acid_density_max'] -  maxmin['acid_density_min'])/10 
            if direction == 'plus':
                new_params.acid_density = self.acid_density + (maxmin['acid_density_max'] -  maxmin['acid_density_min'])/10 
        if parameter == 'acid_per_resin_L_kg':
            if direction == 'minus':
                new_params.acid_per_resin_L_kg = self.acid_per_resin_L_kg - (maxmin['acid_per_resin_L_kg_max'] -  maxmin['acid_per_resin_L_kg_min'])/10 
            if direction == 'plus':
                new_params.acid_per_resin_L_kg = self.acid_per_resin_L_kg + (maxmin['acid_per_resin_L_kg_max'] -  maxmin['acid_per_resin_L_kg_min'])/10 
        if parameter == 'sulphuric_acid_cost':
            if direction == 'minus':
                new_params.sulphuric_acid_cost = self.sulphuric_acid_cost - (maxmin['sulphuric_acid_cost_max'] -  maxmin['sulphuric_acid_cost_min'])/10 
            if direction == 'plus':
                new_params.sulphuric_acid_cost = self.sulphuric_acid_cost + (maxmin['sulphuric_acid_cost_max'] -  maxmin['sulphuric_acid_cost_min'])/10 
        if parameter == 'acid_flow_rate':
            if direction == 'minus':
                new_params.acid_flow_rate = self.acid_flow_rate - (maxmin['acid_flow_rate_max'] -  maxmin['acid_flow_rate_min'])/10 
            if direction == 'plus':
                new_params.acid_flow_rate = self.acid_flow_rate + (maxmin['acid_flow_rate_max'] -  maxmin['acid_flow_rate_min'])/10 
        if parameter == 'acid_transport':
            if direction == 'minus':
                new_params.acid_transport = self.acid_transport - (maxmin['acid_transport_max'] -  maxmin['acid_transport_min'])/10 
            if direction == 'plus':
                new_params.acid_transport = self.acid_transport + (maxmin['acid_transport_max'] -  maxmin['acid_transport_min'])/10 
        if parameter == 'volume_fertilizer_per_acid':
            if direction == 'minus':
                new_params.volume_fertilizer_per_acid = self.volume_fertilizer_per_acid - (maxmin['volume_fertilizer_per_acid_max'] -  maxmin['volume_fertilizer_per_acid_min'])/10 
            if direction == 'plus':
                new_params.volume_fertilizer_per_acid = self.volume_fertilizer_per_acid + (maxmin['volume_fertilizer_per_acid_max'] -  maxmin['volume_fertilizer_per_acid_min'])/10 
        if parameter == 'volume_bottle':
            if direction == 'minus':
                new_params.volume_bottle = self.volume_bottle - (maxmin['volume_bottle_max'] -  maxmin['volume_bottle_min'])/10 
            if direction == 'plus':
                new_params.volume_bottle = self.volume_bottle + (maxmin['volume_bottle_max'] -  maxmin['volume_bottle_min'])/10 
        if parameter == 'bottle_thickness':
            if direction == 'minus':
                new_params.bottle_thickness = self.bottle_thickness - (maxmin['bottle_thickness_max'] -  maxmin['bottle_thickness_min'])/10
            if direction == 'plus':
                new_params.bottle_thickness = self.bottle_thickness + (maxmin['bottle_thickness_max'] -  maxmin['bottle_thickness_min'])/10
        if parameter == 'bottle_lifetime':
            if direction == 'minus':
                new_params.bottle_lifetime = self.bottle_lifetime - (maxmin['bottle_lifetime_max'] -  maxmin['bottle_lifetime_min'])/10
            if direction == 'plus':
                new_params.bottle_lifetime = self.bottle_lifetime + (maxmin['bottle_lifetime_max'] -  maxmin['bottle_lifetime_min'])/10
        if parameter == 'collection_times_per_year':
            if direction == 'minus':
                new_params.collection_times_per_year = self.collection_times_per_year - (maxmin['collection_times_per_year_max'] -  maxmin['collection_times_per_year_min'])/10
            if direction == 'plus':
                new_params.collection_times_per_year = self.collection_times_per_year + (maxmin['collection_times_per_year_max'] -  maxmin['collection_times_per_year_min'])/10
        if parameter == 'facility_manufacturing_energy':
            if direction == 'minus':
                new_params.facility_manufacturing_energy = self.facility_manufacturing_energy - (maxmin['facility_manufacturing_energy_max'] -  maxmin['facility_manufacturing_energy_min'])/10
            if direction == 'plus':
                new_params.facility_manufacturing_energy = self.facility_manufacturing_energy + (maxmin['facility_manufacturing_energy_max'] -  maxmin['facility_manufacturing_energy_min'])/10
        if parameter == 'facility_manufacturing_GHG':
            if direction == 'minus':
                new_params.facility_manufacturing_GHG = self.facility_manufacturing_GHG - (maxmin['facility_manufacturing_GHG_max'] -  maxmin['facility_manufacturing_GHG_min'])/10
            if direction == 'plus':
                new_params.facility_manufacturing_GHG = self.facility_manufacturing_GHG + (maxmin['facility_manufacturing_GHG_max'] -  maxmin['facility_manufacturing_GHG_min'])/10
        if parameter == 'facility_lifetime':
            if direction == 'minus':
                new_params.facility_lifetime = self.facility_lifetime - (maxmin['facility_lifetime_max'] -  maxmin['facility_lifetime_min'])/10
            if direction == 'plus':
                new_params.facility_lifetime = self.facility_lifetime + (maxmin['facility_lifetime_max'] -  maxmin['facility_lifetime_min'])/10
        if parameter == 'min_facility_cost':
            if direction == 'minus':
                new_params.min_facility_cost = self.min_facility_cost - (maxmin['min_facility_cost_max'] -  maxmin['min_facility_cost_min'])/10
            if direction == 'plus':
                new_params.min_facility_cost = self.min_facility_cost + (maxmin['min_facility_cost_max'] -  maxmin['min_facility_cost_min'])/10
        if parameter == 'facility_cost_regression':
            if direction == 'minus':
                new_params.facility_cost_regression = self.facility_cost_regression - (maxmin['facility_cost_regression_max'] -  maxmin['facility_cost_regression_min'])/10
            if direction == 'plus':
                new_params.facility_cost_regression = self.facility_cost_regression + (maxmin['facility_cost_regression_max'] -  maxmin['facility_cost_regression_min'])/10
        return new_params


