# Part A: The Base TV class
class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.channel = 1  # Default channel is 1
        self.volume = 50  # Default volume is 50
        self.price = price
        self.inches = inches
        self.on_off_status = False  # TV is off by default

    def increase_volume(self):
        """Increase volume but ensure it stays between 0 and 100."""
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        """Decrease volume but ensure it stays between 0 and 100."""
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        """Set the channel to a valid number between 1 and 50."""
        if 1 <= channel <= 50:
            self.channel = channel

    def reset(self):
        """Reset the TV settings to default values."""
        self.channel = 1
        self.volume = 50

    def status(self):
        """Return the current status of the TV."""
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

# Part B: LED TV class inheriting from TV
class LED(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness  # Thickness of the screen in mm
        self.energy_usage = energy_usage  # Energy consumption in watts
        self.lifespan = lifespan  # Expected lifespan in hours
        self.refresh_rate = refresh_rate  # Refresh rate in Hz

    def viewing_angle(self):
        """Display the viewing angle of the LED TV."""
        print("Viewing angle is 178 degrees.")

    def backlight(self):
        """Display backlight feature of the LED TV."""
        print("LED TV uses LED backlighting.")

    def display_details(self):
        """Display detailed features of the LED TV."""
        return (f"LED TV details:\n"
                f"Screen thickness: {self.screen_thickness} mm\n"
                f"Energy usage: {self.energy_usage} watts\n"
                f"Lifespan: {self.lifespan} hours\n"
                f"Refresh rate: {self.refresh_rate} Hz\n"
                f"Viewing angle: 178 degrees\n"
                f"Backlight: Yes")

# Part B: Plasma TV class inheriting from TV
class Plasma(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness  # Thickness of the screen in mm
        self.energy_usage = energy_usage  # Energy consumption in watts
        self.lifespan = lifespan  # Expected lifespan in hours
        self.refresh_rate = refresh_rate  # Refresh rate in Hz

    def viewing_angle(self):
        """Display the viewing angle of the Plasma TV."""
        print("Viewing angle is 160 degrees.")

    def backlight(self):
        """Display backlight feature of the Plasma TV."""
        print("Plasma TV uses traditional backlighting.")

    def display_details(self):
        """Display detailed features of the Plasma TV."""
        return (f"Plasma TV details:\n"
                f"Screen thickness: {self.screen_thickness} mm\n"
                f"Energy usage: {self.energy_usage} watts\n"
                f"Lifespan: {self.lifespan} hours\n"
                f"Refresh rate: {self.refresh_rate} Hz\n"
                f"Viewing angle: 160 degrees\n"
                f"Backlight: Yes")

# Example usage:
# Create a LED TV object
led_tv = LED(brand="Samsung", price=500, inches=55, screen_thickness=6, energy_usage=120, lifespan=50000, refresh_rate=120)

# Display details of the LED TV
print(led_tv.display_details())

# Call methods on the LED TV object
led_tv.set_channel(5)
led_tv.increase_volume()
led_tv.increase_volume()
print(led_tv.status())

# Create a Plasma TV object
plasma_tv = Plasma(brand="LG", price=700, inches=60, screen_thickness=10, energy_usage=200, lifespan=40000, refresh_rate=60)

# Display details of the Plasma TV
print(plasma_tv.display_details())

# Call methods on the Plasma TV object
plasma_tv.set_channel(20)
plasma_tv.decrease_volume()
print(plasma_tv.status())
