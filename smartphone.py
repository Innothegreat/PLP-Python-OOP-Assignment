class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        print(f"Device: {self.brand} {self.model}")


# Child class: Smartphone (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call parent constructor
        self.brand = brand
        self.model = model
        self.storage = storage  # GB
        self.battery = battery  # mAh

    # Method to check storage
    def check_storage(self):
        print(f"Storage available: {self.storage} GB")


    # Method to check battery
    def check_battery(self):
        print(f"Battery: {self.battery} mAh")


# Example usage
#creating an objects of Smartphone class
phone1 = Smartphone("Samsung", "Galaxy S23", 256, 5000)
phone2 = Smartphone("Apple", "iPhone 14", 128, 3200)

print(phone1.device_info())
print(phone1.check_storage())
print(phone1.check_battery())
print(phone2.device_info())
print(phone2.check_storage())
print(phone2.check_battery())
