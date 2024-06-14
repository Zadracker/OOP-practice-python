# Challenge: Create a Car class with attributes like make, model, and year, and methods like start and stop.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def set_manufacture_year_range(self):
        self.manufacture_year_begin = int(input("Start of year of manufacturing: "))
        self.manufacture_year_end = int(input("Ending of year of manufacturing: "))
    
    def print_car_details(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")
        if hasattr(self, 'manufacture_year_begin') and hasattr(self, 'manufacture_year_end'):
            print(f"Manufacture Year Range: {self.manufacture_year_begin} to {self.manufacture_year_end}")

# Creating an instance of the Car class
ford_mustang = Car("Ford", "Mustang", 1964)
ford_mustang.print_car_details()

# Setting the manufacture year range
ford_mustang.set_manufacture_year_range()

# Printing the updated car details
ford_mustang.print_car_details()