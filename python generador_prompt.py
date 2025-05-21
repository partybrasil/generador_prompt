import os
import textwrap

def ask(question, options=None, allow_custom=False, explanation=None):
    print(f"\n{question}")
    if explanation:
        print(textwrap.fill(f"💡 {explanation}", width=80))

    if options:
        for idx, opt in enumerate(options, 1):
            print(f"  {idx}. {opt['name']} - {opt.get('description', '')}")

    while True:
        choice = input("\n👉 Tu elección (número o texto): ").strip()
        if options and choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]['name']
        elif allow_custom and choice:
            return choice
        elif not options and choice:
            return choice
        else:
            print("❌ Entrada no válida. Intenta de nuevo.")

def collect_project_info():
    data = {}

    data['project_name'] = ask("¿Cómo se llama tu proyecto?")
    data['description'] = ask("Describe brevemente qué hace la app.")

    data['ide'] = ask("¿Con qué IDE trabajarás?", [
        {"name": "Visual Studio Code", "description": "Popular, extensible y con integración directa con Copilot."},
        {"name": "PyCharm", "description": "Potente para Python, con herramientas integradas para testing, depuración, etc."}
    ])

    data['language'] = ask("¿Qué lenguaje principal usará tu app?", [
        {"name": "Python", "description": "Fácil de usar, gran ecosistema."},
        {"name": "JavaScript", "description": "Ideal para apps web con Node.js."},
        {"name": "Java", "description": "Robusto, multiplataforma, ideal para Android y backend."},
        {"name": "Otro"},
    ], allow_custom=True)

    data['gui'] = ask("¿Tu app tendrá interfaz gráfica?", [
        {"name": "Sí"},
        {"name": "No"}
    ])
    
    if data['gui'] == "Sí":
        data['gui_toolkit'] = ask("¿Qué toolkit para GUI prefieres?", [
            {"name": "PySide6", "description": "Moderno, potente, basado en Qt."},
            {"name": "Tkinter", "description": "Simple, viene con Python por defecto."},
            {"name": "Kivy", "description": "Ideal para apps móviles y multitáctiles."},
            {"name": "Electron + JS", "description": "Para interfaces web de escritorio."}
        ])

    data['features'] = []
    print("\n🔧 Enumera las características principales de tu app (escribe 'fin' para terminar):")
    while True:
        feat = input("➕ Característica: ").strip()
        if feat.lower() == "fin":
            break
        elif feat:
            data['features'].append(feat)

    data['extra_files'] = {
        "README.md": True,
        "LICENSE": "MIT"
    }

    return data

def generate_prompt_file(data):
    project_dir = os.path.join(os.getcwd(), data['project_name'])
    os.makedirs(project_dir, exist_ok=True)
    filepath = os.path.join(project_dir, "prompt.md")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Prompt para GitHub Copilot: {data['project_name']}\n\n")
        f.write(f"## Descripción del Proyecto\n{data['description']}\n\n")
        f.write(f"**IDE sugerida:** {data['ide']}\n")
        f.write(f"**Lenguaje principal:** {data['language']}\n")

        if data['gui'] == "Sí":
            f.write(f"**Interfaz gráfica:** Sí, usando {data['gui_toolkit']}\n")
        else:
            f.write(f"**Interfaz gráfica:** No\n")

        f.write("\n## Características clave\n")
        for feat in data['features']:
            f.write(f"- {feat}\n")

        f.write("\n## Estructura del proyecto esperada\n```plaintext\n")
        f.write(f"{data['project_name']}/\n")
        f.write("├── src/\n")
        f.write("│   └── main.py\n")
        f.write("├── README.md\n")
        f.write("├── LICENSE\n")
        f.write("└── requirements.txt\n```\n")

        f.write("\n## Archivos adicionales requeridos\n")
        f.write("- `README.md` con descripción clara de la app.\n")
        f.write("- `LICENSE` bajo licencia MIT.\n")

        f.write("\n## Instrucciones para la IDE/Copilot\n")
        f.write(textwrap.dedent("""\
            Por favor, crea toda la estructura del proyecto automáticamente en el workspace activo.
            Asegúrate de generar los siguientes archivos y carpetas:
            - Una carpeta `/src` con un archivo `main.py` como punto de entrada.
            - Un archivo `README.md` en la raíz con la descripción del proyecto.
            - Un archivo `LICENSE` bajo la licencia MIT.
            - Un archivo `requirements.txt` con dependencias necesarias.

            Usa buenas prácticas, separación de lógica, y comentarios explicativos.
        """))

    print(f"\n✅ Prompt generado con éxito en: {filepath}")

if __name__ == "__main__":
    print("🧠 Bienvenido al generador de prompts para apps con Copilot\n")
    data = collect_project_info()
    generate_prompt_file(data)
