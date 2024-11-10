from salary_calculator import calculate_net_salary, calculate_employer_cost

def main_menu():
    """
    Menú principal para la ejecución de cálculos salariales y costos de nómina.
    """
    while True:
        print("\nMenú de Cálculos Salariales")
        print("1. Calcular Salario Neto")
        print("2. Calcular Costo Total para el Empleador")
        print("3. Calcular Nómina Completa")
        print("4. Salir")
        option = input("Seleccione una opción: ")
        
        if option in ["1", "2", "3"]:
            try:
                gross_salary = float(input("Ingrese el salario bruto mensual: "))
                if gross_salary <= 0:
                    raise ValueError("El salario bruto debe ser mayor que cero.")
            except ValueError as e:
                print(f"Error: {e}")
                continue

            add_overtime = input("¿Desea agregar horas extras? (si/no): ").lower()
            day_overtime = night_overtime = full_overtime = 0
            if add_overtime == "si":
                try:
                    day_overtime = float(input("Ingrese las horas extras diurnas: "))
                    night_overtime = float(input("Ingrese las horas extras nocturnas: "))
                    full_overtime = float(input("Ingrese las horas con recargo del 100%: "))
                except ValueError:
                    print("Error: Las horas extras deben ser valores numéricos.")
                    continue

            if option == "1":
                net_salary = calculate_net_salary(gross_salary, day_overtime, night_overtime, full_overtime)
                print(f"\nEl salario neto es: ${net_salary:.2f} pesos")

            elif option == "2":
                employer_cost = calculate_employer_cost(gross_salary, day_overtime, night_overtime, full_overtime)
                print(f"\nEl costo total de la nómina para el empleador es: ${employer_cost:.2f} pesos")

            elif option == "3":
                print("\n--- Cálculo de Nómina Completa ---")
                net_salary = calculate_net_salary(gross_salary, day_overtime, night_overtime, full_overtime)
                employer_cost = calculate_employer_cost(gross_salary, day_overtime, night_overtime, full_overtime)
                print(f"El salario neto es: ${net_salary:.2f} pesos")
                print(f"El costo total de la nómina para el empleador es: ${employer_cost:.2f} pesos")

        elif option == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main_menu()
