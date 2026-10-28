def validar_codigo_formato(codigo):
    valido = False
    if len(codigo) == 8:
        if codigo[:4] == "TKT-":
            if codigo[4:].isdigit():
                valido = True
    return valido

def validar_fecha_formato(fecha):
    valido = False
    if len(fecha) == 10:
        if fecha[2] == "/" and fecha[5] == "/":
            dia = fecha[:2]
            mes = fecha[3:5]
            anio = fecha[6:]
            if dia.isdigit() and mes.isdigit() and anio.isdigit():
                valido = True
    return valido

def buscar_ticket_posicion(tickets, codigo):
    posicion = -1
    for indice in range(len(tickets)):
        if (tickets[indice][0].upper() == codigo.upper() and posicion == -1):
            posicion = indice
    return posicion

def crear_ticket(codigo, fecha, cliente, categoria, prioridad, estado, responsable, descripcion):
    ticket = (codigo, fecha, cliente, categoria, prioridad, estado, responsable, descripcion)
    return ticket

def cambiar_estado(tickets, codigo, nuevo_estado):
    posicion = buscar_ticket_posicion(tickets, codigo)
    actualizado = False
    if posicion != -1:
        ticket = tickets[posicion]
        ticket_actualizado = (ticket[:5] + (nuevo_estado,) + ticket[6:])
        tickets[posicion] = ticket_actualizado
        actualizado = True
    return actualizado

def contar_total_tickets(tickets):
    total = 0
    for ticket in tickets:
        total += 1
    return total

def contar_por_estado(tickets, estados):
    cantidades = [0 for estado in estados]
    for ticket in tickets:
        for indice in range(len(estados)):
            if ticket[5] == estados[indice]:
                cantidades[indice] += 1
    return cantidades

def contar_por_categoria(tickets, categorias):
    cantidades = [0 for categoria in categorias]
    for ticket in tickets:
        for indice in range(len(categorias)):
            if ticket[3] == categorias[indice]:
                cantidades[indice] += 1
    return cantidades

def porcentaje_resueltos(tickets):
    total = contar_total_tickets(tickets)
    resueltos = 0
    for ticket in tickets:
        if ticket[5] == "Resuelto":
            resueltos += 1
    porcentaje = 0
    if total > 0:
        porcentaje = resueltos * 100 / total
    return porcentaje

def categoria_mayor_cantidad(tickets, categorias):
    cantidades = contar_por_categoria(tickets, categorias)
    categoria_mayor = None
    cantidad_mayor = 0
    if len(tickets) > 0:
        cantidad_mayor = cantidades[0]
        categoria_mayor = categorias[0]
        for indice in range(1, len(categorias)):
            if cantidades[indice] > cantidad_mayor:
                cantidad_mayor = cantidades[indice]
                categoria_mayor = categorias[indice]
    return categoria_mayor, cantidad_mayor

def obtener_tickets_criticos(tickets):
    criticos = [ticket for ticket in tickets if (ticket[4] == "Alta" and ticket[5] != "Resuelto")]
    return criticos

def categorias_en_alerta(tickets, categorias, limite):
    cantidades_abiertas = [0 for categoria in categorias]
    for ticket in tickets:
        if ticket[5] == "Abierto":
            for indice in range(len(categorias)):
                if ticket[3] == categorias[indice]:
                    cantidades_abiertas[indice] += 1
    alertas = []
    for indice in range(len(categorias)):
        if cantidades_abiertas[indice] >= limite:
            alerta = (categorias[indice], cantidades_abiertas[indice])
            alertas.append(alerta)
    return alertas

def ranking_categorias(tickets, categorias):
    cantidades = contar_por_categoria(tickets, categorias)
    ranking = []
    for indice in range(len(categorias)):
        registro = (categorias[indice], cantidades[indice])
        ranking.append(registro)
    ranking = sorted(ranking, key=lambda elemento: elemento[1], reverse=True)
    return ranking

def crear_matriz_categoria_prioridad(tickets, categorias, prioridades):
    matriz = [[0 for columna in range(len(prioridades))] for fila in range(len(categorias))]
    for ticket in tickets:
        fila = -1
        columna = -1
        for indice in range(len(categorias)):
            if ticket[3] == categorias[indice]:
                fila = indice
        for indice in range(len(prioridades)):
            if ticket[4] == prioridades[indice]:
                columna = indice
        if fila != -1 and columna != -1:
            matriz[fila][columna] += 1
    return matriz