def career_suggestion(grades, interest):
    interest = (interest or "").lower()
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

