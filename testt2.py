import nltk

nltk.download('punkt')  # Download sentence tokenizer if not already available

class Complaint:
    def __init__(self, description):
        self.description = description.lower()  # Case-insensitive matching
        self.tokens = nltk.word_tokenize(self.description)  # Tokenize the description

    def get_keywords(self):
        keywords_eca = [
            "academic", "teaching", "faculty", "grades", "course", "professor",
            "instructor", "lecture", "assignment", "exam"
        ]
        keywords_canteen = [
            "food", "service", "hygiene", "cafeteria", "meal", "drink", "menu",
            "cleanliness", "staff", "utensils"
        ]
        keywords_facilities = [
            "building", "classroom", "lab", "equipment", "maintenance", "repair",
            "furniture", "internet", "electricity", "washroom"
        ]
        keywords_library = ["book", "resource", "hours", "staff", "availability", "noise"]
        keywords_registration = ["application", "process", "account", "enrollment", "documents"]

        extracted_keywords = []
        for token in self.tokens:
            if token in keywords_eca:
                extracted_keywords.append("ECA")
            elif token in keywords_canteen:
                extracted_keywords.append("Canteen")
            elif token in keywords_facilities:
                extracted_keywords.append("Facilities")
            elif token in keywords_library:
                extracted_keywords.append("Library")
            elif token in keywords_registration:
                extracted_keywords.append("Registration")
        return extracted_keywords

    def get_department(self):
        keywords = self.get_keywords()  # Call get_keywords within get_department
        # Prioritize more specific categories with any match
        if any(keyword in keywords for keyword in keywords_eca):
            return "ECA"
        elif any(keyword in keywords for keyword in keywords_canteen):
            return "Canteen"

        # ... rest of the code in get_department remains the same

def main():
    # Sample complaints (you can adjust these)
    complaints = [
        Complaint("The professor didn't explain the concept clearly."),
        # ... other complaints
    ]

    for complaint in complaints:
        department = complaint.get_department()
        print(f"Complaint: {complaint.description}\nDepartment: {department}\n")

if __name__ == "__main__":
    main()
