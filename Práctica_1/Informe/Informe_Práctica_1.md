    \documentclass[conference,spanish]{IEEEtran}
\IEEEoverridecommandlockouts
% The preceding line is only needed to identify funding in the first footnote. If that is unneeded, please comment it out.
%Template version as of 6/27/2024
\usepackage{cite}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{algorithmic}
\usepackage{algpseudocode}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage[linesnumbered,ruled,vlined]{algorithm2e}
\usepackage{graphicx}
\usepackage{textcomp}
\usepackage[utf8]{inputenc}
\usepackage{circuitikz}
\usepackage{xcolor}
\def\BibTeX{{\rm B\kern-.05em{\sc i\kern-.025em b}\kern-.08em
    T\kern-.1667em\lower.7ex\hbox{E}\kern-.125emX}}
\begin{document}
\title{\textbf{Formulacion de proyecto}}

\author{{Mendoza Aguirre Juan David, juan2220419@correo.uis.edu.co}\\
{Pacheco Jurado Edward Andres, edward2222236@correo.uis.edu.co}\\
{Álbarracin Contreras Joseph Thomas, joseph2220415@correo.uis.edu.co}}

\maketitle


\section{Introducción y descripcion del proyecto }
El estudio del procesamiento digital de señales de audio en el campo de la ingenieria electronica en la actualidad es fundamental debido a las distintas aplicaciones que tienen en el campo que van desde interpretar mensajes a diferenciar voces por medio de la frecuencia de la voz.

El desarrollo de un “código” de MATLAB que toma como entrada una señal de voz humana afectada (manipulada para añadirle distorsiones como cortes, ruido, etc.)  y mediante procesos de tratamiento de la señal genere como salida una señal de audio correspondiente a la voz original de la entrada con un porcentaje menor de distorsión; implementando funciones propias que realicen muestreos para poder analizar las señales con propiedades vistas en el curso de señales discretas.

\section{FUNDAMENTACIÓN TEÓRICA}
 
    Las señales de voz se caracterizan por no ser estacionarias y tener variaciones lentas en el dominio del tiempo, por lo que normalmente se procesan en periodos cortos de tiempo, entre 5 y 30 ms, los cuales se aproximan a señales cuasiperiodicas permitiendo clasificar la voz como sonoro, sordo o silencio. [primera referencia]
    El tono de voz viene determinado por la frecuencia fundamental de las ondas sonoras, debido a esto se puede determinar la diferencia entre sonidos graves, agudos o medios, las cuales son medidas en ciplos por segundo o Hercios (Hz). Para lograr percibir un sonido este debe estar en el rando de audicion de 20 a 20000 Hz. La frecuencia  fundamental de la voz varia dependiendo de si es una voz masculina o femenina, ya que, en el caso de los hombres el rango de la frecuencia oscila entre 110-130 Hz y en el caso de las mujeres entre 200-230 Hz.

    Por otro lado esta la intensidad sonora la cual se define como la cantidad de energia acustica que tiene el sonido. Esta intensidad viene dada por la potencia, que a su vez viene dada de la amplitud que permite distinguir si el sonido es fuerte o debil. Los sonidos que percibe el oido humano tienen que superar el umbral auditivo y no llegar al umbral de dolor (0-140 dB)

    Los filtros de audio tienen como finalidad atenuar la señal de manera progresiva desde una frecuencia determinada dependiendo del tipo de filtro que se requiera usar. Su funcion  recae en limpiar señales de frecuencias no deseadas, ya que, las pistas de audio generalmente cuentan con ruido de baja o alta frecuencia los cuales ocupan energia del sistema. Asimismo sirven para proteger el sistema de daños por exceso de energia de bajas frecuencias las cuales no son controladas.[segunda referencia]



\section{OBJETIVOS}
\subsection{Objetivo general}
    Implementar una herramienta en matlab la cual sea capaz de procesar señales de voz humana afectadas por factores externos, aplicando tecnicas de tratamiento y filtración que permitan reconstruir la señal de voz obteniendo una salida lo mas limpia posible.
\subsection{Objetivos especificos}
\begin{itemize}
    \item Investigar  y seleccionar tecnicas de procesamiento digital  de señales adecuadas para la reduccion de ruido en selales de voz, tales como filtado adaptativo y tecnicas basadas en las transformadas de Fourier.
    \item Implementar funciones personalizadas en Matlab las cuales satisfagan los parametros requeridos para el procesamiento y limpieza de voz
    \item Establecer una evaluación del desempeño de la herramienta que sea realista y, a su vez, objetiva, considerando escenarios de uso prácticos y diversos niveles de afectación de las señales.  
\end{itemize}


\section{METODOLOGÍA A SEGUIR}
\begin{enumerate}

    \item Investigación sobre características y aspectos de la voz humana, frecuencia de operacion y armonicos caracteriscos de la voz humana.
    \item Componentes de una señal de audio de voz en matlab. 
    \item Tratamiento de señales de audio en matlab.

    \item 

    digitalizacion de la señal, frecuencia dominante,caracteristicas,filtrado.

    escalas de mel "
    buscar como funciona y como dan caracteristicas distintivas a las señales de audio "
\end{enumerate}



\bibliographystyle{ieeetr}
\bibliography{citas}

\end{document}
