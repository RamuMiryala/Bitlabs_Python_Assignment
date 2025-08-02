# hospital_patient_management.py

class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def to_dict(self):
        return {"Name": self.name, "Age": self.age, "Disease": self.disease}


def search_patients_by_disease(patients, disease):
    """
    Searches for patients with the given disease.

    Parameters:
    patients (list): List of patient dictionaries.
    disease (str): Disease to search for.

    Returns:
    list: List of names of patients with the given disease.
    """
    result = [patient["Name"] for patient in patients if patient["Disease"].lower() == disease.lower()]
    return result


def main():
    # Initial patient records using class (optional usage)
    patients = [
        Patient("Alice", 30, "Flu").to_dict(),
        Patient("Bob", 45, "Diabetes").to_dict(),
        Patient("Charlie", 35, "Flu").to_dict()
    ]

    search_disease = "Flu"
    matched_patients = search_patients_by_disease(patients, search_disease)

    print(f"Patients with {search_disease}: {matched_patients}")


if __name__ == "__main__":
    main()
