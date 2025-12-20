class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f"House: {self.area} m2, rooms={self.rooms}, price={self.price}, "
            f"address={self.address}, plot={self.plot} m2")

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Flat: {self.area} m2, rooms={self.rooms}, price={self.price}, "
            f"address={self.address}, floor={self.floor}")

house1 = House(area=100, rooms=7, price=150000, address="Kraków, ul. Długa 125/6", plot=255)

flat1 = Flat(area=222,rooms=8,price=450000, address="Kraków, ul. Wincentego Witosa 3/12", floor=7)

print(house1)
print(flat1)