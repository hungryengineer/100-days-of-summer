class Car:
    def __init__(self, price,color,topspeed):
        self.price = price
        self.color = color
        self.topspeed = topspeed
        self.engine_type = 0
        self.power = 0
        self.displacement = 0
        self.torque = 0

    def engine(self, power, displacement, torque):
        # self.engine_details = {
        # 'power': power,
        # 'displacement': displacement,
        # 'torque': torque
        # }
        self.power = power
        self.displacement = 0
        self.torque = 0



#now using constructors
audi = Car("$55000", "red", "200kmph")
audi.fuel_type = "gas"
audi.engine("200HP","3000cc","300nm")

bmw = Car("$65000", "white", "160kmph")
bmw.fuel_type = "electric"
print(f"Audi specs:{audi.price}\n{audi.color}\n{audi.topspeed}\n{audi.fuel_type}\n{audi.power}\n\n"
      f"BMW specs:{bmw.price}\n{bmw.color}\n{bmw.topspeed}\n{bmw.fuel_type}\n")
