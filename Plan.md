Build a basic expert system for educational
purposes, such as a career counseling system that
suggests potential career paths based on student
inputs (grades, interests, etc.). Use simple if-then
rules to simulate expert advice.
Here’s a simple rule-based expert system in Python that simulates career counseling advice. It uses if–then rules to suggest career paths based on student grades and interests.

python
# Basic Expert System for Career Counseling

def career_counseling(grades, interests):
    # Rule-based suggestions
    if grades >= 85 and "science" in interests.lower():
        return "You could pursue a career in Engineering, Medicine, or Research."
    
    elif grades >= 80 and "math" in interests.lower():
        return "You might consider careers in Data Science, Finance, or Actuarial Science."
    
    elif grades >= 75 and "arts" in interests.lower():
        return "You could explore careers in Design, Fine Arts, or Media."
    
    elif grades >= 70 and "technology" in interests.lower():
        return "You might enjoy careers in Software Development, IT, or Cybersecurity."
    
    elif grades >= 65 and "business" in interests.lower():
        return "You could pursue careers in Management, Marketing, or Entrepreneurship."
    
    elif grades >= 60 and "social" in interests.lower():
        return "You might consider careers in Education, Social Work, or Psychology."
    
    else:
        return "You may want to explore vocational training, skill-based careers, or entrepreneurship."

# Example usage
print(career_counseling(88, "Science and Technology"))
print(career_counseling(72, "Arts"))
print(career_counseling(67, "Business"))
🔑 How it works
Inputs: Student’s average grade and their interest area (e.g., science, math, arts, business).

Rules: Simple if–elif conditions check grade thresholds and match interests.

Output: Suggested career paths tailored to the student.

Example Output
Code
You could pursue a career in Engineering, Medicine, or Research.
You could explore careers in Design, Fine Arts, or Media.
You could pursue careers in Management, Marketing, or Entrepreneurship.
This is a basic prototype. In practice, you could expand it by:

Adding more detailed rules (e.g., specific subjects like biology vs. physics).

Using a knowledge base stored in JSON or a database.

Allowing multiple interests and combining suggestions.

Building a simple UI for students to input their data.

Would you like me to expand this into a more interactive system (like a questionnaire that asks students step by step), or keep it as a simple rule-based function?

yes
Perfect! Let’s expand the basic career counseling expert system into a more interactive questionnaire-style program. This way, instead of just passing grades and interests directly, the system will ask the student step by step and then give advice based on simple rules.

Here’s a Python prototype:

python
# Interactive Career Counseling Expert System

def career_counseling():
    print("Welcome to the Career Counseling Expert System!")
    print("Answer a few questions to get career suggestions.\n")

    # Step 1: Ask for grades
    grades = int(input("Enter your average grade percentage (0-100): "))

    # Step 2: Ask for interests
    print("\nChoose your main interest area:")
    print("1. Science")
    print("2. Math")
    print("3. Arts")
    print("4. Technology")
    print("5. Business")
    print("6. Social Studies")
    choice = int(input("Enter the number of your choice: "))

    # Map choice to interest string
    interests = {
        1: "science",
        2: "math",
        3: "arts",
        4: "technology",
        5: "business",
        6: "social"
    }
    interest = interests.get(choice, "general")

    # Rule-based suggestions
    if grades >= 85 and interest == "science":
        suggestion = "Engineering, Medicine, or Scientific Research."
    elif grades >= 80 and interest == "math":
        suggestion = "Data Science, Finance, or Actuarial Science."
    elif grades >= 75 and interest == "arts":
        suggestion = "Design, Fine Arts, or Media."
    elif grades >= 70 and interest == "technology":
        suggestion = "Software Development, IT, or Cybersecurity."
    elif grades >= 65 and interest == "business":
        suggestion = "Management, Marketing, or Entrepreneurship."
    elif grades >= 60 and interest == "social":
        suggestion = "Education, Social Work, or Psychology."
    else:
        suggestion = "Vocational training, skill-based careers, or entrepreneurship."

    print(f"\nBased on your inputs, you could explore careers in: {suggestion}")

# Run the system
career_counseling()
🔑 Features
Interactive Q&A: Students input grades and select interests step by step.

Rule-based logic: Uses simple if–then rules to simulate expert advice.

Clear suggestions: Provides tailored career paths based on responses.

Example Run
Code
Welcome to the Career Counseling Expert System!
Answer a few questions to get career suggestions.

Enter your average grade percentage (0-100): 82

Choose your main interest area:
1. Science
2. Math
3. Arts
4. Technology
5. Business
6. Social Studies
Enter the number of your choice: 2

Based on your inputs, you could explore careers in: Data Science, Finance, or Actuarial Science.
👉 This is a basic prototype. You could expand it by:

Asking more detailed questions (favorite subjects, hobbies, personality traits).

Storing rules in a knowledge base (JSON or database).

Adding multiple interest selections and combining advice.

Building a simple GUI or web app for students.

Would you like me to extend this into a GUI version (like a Tkinter app with buttons and dropdowns), so it feels more like a real counseling tool?

yes please
Great choice! Let’s turn the career counseling expert system into a GUI application using Tkinter. This way, students can interact with buttons, dropdowns, and text fields instead of typing everything in the console.

Here’s a complete Python example:

python
import tkinter as tk
from tkinter import ttk, messagebox

def suggest_career():
    try:
        grades = int(grade_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid grade percentage (0-100).")
        return
    
    interest = interest_var.get()

    # Rule-based suggestions
    if grades >= 85 and interest == "Science":
        suggestion = "Engineering, Medicine, or Scientific Research."
    elif grades >= 80 and interest == "Math":
        suggestion = "Data Science, Finance, or Actuarial Science."
    elif grades >= 75 and interest == "Arts":
        suggestion = "Design, Fine Arts, or Media."
    elif grades >= 70 and interest == "Technology":
        suggestion = "Software Development, IT, or Cybersecurity."
    elif grades >= 65 and interest == "Business":
        suggestion = "Management, Marketing, or Entrepreneurship."
    elif grades >= 60 and interest == "Social Studies":
        suggestion = "Education, Social Work, or Psychology."
    else:
        suggestion = "Vocational training, skill-based careers, or entrepreneurship."

    messagebox.showinfo("Career Suggestion", f"Based on your inputs, you could explore careers in: {suggestion}")

# GUI setup
root = tk.Tk()
root.title("Career Counseling Expert System")
root.geometry("400x250")

# Labels and inputs
tk.Label(root, text="Enter your average grade percentage (0-100):").pack(pady=5)
grade_entry = tk.Entry(root)
grade_entry.pack(pady=5)

tk.Label(root, text="Select your main interest area:").pack(pady=5)
interest_var = tk.StringVar()
interest_dropdown = ttk.Combobox(root, textvariable=interest_var, state="readonly")
interest_dropdown['values'] = ("Science", "Math", "Arts", "Technology", "Business", "Social Studies")
interest_dropdown.pack(pady=5)

# Button
tk.Button(root, text="Get Career Suggestion", command=suggest_career).pack(pady=20)

root.mainloop()
🔑 Features
Text field for grades.

Dropdown menu for interests.

Button to generate suggestions.

Pop-up message box with tailored career advice.

Example Interaction
Student enters 82 in the grade field.

Selects Math from the dropdown.

Clicks Get Career Suggestion.

A pop-up appears:
“Based on your inputs, you could explore careers in: Data Science, Finance, or Actuarial Science.”

This is a basic GUI prototype. You could expand it by:

Adding multiple interest selections.

Including personality questions (introvert/extrovert, creative/analytical).

Saving results to a file or database.

Styling the interface with colors, fonts, and layouts.

Would you like me to upgrade this into a more polished version with multiple questions (like a mini quiz) and a final career report at the end, instead of just one suggestion pop-up?

i want web app like djnago to handle this
Excellent idea! Let’s build this career counseling expert system as a Django web app. I’ll walk you through a simple structure:

🏗 Project Setup
Create Django project

bash
django-admin startproject career_counseling
cd career_counseling
python manage.py startapp counseling
Add app to settings

python
# career_counseling/settings.py
INSTALLED_APPS = [
    ...,
    'counseling',
]
📂 App Structure
Code
career_counseling/
│
├── counseling/
│   ├── templates/
│   │   └── counseling/
│   │       └── form.html
│   ├── views.py
│   ├── urls.py
│   └── rules.py
⚙️ Rule Engine (Expert System)
python
# counseling/rules.py

def career_suggestion(grades, interest):
    interest = interest.lower()
    if grades >= 85 and "science" in interest:
        return "Engineering, Medicine, or Scientific Research"
    elif grades >= 80 and "math" in interest:
        return "Data Science, Finance, or Actuarial Science"
    elif grades >= 75 and "arts" in interest:
        return "Design, Fine Arts, or Media"
    elif grades >= 70 and "technology" in interest:
        return "Software Development, IT, or Cybersecurity"
    elif grades >= 65 and "business" in interest:
        return "Management, Marketing, or Entrepreneurship"
    elif grades >= 60 and "social" in interest:
        return "Education, Social Work, or Psychology"
    else:
        return "Vocational training, skill-based careers, or entrepreneurship"
🎛 Views
python
# counseling/views.py
from django.shortcuts import render
from .rules import career_suggestion

def counseling_form(request):
    suggestion = None
    if request.method == "POST":
        grades = int(request.POST.get("grades"))
        interest = request.POST.get("interest")
        suggestion = career_suggestion(grades, interest)
    return render(request, "counseling/form.html", {"suggestion": suggestion})
🌐 URLs
python
# counseling/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.counseling_form, name="counseling_form"),
]
And include in project urls.py:

python
# career_counseling/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('counseling.urls')),
]
🎨 Template
html
<!-- counseling/templates/counseling/form.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Career Counseling Expert System</title>
</head>
<body>
    <h2>Career Counseling Expert System</h2>
    <form method="post">
        {% csrf_token %}
        <label>Enter your average grade percentage:</label><br>
        <input type="number" name="grades" required><br><br>

        <label>Select your interest area:</label><br>
        <select name="interest" required>
            <option>Science</option>
            <option>Math</option>
            <option>Arts</option>
            <option>Technology</option>
            <option>Business</option>
            <option>Social Studies</option>
        </select><br><br>

        <button type="submit">Get Career Suggestion</button>
    </form>

    {% if suggestion %}
        <h3>Suggested Career Path:</h3>
        <p>{{ suggestion }}</p>
    {% endif %}
</body>
</html>
🚀 Run the App
bash
python manage.py runserver
Open in browser:
👉 http://127.0.0.1:8000/

✅ Result
Students enter their grades and select an interest area. The system applies if–then rules and displays a tailored career suggestion.

Would you like me to extend this Django app with a database model (so you can store student inputs and generate reports later), or keep it as a simple rule-based form?

ok
Perfect, Samir! Let’s take the Django prototype we built and extend it into a full web app that can handle student inputs, store them in a database, and generate career counseling reports. This way, it’s not just a form—it becomes a proper system.

🏗 Step 1: Create a Model for Student Inputs
We’ll store grades, interests, and suggestions in the database.

python
# counseling/models.py
from django.db import models

class StudentInput(models.Model):
    name = models.CharField(max_length=100)
    grades = models.IntegerField()
    interest = models.CharField(max_length=50)
    suggestion = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.suggestion}"
Run migrations:

bash
python manage.py makemigrations
python manage.py migrate
⚙️ Step 2: Update Views to Save Data
We’ll save each counseling session to the database.

python
# counseling/views.py
from django.shortcuts import render
from .rules import career_suggestion
from .models import StudentInput

def counseling_form(request):
    suggestion = None
    if request.method == "POST":
        name = request.POST.get("name")
        grades = int(request.POST.get("grades"))
        interest = request.POST.get("interest")
        suggestion = career_suggestion(grades, interest)

        # Save to database
        StudentInput.objects.create(
            name=name,
            grades=grades,
            interest=interest,
            suggestion=suggestion
        )

    return render(request, "counseling/form.html", {"suggestion": suggestion})
🎨 Step 3: Update Template
Add a field for student name and display results nicely.

html
<!-- counseling/templates/counseling/form.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Career Counseling Expert System</title>
</head>
<body>
    <h2>Career Counseling Expert System</h2>
    <form method="post">
        {% csrf_token %}
        <label>Your Name:</label><br>
        <input type="text" name="name" required><br><br>

        <label>Enter your average grade percentage:</label><br>
        <input type="number" name="grades" required><br><br>

        <label>Select your interest area:</label><br>
        <select name="interest" required>
            <option>Science</option>
            <option>Math</option>
            <option>Arts</option>
            <option>Technology</option>
            <option>Business</option>
            <option>Social Studies</option>
        </select><br><br>

        <button type="submit">Get Career Suggestion</button>
    </form>

    {% if suggestion %}
        <h3>Suggested Career Path:</h3>
        <p>{{ suggestion }}</p>
    {% endif %}
</body>
</html>
📊 Step 4: Admin Panel
Enable admin access to review student counseling records.

python
# counseling/admin.py
from django.contrib import admin
from .models import StudentInput

admin.site.register(StudentInput)
Now you can log in to /admin and see all counseling sessions.

🚀 Step 5: Run the App
bash
python manage.py runserver
Visit: http://127.0.0.1:8000/

✅ Result
Students enter their name, grades, and interest.

The system applies if–then rules and suggests careers.

Each session is saved in the database for later review.

Admins can view all counseling records.

👉 Next step could be making it more dynamic:

Add multiple questions (favorite subjects, hobbies, personality traits).

Generate a career report PDF for each student.

Build a dashboard to analyze trends (e.g., most popular career suggestions).

Would you like me to extend this into a dashboard view (where teachers can see all students’ inputs and suggestions in one place), or keep it focused on individual counseling sessions?

Add multiple questions (favorite subjects, hobbies, personality traits).

Generate a career report PDF for each student.

Build a dashboard to analyze trends (e.g., most popular career suggestions).
Alright, let’s take your Django career counseling app to the next level by adding multiple questions, generating a PDF career report, and building a dashboard for trend analysis. Here’s how you can structure it:

📝 Step 1: Expand the Form (Multiple Questions)
Update your template to include favorite subjects, hobbies, and personality traits.

html
<!-- counseling/templates/counseling/form.html -->
<form method="post">
    {% csrf_token %}
    <label>Your Name:</label><br>
    <input type="text" name="name" required><br><br>

    <label>Average Grade Percentage:</label><br>
    <input type="number" name="grades" required><br><br>

    <label>Interest Area:</label><br>
    <select name="interest" required>
        <option>Science</option>
        <option>Math</option>
        <option>Arts</option>
        <option>Technology</option>
        <option>Business</option>
        <option>Social Studies</option>
    </select><br><br>

    <label>Favorite Subject:</label><br>
    <input type="text" name="subject"><br><br>

    <label>Hobbies:</label><br>
    <input type="text" name="hobbies"><br><br>

    <label>Personality Traits:</label><br>
    <input type="text" name="traits"><br><br>

    <button type="submit">Get Career Suggestion</button>
</form>
⚙️ Step 2: Update Model
Store the extra fields.

python
# counseling/models.py
class StudentInput(models.Model):
    name = models.CharField(max_length=100)
    grades = models.IntegerField()
    interest = models.CharField(max_length=50)
    subject = models.CharField(max_length=100, blank=True)
    hobbies = models.TextField(blank=True)
    traits = models.TextField(blank=True)
    suggestion = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.suggestion}"
📄 Step 3: Generate PDF Career Report
Use ReportLab or xhtml2pdf to generate a PDF.

Install:

bash
pip install reportlab
Add a PDF view:

python
# counseling/views.py
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import StudentInput

def generate_pdf(request, student_id):
    student = StudentInput.objects.get(id=student_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.name}_career_report.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica", 12)
    p.drawString(100, 800, f"Career Report for {student.name}")
    p.drawString(100, 770, f"Grades: {student.grades}")
    p.drawString(100, 750, f"Interest: {student.interest}")
    p.drawString(100, 730, f"Favorite Subject: {student.subject}")
    p.drawString(100, 710, f"Hobbies: {student.hobbies}")
    p.drawString(100, 690, f"Personality Traits: {student.traits}")
    p.drawString(100, 670, f"Suggested Career Path: {student.suggestion}")
    p.showPage()
    p.save()
    return response
Add a link in the template:

html
{% if suggestion %}
    <h3>Suggested Career Path:</h3>
    <p>{{ suggestion }}</p>
    <a href="{% url 'generate_pdf' student.id %}">Download Career Report (PDF)</a>
{% endif %}
📊 Step 4: Dashboard for Trends
Create a dashboard view to analyze most popular career suggestions.

python
# counseling/views.py
from django.db.models import Count

def dashboard(request):
    trends = StudentInput.objects.values('suggestion').annotate(count=Count('suggestion')).order_by('-count')
    return render(request, "counseling/dashboard.html", {"trends": trends})
Template:

html
<!-- counseling/templates/counseling/dashboard.html -->
<h2>Career Counseling Dashboard</h2>
<table border="1">
    <tr>
        <th>Career Path</th>
        <th>Number of Students</th>
    </tr>
    {% for trend in trends %}
    <tr>
        <td>{{ trend.suggestion }}</td>
        <td>{{ trend.count }}</td>
    </tr>
    {% endfor %}
</table>
🚀 Final Flow
Student fills out grades, interest, subject, hobbies, traits.

System applies rules → Suggests career path.

Student can download a personalized PDF report.

Teachers/admins can view a dashboard of career trends.