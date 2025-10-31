
# Agente de IA para Investigación

Este proyecto es un agente de IA diseñado para asistir en tareas de investigación. Utiliza el modelo de lenguaje Claude 3.5 Sonnet de Anthropic, junto con herramientas de búsqueda y guardado, para recopilar, resumir y almacenar información sobre un tema determinado.

## Características

- **Modelo de Lenguaje Avanzado:** Impulsado por Claude 3.5 Sonnet para un razonamiento y una generación de texto de alta calidad.
- **Capacidades de Búsqueda:** Integrado con DuckDuckGo y Wikipedia para acceder a una amplia gama de información.
- **Almacenamiento de Resultados:** Guarda los resultados de la investigación en un archivo de texto para referencia futura.
- **Salida Estructurada:** Utiliza Pydantic para analizar y presentar la información de manera organizada, incluyendo el tema, un resumen, las fuentes y las herramientas utilizadas.
- **Fácil de Usar:** Simplemente ejecuta el script y proporciona un tema de investigación para comenzar.

## Cómo Funciona

1.  El usuario inicia el script `main.py`.
2.  Se le pide al usuario que ingrese una consulta de investigación.
3.  El agente de LangChain, utilizando el modelo Claude 3.5 Sonnet, recibe la consulta.
4.  El agente decide qué herramientas utilizar para la tarea (búsqueda en DuckDuckGo, consulta en Wikipedia).
5.  Una vez que se recopila la información, el agente la resume.
6.  La herramienta `save_tool` guarda el resumen en un archivo `research_output.txt`.
7.  La respuesta final, estructurada como un objeto `ResearchResponse`, se imprime en la consola.

## Archivos del Proyecto

- **`main.py`:** El script principal que configura y ejecuta el agente de IA. Maneja la entrada del usuario, la orquestación del agente y el análisis de la salida.
- **`tools.py`:** Define las herramientas que el agente puede utilizar, incluyendo la búsqueda en la web, la consulta a Wikipedia y la función para guardar archivos.
- **`requirements.txt`:** Enumera todas las dependencias de Python necesarias para ejecutar el proyecto.
- **`README.md`:** Este archivo, que proporciona una visión general del proyecto.

## Instalación y Uso

1.  **Clona el repositorio:**
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_DIRECTORIO>
    ```

2.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configura tus variables de entorno:**
    Crea un archivo llamado `.env` en el directorio raíz del proyecto y agrega tu clave de API de Anthropic:
    ```
    ANTHROPIC_API_KEY='tu_clave_de_api_aqui'
    ```

4.  **Ejecuta el agente:**
    ```bash
    python main.py
    ```

5.  **Ingresa tu consulta:**
    Cuando se te solicite, escribe el tema sobre el que deseas investigar y presiona Enter.
    ```
    En que te puedo ayudar hoy? <TU_TEMA_DE_INVESTIGACIÓN>
    ```

6.  **Revisa los resultados:**
    El agente procesará tu solicitud, imprimirá la respuesta estructurada en la consola y guardará los hallazgos en `research_output.txt`.
