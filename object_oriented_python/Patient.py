from Person import Person

class Patient(Person):
    def __init__(self, patient_id, address, num_visits, n='unknown', a=0,):
        super().__init__(n, a)
        self.patient_id = patient_id
        self.address = address
        self.num_visits = num_visits

    def calculate_fees(self):
        return 200 * self.num_visits
    
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('id:',self.patient_id)
        print('address:',self.address)
        print('Number of Visits:',self.num_visits)
    
    def __str__(self):
        return self.name + ', ' + str(self.age) + ", " + str(self.patient_id) + ", " + self.address +  ", " + str(self.num_visits)


# the main method is just for testing the patient class
def main():
    p = Patient(1234, "30 Avenue street", 4,"Sipho", 24,)
    print(p)
    p.display()
    print(f"Your medical fees are R{p.calculate_fees()}")

main()

