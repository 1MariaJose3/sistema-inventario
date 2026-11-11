def buscar_producto(lista_productos, codigo_buscado):
    for prod in lista_productos:
        if prod.codigo == codigo_buscado:
            return prod
    return None