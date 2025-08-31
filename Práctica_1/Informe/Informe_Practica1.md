
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

### **Resultados**
Los resultados obtenidos en la práctica para cada uno de los bloques propuestos se muestra a continuación, además se agrega una apliación de la estadística vista en clase:

### **Acumulador**
Se tiene el diagrama de flujo para el modelo de acumulador, este permite obtener la energía total en una ventana de tiempo de la señal y ayuda a eliminar el ruido dado que al sumar muchas muestras de una señal aleatoria el ruido tiende a cancelarse.

**Diagrama de Flujo del Acumulador**
Para el diagrama de flujo se usó 

<div align="center">

  <img width="921" height="446" alt="diagrama de flujo"  src="https://github.com/user-attachments/assets/3351beac-048d-4e51-92ff-991926e34c38"
 alt="Diagrama de flujo del acumulador" width="400">

  <p><b>Figura 1. Diagrama de Flujo del Acumulador.</p>

</div>

<div align="center">

<img width="1905" height="976" alt="image" src="https://github.com/user-attachments/assets/f04305f9-8ce2-4180-a343-5a31dd18094f" alt="acumulador con 8 muestras y fs=32k" width="400">

  <p><b>Figura 2. Señal de entrada y salida del acumulador.</p>

</div>

### **Diferenciador**

### **Parte Estadística**

### **Aplicación**
