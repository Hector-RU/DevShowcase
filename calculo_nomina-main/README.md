
# Cálculo de Salarios y Costos de Nómina

## Descripción

Este proyecto permite calcular el salario neto de un empleado y el costo total de la nómina para el empleador, considerando las deducciones de salud, pensiones, impuestos sobre la renta (ISR), y aportes para riesgos laborales, INFOTEP, entre otros. También incluye el cálculo de horas extras con diferentes recargos según el tipo de hora extra trabajada (diurna, nocturna y con recargo completo).

## Estructura del Proyecto

El proyecto está dividido en tres módulos principales:

1. **`deductions.py`**: Funciones que calculan las deducciones de nómina como el Seguro Familiar de Salud (SFS), el Fondo de Pensiones (AFP) y el Impuesto sobre la Renta (ISR).
2. **`extras.py`**: Funciones que gestionan el cálculo de horas extras de acuerdo al tipo de recargo (diurno, nocturno y completo).
3. **`salary_calculator.py`**: Funciones que calculan el salario neto del empleado y el costo total de la nómina para el empleador, sumando las deducciones y el pago de horas extras.

El archivo **`main.py`** contiene el menú interactivo para que el usuario pueda elegir la operación que desea realizar (calcular salario neto, calcular costo para el empleador o ambos).

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Hector-RU/DevShowcase.git
    cd <nombre_del_directorio>
    ```

2. Asegúrate de tener Python 3.x instalado. No es necesario instalar dependencias adicionales, ya que este proyecto solo utiliza bibliotecas estándar de Python.

## Uso

1. Ejecuta el archivo principal **`main.py`**:
    ```bash
    python main.py
    ```

2. El programa te presentará un menú con las siguientes opciones:
    - **Calcular Salario Neto**: Ingresa el salario bruto y las horas extras (si las tienes) para calcular el salario neto después de deducciones.
    - **Calcular Costo Total para el Empleador**: Ingresa el salario bruto y las horas extras para calcular el costo total que el empleador debe pagar, considerando las contribuciones a la seguridad social, riesgos laborales, INFOTEP, y otras deducciones.
    - **Calcular Nómina Completa**: Calcula tanto el salario neto como el costo total de la nómina de una vez.
    - **Salir**: Termina el programa.

## Funcionalidades

- **Cálculo del Salario Neto**: Calcula el salario después de las deducciones por SFS, AFP, ISR, y horas extras.
- **Cálculo del Costo Total para el Empleador**: Calcula el costo total de la nómina para el empleador, sumando el salario bruto, las horas extras y los aportes a la seguridad social.
- **Horas Extras**: El sistema permite calcular horas extras diurnas, nocturnas y con recargo completo.

## Ejemplo de uso

```bash
$ python main.py
Menú de Cálculos Salariales
1. Calcular Salario Neto
2. Calcular Costo Total para el Empleador
3. Calcular Nómina Completa
4. Salir
Seleccione una opción: 1
Ingrese el salario bruto mensual: 50000
¿Desea agregar horas extras? (si/no): si
Ingrese las horas extras diurnas: 10
Ingrese las horas extras nocturnas: 5
Ingrese las horas con recargo del 100%: 3

El salario neto es: $38,920.34 pesos
```

## Créditos

Este proyecto fue desarrollado para simplificar el cálculo de salarios y los costos asociados a la nómina de empleados en la República Dominicana, teniendo en cuenta las normativas vigentes de seguridad social, pensiones y riesgos laborales.

## Licencia

Este proyecto está licenciado bajo la MIT License - ver el archivo [LICENSE](LICENSE) para más detalles.

## Detalles Técnicos

### Módulos

1. **`deductions.py`**
    - **Función `calcular_deducciones_sfs(salario_bruto)`**: Calcula la deducción por el Seguro Familiar de Salud (SFS).
    - **Función `calcular_deducciones_afp(salario_bruto)`**: Calcula la deducción para el Fondo de Pensiones (AFP).
    - **Función `calcular_deducciones_isr(salario_bruto)`**: Calcula el Impuesto sobre la Renta (ISR) para un salario bruto.
    
2. **`extras.py`**
    - **Función `calcular_horas_extras(salario_bruto, horas_diurnas, horas_nocturnas, horas_con_recargo)`**: Calcula las horas extras diurnas, nocturnas y con recargo completo según las reglas vigentes.

3. **`salary_calculator.py`**
    - **Función `calcular_salario_neto(salario_bruto, horas_diurnas, horas_nocturnas, horas_con_recargo)`**: Calcula el salario neto, incluyendo las deducciones y horas extras.
    - **Función `calcular_costo_empleador(salario_bruto, horas_diurnas, horas_nocturnas, horas_con_recargo)`**: Calcula el costo total de la nómina para el empleador, considerando las contribuciones de seguridad social, INFOTEP, y demás deducciones.

### Convenciones de Nombres

- Las funciones de cálculo de deducciones y horas extras están nombradas de manera descriptiva.
- Las variables que almacenan las horas extras y el salario bruto son claramente indicadas, para evitar confusión.

### Recomendaciones

- Se recomienda asegurarse de ingresar los valores en formato numérico. En caso de ingresar texto o valores no válidos, el programa pedirá nuevamente la entrada.
- Las deducciones y horas extras son opcionales, pero se recomienda introducirlas correctamente para obtener resultados precisos.

## Aportes y Mejoras Futuras

Este proyecto puede expandirse para incluir más funcionalidades, como el cálculo de beneficios adicionales o el ajuste de las deducciones a cambios en las leyes fiscales o laborales. Además, podría integrarse con una base de datos para almacenar y consultar los registros de salarios de los empleados.
