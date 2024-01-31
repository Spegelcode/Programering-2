# Överklass (Superklass)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} startar.")

    def stop(self):
        print(f"{self.brand} {self.model} stannar.")


# Underklass (Subklass) som ärver från Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        # Anropa överklassens konstruktor för att ärva egenskaperna brand och model
        super().__init__(brand, model)
        self.num_doors = num_doors

    def open_doors(self):
        print(f"{self.brand} {self.model} har {self.num_doors} dörrar som öppnas.")


# Skapa ett objekt av Car-klassen och använda dess metoder
my_car = Car("Volvo", "XC60", 5)
my_car.start()  # Output: "Volvo XC60 startar."
my_car.open_doors()  # Output: "Volvo XC60 har 5 dörrar som öppnas."
my_car.stop()  # Output: "Volvo XC60 stannar."
