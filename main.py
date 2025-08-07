
OBJETOS = {
    "botella de plástico": {
        "reciclable": True,
        "tiempo_descomposicion": "450 años"
    },
    "bolsa de plástico": {
        "reciclable": True,
        "tiempo_descomposicion": "10-20 años"
    },
    "caja de cartón": {
        "reciclable": True,
        "tiempo_descomposicion": "2 meses"
    },
    "cepillo de dientes": {
        "reciclable": False,
        "tiempo_descomposicion": "500 años",
        "manualidad": "puedes usarlo para limpiar esquinas o teclados difíciles"
    },
    "envase de yogur": {
        "reciclable": True,
        "tiempo_descomposicion": "30-50 años"
    },
    "vaso de papel con recubrimiento plástico": {
        "reciclable": False,
        "tiempo_descomposicion": "30 años",
        "manualidad": "puedes usarlo como maceta para plantar semillas o hacer títeres de dedos"
    }
}
def evaluar_objeto(nombre_objeto):
    nombre_objeto = nombre_objeto.lower()

    if nombre_objeto not in OBJETOS:
        return f"No se ha encontrado este objeto. Intenta con estos otros : {list(OBJETOS.keys())}"
    datos = OBJETOS[nombre_objeto]
    if datos["reciclable"] == True:
        accion = "RECICLAR"
    else:
        accion = "Intenta hacer una manualidad"
    resultado = f"🔎 OBJETO: {nombre_objeto} \n"
    resultado += f"♻️ ACCION {accion} \n"
    resultado += f"⏰ TIEMPO DE DESCOMPOSICION: {datos["tiempo_descomposicion"]} \n"
    if not datos["reciclable"] and "manualidad" in datos:
        resultado += f"🍾 MANUALIDAD : {datos["manualidad"]}" 
    
    return resultado
print(evaluar_objeto("vaso de papel con recubrimiento plástico"))