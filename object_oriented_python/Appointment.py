"""
    Author : Siphosethu Shumani
    Date : 28 Jan 2022
"""

class Appointment:
    def __init__(self, patient_id, doctor_id, time_stamp, memo):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.time_stamp = time_stamp
        self.memo = memo

    def __str__(self):
        return "Patient's ID: "+str(self.patient_id) + "\nDoctor's ID: " + str(self.doctor_id) + "\nFull timestamp: " + str(self.time_stamp) + "\nMemo: " + self.memo
        
