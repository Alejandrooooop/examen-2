# notas.py


def calcular_promedio(notas):
    """
    Calcula el promedio de una lista de notas.

    Args:
        notas (list): Lista de números.

    Returns:
        float: Promedio de las notas.
    """
    if not notas:
        return 0

    return sum(notas) / len(notas)


def clasificar_nota(nota):
    """
    Clasifica una nota según su valor.

    Args:
        nota (float): Nota del estudiante.

    Returns:
        str: Clasificación de la nota.
    """
    if nota >= 4.5:
        return "impresionante"
    elif nota >= 3.5:
        return "Bueno"
    elif nota >= 3.0:
        return "Aceptable"
    else:
        return "Deficiente"


def esta_aprobado(nota, min_aprobacion=3.0):
    """
    Determina si una nota está aprobada.

    Args:
        nota (float): Nota del estudiante.
        min_aprobacion (float): Nota mínima para aprobar.

    Returns:
        bool: True si aprueba, False si no.
    """
    return nota >= min_aprobacion

#cambio en el codigo de notas.py