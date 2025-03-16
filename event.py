import random

class Event:
    def __init__(self, plant):
        self.plant = plant
        self.last_negative = False
    def random_event(self):
        event_chance = random.random()
        if self.last_negative and event_chance < 0.7:
            event_chance = 0.95
        print("\n╔══════════════════════════════════╗")
        print("║ ⚡ Evento aleatorio:              ║")
        print("╚══════════════════════════════════╝")
        if event_chance < 0.1:
            print("╔══════════════════════════════════╗")
            print("║ ⚠️  Tormenta solar detectada.    ║")
            print("║ 🛑 Efecto: Salud -10 puntos.      ║")
            print("╚══════════════════════════════════╝")
            self.plant.health -= 10
            self.last_negative = True
        elif event_chance < 0.2:
            print("╔══════════════════════════════════╗")
            print("║ 🟡 Lluvia ácida.                 ║")
            print("║ 🌧️ Efecto: Contaminación +5, Salud +5 puntos. ║")
            print("╚══════════════════════════════════╝")
            self.plant.contamination_level += 5
            self.plant.health += 5
            self.last_negative = False
        elif event_chance < 0.3:
            print("╔══════════════════════════════════╗")
            print("║ ❄️  Eclipse solar.               ║")
            print("║ 🌌 Efecto: Temperatura baja, crecimiento ralentizado. ║")
            print("╚══════════════════════════════════╝")
            self.plant.update_temperature()
            self.plant.growth_rate *= 0.5
            self.last_negative = True
        elif event_chance < 0.7:
            print("╔══════════════════════════════════╗")
            print("║ 🐛 Plaga de insectos.            ║")
            print("║ 🟢 Efecto: Salud -10, Tamaño -10%.║")
            print("╚══════════════════════════════════╝")
            self.plant.health -= 10
            self.plant.size *= 0.9
            self.last_negative = True
        elif event_chance < 0.8:
            print("╔══════════════════════════════════╗")
            print("║ 🌟 Sol radiante.                ║")
            print("║ ☀️  Efecto: Crecimiento acelerado. ║")
            print("╚══════════════════════════════════╝")
            self.plant.temperature += 2
            self.plant.size += self.plant.growth_rate * 2
            self.last_negative = False
        elif event_chance < 0.9:
            print("╔══════════════════════════════════╗")
            print("║ ✨ Fertilizante natural.         ║")
            print("║ 🌿 Efecto: Salud +15, Tamaño +1.  ║")
            print("╚══════════════════════════════════╝")
            self.plant.health = min(100, self.plant.health + 15)
            self.plant.size += 1.0
            self.last_negative = False
        else:
            print("╔══════════════════════════════════╗")
            print("║ ⚖️  Ambiente estable, sin impacto.║")
            print("╚══════════════════════════════════╝")
            self.last_negative = False
