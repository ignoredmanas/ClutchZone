from django.shortcuts import render

from registrations.models import Registrations


def home(request):
    context = {}

    if request.method == "POST":
        team_name = request.POST.get("team_name", "").strip()
        game = request.POST.get("game", "")
        leader_name = request.POST.get("leader_name", "").strip()
        game_id = request.POST.get("game_id", "").strip()

        valid_games = ["valorant", "bgmi", "free-fire"]

        if not team_name or not leader_name or not game_id:
            context["error"] = "Please fill in every field."

        elif game not in valid_games:
            context["error"] = "Please choose a valid game."

        else:
            Registrations.objects.create(
                team_name=team_name,
                game=game,
                leader_name=leader_name,
                game_id=game_id,
            )
            context["success"] = "Your team registration was submitted successfully."

    return render(request, "core/home.html", context)