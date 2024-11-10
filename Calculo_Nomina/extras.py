def calculate_overtime(hourly_rate, hours, overtime_type):
    """
    Calcula el pago por horas extras de acuerdo al tipo de recargo.
    :param hourly_rate: Salario por hora.
    :param hours: Número de horas extra trabajadas.
    :param overtime_type: Tipo de horas extra (1: Diurnas, 2: Nocturnas, 3: Recargo completo).
    """
    if overtime_type == 1:
        return hourly_rate * hours * 0.15
    elif overtime_type == 2:
        return hourly_rate * hours * 0.35
    elif overtime_type == 3:
        return hourly_rate * hours * 1.00
    else:
        return 0
