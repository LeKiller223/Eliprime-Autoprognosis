from django.shortcuts import render, redirect
from .forms import EngineIssueForm
from .models import CarScanner


def home(request):
    return render(request, "ELIPRIME.html")


def diagnostic_form(request):
    if request.method == "POST":
        form = EngineIssueForm(request.POST)
        if form.is_valid():
            diagnostic_report = form.save(commit=False)
            symptoms = diagnostic_report.symptoms.lower()
            diagnostic_result, suggested_actions = diagnose(symptoms)

            diagnostic_report.diagnostic_result = diagnostic_result
            diagnostic_report.suggested_actions = suggested_actions
            # diagnostic_report.save()

            return render(
                request,
                "engine_success.html",
                {
                    "diagnostic_result": diagnostic_result,
                    "suggested_actions": suggested_actions,
                },
            )
    else:
        form = EngineIssueForm()
    return render(request, "engine.html", {"form": form})


def diagnose(symptoms):
    if "strange noise" in symptoms:
        diagnostic_result = "Possible issue: Engine noise detected"
        suggested_actions = (
            "Inspect engine components, check for loose parts or damaged components"
        )
    elif "warning light" in symptoms:
        diagnostic_result = "Possible issue: Warning light activated"
        suggested_actions = (
            "Perform diagnostic scan, check trouble codes, consult vehicle manual"
        )
    elif "overheating" in symptoms:
        diagnostic_result = "Possible issue: Overheating"
        suggested_actions = (
            "Check coolant levels regularly, inspect for leaks, replace worn components."
        )
    elif "Spark" or "sparking" in symptoms:
        diagnostic_result = "Possible issue: Engine misfiring"
        suggested_actions = (
            "Replace worn out spark plugs."
        )       

    else:
        diagnostic_result = "No specific issue detected"
        suggested_actions = "Monitor vehicle performance, schedule regular maintenance"

    return diagnostic_result, suggested_actions
