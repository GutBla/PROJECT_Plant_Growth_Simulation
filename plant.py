import math

from colorama import Fore
from art import plant_art

class Plant:
    def __init__(self, name, p0, growth_rate):
        self.name = name
        self.size = p0
        self.growth_rate = growth_rate
        self.health = 100
        self.phase = "Inicio"
        self.contamination_level = 0
        self.temperature = 20
        self.age = 0
        self.water = 10
        self.fertilizer = 5
        self.protection = 1
    def update_phase(self):
        if self.age < 3:
            self.phase = "Germinación"
        elif 3 <= self.age < 6:
            self.phase = "Plántula"
        elif 6 <= self.age < 8:
            self.phase = "Crecimiento"
        elif 8 <= self.age < 11:
            self.phase = "Floración"
        elif 11 <= self.age < 14:
            self.phase = "Fructificación"
        elif 14 <= self.age < 16:
            self.phase = "Madurez"
        else:
            self.phase = "Muerte"
    def calculate_growth(self, t):
        return self.size * math.exp(self.growth_rate * t)
    def update_contamination(self, planet, t):
        x = 0.01
        self.contamination_level += x * self.calculate_growth(t)
        if self.contamination_level > 50:
            self.health -= 5
    def update_temperature(self):
        y = 0.05
        self.temperature += y * self.contamination_level
        if self.temperature > 40:
            self.health -= 10
    def apply_fertilizer(self):
        print("\n╔══════════════════════════════════════════════════╗")
        if self.fertilizer > 0:
            self.growth_rate *= 1.2
            self.contamination_level += 5
            self.fertilizer -= 1
            print(f"🌱 Has usado fertilizante. Crecimiento: {self.growth_rate:.2f}, Contaminación: {self.contamination_level:.2f}")
        else:
            print("⚠️ No tienes fertilizante disponible.")
        print("╚══════════════════════════════════════════════════╝")
    def water_plant(self):
        print("\n╔══════════════════════════════════════════════════╗")
        if self.water > 0:
            self.health += 5
            self.temperature -= 2
            self.water -= 1
            print(f"💧 Has regado la planta. Salud: {self.health}, Temperatura: {self.temperature}°C")
        else:
            print("⚠️ No tienes agua disponible.")
        print("╚══════════════════════════════════════════════════╝")
    def protect_plant(self):
        print("\n╔══════════════════════════════════════════════════╗")
        if self.protection > 0:
            self.protection -= 0.1
            print(f"🛡️ Has protegido la planta. Protección restante: {self.protection * 100}%")
            print("╚══════════════════════════════════════════════════╝")
            return True
        else:
            print("⚠️ No tienes protección disponible.")
            print("╚══════════════════════════════════════════════════╝")
            return False
    def recharge_protection(self):
        self.protection = 1
        print("\n🔄 Protección recargada al 100%.")
    def display_status(self):
        print("╔══════════════════════════════════╗")
        print(f"🌱 Planta: {self.name}")
        print("╚══════════════════════════════════╝")
        print(plant_art[self.phase])
        print("╔══════════════════════════════════╗")
        print(f"║ Fase: {self.phase}")
        print(f"║ Tamaño: {self.size:.2f}")
        print(f"║ Salud: {self.health}")
        print(f"║ Contaminación: {self.contamination_level:.2f}")
        print(f"║ Temperatura: {self.temperature:.2f}°C")
        print(f"║ Días vivos: {self.age}")
        print("╚══════════════════════════════════╝")
        print("-" * 30)
    def log_daily_changes(self, prev_size, prev_health, prev_contamination, prev_temperature):
        size_change = self.size - prev_size
        health_change = self.health - prev_health
        contamination_change = self.contamination_level - prev_contamination
        temperature_change = self.temperature - prev_temperature
        print("\n╔════════════════════════════════════════════════════╗")
        print("║ 📊 Cambios del día                                  ║")
        print("╠════════════════════════════════════════════════════╣")
        print(f"║ 🔸 Cambio en tamaño: {'+' if size_change > 0 else ''}{size_change:.2f}            ║")
        print(f"║ ❤️ Cambio en salud: {'+' if health_change > 0 else ''}{health_change:.2f}          ║")
        print(f"║ ☣️  Cambio en contaminación: {'+' if contamination_change > 0 else ''}{contamination_change:.2f} ║")
        print(f"║ 🌡️ Cambio en temperatura: {'+' if temperature_change > 0 else ''}{temperature_change:.2f} ║")
        print("╚════════════════════════════════════════════════════╝")
        print("=" * 50)
