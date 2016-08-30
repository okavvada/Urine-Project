from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


from Parameters import *

pipe_construction_data = pd.read_csv('pipe_construction_data.csv')
pump_construction_data = pd.read_csv('pump_construction_data.csv')
pipe_construction_data=pipe_construction_data[pipe_construction_data['Material']=='PVC']
nominal_diameter_list=np.array(pipe_construction_data['size_mm'])
pump_size_list=np.array(pump_construction_data['Rating_hp'])


def find_transport_energy(miles,lifetime):
    transport_energy = transport_energy_MJ_mile*miles/(lifetime)
    return transport_energy #MJ_y
    
def find_transport_GHG(miles,lifetime):
    transport_GHG = transport_GHG_kg_mile*miles/(lifetime)
    return transport_GHG #kg_y

def find_nearest(array,value):
    idx = (np.abs(array-value)).argmin()
    return array[idx]


class resin():
    def __init__(self, number_of_people_per_facility):
        self.number_of_houses_per_facility = number_of_people_per_facility/household_size

    def mass_resin_household(self):
        daily_urine_household = household_size*urine_production_scaled #L/day
        volume_urine_treated_before_replacement = time_between_catridge_regeneration*daily_urine_household #L
        mass_resin_household=volume_urine_treated_before_replacement*N_urine/(adsorption_density*molar_mass_N)#kg
        return mass_resin_household #kg
    
    def resin_energy(self):
        resin_energy = self.mass_resin_household()*resin_energy_MJ_kg/resin_lifetime*self.number_of_houses_per_facility
        return resin_energy #MJ_y
    
    def resin_GHG(self):
        resin_GHG = self.mass_resin_household()*resin_GHG_kg_kg/resin_lifetime*self.number_of_houses_per_facility
        return resin_GHG #kg_y
    
    def transportation_energy(self):
        resin_transport_energy=find_transport_energy(miles, resin_lifetime)
        return resin_transport_energy #MJ_y
    
    def transportation_GHG(self):
        resin_transport_GHG=find_transport_GHG(miles, resin_lifetime)
        return resin_transport_GHG #kg_y
    
    def total_energy(self):
        total_energy = self.resin_energy()+self.transportation_energy()
        return total_energy #MJ_y
    
    def total_GHG(self):
        total_GHG = self.resin_GHG()+self.transportation_GHG()
        return total_GHG #kg_y


class catridge():
    def __init__(self, diameter, mass_resin_household, number_of_people_per_facility):
        self.diameter = diameter
        self.number_of_houses_per_facility = number_of_people_per_facility/household_size
        self.mass_resin_household = mass_resin_household
        
    def catridge_volume(self):
        catridge_volume = self.mass_resin_household/resin_density*1000 #L
        return catridge_volume
    
    def catridge_length(self):
        catridge_length = self.catridge_volume()*1000/(math.pi*((self.diameter/10)/2)**2)/100 #m
        return catridge_length
    
    def mass_PVC(self):
        diameter_mm=self.diameter
        diameter=find_nearest(nominal_diameter_list,diameter_mm)
        pipe_index=pipe_construction_data.set_index('size_mm')
        pipe_weight_kg=pipe_index.Wt_kg_m[diameter]*self.catridge_length()*self.number_of_houses_per_facility
        return pipe_weight_kg

    def PVC_energy(self):
        pipe_index=pipe_construction_data.set_index('size_mm')
        diameter_mm=self.diameter
        diameter=find_nearest(nominal_diameter_list,diameter_mm)
        PVC_energy_MJ=pipe_index.Embodied_Energy_MJ_kg[diameter]*self.mass_PVC()/PVC_lifetime
        return PVC_energy_MJ #MJ_y

    def PVC_GHG(self):
        pipe_index=pipe_construction_data.set_index('size_mm')
        diameter_mm=self.diameter
        diameter=find_nearest(nominal_diameter_list,diameter_mm)
        PVC_GHG_kg=pipe_index.Emissions_kgCO2_eq_m[diameter]*self.catridge_length()*self.number_of_houses_per_facility/PVC_lifetime
        return PVC_GHG_kg #kg_y
    
    def transportation_energy(self):
        PVC_transport_energy=find_transport_energy(miles, PVC_lifetime)
        return PVC_transport_energy #MJ_y
    
    def transportation_GHG(self):
        PVC_transport_GHG=find_transport_GHG(miles, PVC_lifetime)
        return PVC_transport_GHG #kg_y
    
    def total_energy(self):
        total_energy = self.PVC_energy()+self.transportation_energy()
        return total_energy #MJ_y
    
    def total_GHG(self):
        total_GHG = self.PVC_GHG()+self.transportation_GHG()
        return total_GHG #kg_y


class flow_equalization_plastic():
    def __init__(self, number_of_people_per_facility):
    	self.number_of_houses_per_facility = number_of_people_per_facility/household_size
        
    def volume(self):
        daily_urine_household = household_size*urine_production_scaled #L/day
        volume = daily_urine_household*flow_equalization_retention_time/1000*self.number_of_houses_per_facility
        return volume #m3
    
    def area_cylinder(self):
        radius = math.sqrt(self.volume()/(math.pi*tank_height))
        area = 2*math.pi*radius*tank_height+2*math.pi*radius**2
        return area
    
    def mass_plastic(self):
        area = self.area_cylinder()       
        mass = area*tank_thickness*plastic_density
        return mass
        
    def plastic_energy(self):
        mass = self.mass_plastic()
        plastic_energy = mass*plastic_energy_MJ_kg/plastic_lifetime
        return plastic_energy #MJ_y

    def plastic_GHG(self):
        mass = self.mass_plastic()
        plastic_GHG = mass*plastic_GHG_kg_kg/plastic_lifetime
        return plastic_GHG #kg_y
    
    def transportation_energy(self):
        plastic_transport_energy=find_transport_energy(miles, plastic_lifetime)
        return plastic_transport_energy #MJ_y
    
    def transportation_GHG(self):
        plastic_transport_GHG=find_transport_GHG(miles, plastic_lifetime)
        return plastic_transport_GHG #kg_y
    
    def total_energy(self):
        total_energy = self.plastic_energy()+self.transportation_energy()
        return total_energy #MJ_y
    
    def total_GHG(self):
        total_GHG = self.plastic_GHG()+self.transportation_GHG()
        return total_GHG #kg_y


class pump_flow():
    def __init__(self, catridge_diameter,catridge_length, number_of_people_per_facility):
        self.catridge_diameter = catridge_diameter
        self.catridge_length = catridge_length
        self.number_of_houses_per_facility =number_of_people_per_facility/household_size

    def headloss(self):
        daily_urine_household = (household_size*urine_production_scaled)/(24*3600*1000) #m3/s
        surface_area = math.pi*(self.catridge_diameter/1000/2)**2
        headloss = daily_urine_household*self.catridge_length/(surface_area*hydraulic_conductivity)
        return headloss
    
    def pump_power(self):
        daily_urine_household = (household_size*urine_production_scaled)/(24*3600*1000)*self.number_of_houses_per_facility #m3/s
        p_hp = specific_weight*daily_urine_household*self.headloss()*self.number_of_houses_per_facility/(0.4*motor_efficiency)*1.34
        if p_hp<3:
            pump_efficiency=0.4
        elif 3<=p_hp<7:
            pump_efficiency=0.45
        elif 7<=p_hp<15:
            pump_efficiency=0.5
        elif 15<=p_hp<40:
            pump_efficiency=0.55
        elif 40<=p_hp<60:
            pump_efficiency=0.6
        else:
            pump_efficiency=0.7

        power = specific_weight*daily_urine_household*self.headloss()*self.number_of_houses_per_facility/(pump_efficiency*motor_efficiency)
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
        energy = self.pump_power()*24*365*3.6
        return energy #MJ/y
    
    def pump_operating_GHG(self):
        GHG = self.pump_operating_energy()/3.6*electricity_EF
        return GHG #Kg/y
    
    def pump_embodied_energy(self):
        pump_index=pump_construction_data.set_index('Rating_hp')
        pump_size = self.pump_size()
        pump_energy_MJ=pump_index.Embodied_Energy_MJ[pump_size]/pump_lifetime
        return pump_energy_MJ #MJ/y
    
    def pump_embodied_GHG(self):
        pump_index=pump_construction_data.set_index('Rating_hp')
        pump_size = self.pump_size()
        pump_GHG_kg=pump_index.Emissions_kgCO_eq[pump_size]/pump_lifetime
        return pump_GHG_kg #MJ/y
        
    def transportation_energy(self):
        pump_transport_energy=find_transport_energy(miles, pump_lifetime)
        return pump_transport_energy #MJ_y
    
    def transportation_GHG(self):
        pump_transport_GHG=find_transport_GHG(miles, pump_lifetime)
        return pump_transport_GHG #kg_y
    
    def total_energy(self):
        total_energy = self.pump_operating_energy()+pump_embodied_energy+self.transportation_energy()
        return total_energy #MJ_y
    
    def total_GHG(self):
        total_GHG = self.pump_operating_GHG()+pump_embodied_GHG+self.transportation_GHG()
        return total_GHG #kg_y    


class regeneration():
    def __init__(self, mass_resin, acid_per_resin, number_of_people_per_facility):
        self.mass_resin=mass_resin
        self.acid_per_resin=acid_per_resin
        self.number_of_houses_per_facility = number_of_people_per_facility/household_size
        
    def mass_sulphuric_facility(self):
        mass_sulphuric_facility=self.mass_resin*self.number_of_houses_per_facility*self.acid_per_resin*365/time_between_catridge_regeneration
        return mass_sulphuric_facility #kg_y
    
    def sulphuric_energy(self):
        sulphuric_energy = self.mass_sulphuric_facility()*sulphuric_acid_energy
        return sulphuric_energy #MJ_y
    
    def sulphuric_GHG(self):
        sulphuric_GHG = self.mass_sulphuric_facility()*sulphuric_acid_GHG
        return sulphuric_GHG #kg_y
    
    def transportation_energy(self):
        sulphuric_transport_energy=find_transport_energy(miles, 1)
        return sulphuric_transport_energy #MJ_y
    
    def transportation_GHG(self):
        sulphuric_transport_GHG=find_transport_GHG(miles, 1)
        return sulphuric_transport_GHG #kg_y
    
    def total_energy(self):
        total_energy = self.sulphuric_energy()+self.transportation_energy()
        return total_energy #MJ_y
    
    def total_GHG(self):
        total_GHG = self.sulphuric_GHG()+self.transportation_GHG()
        return total_GHG #kg_y


class logistics():
    def __init__(self, distance):
        self.distance=distance
            
    def transportation_energy(self):
        logistics_transport_energy=find_transport_energy(self.distance,1)
        return logistics_transport_energy #MJ_y
    
    def transportation_GHG(self):
        logistics_transport_GHG=find_transport_GHG(self.distance,1)
        return logistics_transport_GHG #kg_y
    
    def total_energy(self):
        total_energy = self.transportation_energy()
        return total_energy #MJ_y
    
    def total_GHG(self):
        total_GHG = self.transportation_GHG()
        return total_GHG #kg_y