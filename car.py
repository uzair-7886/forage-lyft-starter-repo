from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self):
        self.engine = None
        self.battery = None

    def set_engine(self, engine):
        self.engine = engine

    def set_battery(self, battery):
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()