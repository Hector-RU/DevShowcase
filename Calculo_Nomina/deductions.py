def calculate_sfs(gross_salary):
    """Calcula la deducción para el Seguro Familiar de Salud (SFS)"""
    return gross_salary * 0.0304

def calculate_afp(gross_salary):
    """Calcula la deducción para el Fondo de Pensiones (AFP)"""
    return gross_salary * 0.0287

def calculate_isr(monthly_salary):
    """
    Calcula el Impuesto sobre la Renta (ISR) basado en el salario anual.
    """
    annual_salary = monthly_salary * 12
    if annual_salary <= 416220.00:
        return 0
    elif annual_salary <= 624329.00:
        excess = annual_salary - 416220.01
        return excess * 0.15 / 12
    elif annual_salary <= 867123.00:
        excess = annual_salary - 624329.01
        return (31216.00 + (excess * 0.20)) / 12
    else:
        excess = annual_salary - 867123.01
        return (79776.00 + (excess * 0.25)) / 12
