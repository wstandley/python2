"""
    This is for assignment OOP 2.8 Composition vs Inheritance
"""

class Device:
    def __init__(self, device_name, status, power_method):
        self.device_name = device_name
        self.status = status
        self.power_method = power_method

class Light(Device):
    def __init__(self, device_name, status, power_method, brightness_level):
        super().__init__(device_name, status, power_method)
        self.brightness_level = brightness_level


class LEDLight(Light):
    def __init__(self, device_name, status, power_method, brightness_level, light_color):
        super().__init__(device_name, status, power_method, brightness_level)
        self.light_color = light_color

    def power_status(self):
        return f"{self.status}"
    
    def brightness(self):
        return f"{self.brightness_level}%"

class SmartBulb(Light):
    def __init__(self, device_name, status, power_method, brightness_level, light_color, connectivity):
        super().__init__(device_name, status, power_method, brightness_level)
        self.light_color = light_color
        self.connectivity = connectivity

    def power_status(self):
        return f"{self.status}"

class Thermostat(Device):
    def __init__(self, device_name, status, power_method, current_temperature, target_temperature):
        super().__init__(device_name, status, power_method)
        self.current_temperature = current_temperature
        self.target_temperature = target_temperature

    def power_status(self):
        return f"{self.status}"
    
    def current_temperature_amount(self):
        return f"{self.current_temperature}"
    
    def target_temperature_amount(self):
        return f"{self.target_temperature}"

class SmartHome:
    def __init__(self, led_lights, smart_bulbs, thermostats):
        self.led_lights = led_lights
        self.smart_bulbs = smart_bulbs
        self.thermostats = thermostats

    def display_devices(self):
        print("Devices:")
        print(f"1. Living Room Light - Status: {self.led_lights.power_status()}, Brightness: {self.led_lights.brightness()}")
        print(f"2. Bedroom Light - Status: {self.smart_bulbs.power_status()}")
        print(f"3. Thermostat - Status: {self.thermostats.power_status()}, Current Temperature: {self.thermostats.current_temperature_amount()}, Target Temperature: {self.thermostats.target_temperature_amount()} ")

    def user_actions(self):
        change_devices = True

        while change_devices == True:
            self.display_devices()
            print("\nActions:")

            if led_lights.status == "OFF":
                print("1. Turn Living Room light ON")
            else:
                print("1. Turn Living Room light OFF")

            if led_lights.brightness_level == 80:
                print("2. Set Living Room brightness to 40")
            else:
                print("2. Set Living Room brightness to 80")

            if smart_bulbs.status == "OFF":
                print("3. Turn Bedroom light ON")
            else:
                print("3. Turn Bedroom light OFF")

            if thermostats.status == "OFF":
                print("4. Turn Thermostat ON")
            else:
                print("4. Turn Thermostat OFF")

            if thermostats.target_temperature == "70°":
                print("5. Set Target Temperature to 74°")
            else:
                print("5. Set Target Temperature to 70°")

            choice_action = input("\nType one of the above number to perform Action\nIf you want to stop, type 0: ")

            if choice_action == "1":
                if self.led_lights.status == "OFF":
                    self.led_lights.status = "ON"
                    print(f"Living Room Light has been turned ON.")
                else:
                    self.led_lights.status = "OFF"
                    print(f"Living Room Light has been turned OFF.")
            elif choice_action == "2":
                if self.led_lights.brightness_level == 80:
                    self.led_lights.brightness_level = 40
                    print(f"Living Room Light has been set to 40.")
                else:
                    self.led_lights.brightness_level = 80
                    print(f"Living Room Light has been set to 80.")
            elif choice_action == "3":
                if self.smart_bulbs.status == "OFF":
                    self.smart_bulbs.status = "ON"
                    print(f"Bedroom Light has been turned ON.")
                else:
                    self.smart_bulbs.status = "OFF"
                    print(f"Bedroom Light has been turned OFF.")
            elif choice_action == "4":
                if self.thermostats.status == "OFF":
                    self.thermostats.status = "ON"
                    print(f"Thermostat has been turned ON.")
                else:
                    self.thermostats.status = "OFF"
                    print(f"Thermostat has been turned OFF.")
            elif choice_action == "5":
                if self.thermostats.target_temperature == "70°":
                    self.thermostats.target_temperature = "74°"
                    print(f"Thermostat has been set to 74°.")
                else:
                    self.thermostats.target_temperature = "70°"
                    print(f"Thermostat has been set to 70°")
            elif choice_action == "0":
                # Stop listing actions
                change_devices = False
            else:
                print("That number was not an action on the list, try again.")
        
led_lights = LEDLight(device_name = "Living Room light", status = "OFF", power_method = "Light Switch", brightness_level = 80, light_color = "Yellow")
smart_bulbs = SmartBulb(device_name = "Bedroom light", status = "OFF", power_method = "Light Switch", brightness_level = 40, light_color = "Purple", connectivity = "WiFi")
thermostats = Thermostat(device_name = "Main Thermostat", status = "ON", power_method = "Constant", current_temperature = "74°", target_temperature = "70°")

devices = SmartHome(led_lights, smart_bulbs, thermostats)

devices.user_actions()