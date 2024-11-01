from flask import jsonify

class Patient:
    def __init__(self, id, name, gender, birth_date):
        self.resourceType = "Patient"
        self.id = id
        self.name = [{"use": "official", "text": name}]
        self.gender = gender
        self.birthDate = birth_date

    def to_dict(self):
        return vars(self)

    @staticmethod
    def from_dict(data):
        return Patient(data["id"], data["name"][0]["text"], data["gender"], data["birthDate"])
