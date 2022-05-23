def run():
    mi_diccionario = {
        "nombre": "Fernando",
        "apellido_paterno": "Reyes",
        "apellido_materno": "Montes"
    }
    for propiedad in mi_diccionario:
        print(mi_diccionario[propiedad])

    población_paises = {
        'Argentina': 44_938_712,
        'Brasil': 210_147_125,
        'Colombia': 50_372_424
    }
    
    for pais, poblacion in  población_paises.items():
        print(pais+" tiene "+str(poblacion)+" habitantes")

if __name__ == "__main__":
    run()
