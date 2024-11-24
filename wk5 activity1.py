class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def display_info(self):
        print(f"Smartphone Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery Life: {self.battery_life} hours")

    def check_battery(self):
        if self.battery_life > 20:
            return "Battery is good!"
        elif self.battery_life > 0:
            return "Battery is low!"
        else:
            return "Battery is dead!"

# Subclass with additional functionality
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery_life, camera_quality):
        super().__init__(brand, model, battery_life)
        self.camera_quality = camera_quality  # in megapixels

    def take_photo(self):
        return f"Taking a photo with {self.camera_quality}MP camera!"

# Example usage
smartphone = Smartphone("Apple", "iPhone 14", 24)
smartphone.display_info()
print(smartphone.check_battery())

camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S21", 18, 108)
camera_phone.display_info()
print(camera_phone.take_photo())
