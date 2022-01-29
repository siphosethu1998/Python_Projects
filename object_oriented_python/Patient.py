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



