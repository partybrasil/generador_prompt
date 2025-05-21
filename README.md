# Generador de Prompts para Apps con Copilot

Este proyecto es un generador interactivo de prompts para describir aplicaciones de software, pensado para facilitar la creación de especificaciones detalladas que pueden ser usadas con GitHub Copilot u otras IA de desarrollo.

## Características

- Interfaz de consola amigable y guiada.
- Preguntas sobre tipo de app, público objetivo, plataforma, lenguaje, IDE, base de datos, autenticación, despliegue, estructura, opciones de inicio y características.
- Selección de características desde una lista extensa y posibilidad de añadir propias.
- Opción de randomizar un proyecto completo para inspiración o pruebas.
- Generación automática de un archivo de prompt en formato Markdown, listo para usar.
- Uso de iconos y descripciones para mayor claridad en las opciones.

## Uso

1. Ejecuta el script principal:

   ```bash
   python "python generador_prompt.py"
   ```

2. Elige si deseas crear un proyecto manualmente o randomizar uno.
3. Responde a las preguntas que aparecen en pantalla.
4. Al finalizar, se generará un archivo `<nombre_proyecto>-prompt.md` en una carpeta con el nombre de tu proyecto.

## Ejemplo de ejecución

```
🧠 Bienvenido al generador de prompts para apps con Copilot

❓ ¿Qué deseas hacer?
  1. 🛠️ Crear un proyecto - 
  2. 🎲 Randomizar - 

👉 Tu elección (número(s) o texto): 1

📛 ¿Cómo se llama tu proyecto?
...
```

## Estructura generada

```
<nombre_proyecto>/
├── src/
│   └── main.py
├── README.md
├── LICENSE
├── requirements.txt
└── <nombre_proyecto>-prompt.md
```

## Requisitos

- Python 3.7 o superior

## Instalación

No requiere dependencias externas. Solo asegúrate de tener Python instalado.

## Licencia

MIT

## Autor

Hecho con ❤️ para facilitar la creación de prompts y especificaciones para IA y desarrolladores.
