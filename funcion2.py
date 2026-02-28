#Una funcion que crea una lista de n notas

def crear_lista_notas(numeroNotas):
    import random
    notas = []
    for _ in range(numeroNotas):
        nota = random.randint(1,5)
        notas.append(nota)
    return notas