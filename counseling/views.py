from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import StudentInput
from .rules import career_suggestion


def counseling_form(request):
    suggestion = None
    student = None

    if request.method == "POST":
        name = request.POST.get("name")
        grades = int(request.POST.get("grades"))
        interest = request.POST.get("interest")
        subject = request.POST.get("subject", "")
        hobbies = request.POST.get("hobbies", "")
        traits = request.POST.get("traits", "")

        suggestion = career_suggestion(grades, interest)

        student = StudentInput.objects.create(
            name=name,
            grades=grades,
            interest=interest,
            subject=subject,
            hobbies=hobbies,
            traits=traits,
            suggestion=suggestion,
        )

    context = {
        "suggestion": suggestion,
        "student": student,
    }
    return render(request, "counseling/form_bootstrap.html", context)


def dashboard(request):
    trends = (
        StudentInput.objects.values("suggestion")
        .annotate(count=Count("suggestion"))
        .order_by("-count")
    )
    students = StudentInput.objects.order_by("-id")
    return render(
        request,
        "counseling/dashboard_bootstrap.html",
        {"trends": trends, "students": students},
    )


def generate_pdf(request, student_id):
    try:
        from reportlab.pdfgen import canvas
    except ImportError:
        return HttpResponse(
            "ReportLab is not installed. Please install it with 'pip install reportlab'.",
            status=500,
        )

    student = get_object_or_404(StudentInput, id=student_id)
    response = HttpResponse(content_type="application/pdf")
    response[
        "Content-Disposition"
    ] = f'attachment; filename="{student.name}_career_report.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica", 14)
    y = 800

    lines = [
        f"Career Report for {student.name}",
        f"Grades: {student.grades}",
        f"Interest: {student.interest}",
        f"Favorite Subject: {student.subject}",
        f"Hobbies: {student.hobbies}",
        f"Personality Traits: {student.traits}",
        f"Suggested Career Path: {student.suggestion}",
    ]

    for line in lines:
        p.drawString(80, y, line)
        y -= 24

    p.showPage()
    p.save()
    return response

