📷 Portafolio Fotográfico Web

Aplicación web desarrollada con Django para presentar un portafolio fotográfico organizado por categorías.
El proyecto muestra diferentes galerías de imágenes como paisajes, retratos, viajes y vida silvestre, utilizando plantillas HTML, archivos estáticos y rutas definidas en Django.

Este proyecto fue desarrollado como ejercicio práctico para comprender la estructura de aplicaciones web con Python y Django.

⸻

🚀 Características
	•	Sitio web de portafolio fotográfico
	•	Navegación entre diferentes categorías
	•	Plantillas reutilizables con base.html
	•	Uso de archivos estáticos (CSS, imágenes)
	•	Organización modular mediante una app de Django
	•	Galerías de imágenes en formato WebP

⸻

🖼 Categorías del portafolio

El sitio incluye las siguientes secciones:
	•	🌄 Paisajes
	•	🧑 Retratos
	•	✈️ Viajes
	•	🦅 Vida Silvestre
	•	📩 Contacto

Cada sección presenta una galería de fotografías almacenadas dentro de los archivos estáticos del proyecto.

⸻

🏗 Estructura del proyecto
portafolio_ABP/
│
├── manage.py
├── db.sqlite3
│
├── portafolio/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── web/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── admin.py
│   │
│   ├── templates/
│   │   └── web/
│   │       ├── base.html
│   │       ├── inicio.html
│   │       ├── paisajes.html
│   │       ├── retratos.html
│   │       ├── viajes.html
│   │       ├── vida_silvestre.html
│   │       └── contacto.html
│   │
│   └── static/
│       └── web/
│           ├── css/
│           │   └── estilo.css
│           └── img/
│               ├── paisajes/
│               ├── retratos/
│               ├── viajes/
│               └── vida_silvestre/
