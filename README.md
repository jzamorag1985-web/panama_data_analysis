# panama_data_analysis
Programa creado para documentar los procedimientos y códigos del Panama_Data_Analysis. Que es un sistema en python que consiste en analizar datos de venta, genera estadísticas, detecta patrones, crea visualizaciones y reportes automáticos.


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
       OS para creacion automatica de carpetas dentro del sistema.  

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

Flujo del Sistema

Pipeline de procesamiento de datos.

Carga de datos
El sistema lee el archivo original (Excel o CSV) desde la carpeta data/raw.
Limpieza de datos
Se eliminan valores nulos, se normalizan columnas y se preparan los datos para análisis.
Procesamiento estadístico
Se calculan correlaciones, distribuciones, percentiles y detección de outliers.
Generación de visualizaciones
Se crean gráficos como histogramas, boxplots y mapas de calor.
Exportación de resultados
Los resultados se guardan en archivos CSV y gráficos en la carpeta output/.
Generación de reporte (opcional)
Se consolidan los resultados en un reporte final (PDF).

Casos de uso:
Analisis de ventas.
Evaluacion de desempeño comercial.
Evaluación de desempeño comercial
Identificación de patrones y tendencias
Detección de valores atípicos (outliers)
Soporte para toma de decisiones empresariales.

Entrada y Salida del sistema
  Entrada:
    Archivos de datos en Excel(.xlxs) y CSV (.csv)
    ubicacion:
    data/raw/

  Salida
    Archivos CSV con resultados estadísticos
    Gráficos en formato PNG (Opcional) reporte en PDF






 
           








