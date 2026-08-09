from django.http import JsonResponse

from ai_engine.agents.writer import WriterAgent


def run_agent(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)

    agent = WriterAgent()
    result = agent.execute("ZZEN AI OS task")

    return JsonResponse({
        "status": "success",
        "result": result,
    })
