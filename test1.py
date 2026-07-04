class Patient:
    def __init__(self, pid, name, age):
        if age <= 0:
            raise ValueError("Invalid age")
        self.pid = pid
        self.name = name
        self.age = age
class Doctor:
    def __init__(self, did, name):
        self.did = did
        self.name = name
patients = {}    
patient_ids = []   
try:
    p = Patient(101, "Rahul", 25)
    patients[p.pid] = {"Name": p.name, "Age": p.age}
    patient_ids.append(p.pid)
    file = open("patients.txt", "a")
    file.write(f"{p.pid}, {p.name}, {p.age}\n")
    file.close()
    print("Patient Added Successfully")
except ValueError as e:
    print("Error:", e)
print("Patient Records:", patients)
print("Patient IDs:", patient_ids)