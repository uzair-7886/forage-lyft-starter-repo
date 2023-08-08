from car import Car

from engine.capulet_engine import CapuletEngine 
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.splinder_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car = Car()
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        car.set_engine(engine)
        car.set_battery(battery)
        return car
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car = Car() 
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        car.set_engine(engine)
        car.set_battery(battery)
        return car 
    
    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car = Car() 
        engine = SternmanEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        car.set_engine(engine)
        car.set_battery(battery)
        return car
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car = Car() 
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        car.set_engine(engine)
        car.set_battery(battery)
        return car 
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car = Car() 
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        car.set_engine(engine)
        car.set_battery(battery)
        return car 