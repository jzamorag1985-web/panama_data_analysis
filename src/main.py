from data_loader import ejecutar as ingesta
from analyzer import ejecutar as estadistico
from visualizer import ejecutar as visualizacion
from report_generator import ejecutar as reporte

def mostrar_menu():
    print("\n" + "=" * 45)
    print("   Sistema EDA — Datos Socioeconómicos Panamá")
    print("   main.py · Punto de entrada del sistema")
    print("=" * 45)
    print("  1. Módulo 1 · Ingesta y limpieza    ")
    print("  2. Módulo 2 · Análisis estadístico  ")
    print("  3. Módulo 3 · Visualización          ")
    print("  4. Módulo 4 · Reporte automático    ")
    print("  5. Salir")
    print("=" * 45)

def main():
    while True:
        mostrar_menu()
        opcion = input("\n  Selecciona una opción: ").strip()

        match opcion:
            case "1":
                ingesta()
            case "2":
                estadistico()
            case "3":
                visualizacion()
            case "4":
                reporte()
            case "5":
                print("\n  Cerrando sistema. ¡Hasta luego!\n")
                break
            case _:
                print("\n   ️ Opción no válida. Intenta de nuevo.")

       
main()

