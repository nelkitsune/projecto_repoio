import pr_funciones
print("Bienvenido a te comiste una pifia")
while True:
    condicion = input("ingrese si la pifia fue en un combate cuerpo a cuerpo (A), combate con conjuros(B) o C para salir: ").upper()
    if condicion == "C":
        print("gracias, vuelva pronto")
        break
    elif condicion == "A":
        pr_funciones.pifia_combate_cuerpo()
    elif condicion == "B":
        pr_funciones.pifia_conjuros()
    else:
        print("parametro ingresado erroneo, reiniciando el programa")