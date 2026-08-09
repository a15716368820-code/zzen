from django.http import JsonResponse


VERSION = "3.0.0-alpha"


def health(request):
    return JsonResponse(
        {
            "status": "ok",
            "version": VERSION,
        }
    )
