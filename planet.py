
from colorama import Fore

class Planet:
    def __init__(self, name, light_hours, co2, humidity, water, nutrients, contamination, radiation, description, color):
        self.name = name
        self.light_hours = light_hours
        self.co2 = co2
        self.humidity = humidity
        self.water = water
        self.nutrients = nutrients
        self.contamination = contamination
        self.radiation = radiation
        self.description = description
        self.color = color

def create_planets():
    return [
        Planet("Gaiara", 12, 0.78, 0.60, 0.50, 0.70, 0.30, 0.40, "Un planeta de pruebas con desafíos moderados.", Fore.GREEN),
        Planet("Dunaris", 10, 0.96, 0.10, 0.20, 0.30, 0.70, 0.80, "Desiertos eternos y tormentas de arena.", Fore.YELLOW),
        Planet("Aquara", 14, 0.50, 0.90, 0.80, 0.60, 0.20, 0.50, "Planeta oceánico con alta humedad.", Fore.MAGENTA),
        Planet("Frostis", 6, 0.80, 0.20, 0.10, 0.40, 0.10, 0.20, "Un mundo helado con temperaturas extremas.", Fore.CYAN),
        Planet("Vulcanis", 8, 0.70, 0.10, 0.10, 0.20, 0.90, 0.95, "Montañas volcánicas y tormentas de lava.", Fore.RED),
        Planet("Aetheris", 10, 0.85, 0.40, 0.30, 0.80, 0.25, 0.70, "Un planeta cristalino con radiación intensa.", Fore.MAGENTA)
    ]
