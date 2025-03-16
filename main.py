
from art import planet_art, game_text_art, ascii_art_titles, colors
from planet import create_planets
from plant import Plant
from utils import validate_positive_float
from event import Event
from clear_screen import clear

def derivada_tamaño(tamaño_actual, tasa_crecimiento, salud):
    return (tamaño_actual + tasa_crecimiento) * (salud / 100)

def integral_salud(salud_actual, temperatura, contaminacion, dias):
    daño_acumulado = (temperatura + contaminacion) * dias
    salud_nueva = salud_actual - daño_acumulado
    return max(0, min(salud_nueva, 100))

def integral_contaminacion(contaminacion_actual, dias):
    return contaminacion_actual + 0.1 * dias

def derivada_temperatura(temperatura_actual, eventos):
    if eventos == "tormenta solar":
        return 10
    elif eventos == "noche":
        return -5
    else:
        return 0

def generate_report(plant, dias):
    print("\n╔══════════════════════════════════════════════════╗")
    print("║ 📊 Reporte Final                                 ║")
    print("╠══════════════════════════════════════════════════╣")
    print(f"║ Días sobrevividos: {dias}                         ║")
    print(f"║ Fase final: {plant.phase}                        ║")
    print(f"║ Tamaño final: {plant.size:.2f}                   ║")
    print(f"║ Nivel de salud final: {plant.health}             ║")
    print(f"║ Nivel de contaminación: {plant.contamination_level:.2f} ║")
    print("╚══════════════════════════════════════════════════╝")
    print("=" * 50)
    input("Presiona Enter para salir.")

def mostrar_historia():
    print("\n╔══════════════════════════════════╗")
    print("║ 📜 Historia del juego:           ║")
    print("╚══════════════════════════════════╝")
    historia = '''
En un futuro donde la Tierra enfrenta la escasez de recursos y cambios climáticos extremos, 
la humanidad busca sobrevivir más allá de nuestro planeta. La Agencia Espacial Unificada 
lidera el proyecto Simulaciones de Vida, cuyo objetivo es desarrollar tecnologías agrícolas 
para colonizar planetas hostiles. La primera prueba se realiza en Gaiara, un planeta con 
radiación mortal, agua limitada y suelo infértil. El éxito en este proyecto podría asegurar 
la supervivencia humana en el espacio, pero cada avance también plantea preguntas sobre los 
peligros desconocidos que aguardan en el cosmos.
'''
    print(historia)
    print(f"{colors['CYAN']}{game_text_art.get('Historia')}{colors['RESET']}")
    print("\n╔═════════════════════════════════════╗")
    print("║ Presiona Enter para regresar al menú.║")
    print("╚═════════════════════════════════════╝")
    input()
    game()

def sugerir_accion(plant):
    print("\n╔══════════════════════════════════╗")
    print("║ 🤔 Sugerencia de acción:           ║")
    print("╠══════════════════════════════════╣")
    if plant.health < 50:
        print("║ ⚠️  ¡Atención! La salud de tu planta está baja.               ║")
    elif plant.contamination_level > 20:
        print("║ 🌫️  La contaminación está alta.                           ║")
    elif plant.temperature > 30:
        print("║ 🌞  La temperatura es muy alta.                           ║")
    elif plant.size < 10:
        print("║ 🌱  Tu planta es pequeña.                                 ║")
    else:
        print("║ 👍  Todo parece estar en orden.                          ║")
    print("╚══════════════════════════════════╝")

def game():
    planets = create_planets()
    print(f"{colors['GREEN']}{ascii_art_titles['Menu']}{colors['RESET']}")
    print(f"{colors['MAGENTA']}{ascii_art_titles['Opciones']}{colors['RESET']}")
    opcion = input("Selecciona una opción (1, 2, 3): ")
    if opcion == "1":
        iniciar_juego()
    elif opcion == "2":
        mostrar_historia()
    elif opcion == "3":
        print("\n╔══════════════════════════════════╗")
        print("║ 🙌 Gracias por jugar. ¡Hasta pronto!║")
        print("╚══════════════════════════════════╝")
        exit()
    else:
        print("\n╔══════════════════════════════════╗")
        print("║ ⚠️  Opción no válida.             ║")
        print("╚══════════════════════════════════╝")
        game()

def iniciar_juego():
    planets = create_planets()
    print(f"{colors['BLUE']}{ascii_art_titles['Planetas']}{colors['RESET']}")
    for i, planet in enumerate(planets, 1):
        print(f"{planet.color}  {i}. {planet.name} - {planet.description}{colors['RESET']}")
    print("=" * 46)
    while True:
        try:
            choice = int(input("Selecciona un planeta (1-6): "))
            if 1 <= choice <= 6:
                selected_planet = planets[choice - 1]
                break
            else:
                print("\n╔══════════════════════════════════╗")
                print("║ ⚠️  Opción inválida.              ║")
                print("╚══════════════════════════════════╝")
        except ValueError:
            print("\n╔══════════════════════════════════╗")
            print("║ ⚠️  Entrada inválida.             ║")
            print("╚══════════════════════════════════╝")
    print(selected_planet.color + "\n╔══════════════════════════════════╗")
    print(f"║ 🌌 Has seleccionado el planeta {selected_planet.name}!")
    print(f"║ {selected_planet.description}")
    print("╚══════════════════════════════════╝")
    print(planet_art[selected_planet.name])
    plant_name = input("Nombre de tu planta: ")
    initial_size = validate_positive_float("Tamaño inicial de la planta (e.g., 1.0): ")
    growth_rate = validate_positive_float("Tasa de crecimiento (e.g., 0.1): ")
    plant = Plant(plant_name, initial_size, growth_rate)
    print("\n╔══════════════════════════════════╗")
    print("║ 🌱 ¡Tu misión comienza ahora!    ║")
    print("╠══════════════════════════════════╣")
    print("║ 🛠️  Objetivo: Sobrevive 17 días.   ║")
    print("║ 🌌 Elige sabiamente tus acciones.  ║")
    print("╚══════════════════════════════════╝\n")
    dias = 0
    event = Event(plant)
    while plant.health > 0:
        plant.age += 1
        plant.update_phase()
        if plant.age > 1:
            clear()
        prev_size = plant.size
        prev_health = plant.health
        prev_contamination = plant.contamination_level
        prev_temperature = plant.temperature
        plant.contamination_level = integral_contaminacion(plant.contamination_level, dias)
        plant.temperature += derivada_temperatura(plant.temperature, "ninguno")
        plant.size += derivada_tamaño(plant.size, growth_rate, plant.health)
        plant.health = integral_salud(plant.health, plant.temperature, plant.contamination_level, dias)
        plant.display_status()
        plant.log_daily_changes(prev_size, prev_health, prev_contamination, prev_temperature)
        event.random_event()
        if plant.phase == "Madurez" and plant.age >= 16:
            print("Tu planta ha completado su ciclo de vida. Misión completada")
            generate_report(plant, dias)
            break
        if plant.health <= 0:
            print("\n💀 ═══════════════════════════════════════════════ 💀")
            print("║ Tu planta ha muerto.                           ║")
            generate_report(plant, dias)
            print("💀 ═══════════════════════════════════════════════ 💀")
            break
        user_input = input("¿Deseas continuar cuidando tu planta? (s/n): ").strip().lower()
        if user_input != 's':
            print("\n🌱 ═══════════════════════════════════════════════ 🌱")
            print("║ El juego ha terminado. ¡Gracias por jugar!       ║")
            generate_report(plant, dias)
            print("🌱 ═══════════════════════════════════════════════ 🌱")
            break
        print("\n╔════════════════════════════════════════════════════╗")
        print("║ 🌱 ¿Qué te gustaría hacer ahora?                   ║")
        print("╠════════════════════════════════════════════════════╣")
        print("║ 1. 🌾 Usar fertilizante                            ║")
        print("║ 2. 💧 Regar la planta                              ║")
        print("║ 3. 🛡️ Proteger la planta contra eventos            ║")
        print("║ 4. ⏳ Pasar al siguiente día                       ║")
        print("║ 5. 🔄 Recargar protección                         ║")
        print("\n╚════════════════════════════════════════════════════╝")
        choice = input("Elige una opción (1-5): ").strip()
        if choice == '1':
            plant.apply_fertilizer()
        elif choice == '2':
            plant.water_plant()
        elif choice == '3':
            if plant.protect_plant():
                event.random_event()
        elif choice == '4':
            print("\n⏳ Pasando al siguiente día... 🌅")
        elif choice == '5':
            plant.recharge_protection()
        else:
            print("\n❌ Opción inválida, intenta nuevamente.")
            continue
        dias += 1

if __name__ == "__main__":
    game()
