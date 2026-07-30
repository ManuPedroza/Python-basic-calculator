# Primer Proyecto para Desarrollador Junior

# Calculadora Básica
 
def mostrar_menu():
    """Muestra las opciones de las operaciones a calcular."""

    print("=" * 15, "Calculadora Básica", "=" * 15, "\n")
    print("1. Suma: ")
    print("2. Resta: ")
    print("3. Multiplicación: ")
    print("4. División: ")
    print("5. Salir: ")
    opcion = input("\nSelecciona el número de la operación a realizar: ")
    return opcion

def validar_numero_entero(num):
    """Valida que un número para la opción del menú sea entero."""
    
    try:
        return int(num)

    except ValueError:
        print("Debes ingresar un número válido. \n")

def ingreso_valores(operacion):
    """Pide los número con los que se harán los calculos."""

    while True:
        while True:
            try:
                num1 = float(input(f"\nEscribe el primer número a {operacion}: "))
                break
                
            except ValueError:
                print("Debes ingresar un número válido para realizar la operación.")

        while True:
            try:
                num2 = float(input(f"\nEscribe el segundo número a {operacion}: "))
                break

            except ValueError:
                print("Debes ingresar un número válido para realizar la operación.")
        return num1, num2

def suma(num1, num2):
    """Retorna la suma de los valores."""

    return num1 + num2

def resta(num1, num2):
    """Retorna la resta de los valores."""

    return num1 - num2

def multiplicacion(num1, num2):
    """Retorna la multiplicación de los valores."""

    return num1 * num2

def division(num1, num2):
    """Retorna la división de los valores."""
    try:
        return num1 / num2
        
    except ZeroDivisionError:
        return False #"\nNo se puede dividir un número entre zero."
            

def main():
    """Declaración de la función principal del programa."""
    while True:

        opcion = validar_numero_entero(mostrar_menu())

        if opcion == 1:
            operacion = "sumar"
            num1, num2 = ingreso_valores(operacion)
            resultado = suma(num1, num2)
            print(f"\nEl resultado de {operacion} {num1} + {num2} es: {resultado}")

        elif opcion == 2:
            operacion = "restar"
            num1, num2 = ingreso_valores(operacion)
            resultado = resta(num1, num2)
            print(f"\nEl resultado de {operacion} {num1} - {num2} es: {resultado}")

        elif opcion == 3:
            operacion = "multiplicar"
            num1, num2 = ingreso_valores(operacion)
            resultado = multiplicacion(num1, num2)
            print(f"\nEl resultado de {operacion} {num1} * {num2} es: {resultado}")

        elif opcion == 4:
            operacion = "dividir"
            num1, num2 = ingreso_valores(operacion)
            resultado = division(num1, num2)
            if resultado == False:
                print("\nNo se puede dividir un número entre zero.")
            else:
                print(f"\nEl resultado de {operacion} {num1} / {num2} es: {resultado}")

        elif opcion == 5:
            print("\nGracias por usar mi calculadora, saliendo del programa.")
            break

        else: 
            print("\nPorfavor ingrese un número válido del menú.")
    
        opcion = input("\n¿Desea realizar otra operación? (s/n) ").strip().lower()

        if opcion == "s":
            continue
        elif opcion == "n":
            print("\nGracias por usar mi calculadora, saliendo del programa.")
            break

if __name__ == "__main__":
    main()