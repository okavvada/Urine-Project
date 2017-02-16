from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from utils.logistics_functions import *

pipe_construction_data = pd.read_csv('pipe_construction_data.csv')
pump_construction_data = pd.read_csv('pump_construction_data.csv')
pipe_construction_data=pipe_construction_data[pipe_construction_data['Material']=='PVC']
nominal_diameter_list=np.array(pipe_construction_data['size_mm'])
pump_size_list=np.array(pump_construction_data['Rating_hp'])



def find_transport_energy(tons, km, lifetime, Parameters, mode = 'truck'):
    if mode == 'truck':
        transport_energy = Parameters.truck_payload*Parameters.transport_energy_MJ_km*km/(lifetime)
    if mode == 'train':
        transport_energy = tons*Parameters.train_energy_MJ_km*km/(lifetime)
    return transport_energy #MJ_y
    
def find_transport_GHG(tons,km, lifetime, Parameters, mode = 'truck'):
    if mode == 'truck':
        transport_GHG = Parameters.truck_payload*Parameters.transport_GHG_kg_km*km/(lifetime)
    if mode == 'train':
        transport_GHG = tons*Parameters.train_GHG_kg_km*km/(lifetime)
    return transport_GHG #kg_y

def find_transport_cost(tons, km, lifetime, Parameters, truck_num, mode = 'truck'):
    if mode == 'truck':
        #transport_cost = tons*Parameters.transport_cost_km*km/(lifetime)
        transport_cost = Parameters.diesel_cost/(Parameters.truck_mpg*1.6)*km/(lifetime)
    if mode == 'train':
        transport_cost = tons*Parameters.train_cost_km*km/(lifetime)
    return transport_cost #$_y

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]


class resin():
    def __init__(self, number_of_people_per_facility, Parameters):
        self.Parameters = Parameters
        self.number_of_cartridges_per_facility = number_of_people_per_facility/self.Parameters.household_size

    def mass_resin_household(self):
        daily_urine_household = self.Parameters.household_size*self.Parameters.urine_production #L/day
        volume_urine_treated_before_replacement = self.Parameters.time_between_catridge_regeneration*daily_urine_household #L
        mass_resin_household=volume_urine_treated_before_replacement*self.Parameters.N_urine/(self.Parameters.adsorption_density*self.Parameters.molar_mass_N)#kg
        return mass_resin_household #kg
    
    def resin_energy(self):
        resin_energy = self.mass_resin_household()*self.Parameters.resin_energy_MJ_kg/self.Parameters.resin_lifetime*self.number_of_cartridges_per_facility*self.Parameters.percent_served
        return resin_energy #MJ_y
    
    def resin_GHG(self):
        resin_GHG = self.mass_resin_household()*self.Parameters.resin_GHG_kg_kg/self.Parameters.resin_lifetime*self.number_of_cartridges_per_facility*self.Parameters.percent_served
        return resin_GHG #kg_y
    
    def resin_cost(self):
        resin_cost = self.mass_resin_household()*self.Parameters.resin_cost_kg/self.Parameters.resin_lifetime*self.number_of_cartridges_per_facility*self.Parameters.percent_served
        return resin_cost #$_y

    def resin_transport(self):
        Transport_energy = find_transport_energy(self.mass_resin_household()*self.number_of_cartridges_per_facility*self.Parameters.percent_served/1000, self.Parameters.resin_transport, self.Parameters.resin_lifetime, self.Parameters, mode='train')
        Transport_GHG = find_transport_GHG(self.mass_resin_household()*self.number_of_cartridges_per_facility*self.Parameters.percent_served/1000, self.Parameters.resin_transport, self.Parameters.resin_lifetime, self.Parameters, mode='train')
        Transport_cost = find_transport_cost(self.mass_resin_household()*self.number_of_cartridges_per_facility*self.Parameters.percent_served/1000, self.Parameters.resin_transport, self.Parameters.resin_lifetime, self.Parameters, 1, mode='train')
        return Transport_energy,Transport_GHG,Transport_cost



class catridge():
    def __init__(self, mass_resin_household, number_of_people_per_facility, Parameters):
        self.Parameters = Parameters
        self.number_of_cartridges_per_facility = number_of_people_per_facility*self.Parameters.percent_served/self.Parameters.household_size
        self.mass_resin_household = mass_resin_household
        
    def catridge_volume(self):
        catridge_volume = self.mass_resin_household/self.Parameters.resin_density*1000 #L
        return catridge_volume
    
    def catridge_length(self):
        catridge_length = self.catridge_volume()*10000/(math.pi*((self.Parameters.catridge_diameter)/2)**2)/1000 #m
        return catridge_length

    def area_cylinder(self):
        radius = self.Parameters.catridge_diameter/2/100
        area = 2*math.pi*radius*self.catridge_length()+2*math.pi*(radius**2)
        return area
    
    def mass_fiberglass(self):
        area = self.area_cylinder()       
        mass = area*self.Parameters.catridge_thickness*self.Parameters.fiberglass_density*1000*self.number_of_cartridges_per_facility
        kg = area*self.Parameters.catridge_thickness*self.Parameters.fiberglass_density*1000
        return mass
    
    # def mass_PVC(self):
    #     diameter_mm=self.diameter
    #     diameter=find_nearest(nominal_diameter_list,diameter_mm)
    #     pipe_index=pipe_construction_data.set_index('size_mm')
    #     pipe_weight_kg=pipe_index.Wt_kg_m[diameter]*self.catridge_length()*self.number_of_cartridges_per_facility*self.Parameters.percent_served
    #     return pipe_weight_kg

    def PVC_energy(self):
        #pipe_index=pipe_construction_data.set_index('size_mm')
        #diameter_mm=self.diameter
        #diameter=find_nearest(nominal_diameter_list,diameter_mm)
        #PVC_energy_MJ=pipe_index.Embodied_Energy_MJ_kg[diameter]*self.mass_PVC()/self.Parameters.PVC_lifetime
        mass = self.mass_fiberglass()
        PVC_energy_MJ = mass*self.Parameters.fiberglass_energy_MJ_kg/self.Parameters.catridge_lifetime
        return PVC_energy_MJ # MJ_y

    def PVC_GHG(self):
        #pipe_index=pipe_construction_data.set_index('size_mm')
        #diameter_mm=self.diameter
        #diameter=find_nearest(nominal_diameter_list,diameter_mm)
        #PVC_GHG_kg=pipe_index.Emissions_kgCO2_eq_m[diameter]*self.catridge_length()*self.number_of_cartridges_per_facility*self.Parameters.percent_served/self.Parameters.PVC_lifetime
        mass = self.mass_fiberglass()
        PVC_GHG_kg = mass*self.Parameters.fiberglass_GHG_kg_kg/self.Parameters.catridge_lifetime
        return PVC_GHG_kg # kg_y

    def PVC_cost(self):
        #pipe_index=pipe_construction_data.set_index('size_mm')
        #diameter_mm=self.diameter
        #diameter=find_nearest(nominal_diameter_list,diameter_mm)
        #PVC_cost=pipe_index.cost_2012_m[diameter]*self.catridge_length()*self.number_of_cartridges_per_facility*self.Parameters.percent_served/self.Parameters.PVC_lifetime
        mass = self.mass_fiberglass()
        PVC_cost = mass*self.Parameters.fiberglass_cost_kg/self.Parameters.catridge_lifetime
        return PVC_cost # $_y

    def cartridge_transport(self):
        Transport_energy = find_transport_energy(self.mass_fiberglass()/1000, self.Parameters.km, self.Parameters.fiberglass_lifetime, self.Parameters, mode='truck')
        Transport_GHG = find_transport_GHG(self.mass_fiberglass()/1000, self.Parameters.km, self.Parameters.fiberglass_lifetime, self.Parameters, mode='truck')
        Transport_cost = find_transport_cost(self.mass_fiberglass()/1000, self.Parameters.km, self.Parameters.fiberglass_lifetime, self.Parameters, 1, mode='truck')
        return Transport_energy,Transport_GHG,Transport_cost


class flow_equalization_plastic():
    def __init__(self, number_of_people_per_facility, Parameters):
        self.Parameters = Parameters
        self.number_of_cartridges_per_facility = number_of_people_per_facility*self.Parameters.percent_served/self.Parameters.household_size
        
    def volume(self):
        daily_urine_household = self.Parameters.household_size*1.5*self.Parameters.urine_production #L/day
        volume = daily_urine_household*self.Parameters.flow_equalization_retention_time/1000*self.number_of_cartridges_per_facility
        return volume #m3
    
    def area_cylinder(self):
        radius = math.sqrt(abs(self.volume()/(math.pi*self.Parameters.tank_height)))
        area = 2*math.pi*radius*self.Parameters.tank_height+2*math.pi*radius**2
        return area
    
    def mass_plastic(self):
        area = self.area_cylinder()       
        mass = area*self.Parameters.tank_thickness*self.Parameters.plastic_density
        return mass
        
    def plastic_energy(self):
        mass = self.mass_plastic()
        plastic_energy = mass*self.Parameters.plastic_energy_MJ_kg/self.Parameters.plastic_lifetime
        return plastic_energy #MJ_y

    def plastic_GHG(self):
        mass = self.mass_plastic()
        plastic_GHG = mass*self.Parameters.plastic_GHG_kg_kg/self.Parameters.plastic_lifetime
        return plastic_GHG #kg_y

    def plastic_cost(self):
        mass = self.mass_plastic()
        plastic_cost = mass*self.Parameters.plastic_cost_kg/self.Parameters.plastic_lifetime
        return plastic_cost # $_y

    def tank_transport(self):
        Transport_energy = find_transport_energy(self.mass_plastic()/1000, self.Parameters.km, self.Parameters.plastic_lifetime, self.Parameters, mode='truck')
        Transport_GHG = find_transport_GHG(self.mass_plastic()/1000, self.Parameters.km, self.Parameters.plastic_lifetime, self.Parameters, mode='truck')
        Transport_cost = find_transport_cost(self.mass_plastic()/1000, self.Parameters.km, self.Parameters.plastic_lifetime, self.Parameters, 1, mode='truck')
        return Transport_energy,Transport_GHG,Transport_cost


class pump_flow():
    def __init__(self, catridge_length, number_of_people_per_facility, Parameters):
        self.Parameters = Parameters
        self.catridge_length = catridge_length
        self.number_of_cartridges_per_facility =number_of_people_per_facility/self.Parameters.household_size

    def headloss(self):
        daily_acid_household = self.Parameters.acid_flow_rate_m3_s #m3/s
        surface_area = math.pi*(self.Parameters.catridge_diameter/100/2)**2
        headloss = daily_acid_household*self.catridge_length/(surface_area*self.Parameters.hydraulic_conductivity)*1.1
        return headloss
    
    def pump_power(self):
        daily_acid_household = self.Parameters.acid_flow_rate_m3_s #m3/s
        p_hp = self.Parameters.specific_weight*daily_acid_household*self.number_of_cartridges_per_facility*self.Parameters.percent_served*self.headloss()/(0.3*self.Parameters.motor_efficiency)*1.34
        if p_hp<7:
            pump_efficiency=0.3
        elif 7<=p_hp<15:
            pump_efficiency=0.35
        elif 15<=p_hp<20:
            pump_efficiency=0.4
        elif 20<=p_hp<40:
            pump_efficiency=0.5
        elif 40<=p_hp<60:
            pump_efficiency=0.6
        else:
            pump_efficiency=0.7

        if p_hp>0.1:
            power = self.Parameters.specific_weight*daily_acid_household*self.number_of_cartridges_per_facility*self.Parameters.percent_served*self.headloss()/(pump_efficiency*self.Parameters.motor_efficiency)
        else:
            power = 0.1 / 1.34
        return power #KW
    
    def pump_size(self):
        size = self.pump_power()*1.34
        pump_index=pump_construction_data.set_index('Rating_hp')
        pump_size=find_nearest(pump_size_list,size)
        return pump_size
    
    def mass_pump(self):
        pump_index=pump_construction_data.set_index('Rating_hp')
        pump_size = self.pump_size()
        mass_pump=pump_index.Wt_kg[pump_size]
        return mass_pump
    
    def pump_operating_energy(self):
        energy = self.pump_power()*self.Parameters.time_for_regeneration*365/self.Parameters.time_between_catridge_regeneration*3.6
        return energy #MJ/y
    
    def pump_operating_GHG(self):
        GHG = self.pump_operating_energy()/3.6*self.Parameters.electricity_EF
        return GHG #Kg/y

    def pump_operating_cost(self):
        cost = self.pump_power()*self.Parameters.time_for_regeneration*365/self.Parameters.time_between_catridge_regeneration*self.Parameters.electricity_cost
        return cost #$/y
    
    def pump_embodied_energy(self):
        pump_index=pump_construction_data.set_index('Rating_hp')
        pump_size = self.pump_size()
        pump_energy_MJ=pump_index.Embodied_Energy_MJ[pump_size]/self.Parameters.pump_lifetime
        return pump_energy_MJ #MJ/y
    
    def pump_embodied_GHG(self):
        pump_index=pump_construction_data.set_index('Rating_hp')
        pump_size = self.pump_size()
        pump_GHG_kg=pump_index.Emissions_kgCO_eq[pump_size]/self.Parameters.pump_lifetime
        return pump_GHG_kg #MJ/y


    def pump_embodied_cost(self):
        pump_index=pump_construction_data.set_index('Rating_hp')
        pump_size = self.pump_size()
        pump_cost=pump_index.Cost_2012[pump_size]/self.Parameters.pump_lifetime
        return pump_cost #$/y

    def pump_transport(self):
        Transport_energy = find_transport_energy(self.mass_pump()/1000, self.Parameters.km, self.Parameters.pump_lifetime, self.Parameters, mode='truck')
        Transport_GHG = find_transport_GHG(self.mass_pump()/1000, self.Parameters.km, self.Parameters.pump_lifetime, self.Parameters, mode='truck')
        Transport_cost = find_transport_cost(self.mass_pump()/1000, self.Parameters.km, self.Parameters.pump_lifetime, self.Parameters, 1, mode='truck')
        return Transport_energy,Transport_GHG,Transport_cost


class regeneration():
    def __init__(self, mass_resin, number_of_people_per_facility, Parameters, acid_type):
        self.Parameters = Parameters
        self.mass_resin = mass_resin
        self.number_of_cartridges_per_facility = number_of_people_per_facility*self.Parameters.percent_served/self.Parameters.household_size
        if acid_type == 'Sulfuric':
            self.acid_per_resin = self.Parameters.acid_per_resin
            self.acid_energy = self.Parameters.sulphuric_acid_energy
            self.acid_GHG = self.Parameters.sulphuric_acid_GHG
            self.acid_cost= self.Parameters.sulphuric_acid_cost
        if acid_type == 'Nitric':
            self.acid_per_resin = self.Parameters.Nitricacid_per_resin
            self.acid_energy = self.Parameters.Nitric_acid_energy
            self.acid_GHG = self.Parameters.Nitric_acid_GHG
            self.acid_cost= self.Parameters.Nitric_acid_cost
        if acid_type == 'Hydrochloric':
            self.acid_per_resin = self.Parameters.Hydrochloricacid_per_resin
            self.acid_energy = self.Parameters.Hydrochloric_acid_energy
            self.acid_GHG = self.Parameters.Hydrochloric_acid_GHG
            self.acid_cost= self.Parameters.Hydrochloric_acid_cost
        if acid_type == 'SodiumChloride':
            self.acid_per_resin = self.Parameters.Sodiumchloride_per_resin
            self.acid_energy = self.Parameters.Sodiumchloride_energy
            self.acid_GHG = self.Parameters.Sodiumchloride_GHG
            self.acid_cost= self.Parameters.Sodiumchloride_cost
        
    def mass_sulphuric_facility(self):
        mass_sulphuric_facility = self.mass_resin*self.number_of_cartridges_per_facility*self.acid_per_resin*self.Parameters.porosity*365/self.Parameters.time_between_catridge_regeneration
        return mass_sulphuric_facility #kg_y
    
    def sulphuric_energy(self):
        sulphuric_energy = self.mass_sulphuric_facility()*self.acid_energy
        return sulphuric_energy #MJ_y
    
    def sulphuric_GHG(self):
        sulphuric_GHG = self.mass_sulphuric_facility()*self.acid_GHG 
        return sulphuric_GHG #kg_y

    def sulphuric_cost(self):
        sulphuric_cost = self.mass_sulphuric_facility()*self.acid_cost
        return sulphuric_cost #kg_y

    def acid_transport(self):
        Transport_energy = find_transport_energy(self.mass_sulphuric_facility()/1000, self.Parameters.acid_transport, 1, self.Parameters, mode='train')
        Transport_GHG = find_transport_GHG(self.mass_sulphuric_facility()/1000, self.Parameters.acid_transport, 1, self.Parameters, mode='train')
        Transport_cost = find_transport_cost(self.mass_sulphuric_facility()/1000, self.Parameters.acid_transport, 1, self.Parameters, 1, mode='train')
        return Transport_energy,Transport_GHG,Transport_cost

class bottling():
    def __init__(self, number_of_people_per_facility, mass_acid, Parameters):
        self.Parameters = Parameters
        self.mass_acid=mass_acid
        self.number_of_people_per_facility = number_of_people_per_facility
        
    def volume_ferilizer(self):
        volume_ferilizer_facility=self.Parameters.volume_fertilizer_per_acid*self.mass_acid/(self.Parameters.acid_density/1000)
        return volume_ferilizer_facility #L/y

    def area_cylinder(self):
        radius = math.sqrt(self.Parameters.volume_bottle/1000/(math.pi*self.Parameters.bottle_height))
        area = 2*math.pi*radius*self.Parameters.bottle_height+2*math.pi*radius**2
        return area
    
    def mass_plastic(self):
        area = self.area_cylinder()       
        mass = area*self.Parameters.bottle_thickness*self.Parameters.fiberglass_density*1000
        mass_total = self.volume_ferilizer()/self.Parameters.volume_bottle*mass/(self.Parameters.collection_times_per_year/2)
        return mass_total
        
    def plastic_energy(self):
        mass = self.mass_plastic()
        plastic_energy = mass*self.Parameters.fiberglass_energy_MJ_kg/self.Parameters.bottle_lifetime
        return plastic_energy #MJ_y

    def plastic_GHG(self):
        mass = self.mass_plastic()
        plastic_GHG = mass*self.Parameters.fiberglass_GHG_kg_kg/self.Parameters.bottle_lifetime
        return plastic_GHG #kg_y

    def plastic_cost(self):
        mass = self.mass_plastic()
        plastic_cost = mass*self.Parameters.fiberglass_cost_kg/self.Parameters.bottle_lifetime
        return plastic_cost # $_y

    def bottle_transport(self):
        Transport_energy = find_transport_energy(self.mass_plastic()/1000, self.Parameters.km, self.Parameters.bottle_lifetime, self.Parameters, mode='truck')
        Transport_GHG = find_transport_GHG(self.mass_plastic()/1000, self.Parameters.km, self.Parameters.bottle_lifetime, self.Parameters, mode='truck')
        Transport_cost = find_transport_cost(self.mass_plastic()/1000, self.Parameters.km, self.Parameters.bottle_lifetime, self.Parameters, 1, mode='truck')
        return Transport_energy,Transport_GHG,Transport_cost


class trucks():
    def __init__(self, num_trucks, Parameters):
        self.Parameters = Parameters
        self.num_trucks = num_trucks

    def total_energy(self):
        total_energy = self.num_trucks*self.Parameters.truck_manufacturing_energy
        return total_energy

    def total_GHG(self):
        total_GHG = self.num_trucks*self.Parameters.truck_manufacturing_GHG
        return total_GHG

    def total_cost(self):
        total_cost = self.num_trucks*self.Parameters.truck_cost_y
        return total_cost
        

class regeneration_facility():
    def __init__(self, number_of_people_per_facility, Parameters, cartridge_length, scenario):
        self.Parameters = Parameters
        self.number_of_cartridges_per_facility = number_of_people_per_facility*self.Parameters.percent_served/self.Parameters.household_size
        self.cartridge_length = cartridge_length
        self.scenario = scenario

    def total_energy(self):
        total_energy = self.Parameters.facility_manufacturing_energy/self.Parameters.facility_lifetime
        return total_energy

    def total_GHG(self):
        total_GHG = self.Parameters.facility_manufacturing_GHG/self.Parameters.facility_lifetime
        return total_GHG

    def total_cost(self):
        total_cost = facility_manufacturing_curve(self.number_of_cartridges_per_facility, self.Parameters.catridge_diameter, self.cartridge_length, self.Parameters.facility_cost_regression, self.scenario)
        return total_cost


class logistics():
    def __init__(self, tons, distance, Parameters, truck_num):
        self.tons = tons
        self.distance=distance
        self.Parameters = Parameters
        self.truck_num = truck_num
            
    def transportation_energy(self):
        logistics_transport_energy=find_transport_energy(self.tons, self.distance, 1, self.Parameters)
        return logistics_transport_energy #MJ_y
    
    def transportation_GHG(self):
        logistics_transport_GHG=find_transport_GHG(self.tons, self.distance, 1, self.Parameters)
        return logistics_transport_GHG #kg_y

    def transportation_cost(self):
        logistics_transport_cost=find_transport_cost(self.tons, self.distance, 1, self.Parameters, self.truck_num)
        return logistics_transport_cost #$_y
    
