class Car:
    def __init__(self, maxspeed, unit):
        self.maxspeed = maxspeed
        self.unit = unit
    def show_car(self):
        print("Car with the maximum speed of",self.maxspeed,self.unit)
        
       
        
    pass

class Boat:
    def __init__(self,max_speed_in_knots):
        self.max_speed_in_knots = max_speed_in_knots
    def show_Boat(self):
        print("Boat with the maximum speed of",self.max_speed_in_knots)
   
    pass
if __name__ == '__main__':
    vehicle = Car('120','km/h')
    vehicle.show_car()