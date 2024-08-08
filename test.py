class Complaint:
    def __init__(self, description):
        self.description = description.lower()  # Case-insensitive matching

    def get_department(self):
        keywords_eca = [
            "academic",
            "teaching",
            "faculty",
            "grades",
            "course",
            "damage",
            "professor",
            "instructor",
            "lecture",
            "assignment",
            "exam",
        ]
        keywords_canteen = [
            "food",
            "service",
            "hygiene",
            "cafeteria",
            "meal",
            "drink",
            "menu",
            "cleanliness",
            "staff",
            "utensils",
        ]
        keywords_facilities = [
            "building",
            "classroom",
            "lab",
            "equipment",
            "maintenance",
            "repair",
            "furniture",
            "internet",
            "electricity",
            "washroom",
        ]
        keywords_library = [
            "book",
            "resource",
            "hours",
            "staff",
            "availability",
            "noise",
        ]
        keywords_registration = [
            "application",
            "process",
            "account",
            "enrollment",
            "documents",
        ]

        # Prioritize more specific categories (ECA, Canteen)
        if any(keyword in self.description for keyword in keywords_eca):
            return "ECA"
        elif any(keyword in self.description for keyword in keywords_canteen):
            return "Canteen"

        # Check for other categories with lower priority
        elif any(keyword in self.description for keyword in keywords_facilities):
            return "Facilities"
        elif any(keyword in self.description for keyword in keywords_library):
            return "Library"
        elif any(keyword in self.description for keyword in keywords_registration):
            return "Registration"
        else:
            return "Unassigned"


def main():
    # Sample complaints (you can adjust these)
    complaints = [
        Complaint("The professor didn't explain the concept clearly."),
        Complaint("The cafeteria food is cold and tasteless."),
        Complaint("There's a leak in the ECA building."),
        Complaint("The canteen staff is rude and unhelpful."),
        Complaint("My grades are not reflecting my hard work."),
        Complaint("There's a power outage in the computer labs."),
        Complaint("I found a hair in my soup."),
        Complaint("The library hours are inconvenient."),
        Complaint("The new registration process is confusing."),
        Complaint("The ECA equipment needs maintenance."),
        Complaint("The cricket bat is damage."),
        Complaint("The exam papers were low quality."),
    ]

    for complaint in complaints:
        department = complaint.get_department()
        print(f"Complaint: {complaint.description}\nDepartment: {department}\n")


if __name__ == "__main__":
    main()
