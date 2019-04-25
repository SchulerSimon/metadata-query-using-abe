'''
represents a patient
'''
from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT, pair
from charm.toolbox.secretutil import SecretUtil
from charm.toolbox.ABEnc import ABEnc
from .CPabe09 import CPabe09
from .const import *
from .queue import *


class Patient():

    def __init__(self, ethnicity, age, desease):
        self.group = PairingGroup('SS512')
        self.cpabe = CPabe09(self.group)
        self.ethnicity = ethnicity
        self.age = age
        self.desease = desease

    def get_age_attributes(self):
        attr_list = []
        for n, b in enumerate('{0:07b}'.format(self.age)):
            attr_list += [abx + str(n) if b == '1' else anbx + str(n)]
        return attr_list

    def get_attr_list(self):
        return self.ethnicity + self.get_age_attributes() + self.desease

    def queue(self, queue):
        (master_secret_key, master_public_key) = self.cpabe.setup(
            queue['g1'], queue['g2'], queue['alpha'], queue['a'])
        attr_list = self.get_attr_list()
        secret_key = self.cpabe.keygen(
            master_public_key, master_secret_key, attr_list)
        return (queue['msg'] == self.cpabe.decrypt(master_public_key, secret_key, queue['cipher'])) and self.ask_if_patient_wants_to_participate()

    def ask_if_patient_wants_to_participate(self):
        return True


def create_test_patients():
    '''
    creates a list of patients 
    '''
    temp = [
        Patient(asian, 22, autism),
        Patient(asian, 23, alzheimers),
        Patient(asian, 100, diabetes),
        Patient(asian, 12, cancer),
        Patient(european, 77, cancer),
        Patient(european, 54, autism),
        Patient(european, 34, alzheimers),
        Patient(european, 29, diabetes),
        Patient(north_american, 31, cancer),
        Patient(north_american, 17, autism),
        Patient(north_american, 1, tuberculosis),
        Patient(south_american, 50, tuberculosis),
        Patient(south_american, 98, autism),
        Patient(persian, 63, cancer),
        Patient(persian, 32, tuberculosis),
        Patient(arabic, 10, autism),
        Patient(arabic, 80, cancer),
        Patient(arabic, 39, diabetes),
    ]
    return temp


if __name__ == '__main__':
    p = Patient(asian, 55, cancer)
    print(p.get_attr_list())
