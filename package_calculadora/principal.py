from calculadora import Calculadora

print("Bienvenido a la calculadora funcional. Tener en cuenta que sólo opera con 2 números.")

CONST_PRIMER_NUMERO = "Ingrese el primer número: "
CONST_SEGUNDO_NUMERO = "Ingrese el segundo número: "


def seleccionar_operacion() -> int:
    validacion = True
    while validacion:
        try:
            print("Ingrese la operación que desea realizar")
            print("1. Sumar")
            print("2. Restar")
            print("3. Dividir")
            print("4. Multiplicar")
            print("5. Potenciar")
            print("6. Raíz")
            opcion = int(input("Opción: Ingrese la opción que desea realizar (1-6): "))
            
            if opcion < 1 or opcion > 6:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
                validacion = True
            else:
                validacion = False

        except Exception:
            validacion = True
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")
    

    return opcion


def realizar_operacion(opcion : int):
    
    validacion = True
    resultado = 0
    
    while validacion:
        
        try:

            a = float(input(CONST_PRIMER_NUMERO))
            b = float(input(CONST_SEGUNDO_NUMERO))

            if opcion == 1:
                resultado = Calculadora.sumar(a, b)
                print(f"La suma de {a} y {b} es: {resultado}")
            elif opcion == 2:
                resultado = Calculadora.restar(a, b)
                print(f"La resta de {a} y {b} es: {resultado}")
            elif opcion == 3:
                resultado = Calculadora.dividir(a, b)
                print(f"La división entre {a} y {b} es: {resultado}")
            elif opcion == 4:
                resultado = Calculadora.multiplicar(a, b)
                print(f"La multiplicación de {a} y {b} es: {resultado}")
            elif opcion == 5:
                resultado = Calculadora.exponenciar(a, b)
                print(f"La potenciación de {a} elevado {b} es: {resultado}")
            elif opcion == 6:
                resultado = Calculadora.obtener_raiz(a, b)
                print(f"La raíz {a} de {b} es: {resultado}")

            validacion = False

        except Exception:
            validacion = True
            print("Entrada no válida. Por favor, ingrese números válidos (ENTEROS | DECIMALES).")


def principal():
    
    validacion = True
    
    while validacion:
        valor = seleccionar_operacion()
        realizar_operacion(valor)
        respuesta = str(input("¿Desea realizar otra operación? (y/n): ")).strip().lower()
        if respuesta == "y":
            validacion = True
        else:
            validacion = False
            print("Gracias por usar la calculadora. ¡Hasta luego!")
    
    

principal()
