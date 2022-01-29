"""
    Author : Siphosethu Shumani
    Date : 28 Jan 2022
"""

from Person import Person

class Doctor(Person):
    def __init__(self, doctor_id, address, n='unknown',a=0):
        super().__init__(n, a)
        self.doctor_id = doctor_id
        self.address = address

    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print("Doctor's id:",self.doctor_id)
        print("address:",self.address)

    def __str__(self):
        return self.name + ', ' + str(self.age) + ", " + str(self.doctor_id) + ", " + self.address

