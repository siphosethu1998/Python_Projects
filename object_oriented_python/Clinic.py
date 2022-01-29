"""
    This a menu based program for the Patients, doctors and appointments class
    Author : Siphosethu Shumani
    Date : 28 Jan 2022
"""

from  Appointment import Appointment
from  Doctor import Doctor
from  Patient import Patient

import pickle

import datetime

def print_menu():
    print("***Welcome to the Clinic Program***")
    print()
    print("1. To to add a patient, doctor or appointment")
    print("2. To display all the patients, doctors or appointments")
    print("3. To search for and display all the appointments for a particular patient or doctor")
    print("4. To quit")
    
def print_menu1():
    print("1. To add a Patient")
    print("2. To add a Doctor")
    print("3. To add an Appointment")
    
def print_menu2():
    print("1. To display all the Patients")
    print("2. To display all the Doctors")
    print("3. To display all the Appointments")

def print_menu3():
    print("1. To search for a patient and display their appointments")
    print("2. To search for a doctor and display their appointments" )

def main():
    patients = []
    doctors = []
    appointments = []
    
    outFile = open('patients.txt','wb')  # writing to the patients file
    outFile1 = open('doctors.txt','wb') # writing to the doctors file
    outFile2 = open('appointments.txt','wb') # writing to the appointments file

    while True:
        print_menu()
        command = int(input(">> "))
        if command == 1:
            print_menu1()
            command = int(input(">> "))
            if command == 1:
                patient_id = int(input("Enter the patient's id: "))
                address = input("Enter the patient's address: ")
                num_visits = int(input("Enter the patient's number of visits: "))
                name = input("Enter the patient's name: ")
                age = int(input("Enter the patient's age: "))
                patients.append(Patient(patient_id, address, num_visits, name, age))
            elif command == 2:
                doctor_id = int(input("Enter the doctor's id: "))
                address = input("Enter the doctor's address: ")
                name = input("Enter the doctor's name: ")
                age = int(input("Enter the doctor's age: "))
                doctors.append(Doctor(doctor_id, address, name, age))
            else: # for the appointments
                patient_id = int(input("Enter the patient's id: "))
                doctor_id = int(input("Enter the doctor's id: "))
                time_stamp = input("Enter the appointment's time stamp: ")
                memo = input("Enter the memo for the appointment: ")
                appointments.append(Appointment(patient_id, doctor_id, time_stamp, memo))
            print()

        elif command == 2:
            print_menu2()
            command = int(input(">> "))
            if command == 1:
                for patient in patients:
                    patient.display()
            elif command == 2:
                for doctor in doctors:
                    doctor.display()
            else:
                for appointment in appointments:
                    print(appointment)
            print()

        elif command == 3:
            print_menu3()
            command = int(input(">> "))
            if command == 1:
                pat_id = int(input("Enter the patient's id: "))
                for appointment in appointments:
                    if appointment.patient_id == pat_id:
                        print(appointment)
            else: # for doctor appointments
                doc_id = int(input("Enter the doctor's id: "))
                for appointment in appointments:
                    if appointment.doctor_id == doc_id:
                        print(appointment)
            print()

        else:
            break

main()
