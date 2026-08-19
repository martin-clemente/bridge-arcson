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
        institucion = request.POST.get("institucion", "").strip()
        mensaje = request.POST.get("mensaje", "").strip()

        if nombre and mensaje:
            # Acá se integraría el envío real (email, CRM, etc.).
            # Por ahora confirmamos la recepción al usuario.
            messages.success(
                request,
                f"¡Gracias {nombre}! Recibimos tu consulta"
                f"{' de ' + institucion if institucion else ''} "
                "y te vamos a contactar a la brevedad.",
            )
            return redirect("core:contacto")
        messages.error(request, "Completá al menos tu nombre y tu consulta.")

    context = {"empresa": content.EMPRESA}
    return render(request, "core/contacto.html", context)
