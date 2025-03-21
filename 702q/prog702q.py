from cl702q import *


def main():
    try:
        vehicles: list[Vehicle] = []
        with open("../Langdat/prog702q(1).txt", 'r') as f:
            num = int(f.readline())
            while num != 99:
                name = f.readline()
                tires = int(f.readline())
                if num == 1:
                    worth = float(f.readline())
                    v = Car(name, tires, worth)
                    vehicles.append(v)
                elif num == 2:
                    miles = int(f.readline())
                    v = Truck(name, tires, miles)
                    vehicles.append(v)
                elif num == 3:
                    home = f.readline().strip()
                    v = Bus(name, tires, home)
                    vehicles.append(v)
                num = int(f.readline())
            vehicle_amount = 0.0
            car_worth = 0.0
            car_tires = 0
            truck_tires = 0
            bus_tires = 0
            low_truck_value = 10000
            large = ""
            for vehicle in vehicles:
                if isinstance(Vehicle, Car):
                    car_worth += vehicle.worth
                    vehicle_amount += 1
                    car_tires += 1
                elif isinstance(Vehicle, Truck):
                    worth = 50000 - vehicle.miles / 4
                    if worth < low_truck_value:
                        low_truck_value = worth
                    vehicle_amount += 1
                    truck_tires += 1
                elif isinstance(Vehicle, Bus):
                    h = vehicle.home
                    vehicle_amount += 1
                    bus_tires += 1
                    if len(h) > len(large):
                        large = h
            print("Total number of vehicles:", vehicle_amount)
            print("Total worth of all cars:", car_worth)
            print("Longest name of bus hometown:", large)
            print("Lowest value truck:", low_truck_value)
            print("Total number of car tires:", car_tires)
            print("Total number of truck tires:", truck_tires)
            print("Total number of bus tires:", bus_tires)
    except Exception as e:
        print("Error:", e)
    pass


if __name__ == "__main__":
    main()
