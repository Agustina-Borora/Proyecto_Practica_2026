from datetime import date

def calcular_edad():
    print("--- CALCULADORA DE EDAD ---")
    fecha_input = input("Ingresa tu fecha de nacimiento (AAAA-MM-DD): ")
    try:
        # Dividimos la fecha ingresada
        año, mes, dia = map(int, fecha_input.split("-"))
        nacimiento = date(año, mes, dia)
        hoy = date.today()
        
        # Cálculo lógico
        edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
        
        print(f"\nResultado: Tienes {edad} años.")
    except ValueError:
        print("\nError: Formato incorrecto. Asegúrate de usar AAAA-MM-DD (ejemplo: 1995-05-15).")

if __name__ == "__main__":
    calcular_edad()