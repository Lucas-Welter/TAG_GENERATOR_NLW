from src.views.http_types.http_response import HttpResponse
from.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        # enviar para um log
        # enviar para um e-mail de notificação
        return HttpResponse(
            status_code=error.status_code,
            body= {
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "erros": [{
                "title": "Server error",
                "detail": str(error)
            }]
        }
    )
