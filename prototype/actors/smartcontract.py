'''
represents an agent of any sort (eg smart contract on blockchain)
could aswell be a trusted third party etc.
'''
from .patient import *
from .queue import *
from .const import *


class Smartcontract():

    def __init__(self):
        self.patients = []
        self.queues = []

    def register(self, patient):
        self.patients.append(patient)
        self.update()

    def add_queues(self, queue):
        self.queues.extend(queue)
        self.update()

    def update(self):
        for p in self.patients:
            for q in self.queues:
                if p.queue(q.get()):
                    print('found:' + '-'.join(p.get_attr_list()))
