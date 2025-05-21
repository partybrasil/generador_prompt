import os
import textwrap

def ask(question, options=None, allow_custom=False, explanation=None, icon=None, multi_select=False):
    icon_str = f"{icon} " if icon else ""
    print(f"\n{icon_str}{question}")
    if explanation:
        print(textwrap.fill(f"💡 {explanation}", width=80))

    if options:
        for idx, opt in enumerate(options, 1):
            icon_opt = opt.get('icon', '')
            desc = opt.get('description', '')
            print(f"  {idx}. {icon_opt} {opt['name']} - {desc}")

    if multi_select and options:
        print("👉 Puedes seleccionar varios números separados por coma (ej: 1,3,5). Escribe 'fin' para terminar.")

    while True:
        choice = input("\n👉 Tu elección (número(s) o texto): ").strip()
        if multi_select and options:
            if choice.lower() == "fin":
                return []
            nums = [c.strip() for c in choice.split(",") if c.strip().isdigit()]
            if nums:
                selected = []
                for n in nums:
                    idx = int(n)
                    if 1 <= idx <= len(options):
                        selected.append(options[idx-1]['name'])
                if selected:
                    return selected
            print("❌ Entrada no válida. Intenta de nuevo.")
        elif options and choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]['name']
        elif allow_custom and choice:
            return choice
        elif not options and choice:
            return choice
        else:
            print("❌ Entrada no válida. Intenta de nuevo.")

def collect_project_info():
    data = {}

    data['project_name'] = ask("¿Cómo se llama tu proyecto?", icon="📛")
    data['description'] = ask("Describe brevemente qué hace la app.", icon="📝")

    data['app_type'] = ask("¿Qué tipo de aplicación es?", [
        {"name": "Web", "icon": "🌐"},
        {"name": "Escritorio", "icon": "🖥️"},
        {"name": "Móvil", "icon": "📱"},
        {"name": "API/Backend", "icon": "🔗"},
        {"name": "CLI", "icon": "💻"},
        {"name": "Otro", "icon": "❓"}
    ], allow_custom=True, icon="🗂️")

    data['target_audience'] = ask("¿Quién es el público objetivo?", [
        {"name": "Usuarios finales", "icon": "👤"},
        {"name": "Empresas", "icon": "🏢"},
        {"name": "Desarrolladores", "icon": "👨‍💻"},
        {"name": "Educativo", "icon": "🎓"},
        {"name": "Otro", "icon": "❓"}
    ], allow_custom=True, icon="🎯")

    data['platform'] = ask("¿En qué plataforma funcionará?", [
        {"name": "Windows", "icon": "🪟"},
        {"name": "Linux", "icon": "🐧"},
        {"name": "macOS", "icon": "🍏"},
        {"name": "Android", "icon": "🤖"},
        {"name": "iOS", "icon": "📱"},
        {"name": "Multiplataforma", "icon": "🌍"},
        {"name": "Otro", "icon": "❓"}
    ], allow_custom=True, icon="💻")

    data['ide'] = ask("¿Con qué IDE trabajarás?", [
        {"name": "Visual Studio Code", "icon": "🟦", "description": "Popular, extensible y con integración directa con Copilot."},
        {"name": "PyCharm", "icon": "🐍", "description": "Potente para Python, con herramientas integradas para testing, depuración, etc."},
        {"name": "Otro", "icon": "❓"}
    ], allow_custom=True, icon="🛠️")

    data['language'] = ask("¿Qué lenguaje principal usará tu app?", [
        {"name": "Python", "icon": "🐍", "description": "Fácil de usar, gran ecosistema."},
        {"name": "JavaScript", "icon": "🟨", "description": "Ideal para apps web con Node.js."},
        {"name": "Java", "icon": "☕", "description": "Robusto, multiplataforma, ideal para Android y backend."},
        {"name": "C#", "icon": "⚙️", "description": "Potente para apps de escritorio y web."},
        {"name": "C++", "icon": "💻", "description": "Alto rendimiento, ideal para sistemas y juegos."},
        {"name": "Go", "icon": "🐹", "description": "Eficiente, ideal para backend y sistemas concurrentes."},
        {"name": "Rust", "icon": "🦀", "description": "Seguro y rápido, ideal para sistemas críticos."},
        {"name": "TypeScript", "icon": "🔷", "description": "Superset de JavaScript, tipado estático."},
        {"name": "Kotlin", "icon": "🅺", "description": "Moderno, ideal para Android y backend JVM."},
        {"name": "Swift", "icon": "🦅", "description": "Lenguaje de Apple para iOS/macOS."},
        {"name": "PHP", "icon": "🐘", "description": "Popular para desarrollo web backend."},
        {"name": "Ruby", "icon": "💎", "description": "Sencillo y productivo, ideal para web (Rails)."},
        {"name": "Dart", "icon": "🎯", "description": "Ideal para apps móviles con Flutter."},
        {"name": "Scala", "icon": "🔺", "description": "Funcional y orientado a objetos sobre JVM."},
        {"name": "C", "icon": "🔵", "description": "Lenguaje clásico, bajo nivel, muy usado en sistemas."},
        {"name": "R", "icon": "📊", "description": "Especializado en estadística y análisis de datos."},
        {"name": "MATLAB", "icon": "📐", "description": "Ideal para matemáticas, ingeniería y simulación."},
        {"name": "Perl", "icon": "🦋", "description": "Potente para scripting y procesamiento de texto."},
        {"name": "Shell/Bash", "icon": "💻", "description": "Automatización y scripts en sistemas Unix."},
        {"name": "Otro", "icon": "❓"}
    ], allow_custom=True, icon="💬")

    data['gui'] = ask("¿Tu app tendrá interfaz gráfica?", [
        {"name": "Sí", "icon": "🖼️"},
        {"name": "No", "icon": "🚫"}
    ], icon="🖌️")
    
    if data['gui'] == "Sí":
        data['gui_toolkit'] = ask("¿Qué toolkit para GUI prefieres?", [
            {"name": "PySide6", "icon": "🟪", "description": "Moderno, potente, basado en Qt."},
            {"name": "Tkinter", "icon": "🟦", "description": "Simple, viene con Python por defecto."},
            {"name": "Kivy", "icon": "🌱", "description": "Ideal para apps móviles y multitáctiles."},
            {"name": "Electron + JS", "icon": "⚡", "description": "Para interfaces web de escritorio."},
            {"name": "PyQt5", "icon": "🟥", "description": "Popular, multiplataforma, basado en Qt."},
            {"name": "wxPython", "icon": "🟧", "description": "Nativo, multiplataforma, fácil de usar."},
            {"name": "Dear PyGui", "icon": "🎨", "description": "Rápido, orientado a gráficos y visualización."},
            {"name": "FLTK", "icon": "🟩", "description": "Ligero, multiplataforma, ideal para apps sencillas."},
            {"name": "PySimpleGUI", "icon": "🟦", "description": "Muy fácil de usar, abstrae otros toolkits."},
            {"name": "GTK+ (PyGObject)", "icon": "🟩", "description": "Moderno, usado en GNOME, multiplataforma."},
            {"name": "CustomTkinter", "icon": "🟦", "description": "Extiende Tkinter con estilos modernos."},
            {"name": "Remi", "icon": "🌐", "description": "GUI en navegador, sin dependencias externas."},
            {"name": "PyForms", "icon": "📝", "description": "Framework modular para interfaces complejas."},
            {"name": "PyGame", "icon": "🎮", "description": "Ideal para juegos y visualizaciones interactivas."},
            {"name": "Toga", "icon": "🦙", "description": "Nativo, multiplataforma, parte de BeeWare."},
            {"name": "Enaml", "icon": "🧩", "description": "Declarativo, inspirado en QML, para UIs reactivas."},
            {"name": "cefpython", "icon": "🌐", "description": "Embebe Chromium, para apps con HTML/JS."},
            {"name": "PyWebview", "icon": "🖼️", "description": "Ventanas nativas para apps web ligeras."},
            {"name": "KivyMD", "icon": "📱", "description": "Material Design sobre Kivy, para apps modernas."},
            {"name": "PyGTK", "icon": "🟩", "description": "Envoltorio clásico de GTK+ para Python."},
            {"name": "PyObjC", "icon": "🍏", "description": "Para apps nativas en macOS usando Cocoa."},
            {"name": "PyFLTK", "icon": "🟩", "description": "Ligero, multiplataforma, basado en FLTK."},
            {"name": "PySDL2", "icon": "🎮", "description": "Para interfaces gráficas y multimedia avanzadas."},
            {"name": "PyOpenGL", "icon": "🔺", "description": "Para interfaces 3D y visualización avanzada."},
            {"name": "PyQt6", "icon": "🟥", "description": "Versión moderna de PyQt, soporte Qt6."},
            {"name": "PySide2", "icon": "🟪", "description": "Versión anterior de PySide, basado en Qt5."},
            {"name": "PyForms-Web", "icon": "🌐", "description": "Interfaces web usando PyForms."},
            {"name": "PySciter", "icon": "🖼️", "description": "GUI nativa con HTML/CSS/JS, multiplataforma."},
            {"name": "PyAutoGUI", "icon": "🤖", "description": "Automatización de GUI, útil para testing."},
            {"name": "Otro", "icon": "❓"}
        ], allow_custom=True, icon="🧰")

    data['database'] = ask("¿Usarás base de datos?", [
        {"name": "No", "icon": "🚫"},
        {"name": "SQLite", "icon": "🗄️"},
        {"name": "PostgreSQL", "icon": "🐘"},
        {"name": "MySQL", "icon": "🛢️"},
        {"name": "MongoDB", "icon": "🍃"},
        {"name": "Otro", "icon": "❓"}
    ], allow_custom=True, icon="🗃️")

    data['authentication'] = ask("¿Requiere autenticación de usuarios?", [
        {"name": "No", "icon": "🚫"},
        {"name": "Sí, local", "icon": "🔒"},
        {"name": "Sí, OAuth/Google/Facebook", "icon": "🌐"},
        {"name": "Otro", "icon": "❓"}
    ], allow_custom=True, icon="🔑")

    data['deployment'] = ask("¿Dónde planeas desplegar la app?", [
        {"name": "No aplica", "icon": "🚫"},
        {"name": "Heroku", "icon": "☁️"},
        {"name": "Vercel", "icon": "▲"},
        {"name": "AWS", "icon": "🟧"},
        {"name": "Servidor propio", "icon": "🖥️"},
        {"name": "Google Cloud", "icon": "☁️"},
        {"name": "Otro", "icon": "❓"}
    ], allow_custom=True, icon="🚀")

    # Lista predefinida de características
    predefined_features = [
        {"name": "Registro de usuarios", "icon": "📝"},
        {"name": "Inicio de sesión", "icon": "🔑"},
        {"name": "Panel de administración", "icon": "🛠️"},
        {"name": "Notificaciones", "icon": "🔔"},
        {"name": "Soporte multi-idioma", "icon": "🌐"},
        {"name": "Exportar a PDF", "icon": "📄"},
        {"name": "Carga de archivos", "icon": "📤"},
        {"name": "Búsqueda avanzada", "icon": "🔍"},
        {"name": "Gráficas y reportes", "icon": "📊"},
        {"name": "Integración con API externa", "icon": "🔗"},
        {"name": "Modo oscuro", "icon": "🌙"},
        {"name": "Soporte offline", "icon": "📴"},
        {"name": "Chat en tiempo real", "icon": "💬"},
        {"name": "Geolocalización", "icon": "📍"},
        {"name": "Carrito de compras", "icon": "🛒"},
        {"name": "Pagos en línea", "icon": "💳"},
        {"name": "Sistema de comentarios", "icon": "💬"},
        {"name": "Calendario", "icon": "📅"},
        {"name": "Gestión de usuarios", "icon": "👥"},
        {"name": "Soporte para plugins/extensiones", "icon": "🧩"},
        {"name": "API REST", "icon": "🔗"},
        {"name": "Autoguardado", "icon": "💾"},
        {"name": "Historial de cambios", "icon": "🕒"},
        {"name": "Soporte para notificaciones push", "icon": "📲"},
        {"name": "Integración con redes sociales", "icon": "📱"},
        {"name": "Soporte para temas personalizados", "icon": "🎨"},
        {"name": "Soporte para accesibilidad", "icon": "♿"},
        {"name": "Sistema de roles y permisos", "icon": "🛡️"},
        {"name": "Soporte para múltiples dispositivos", "icon": "📱🖥️"},
        {"name": "Soporte para código QR", "icon": "🔳"},
        {"name": "Soporte para escaneo de documentos", "icon": "📠"},
        {"name": "Integración con correo electrónico", "icon": "✉️"},
        {"name": "Soporte para exportar a Excel/CSV", "icon": "📑"},
        {"name": "Soporte para gráficos interactivos", "icon": "📈"},
        {"name": "Soporte para mapas interactivos", "icon": "🗺️"},
        {"name": "Soporte para autenticación de dos factores", "icon": "🔐"},
        {"name": "Soporte para subida de imágenes", "icon": "🖼️"},
        {"name": "Soporte para audio y video", "icon": "🎥"},
        {"name": "Soporte para notificaciones por SMS", "icon": "📩"},
        {"name": "Soporte para backup automático", "icon": "🗄️"},
        {"name": "Soporte para importación de datos", "icon": "⬆️"},
        {"name": "Soporte para exportación de datos", "icon": "⬇️"},
        {"name": "Soporte para firma electrónica", "icon": "✍️"},
        {"name": "Soporte para pagos recurrentes", "icon": "🔁"},
        {"name": "Soporte para integración con IoT", "icon": "📡"},
        {"name": "Soporte para realidad aumentada", "icon": "🕶️"},
        {"name": "Soporte para inteligencia artificial", "icon": "🤖"},
        {"name": "Soporte para recomendaciones personalizadas", "icon": "✨"},
        {"name": "Soporte para gamificación", "icon": "🏆"},
        {"name": "Soporte para chatbots", "icon": "🤖"},
        {"name": "Soporte para análisis de sentimiento", "icon": "😊"},
        {"name": "Soporte para OCR (Reconocimiento óptico de caracteres)", "icon": "🔤"},
        {"name": "Soporte para control por voz", "icon": "🎙️"},
        {"name": "Soporte para widgets personalizables", "icon": "🧱"},
        {"name": "Soporte para integración con calendarios externos", "icon": "📆"},
        {"name": "Soporte para gestión de tareas", "icon": "✅"},
        {"name": "Soporte para notificaciones programadas", "icon": "⏰"},
        {"name": "Soporte para integración con servicios en la nube", "icon": "☁️"},
        {"name": "Soporte para dashboards personalizados", "icon": "📊"},
        {"name": "Soporte para logs de actividad", "icon": "📋"},
        {"name": "Soporte para multi-tenant", "icon": "🏢"},
        {"name": "Soporte para sandbox de pruebas", "icon": "🧪"},
        {"name": "Soporte para monitorización en tiempo real", "icon": "📡"},
        {"name": "Soporte para API GraphQL", "icon": "🔗"},
        {"name": "Soporte para integración con blockchain", "icon": "⛓️"},
        {"name": "Soporte para exportar a imagen", "icon": "🖼️"},
        {"name": "Soporte para integración con CRM", "icon": "📇"},
        {"name": "Soporte para integración con ERP", "icon": "💼"},
        {"name": "Soporte para integración con sistemas legacy", "icon": "🗃️"},
        {"name": "Soporte para pruebas automatizadas", "icon": "🧪"},
        {"name": "Soporte para control de versiones", "icon": "🔀"},
        {"name": "Soporte para otro", "icon": "➕"},
        {"name": "Otro", "icon": "➕"}
    ]

    print("\n🔧 Selecciona las características principales de tu app:")
    selected_features = ask(
        "Elige de la lista (puedes seleccionar varios):",
        options=predefined_features,
        multi_select=True,
        icon="🧩"
    )
    data['features'] = selected_features if selected_features else []

    # Permitir agregar características personalizadas
    print("➕ Si quieres agregar características propias, escríbelas una por una (escribe 'fin' para terminar):")
    while True:
        feat = input("➕ Característica personalizada: ").strip()
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
    prompt_filename = f"{data['project_name']}-prompt.md"
    filepath = os.path.join(project_dir, prompt_filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# Prompt para GitHub Copilot: {data['project_name']}\n\n")
        f.write(f"## Descripción del Proyecto\n{data['description']}\n\n")
        f.write(f"**Tipo de app:** {data.get('app_type','')}\n")
        f.write(f"**Público objetivo:** {data.get('target_audience','')}\n")
        f.write(f"**Plataforma:** {data.get('platform','')}\n")
        f.write(f"**IDE sugerida:** {data['ide']}\n")
        f.write(f"**Lenguaje principal:** {data['language']}\n")
        if data['gui'] == "Sí":
            f.write(f"**Interfaz gráfica:** Sí, usando {data['gui_toolkit']}\n")
        else:
            f.write(f"**Interfaz gráfica:** No\n")
        f.write(f"**Base de datos:** {data.get('database','')}\n")
        f.write(f"**Autenticación:** {data.get('authentication','')}\n")
        f.write(f"**Despliegue:** {data.get('deployment','')}\n")

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
