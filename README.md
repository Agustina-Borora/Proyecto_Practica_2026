# Sistema de Gestión de Horas Laborales

## Institución
    IES N°7 Populorum Progressio IN.TE.LA

## Año
    2026
## Autor/es
- Apellido y nombre: Borora Melani Agustina
- Email: agustinaborora@gmail.com
- GitHub: Agustina-Borora
## Profesores
- Apellido y nombre: Manuel Serrano y Hoyos Oscar

## Definición del problema
Actualmente, el registro de horas laborales se realiza de forma manual o desorganizada, lo que genera errores en el cálculo de salarios y dificultades en el control de asistencia.

## Objetivo General
Desarrollar un sistema que permita registrar y gestionar las horas laborales del personal.

## Objetivos Específicos
- Registrar horas de entrada y salida de los empleados
- Calcular automáticamente las horas trabajadas
- Generar reportes para el control administrativo

## Beneficiarios
- Empleados
- Área administrativa
- Empresa

## Alcance del proyecto
El sistema permitirá gestionar las horas laborales, asistencia y cálculo de horas trabajadas, sin incluir la liquidación completa de sueldos.


##  Cronograma de actividades
- Semana 1: Análisis del problema  
- Semana 2: Diseño del sistema  
- Semana 3: Desarrollo del sistema  
- Semana 4: Pruebas y correcciones  


##  Estudio de factibilidad

### Técnica
El sistema es viable ya que se utilizarán tecnologías conocidas como Python/Java y bases de datos simples.

### Económica
El desarrollo no requiere grandes costos, ya que se utilizarán herramientas gratuitas.

### Operativa
El sistema será fácil de usar por el personal administrativo sin necesidad de capacitación avanzada.


##  Requerimientos Funcionales

### Requisitos generales
- Interfaz simple y fácil de usar  
- Acceso seguro al sistema  
- Disponibilidad del sistema en horario laboral  

### Requisitos funcionales
- Registrar ingreso y egreso de empleados  
- Calcular horas trabajadas automáticamente  
- Generar reportes de asistencia  
- Almacenar historial de registros 

# Diseño
El sistema contará con una interfaz sencilla e intuitiva para el registro y control de horas laborales.  
Permitirá al personal administrativo registrar entradas y salidas, consultar reportes y visualizar información de empleados.

# Modelo de datos

## Datos de entrada
- Nombre y apellido del empleado
- DNI
- Fecha
- Hora de ingreso
- Hora de salida
- Cargo o puesto

## Datos internos
- ID del empleado
- Historial de asistencia
- Horas acumuladas
- Usuarios del sistema
- Registros almacenados en la base de datos

## Datos de salida
- Reporte de asistencia
- Cantidad de horas trabajadas
- Listado de empleados
- Historial de registros
- Informes administrativos

# Base de datos
Se utilizará una base de datos MySQL para almacenar la información del sistema.  
Las tablas principales serán:
- empleados
- asistencia
- usuarios
- reportes

# Dependencias
- Java JDK o Python
- MySQL
- Conector JDBC
- Git

# Software (herramientas)
- NetBeans
- MySQL Workbench
- Git Bash
- GitHub
- Visual Studio Code

# Procedimientos de instalación
1. Clonar el repositorio desde GitHub.
2. Abrir el proyecto en NetBeans o Visual Studio Code.
3. Crear la base de datos en MySQL.
4. Importar las tablas necesarias.
5. Configurar la conexión a la base de datos.
6. Ejecutar el sistema.

# Procedimientos de testing
1. Verificar el inicio del sistema.
2. Comprobar el registro de empleados.
3. Validar el registro de horas de entrada y salida.
4. Revisar el cálculo automático de horas trabajadas.
5. Probar la generación de reportes.
6. Verificar la conexión con la base de datos.


## Script de Cálculo de Edad
He desarrollado un script en Python para calcular la edad automáticamente.

### Cómo ejecutarlo:
1. Asegúrate de tener Python instalado.
2. Abre la terminal en esta carpeta.
3. Ejecuta el comando: `python edad.py`

[Click aquí para ver el script](./edad.py)



