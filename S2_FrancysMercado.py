    # Funcion
def calcular_edad_en_una_decada(nombre, edad):
    edad_futura = edad + 10
    mensaje = f"Estimado {nombre}, en una década su edad será de {edad_futura} años."
    return mensaje

def main():
    # Pedir al usuario su nombre y edad
    nombre = input("Por favor, ingrese su nombre: ")
    edad = int(input("Ahora ingrese su edad actual: "))

    # llama a la funcion y almacena en la variable mensaje
    mensaje = calcular_edad_en_una_decada(nombre, edad)
    print(mensaje)
    # cambio nuevo
    
if __name__ == "__main__":
    main()
