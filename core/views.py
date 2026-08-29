from django.contrib import messages
from django.shortcuts import redirect, render

from . import content


def home(request):
    context = {
        "empresa": content.EMPRESA,
        "vision": content.VISION,
        "valor_empresa": content.VALOR_EMPRESA,
        "valores_marca": content.VALORES_MARCA,
        "producto": content.PRODUCTO,
        "planes": content.PLANES,
    }
    return render(request, "core/home.html", context)


def producto(request):
    context = {
        "empresa": content.EMPRESA,
        "producto": content.PRODUCTO,
        "funciones": content.FUNCIONES,
        "beneficios": content.BENEFICIOS,
        "propuesta_valor": content.PROPUESTA_VALOR,
        "planes": content.PLANES,
    }
    return render(request, "core/producto.html", context)


def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        email = request.POST.get("email", "").strip()
        asunto = request.POST.get("asunto", "consulta").strip()
        mensaje = request.POST.get("mensaje", "").strip()

        etiquetas = {
            "consulta": "Consulta general",
            "soporte": "Soporte técnico",
            "ventas": "Ventas / presupuesto",
            "otros": "Otros",
        }
        etiqueta = etiquetas.get(asunto, "Consulta general")

        if nombre and email and mensaje:
            # Acá se integraría el envío real (email, CRM, etc.).
            # Por ahora confirmamos la recepción al usuario.
            messages.success(
                request,
                f"¡Gracias {nombre}! Recibimos tu {etiqueta.lower()}"
                " y te vamos a contactar a la brevedad.",
            )
            return redirect("core:contacto")
        messages.error(request, "Completá tu nombre, tu email y tu mensaje.")

    context = {"empresa": content.EMPRESA}
    return render(request, "core/contacto.html", context)
