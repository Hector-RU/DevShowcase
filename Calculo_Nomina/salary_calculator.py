from deductions import calculate_sfs, calculate_afp, calculate_isr
from extras import calculate_overtime

def calculate_net_salary(gross_salary, day_overtime=0, night_overtime=0, full_overtime=0):
    """
    Calcula el salario neto considerando deducciones y horas extras.
    """
    hourly_rate = gross_salary / 23.83 / 8
    total_overtime_pay = (
        calculate_overtime(hourly_rate, day_overtime, 1) +
        calculate_overtime(hourly_rate, night_overtime, 2) +
        calculate_overtime(hourly_rate, full_overtime, 3)
    )
    total_earnings = gross_salary + total_overtime_pay

    sfs_deduction = calculate_sfs(total_earnings)
    afp_deduction = calculate_afp(total_earnings)
    taxable_income = total_earnings - sfs_deduction - afp_deduction
    isr_deduction = calculate_isr(taxable_income)

    total_deductions = sfs_deduction + afp_deduction + isr_deduction
    net_salary = total_earnings - total_deductions

    print(f"\nDetalle de Salario Neto:\nTotal Horas Extras: ${total_overtime_pay:.2f}")
    print(f"Total Ingresos: ${total_earnings:.2f}")
    print(f"Descuentos TSS = ${sfs_deduction + afp_deduction:.2f} (SFS: ${sfs_deduction:.2f} + AFP: ${afp_deduction:.2f})")
    print(f"Descuento ISR = ${isr_deduction:.2f}")
    print(f"Salario Neto = ${net_salary:.2f}\n")
    
    return net_salary

def calculate_employer_cost(gross_salary, day_overtime=0, night_overtime=0, full_overtime=0):
    """
    Calcula el costo total de la nómina para el empleador, considerando horas extras y aportes.
    """
    hourly_rate = gross_salary / 23.83 / 8
    total_overtime_pay = (
        calculate_overtime(hourly_rate, day_overtime, 1) +
        calculate_overtime(hourly_rate, night_overtime, 2) +
        calculate_overtime(hourly_rate, full_overtime, 3)
    )
    total_employer_earnings = gross_salary + total_overtime_pay

    sfs_employer = total_employer_earnings * 0.0709
    afp_employer = total_employer_earnings * 0.0710
    srl = total_employer_earnings * 0.0114
    infotep = total_employer_earnings * 0.0100
    total_employer_cost = total_employer_earnings + sfs_employer + afp_employer + srl + infotep

    print(f"\nCosto Total para el Empleador:\nTotal Horas Extras: ${total_overtime_pay:.2f}")
    print(f"Total Ingresos Empleador: ${total_employer_earnings:.2f}")
    print(f"Aportes Empleador (TSS): ${sfs_employer + afp_employer + srl + infotep:.2f}")
    print(f"Plan Pensiones (7.1%): ${afp_employer:.2f}")
    print(f"Plan Salud (7.09%): ${sfs_employer:.2f}")
    print(f"Riesgo Laboral (1.14%): ${srl:.2f}")
    print(f"INFOTEP (1.00%): ${infotep:.2f}\n")
    
    return total_employer_cost
