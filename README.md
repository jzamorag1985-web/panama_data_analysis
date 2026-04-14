# panama_data_analysis
Sistema en Python que automatiza la carga, limpieza, análisis y visualización de datos, generando información clave para la toma de decisiones basada en datos.

Arquitectura
data/raw → data_loader → data/cleaned
        ↓
     analyzer → output/*.csv
        ↓
     visualizer → output/charts/*.png
        ↓
     report_generator → reporte final PDF


Tecnologias 
      Python
  Analisis de datos
       Pandas
       NumPy
       SciPy

  Visualizacion de datos
       Matplotlib
       Seaborn

  Manejo de archivos y Sistema
       OS para creacion automatica de carpetas dentro del sistema 

Control de versiones 
Git & GitHub.

Arquitectura del Sistema
Programacion Orientada a objetos.

Instalacion
1.Clonar Repositorio
git clone https://github.com/tu-usuario/panama_data_analysis.git
cd panama_data_analysis

2.Crear y Activar entorno virtual
python -m venv venv

3.Instalar Dependencias
pip install -r requirements.txt

4.Ejecutar
  Modulo 1-Limpieza de datos
  python src/data_loader.py

  Modulo 2-Analisis Estadistico
  python src/analyzer.py

  Modulo 3-Visualizacion
  python src/visualizer.py

  Modulo 4-Generacion de reporte
  python src/report_generator.py

 Resultados 
 output/
 Incluyendo:
 Archivos
 graficos en formato PNG
 Reporte final en PDf

 Se recomienda ejecutar los modulos en orden para garantizar el flujo correcto del procesamiento de datos.

Flujo del Sistema:
Pipeline de procesamiento de datos.

Carga de datos:
El sistema lee el archivo original (Excel o CSV) desde la carpeta data/raw.

Limpieza de datos:
Se eliminan valores nulos, se normalizan columnas y se preparan los datos para análisis.

Procesamiento estadístico:
Se calculan correlaciones, distribuciones, percentiles y detección de outliers.

Generación de visualizaciones:
Se crean gráficos como histogramas, boxplots y mapas de calor.

Exportación de resultados:
Los resultados se guardan en archivos CSV y gráficos en la carpeta output/.

Generación de reporte:
Se consolidan los resultados en un reporte final (PDF).

Casos de uso:
1.Analisis de ventas
2.Evaluacion de desempeño comercial
3.Evaluación de desempeño comercial
4.Identificación de patrones y tendencias
5.Detección de valores atípicos (outliers)
6.Soporte para toma de decisiones empresariales

Entrada y Salida del sistema
  Entrada:
    Archivos de datos en Excel(.xlxs) y CSV (.csv)
    ubicacion:
    data/raw/

  Salida
    Archivos CSV con resultados estadísticos
    Gráficos en formato PNG (Opcional) reporte en PDF

 El sistema sigue una arquitectura tipo pipeline, donde cada módulo procesa la información de forma secuencial, permitiendo escalabilidad y reutilización del código.


Seguridad
1.Validacion de integridad de los datos cargados

2.Control de tipo de datos (numericos y categoricos)

3.Manejo seguro de rutas de archivos

4.Prevencion de errores en datasets

Futuras Mejoras
1.Dashboard inetractivo con visualizacion en tiempo real

2.Integracion con herramientas de BI

3.Automatizacion completa del pipeline de datos

4.Implementacion de machine learning para predicciones

5.Generacion automatica de reportes en PDF

6.Integracion con bases de datos(MySQL/PosgreSQL)


Versionado
Este proyecto sigue el estandar SemVer:
MAJOR: Cambios grandes o incompatibles
MINOR:Nuevas funcionalidades
PATCH:Correcciones y mejoras
Version actual: v1.0.0

Autores

Desarrollado por el equipo de Big Data y Ciencia de Datos:
**Natalia Barrelier**
**Adrian Herazo**
**Denis Pineda**
**Juan Rivera**
**Johana Zamora**








 
           








