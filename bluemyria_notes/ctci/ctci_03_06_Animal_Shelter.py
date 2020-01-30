from pprint import pprint
from queue import Queue

class Animal():
    def __init__(self, name, kind, arr_time):
        self.name = name
        self.kind = kind
        self.time = arr_time
    def __str__(self):
        return self.name + " " + self.kind + " " + str(self.time)

class AnimalShelter():
    def __init__(self):
        self.time = 0
        self.dogQueue = Queue()
        self.catQueue = Queue()
        self.q = { 'dog': self.dogQueue, 'cat': self.catQueue }

    def enqueue(self, kind, name):
        self.time += 1
        animal = Animal(name, kind, self.time)
        self.q[kind].put(animal)

    def dequeueAny(self):
        if self.dogQueue.empty():
            return self.dequeueCat()
        if self.catQueue.empty():
            return self.dequeueDog()
            
        cat = self.catQueue.get()
        dog = self.dogQueue.get()
        return cat if cat.time < dog.time else dog

    def dequeueDog(self):
        if self.dogQueue.empty():
            return None
        else:
            return self.dogQueue.get()

    def dequeueCat(self):
        if self.catQueue.empty():
            return None
        else:
            return self.catQueue.get()


if __name__ == '__main__':
    shelter = AnimalShelter()
    shelter.enqueue('dog', 'Bear')
    shelter.enqueue('cat', 'Buffy')
    shelter.enqueue('cat', 'Yoda')
    print(shelter.dequeueCat())
    print(shelter.dequeueCat())
    shelter.enqueue('cat', 'Chelsea')
    print(shelter.dequeueAny())
    print(shelter.dequeueDog())
    shelter.enqueue('cat', 'Oscar')
    print(shelter.dequeueCat())

    