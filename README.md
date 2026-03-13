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


⸻

🧠 Conceptos de Django utilizados

Este proyecto aplica varios conceptos fundamentales de Django:
	•	Apps para modularizar la aplicación (web)
	•	Views para manejar las solicitudes HTTP
	•	Templates para renderizar HTML
	•	Static files para CSS e imágenes
	•	URL routing para la navegación del sitio

⸻

🎯 Objetivo del proyecto

El objetivo principal de este proyecto es:
	•	Comprender la estructura de un proyecto Django
	•	Implementar un sitio web con múltiples páginas
	•	Organizar contenido visual mediante plantillas y rutas
	•	Practicar el flujo petición → vista → template → respuesta

⸻

🛠 Tecnologías utilizadas
	•	Python
	•	Django
	•	HTML5
	•	CSS3
	•	Imágenes WebP

⸻

📌 Posibles mejoras

Algunas mejoras futuras podrían incluir:
	•	Panel de administración para subir fotografías
	•	Base de datos para gestionar galerías
	•	Sistema de autenticación
	•	Formularios de contacto funcionales
	•	Optimización SEO
	•	Diseño responsive completo

⸻

👤 Autor

Proyecto desarrollado por Francisco Rojas como parte de su aprendizaje en desarrollo web con Django.

