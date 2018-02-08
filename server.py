class Patient(object):
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
class Hospital(object):
    def __init__(self,name):
        self.name = name
        self.id = 0
        self.bed = []
        self.waiting_room = ['abcd']
    def Admit(self, patient0):
        self.id += 1
        if self.id >= 1:
            print self.id, "We are at capacity take a seat in the waiting room.", patient0.name
            self.waiting_room.append(patient0)
            # print self.waiting_room[].name
        else:
            print self.id, "Here we are, a bed just opend up for you. Don't ask how...enjoy your stay",patient0.name
            self.bed.append(patient0)
            # print self.bed[0].id
        return self
    def discharge(self,patientX):
        for i in range(0,len(self.bed)):
            if self.bed[i] == patientX:
                self.bed.pop(i)
                self.id -= 1
                print "A room opened. Next!"
                if len(self.waiting_room) > 0:
                    self.bed.append(self.waiting_room.pop(0))
                    print self.bed
            return self
        

        



numb1 = Patient('Steve','peanut')
numb2 = Patient('Fred','bee')
numb3 = Patient('Zedd','coconut')
hop1 = Hospital('hostal')
hop1.Admit(numb1).Admit(numb2).Admit(numb3).discharge(numb1)

# change capacity to id
# change patients to bed
