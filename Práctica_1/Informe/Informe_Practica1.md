
# Laboratorio 2. PROGRAMACIÓN EN RADIO DEFINIDA POR SOFTWARE (GNURADIO) 

### Integrantes
- **Danny Carolina Sierra Téllez** - 2220409
- **Duban Andretti Gutierréz León** - 2220396

Escuela de Ingenierías Eléctrica, Electrónica y de Telecomunicaciones  
Universidad Industrial de Santander

### Fecha
31 de agosto de 2025

---
## Contenido

### Resumen
En esta práctica se implementaron conceptos de radio definida por software (SDR) utilizando la plataforma GNU Radio. El trabajo incluyó la familiarización con el manejo de repositorios en GitHub desde un entorno de programación colaborativo, integrando la terminal local con la nube para simular un trabajo similar al de la industria. Se desarrollaron bloques de programación en Python para implementar funciones como un acumulador, diferenciador y otros operadores estadísticos sobre señales en el dominio del tiempo. Estas implementaciones permitieron fortalecer la comprensión de los sistemas de comunicaciones digitales en tiempo real y evidenciaron la flexibilidad de GNU Radio para el diseño, análisis y evaluación de sistemas de procesamiento de señales.

### Introducción
La Radio Definida por Software (SDR) cumple un papel fundamental en las telecomunicaciones modernas gracias a su flexibilidad y adaptabilidad. Esta tecnología permite que una misma plataforma soporte múltiples estándares y pueda soportar una amplia variedad de señales sólo con usar una computadora y software especializado, reconfigurando tareas relacionadas con la transmisión y recepción de señales de radiofrecuencia.
En el marco de la práctica, se implementaron bloques en Python dentro de GNU Radio para simular funciones clásicas tales como un acumulador, diferenciador y operadores estadísticos de las señales en el tiempo como: la media, media cuadrática, valor RMS, densidad de potencia espectral y desviación estándar. Dichos bloques ofrecen una herramienta útil para analizar el comportamiento de señales digitales en tiempo real y constituyen una base para el desarrollo de aplicaciones más avanzadas en escenarios de la vida real en telecomunicaciones.

---
## Contenido

### **Metodología**
La práctica se desarrolló en 3 etapas principales:

1. Gestión del repositorio en GitHub: 
En esta primera etapa se creó la rama  principal de esta entrega, denominada Practica_1. Dentro de esta rama se organizó la estructura de carpetas requeridas en la guía de laboratorio. Adicionalmente, se ejecutaron los diferentes comandos de Git en el repositorio local, lo que permitió evidenciar los cambios y el progreso del trabajo en la plataforma de GitHub.

2. Implementación en GNU Radio: 
En la segunda etapa, se empleó la aplicación de GNU Radio para programar los bloques en Python, tomando como referencia el libro guía mencionado en la práctica. Se corrigieron errores y se ejecutaron las diferentes funciones de acumulador, diferenciador y operadores estadísticos. Además, se incorporaron bloques adicionales como Vector Source, QT GUI time sink y  QT GUI number sink para la generación y visualización de las señales en tiempo real.

3. Documentación y entrega: 
En la última etapa  se integraron los aportes individuales de los integrantes y se procedió a elaborar el presente informe de manera colaborativa dentro del repositorio.

## **Resultados**
Los resultados obtenidos en la práctica para cada uno de los bloques propuestos se muestra a continuación, además se agrega una apliación de la estadística vista en clase:

### **Acumulador**
Se tiene el diagrama de flujo para el modelo de acumulador, este permite obtener la energía total en una ventana de tiempo de la señal y ayuda a eliminar el ruido dado que al sumar muchas muestras de una señal aleatoria el ruido tiende a cancelarse.

### **Diagrama de Flujo del Acumulador**
Para el diagrama de flujo se usó una frecuencia de muestreo por defecto de 32 kHz debido a que con esta se evita la condición de aliasing al tener más del doble de la frecuencia máxima; un vector source con 8 muestras, un throttle el cual ayuda a regular la velocidad a la que se ejecuta el diagrama de flujo cuando este no está y se está trabajando solo con simulación.

<div align="center">

  <img width="921" height="446" alt="diagrama de flujo"  src="https://github.com/user-attachments/assets/3351beac-048d-4e51-92ff-991926e34c38"
 alt="Diagrama de flujo del acumulador" width="400">

  <p><b>Figura 1. Diagrama de Flujo del Acumulador.</p>

</div>

<div align="center">

<img width="1905" height="976" alt="image" src="https://github.com/user-attachments/assets/f04305f9-8ce2-4180-a343-5a31dd18094f" alt="acumulador con 8 muestras y fs=32k" width="400">

  <p><b>Figura 2. Señal de entrada y salida del acumulador con parámetros iniciales.</p>

</div>

De la figura 2 se pudo observar como ante una señal cuadrada que varía entre A (amplitud) y -A, el acumulador genera una señal rampa que aumenta o disminuye dependiendo de los valores de la señal de entrada.

</div>

<div align="center">

<img width="1890" height="970" alt="image" src="https://github.com/user-attachments/assets/b150aca7-6052-4a12-8bef-4d65b5ca255f" alt="acumulador con 8 muestras y fs=32k" width="400">

  <p><b>Figura 3. Señal de entrada y salida del acumulador con una variación en el número de muestras.</p>

</div>

En la figura 3 se observó como al variar el número de muestras se genera un sobre salto en la señal de salida, esto se debe a que al ser un acumulador la señal guarda memoria donde cada muestra depende de lo anterior, por esto la señal de salida cambia en ciertos puntos su forma y amplitud.

</div>

<div align="center">

<img width="1890" height="970" alt="image" src="https://github.com/user-attachments/assets/d746c942-9064-415a-be26-375222fe05f3" alt="acumulador con 8 muestras y fs=32k" width="400">

  <p><b>Figura 4. Señal de entrada y salida del acumulador con una variación en la frecuencia de muestreo.</p>

</div>

Se pudo observar como en la figura 4 como al aumentar el valor de la frecuencia de muestreo no se presentan grandes cambios en la señal de salida debido a que las muestras van a estar más cerca una de otra, mientras que si se disminuye se tarda un gran tiempo en iniciar el acumulador a funcionar, esto se debe a que el acumulador recibe menos información en tiempo real.

### **Diferenciador**

El diferenciador es una herramienta que permite ver de manera clara y precisa los cambios rápidos que ocurren a lo largo de la señal, además puede ser útil como un filtro pasa-altas, dado que en el dominio de la frecuencia el diferenciador atenua las componentes cercanas a 0.

### **Diagrama de Flujo del Diferenciador**
Para el diagrama de flujo se usó una frecuencia de muestreo por defecto de 32 kHz debido a que con esta se evita la condición de aliasing al tener más del doble de la frecuencia máxima; un vector source con 8 muestras, un throttle el cual ayuda a regular la velocidad a la que se ejecuta el diagrama de flujo cuando este no está y se está trabajando solo con simulación.

<div align="center">

  <img width="958" height="463" alt="image" src="https://github.com/user-attachments/assets/d84070e6-69e0-4802-a0e2-8436e65ec593" alt="Diagrama de flujo del acumulador" width="400">

  <p><b>Figura 5. Diagrama de Flujo del Diferenciador.</p>

</div>

<div align="center">

<img width="1890" height="950" alt="image" src="https://github.com/user-attachments/assets/c4b1fdac-3016-4e2b-9255-606c6f4910c1" alt="acumulador con 8 muestras y fs=32k" width="400">

  <p><b>Figura 6. Señal de entrada y salida del acumulador con parámetros iniciales.</p>

</div>

De la figura 6 se pudo observar como ante una señal cuadrada que varía entre A (amplitud) y -A, el diferenciador presenta una de rampas las cuales tienden a ser pulso que representan los cambios bruzcos sufridos por la señal de entrada a lo largo del tiempo.

</div>

<div align="center">

<img width="1896" height="955" alt="image" src="https://github.com/user-attachments/assets/c9eb452e-4759-41fd-8adc-832cf2e9cae1" alt="acumulador con 8 muestras y fs=32k" width="400">

  <p><b>Figura 7. Señal de entrada y salida del acumulador con una variación en el número de muestras.</p>

</div>

Del análisis de al figura 7 se tiene que el número de muestras está directamente relacionado con el tiempo entre la generación de cada pulso, a mayor número de muestras, mayor fue el tiempo entre cada pulso, mientras que a menor número de muestras los pulsos se generaron uno después del otro, esto se debe a que mientras haya una mayor cantidad de muestras habrá menor disperción entre los datos y por lo tanto menos cambios bruzcos.


### **Parte Estadística**

Se tiene el diagrama de flujo para el modelo de acumulador, este permite obtener la energía total en una ventana de tiempo de la señal y ayuda a eliminar el ruido dado que al sumar muchas muestras de una señal aleatoria el ruido tiende a cancelarse.

### **Diagrama de Flujo de la Parte Estadística**
Para el diagrama de flujo se usó una frecuencia de muestreo por defecto de 32 kHz debido a que con esta se evita la condición de aliasing al tener más del doble de la frecuencia máxima; un vector source con 8 muestras, un throttle el cual ayuda a regular la velocidad a la que se ejecuta el diagrama de flujo cuando este no está y se está trabajando solo con simulación.

<div align="center">

<img width="860" height="700" alt="image" src="https://github.com/user-attachments/assets/06b88c3c-5468-41f9-99ab-792ac0cd0db3" alt="Diagrama de flujo del acumulador" width="400">

  <p><b>Figura 8. Diagrama de Flujo de la Parte Estadística.</p>

| Vector de Entrada | Número de Muestras | Frecuencia de Muestreo [kHz]| RMS | Media | Desviación Estándar | Promedio Tiempo | Media Cuadrática |
|-------------------|-------------------|------------------------------|-----|-------|---------------------|-----------------|------------------|
| (1,1,1,1,-1,-1,-1,-1) | 8 | 32 | 1 | 0 | 1 | 1 | 1 |
| (1,1,-1,-1)| 4 | 32 | 1 | 0 | 1 | 1 | 1 |
| (1,1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,-1,-1) | 16 | 32 | 1 | 0.00073 | 1 | 1 | 1 |
| (1,1,1,1,-1,-1,-1,-1) | 8 | 2 | 1 | 0 | 1 | 1 | 1 |
| (1,1,1,1,-1,-1,-1,-1)| 8 | 64 | 1 | 0 | 1 | 1 | 1 |
| (1,1,1,1,-1,-1,-1,-1) | 8 | 320 | 1 | 0 | 1 | 1 | 1 |
| (1,2,7,5,-2,-1,-8,-3) | 8 | 32 | 4.43011 | 0.125 | 4.448247 | 19.625 | 19.625 |
| (3,2,2,4,-2,-5,-6,-2) | 8 | 32 | 3.570714 | -0.5 | 3.535534 | 12.75 | 12.75 |

<p><b>Tabla 1. Datos Obtenidos para la Parte Estadística.</p>
</b>
</div>
De la tabla 1 se pudo observar como los parámetros de entrada afectan de manera muy directa a los resultados estadísticos obtenidos, en primera instancia se varió el número de muestras en donde se puede apreciar en la tabla 1 como se ve afectada únicamente la media, pues ésta comienza a oscilar entre un valor A positivo a un valor -A, luego se vavrió la frecuencia de muestreo, pero no se envidenció ningún cambio en los valores estadísticos esto se debe a que la frecuencia de muestreo define cada cuanto se toma una muestra, pero esto no afecta a los valores del vector, por último se cambió el vector de entrada, para este caso variaron de gran manera los valores obtenidos dado que este vector simula una señal aleatoria, también se pudo notar como los valores de "promedio de tiempo" y "media cuadrática" son iguales para todos los casos.

### **Aplicación**
### **Sistema de Audio**
En los sistemas de audio, la estadística es fundamental para describir y controlar las propiedades de las señales sonoras, la media permite identificar si la señal está centrada en cero o presenta un desplazamiento indeseado (DC), el RMS se utiliza para medir la potencia percibida del sonido, siendo clave en normalización y control de volumen, la desviación estándar refleja la variabilidad o dinámica del audio, útil en procesos como la compresión para equilibrar partes suaves y fuertes, el promedio en el tiempo y la media cuadrática permiten estimar la energía media de la señal. En conjunto, estas medidas estadísticas permiten analizar, procesar y optimizar la calidad del sonido en aplicaciones como mezcla, ecualización, reducción de ruido y transmisión de audio.

## **Referencia**
[1] H. Ortega Boada y O. M. Reyes Torres, *Comunicaciones digitales basadas en radio definida por software*.  
1ª ed. Bucaramanga, Colombia: Editorial UIS, 2019. [En línea].  Disponible: https://sites.google.com/saber.uis.edu.co/comdig
