class vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage

class bus(vehicle):
    pass

school_bus = bus("School Volvo", 180, 12)
print("vehicle name:",school_bus.name)
print("speed:", school_bus.maxspeed)
print("mileage:", school_bus.mileage)
        
        