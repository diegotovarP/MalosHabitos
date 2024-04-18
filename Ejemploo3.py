
def calcular_area_rectangulo(ancho, largo):
    area_rectangulo = ancho * largo
    return area_rectangulo


def calcular_area_triangulo(ancho, largo):
    area_triangulo = 0.5 * ancho * largo
    return area_triangulo

def principal():
    ancho_rectangulo  = 4
    largo_rectangulo  = 6
    area_rectangulo  = calcular_area_rectangulo(ancho_rectangulo , largo_rectangulo )
    print("HALLANDO EL AREA DEL RECTANGULO")
    print("Ancho del rectangulo:", ancho_rectangulo)
    print("Largo del rectangulo:", largo_rectangulo)
    print("Área del rectángulo:", area_rectangulo )
    print("******************************************")

    ancho_triangulo  = 5
    largo_triangulo  = 8
    area_triangulo = calcular_area_triangulo(ancho_triangulo , largo_triangulo )
    print("HALLANDO EL AREA DEL TRIANGULO")
    print("Largo del triangulo:", ancho_triangulo)
    print("Largo del triangulo:", largo_triangulo)
    print("Área del triángulo:", area_triangulo)

principal()
