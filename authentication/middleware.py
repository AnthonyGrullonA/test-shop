from django.http import HttpResponseForbidden
from .models import CustomUser as User

class ControlAccesoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Procesa directamente la respuesta para la solicitud entrante
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            try:
                usuario = User.objects.get(id=request.user.id)  # Obtiene el usuario autenticado
                if not usuario.cliente:
                    return HttpResponseForbidden("Este usuario no tiene un cliente asociado.")

                # Establece el cliente en el request para que pueda ser accesado en las vistas
                request.cliente_usuario = usuario.cliente

            except User.DoesNotExist:
                return HttpResponseForbidden("Usuario no encontrado.")
        return None
