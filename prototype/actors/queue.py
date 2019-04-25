'''
represents a queue looking for patients
'''
from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT, pair
from charm.toolbox.secretutil import SecretUtil
from charm.toolbox.ABEnc import ABEnc
from .CPabe09 import CPabe09
from .const import *
from .patient import *
import re


class Queue():

    def __init__(self, queue):
        self.group = PairingGroup('SS512')
        self.g1, self.g2 = self.group.random(G1), self.group.random(G2)
        self.alpha, self.a = self.group.random(), self.group.random()
        self.cpabe = CPabe09(self.group)
        (self.master_secret_key, self.master_public_key) = self.cpabe.setup(
            self.g1, self.g2, self.alpha, self.a)
        self.msg = self.group.random(GT)
        self.policy = self.get_policy(queue)
        self.cipher = self.cpabe.encrypt(
            self.master_public_key, self.msg, self.policy)

    def get(self):
        return {
            'msg': self.msg,
            'cipher': self.cipher,
            'g1': self.g1,
            'g2': self.g2,
            'alpha': self.alpha,
            'a': self.a
        }

    def get_age_policy(self, age_string):
        ages = age_string[1:-1].split(' to ')
        temp = ''
        for age in range(int(ages[0]), int(ages[1]) + 1):
            temp_list = []
            for n, b in enumerate('{0:07b}'.format(age)):
                temp_list += [abx + str(n) if b == '1' else anbx + str(n)]
            temp += '(' + ' and '.join(temp_list) + ') or '
        return '(' + temp[:-3] + ')'

    def get_policy(self, queue):
        for a in bit_dict:
            queue = queue.replace(a, '(' + ' and '.join(bit_dict[a]) + ')')
        match = re.search(r'\([0-9]+ to [0-9]+\)', queue).group()
        queue = queue.replace(match, self.get_age_policy(match))
        return queue


def create_test_queues():
    temp = [
        Queue(
            '(asian or european or north_american) and (22 to 100) and (cancer or autism)'),
        #Queue('asian and (23 to 23) and alzheimers'),
        #Queue('(european or asian) and (98 to 100) and diabetes')
    ]
    return temp

if __name__ == '__main__':
    Queue(
        '(asian or european or north_american) and (22 to 100) and (cancer or autism)')
