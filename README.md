# Bridge Arcson — Sitio institucional (Django)

Sitio web institucional para **Bridge Arcson**, hecho con Django, con el
diseño basado en el manual de identidad de la empresa (paleta de colores,
tipografías Montserrat / Open Sans y todo el contenido del producto
ArcBridge One IoT).

## Estructura

```
bridgearcson/
├── manage.py
├── requirements.txt
├── bridgearcson/          # configuración del proyecto (settings, urls)
└── core/                  # app con las páginas del sitio
    ├── content.py         # todo el texto institucional (fácil de editar)
    ├── views.py           # una vista por página
    ├── urls.py
    ├── templates/core/    # inicio, producto, empresa, contacto
    └── static/core/       # css, js e íconos
```

## Páginas incluidas

- **Inicio** (`/`): hero, visión, valores de marca, planes y llamado a la acción.
- **Producto** (`/producto/`): ArcBridge One IoT, componentes, funciones,
  beneficios y planes.
- **Empresa** (`/empresa/`): problema que resuelven, necesidad del mercado,
  propuesta de valor y público objetivo.
- **Contacto** (`/contacto/`): formulario de consulta (guarda un mensaje de
  confirmación; para enviar emails reales hay que conectar un backend de
  envío, ver más abajo) y datos de contacto / redes.

## Cómo correrlo

1. Crear un entorno virtual e instalar dependencias:

   ```bash
   python -m venv venv
   source venv/bin/activate   # en Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Aplicar migraciones (solo crea la base de datos de Django, el sitio no
   usa modelos propios todavía):

   ```bash
   python manage.py migrate
   ```

3. Levantar el servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```

4. Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/) en el navegador.

## Cómo editar el contenido

Todo el texto (visión, problema, planes, funciones, beneficios, redes
sociales, etc.) vive en **`core/content.py`**. No hace falta tocar las
plantillas para cambiar precios, agregar un plan nuevo o actualizar un
párrafo: alcanza con editar ese archivo.

## Cómo conectar el formulario de contacto a un envío real

En `core/views.py`, la vista `contacto` ya valida el formulario. Para que
efectivamente envíe un email, agregá algo así antes del `messages.success`:

```python
from django.core.mail import send_mail

send_mail(
    subject=f"Nueva consulta de {nombre}",
    message=mensaje,
    from_email=None,
    recipient_list=["bridge.arcson.016@gmail.com"],
)
```

y configurá `EMAIL_BACKEND` / credenciales SMTP en `settings.py`.

## Personalización visual

La paleta y tipografías están centralizadas como variables CSS al inicio
de `core/static/core/css/style.css`:

```css
--navy-950: #081527;  /* fondo más oscuro */
--navy-900: #0f2854;  /* color principal de marca */
--blue-700: #1c4d8d;
--blue-400: #4988c4;
--blue-100: #bde8f5;
```

El logo (isotipo puente + circuito) está armado en SVG directamente en
`core/templates/core/partials/_logo.html`, así que se ve nítido en
cualquier resolución. Si más adelante tenés el archivo de logo original en
PNG/SVG, podés reemplazar ese partial por una etiqueta `<img>` apuntando a
`core/static/core/img/logo.svg`.
