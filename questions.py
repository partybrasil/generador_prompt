app_types = [
    "Web", "Escritorio", "Móvil", "API/Backend", "CLI", "Otro"
]
audiences = [
    "Usuarios finales", "Empresas", "Desarrolladores", "Educativo", "Otro"
]
platforms = [
    "Windows", "Linux", "macOS", "Android", "iOS", "Multiplataforma", "Otro"
]
ides = [
    "Visual Studio Code", "PyCharm", "Otro"
]
languages = [
    "Python", "JavaScript", "Java", "C#", "C++", "Go", "Rust", "TypeScript", "Kotlin", "Swift", "PHP", "Ruby",
    "Dart", "Scala", "C", "R", "MATLAB", "Perl", "Shell/Bash", "Otro"
]
gui_choices = ["Sí", "No"]
gui_toolkits = [
    "PySide6", "Tkinter", "Kivy", "Electron + JS", "PyQt5", "wxPython", "Dear PyGui", "FLTK", "PySimpleGUI",
    "GTK+ (PyGObject)", "CustomTkinter", "Remi", "PyForms", "PyGame", "Toga", "Enaml", "cefpython", "PyWebview",
    "KivyMD", "PyGTK", "PyObjC", "PyFLTK", "PySDL2", "PyOpenGL", "PyQt6", "PySide2", "PyForms-Web", "PySciter",
    "PyAutoGUI", "Otro"
]
databases = [
    "No", "SQLite", "PostgreSQL", "MySQL", "MongoDB", "Otro"
]
authentications = [
    "No", "Sí, local", "Sí, OAuth/Google/Facebook", "Otro"
]
deployments = [
    "No aplica", "Heroku", "Vercel", "AWS", "Servidor propio", "Google Cloud", "Otro"
]
structure_options = [
    "Simple (src/, tests/, docs/)", "Modular (src/app/, src/core/, src/utils/)", "MVC (Model, View, Controller)",
    "Hexagonal/Clean Architecture", "Monorepo (apps/, packages/, libs/)", "Microservicios (services/, shared/, gateway/)",
    "DDD (Domain Driven Design)", "Plugin-based (plugins/, core/, shared/)", "Feature-based (features/, shared/, utils/)",
    "Layered (presentation/, business/, data/)", "REST API (api/, models/, schemas/)", "CQRS/ES (commands/, queries/, events/)",
    "Package per module (cada módulo como paquete)", "Clean + Tests (src/, tests/unit/, tests/integration/)",
    "Data Science (notebooks/, data/, src/)", "Serverless (functions/, shared/, config/)",
    "Frontend/Backend separados (frontend/, backend/)", "Mobile (android/, ios/, shared/)", "Monoapp (todo en src/)", "Otro"
]
startup_options_list = [
    "Con pantalla de bienvenida (Welcome Screen)", "Con splash screen", "Inicio silencioso (sin ventanas)",
    "Iniciar en la bandeja del sistema (system tray)", "Con comprobación de actualizaciones", "Con login automático",
    "Cargar configuración previa", "Mostrar tutorial interactivo", "Recuperar sesión anterior",
    "Con animación de carga personalizada", "Con selección de perfil de usuario", "Con notificación de novedades",
    "Con comprobación de conexión a internet", "Con carga de datos en segundo plano", "Con selección de idioma",
    "Con autenticación biométrica", "Con comprobación de permisos", "Con mensaje motivacional",
    "Con integración con calendario", "Con restauración de copias de seguridad", "Otro"
]
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
