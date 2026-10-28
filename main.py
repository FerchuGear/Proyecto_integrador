from datos import obtener_categorias, obtener_prioridades, obtener_estados, obtener_limite_alerta, crear_lista_tickets
from operaciones import validar_codigo_formato, validar_fecha_formato, buscar_ticket_posicion, crear_ticket, cambiar_estado, contar_total_tickets, contar_por_estado, contar_por_categoria, porcentaje_resueltos, categoria_mayor_cantidad, obtener_tickets_criticos, categorias_en_alerta, ranking_categorias, crear_matriz_categoria_prioridad

def mostrar_presentacion():
    print("\nGESTOR DE TICKETS DE SOPORTE TÉCNICO")
    print("====================================")
    print("Sistema para registrar, consultar y analizar tickets de soporte.")

def solicitar_texto_obligatorio(mensaje):
    texto = ""
    while texto.strip() == "":
        texto = input(mensaje)
        if texto.strip() == "":
            print("El campo no puede quedar vacío.")
    return texto.strip()

def solicitar_opcion_lista(titulo, opciones):
    seleccion = None
    while seleccion is None:
        print("\n" + titulo)
        for indice in range(len(opciones)):
            print(str(indice + 1) + ". " + opciones[indice])
        try:
            numero = int(input("Seleccione una opción: "))
            if numero >= 1 and numero <= len(opciones):
                seleccion = opciones[numero - 1]
            else:
                print("La opción seleccionada no es válida.")
        except ValueError:
            print("Debe ingresar un número entero.")
    return seleccion

def solicitar_codigo_nuevo(tickets):
    codigo_valido = False
    codigo = ""
    while codigo_valido == False:
        codigo = input("Código del ticket (TKT-0000): ").upper().strip()
        if not validar_codigo_formato(codigo):
            print("El código debe tener el formato TKT-0000.")
        elif buscar_ticket_posicion(tickets, codigo) != -1:
            print("Ya existe un ticket con ese código.")
        else:
            codigo_valido = True
    return codigo

def solicitar_fecha():
    fecha_valida = False
    fecha = ""
    while fecha_valida == False:
        fecha = input("Fecha (DD/MM/AAAA): ").strip()
        if validar_fecha_formato(fecha):
            fecha_valida = True
        else:
            print("La fecha debe tener el formato DD/MM/AAAA.")
    return fecha

def mostrar_ticket(ticket):
    print("------------------------------")
    print(f"Código: {ticket[0]}")
    print(f"Fecha: {ticket[1]}")
    print(f"Cliente: {ticket[2]}")
    print(f"Categoría: {ticket[3]}")
    print(f"Prioridad: {ticket[4]}")
    print(f"Estado: {ticket[5]}")
    print(f"Responsable: {ticket[6]}")
    print(f"Descripción: {ticket[7]}")

def registrar_ticket(tickets, categorias, prioridades, estados):
    print("\nREGISTRAR TICKET")
    print("================")
    codigo = solicitar_codigo_nuevo(tickets)
    fecha = solicitar_fecha()
    cliente = solicitar_texto_obligatorio("Cliente: ")
    categoria = solicitar_opcion_lista("Categorías", categorias)
    prioridad = solicitar_opcion_lista("Prioridades", prioridades)
    estado = solicitar_opcion_lista("Estados", estados)
    responsable = solicitar_texto_obligatorio("Responsable: ")
    descripcion = solicitar_texto_obligatorio("Descripción: ")
    ticket = crear_ticket(codigo, fecha, cliente, categoria, prioridad, estado, responsable, descripcion)
    tickets.append(ticket)
    print("\nTicket registrado correctamente.")

def listar_tickets(tickets):
    print("\nLISTADO DE TICKETS")
    print("==================")
    if len(tickets) == 0:
        print("No hay tickets registrados.")
    else:
        for ticket in tickets:
            mostrar_ticket(ticket)

def buscar_ticket_interactivo(tickets):
    print("\nBUSCAR TICKET")
    print("=============")
    codigo = input("Código a buscar: ").upper().strip()
    posicion = buscar_ticket_posicion(tickets, codigo)
    if posicion == -1:
        print("El código no está registrado.")
    else:
        mostrar_ticket(tickets[posicion])

def cambiar_estado_interactivo(tickets, estados):
    print("\nCAMBIAR ESTADO")
    print("==============")
    codigo = input("Código del ticket: ").upper().strip()
    posicion = buscar_ticket_posicion(tickets, codigo)
    if posicion == -1:
        print("El código no está registrado.")
    else:
        print("\nTicket actual:")
        mostrar_ticket(tickets[posicion])
        nuevo_estado = solicitar_opcion_lista("Seleccione el nuevo estado", estados)
        actualizado = cambiar_estado(tickets, codigo, nuevo_estado)
        if actualizado:
            print("Estado actualizado correctamente.")

def mostrar_resumen_estados(tickets, estados):
    cantidades = contar_por_estado(tickets, estados)
    print("\nTICKETS POR ESTADO")
    for indice in range(len(estados)):
        print(f"{estados[indice]}: {cantidades[indice]}")
def mostrar_resumen_categorias(tickets, categorias):
    cantidades = contar_por_categoria(tickets, categorias)
    print("\nTICKETS POR CATEGORÍA")
    for indice in range(len(categorias)):
        print(f"{categorias[indice]}: {cantidades[indice]}")

def mostrar_indicadores(tickets, categorias, estados):
    print("\nINDICADORES")
    print("===========")
    total = contar_total_tickets(tickets)
    porcentaje = porcentaje_resueltos(tickets)
    categoria_mayor, cantidad_mayor = categoria_mayor_cantidad(tickets, categorias)
    print(f"Cantidad total de tickets: {total}")
    print(f"Porcentaje de resolución: {porcentaje:.2f}%")
    if categoria_mayor is None:
        print("No hay una categoría con mayor cantidad.")
    else:
        print(f"Categoría con mayor cantidad: {categoria_mayor}")
        print(f"Cantidad: {cantidad_mayor}")
    mostrar_resumen_estados(tickets, estados)
    mostrar_resumen_categorias(tickets, categorias)

def mostrar_alertas(tickets, categorias, limite):
    print("\nALERTAS")
    print("=======")
    criticos = obtener_tickets_criticos(tickets)
    print("\nTickets críticos:")
    if len(criticos) == 0:
        print("No hay tickets críticos.")
    else:
        for ticket in criticos:
            mostrar_ticket(ticket)
    alertas = categorias_en_alerta(tickets, categorias, limite)
    print("\nCategorías con acumulación de tickets abiertos:")
    if len(alertas) == 0:
        print("No existen categorías en condición de alerta.")
    else:
        for alerta in alertas:
            print(f"{alerta[0]} - Tickets abiertos: {alerta[1]}")

def mostrar_ranking(tickets, categorias):
    ranking = ranking_categorias(tickets, categorias)
    print("\nRANKING DE CATEGORÍAS")
    for posicion in range(len(ranking)):
        print(f"{str(posicion + 1)}. {ranking[posicion][0]} - {ranking[posicion][1]}")

def mostrar_matriz(tickets, categorias, prioridades):
    matriz = crear_matriz_categoria_prioridad(tickets, categorias, prioridades)
    print("\nMATRIZ CATEGORÍA / PRIORIDAD")
    print(f"{'Categoría'.ljust(15)}", end="")
    for prioridad in prioridades:
        print(prioridad.ljust(12), end="")
    print()
    for fila in range(len(categorias)):
        print(categorias[fila].ljust(15), end="")
        for columna in range(len(prioridades)):
            print(str(matriz[fila][columna]).ljust(12), end="")
        print()

def mostrar_informes(tickets, categorias, prioridades, estados):
    print("\nINFORMES")
    print("========")
    listar_tickets(tickets)
    mostrar_resumen_estados(tickets, estados)
    mostrar_resumen_categorias(tickets, categorias)
    mostrar_ranking(tickets, categorias)
    print("\nTICKETS CRÍTICOS")
    criticos = obtener_tickets_criticos(tickets)
    if len(criticos) == 0:
        print("No hay tickets críticos.")
    else:
        for ticket in criticos:
            mostrar_ticket(ticket)
    total = contar_total_tickets(tickets)
    porcentaje = porcentaje_resueltos(tickets)
    print("\nRESUMEN GENERAL")
    print(f"Total de tickets: {total}")
    print(f"Porcentaje resuelto: {porcentaje:.2f}%")
    mostrar_matriz(tickets, categorias, prioridades)

def mostrar_menu():
    print("\nMENÚ PRINCIPAL")
    print("==============")
    print("1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar ticket por código")
    print("4. Cambiar estado")
    print("5. Mostrar indicadores")
    print("6. Mostrar alertas")
    print("7. Mostrar informes")
    print("8. Salir")

def solicitar_opcion_menu():
    opcion = 0
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Debe ingresar un número entero.")
    return opcion

def main():
    categorias = obtener_categorias()
    prioridades = obtener_prioridades()
    estados = obtener_estados()
    limite_alerta = obtener_limite_alerta()
    tickets = crear_lista_tickets()
    mostrar_presentacion()
    opcion = 0
    while opcion != 8:
        mostrar_menu()
        opcion = solicitar_opcion_menu()
        if opcion == 1:
            registrar_ticket(tickets, categorias, prioridades, estados)
        elif opcion == 2:
            listar_tickets(tickets)
        elif opcion == 3:
            buscar_ticket_interactivo(tickets)
        elif opcion == 4:
            cambiar_estado_interactivo(tickets, estados)
        elif opcion == 5:
            mostrar_indicadores(tickets, categorias, estados)
        elif opcion == 6:
            mostrar_alertas(tickets, categorias, limite_alerta)
        elif opcion == 7:
            mostrar_informes(tickets, categorias, prioridades, estados)
        elif opcion == 8:
            print("\nPrograma finalizado.")
        else:
            if opcion != 0:
                print("La opción seleccionada no existe.")

main()