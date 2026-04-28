# **Calculadora PAU Andalucía (2026)**



Aplicación de escritorio para estimar la nota de admisión a grados universitarios en Andalucía a partir de las calificaciones de Bachillerato, la Fase de Acceso y la Fase de Admisión de la PAU.



El programa calcula la nota ponderada para cada grado disponible, compara el resultado con las notas de corte y genera informes orientativos para ayudar al alumnado a valorar sus posibilidades de acceso.



IMPORTANTE

&#x20;- La información proporcionada por este programa es meramente orientativa.

&#x20;- No garantiza el acceso real a la universidad ni sustituye la información oficial publicada por el Distrito Único Andaluz, las universidades públicas andaluzas o la normativa aplicable.



### **Características**



&#x20;- Cálculo de la nota de admisión para grados universitarios de Andalucía.

&#x20;- Utilización de ponderaciones por grado y asignatura.

&#x20;- Comparación automática con notas de corte del año anterior extraídas del Distrito Único Andaluz.

&#x20;- Selección de asignaturas entre las permitidas en la PAU.

&#x20;- En esta versión, solo está disponible un número limitado de asignaturas.

&#x20;- Generación de dos informes en formato ".txt":

&#x09;- Informe completo por carreras.

&#x09;- Informe simple por margen de acceso.

&#x20;- Interfaz gráfica de escritorio desarrollada con PySide6 y Qt Designer.

&#x20;- Validación de entradas para evitar valores incorrectos.

&#x20;- Avisos cuando faltan datos antes de calcular.

&#x20;- Bloqueo de seguridad si se detectan errores críticos en los datos internos.



### **Fuentes de datos**



El programa utiliza archivos de datos incluidos en el proyecto:

&#x20;- "Ponderaciones.txt": Contiene los idiomas y asignaturas (separadas las asignaturas troncales) y las ponderaciones de cada asignaturas por grado. Extraído del BOJA.

&#x20;- "Notas de corte.txt": Contiene todos los grados ofertados en universidades públicas de Andalucía, con sus universidades, facultades y notas de corte del año anterior. Extraído del Distrito Único Andaluz.

&#x20;- "LICENSE.txt": Contiene la licencia completa del proyecto.



IMPORTANTE

&#x20;- Las notas de corte pueden cambiar cada año y dependen de la demanda, la oferta de plazas y otros factores. Cada año deberá descargarse la versión actualizada.

&#x20;- El resultado del programa debe entenderse como una estimación.



### **Tecnologías utilizadas**



El programa utiliza las siguientes tecnologías, necesarias si se quiere utilizar el código al completo:

&#x20;- Python (versión 3.10.0 o posterior)

&#x20;- PySide6

&#x20;- Qt Designer

&#x20;- PyInstaller (Utilizado solo para generar el ejecutable)



Estructura del proyecto



### **Archivos principales**



&#x20;- "Main.py": Archivo principal de la aplicación. Inicializa la interfaz, recoge los datos introducidos por el usuario y conecta el resto de archivos entre sí.

&#x20;- "Functions.py": Contiene funciones de cálculo que se ejecutan varias veces en "InformGenerator.py".

&#x20;- "DocumentReader.py": Lee "Ponderaciones.txt" y "Notas de Corte.txt", se asegura de que no haya fallos visibles en los datos y los envía a "Main.py".

&#x20;- "InformGenerator.py": Lleva a cabo los cálculos y genera los informes finales en formato ".txt".

&#x20;- "UI.py": Datos de la interfaz generada a partir del archivo "UI Pyside6.ui" de Qt Designer, que luego utiliza "Main.py".



### **Uso básico**



1\. Introduce tu nombre.

2\. Introduce la media de 1º de Bachillerato.

3\. Introduce la media de 2º de Bachillerato.

4\. Escoge las asignaturas e introduce las notas de la Fase de Acceso:

&#x20;  - Lengua Castellana y Literatura.

&#x20;  - Historia de España o Historia de la Filosofía.

&#x20;  - Lengua extranjera.

&#x20;  - Asignatura troncal.

5\. Añade, de forma opcional, asignaturas de la Fase de Admisión (3 cualquiera + 1 Segunda Lengua Extranjera).

6\. Pulsa el botón de cálculo.

7\. El programa generará los informes correspondientes en la carpeta desde la que se ejecute.



### **Informes generados**



Al realizar el cálculo, el programa genera dos archivos:

&#x20;- "Nombre (Completo).txt"

&#x20;- "Nombre (Margen).txt"

\*"Nombre" será sustituido por lo que introduzcas en el campo "Nombre" del programa.



#### **Informe completo**



Muestra todos los datos recogidos por la interfaz

&#x20;- Datos extraídos directamente (medias de 1º y 2º de Bachillerato, notas de las asignaturas...)

&#x20;- Media de Bachillerato y nota obtenida de esta fase.

&#x20;- Media de la Fase Obligatoria y nota obtenida de esta fase.

&#x20;- Nota general de la PAU (nota de Bachillerato + nota de la Fase Obligatoria).

&#x20;- Asignaturas de la Fase de Admisión.



Muestra un desglose detallado por carreras (orden alfabético), incluyendo:

&#x20;- Nota para la carrera.

&#x20;- Asignaturas que ponderan y han subido la nota.

&#x20;- Asignaturas que ponderan pero no han subido la nota.

&#x20;- Lugares en los que ha entrado.

&#x20;- Lugares en los que ha alcanzado justo la nota de corte.

&#x20;- Lugares en los que no ha entrado.

&#x20;- Margen de diferencia entre la nota y la nota de corte de cada lugar.



#### **Informe por margen**



Ordena las carreras según la diferencia entre tu nota estimada y la nota de corte:



&#x20;- Carreras en las que entrarías con margen (margen positivo).

&#x20;- Carreras en las que alcanzarías justo la nota de corte.

&#x20;- Carreras en las que no alcanzarías la nota de corte (margen negativo).



## **Distribución del ejecutable**



Si se distribuye un ejecutable, debe incluirse o enlazarse claramente:

&#x20;- La licencia completa.

&#x20;- La atribución al autor original.

&#x20;- El acceso a la versión original gratuita.

&#x20;- El código fuente correspondiente.

&#x20;- Otros detalles que indique la licencia.



### **Aviso legal y académico**



Este programa no está afiliado oficialmente al Distrito Único Andaluz, a la Junta de Andalucía ni a ninguna universidad.



Los resultados generados:



\- Son estimaciones orientativas.

\- Pueden no coincidir exactamente con los cálculos oficiales.

\- No garantizan admisión en ningún grado.

\- Dependen de que los datos incluidos estén actualizados y sean correctos.

\- Deben contrastarse siempre con fuentes oficiales.



### **Licencia**



Copyright © 2026 Álvaro López Pérez



Programa original: Calculadora PAU Andalucía (2026)



Este proyecto se distribuye bajo la licencia: ALOPPER BY-RC-SA-NAI v1.0



Se permite el uso, copia, distribución gratuita y modificación bajo la misma licencia, con atribución obligatoria, indicación de cambios y enlace visible a la versión original gratuita.



No se permite, salvo autorización previa, expresa y por escrito del titular:



&#x20;- Vender el programa.

&#x20;- Sublicenciarlo.

&#x20;- Alquilarlo.

&#x20;- Ponerlo detrás de pago.

&#x20;- Incluirlo en productos de pago.

&#x20;- Explotarlo comercialmente como producto o servicio.

&#x20;- Ofrecerlo como servicio remoto comercial.

&#x20;- Usarlo para entrenar, ajustar, evaluar o desarrollar sistemas de inteligencia artificial.



Consulta el texto completo en: LICENSE.txt



### **Versión original gratuita**



La versión original gratuita está disponible en:

https://drive.google.com/drive/folders/1wqzLrA6vG\_kt93CTAKJ6Gax0JJEQPa\_\_



Repositorio oficial:

https://github.com/Alvaro-Lopez-Perez8/Calculadora-PAU-Andalucia.git



### **Autor**

El autor de este programa es Álvaro López Pérez.

Contacto: alopper8@gmail.com



### **Contribuciones**



Se pueden proponer mejoras, correcciones o adaptaciones mediante issues o pull requests, siempre respetando la licencia del proyecto. No dudes en ponerte en contacto conmigo (información en el apartado "Autor").



Cualquier versión modificada deberá:



&#x20;- Indicar claramente que es una versión modificada.

&#x20;- Mantener la atribución al autor original.

&#x20;- Enlazar la versión original gratuita.

&#x20;- Distribuirse gratuitamente.

&#x20;- Compartirse bajo la misma licencia.

&#x20;- Incluir los cambios realizados.

&#x20;- No presentarse como versión oficial si no ha sido publicada por el autor original.



Consulta el texto completo en: LICENSE.txt



### **Estado del proyecto**



Proyecto desarrollado para facilitar una estimación orientativa de la nota de admisión universitaria en Andalucía para la PAU.



El programa puede requerir actualizaciones futuras si cambian:

&#x20;- Las ponderaciones oficiales.

&#x20;- Las notas de corte (varían cada año).

&#x20;- La normativa de admisión.

&#x20;- La estructura de la PAU.

&#x20;- La oferta de grados universitarios.

