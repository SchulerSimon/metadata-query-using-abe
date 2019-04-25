from charm.toolbox.pairinggroup import PairingGroup, ZR, G1, G2, GT, pair
from charm.toolbox.secretutil import SecretUtil
from charm.toolbox.ABEnc import ABEnc
from CPabe09 import CPabe09

import timeit


def test(number_of_attr, split_attributes):
    group = PairingGroup('SS512')
    msg = group.random(GT)

    g1, g2 = group.random(G1), group.random(G2)
    alpha, a = group.random(), group.random()
    cpabe = CPabe09(group)
    (master_secret_key, master_public_key) = cpabe.setup(g1, g2, alpha, a)

    attr_list = ['ATTR' + str(n) for n in range(number_of_attr)]
    policy = '(' + ' and '.join(attr_list[:split_attributes]) + \
        ') and (' + ' or '.join(attr_list[split_attributes:]) + ')'

    secret_key = cpabe.keygen(master_public_key, master_secret_key, attr_list)
    cypher_text = cpabe.encrypt(master_public_key, msg, policy)

    decrypted_msg = cpabe.decrypt(master_public_key, secret_key, cypher_text)


setup_code = '''
from __main__ import test
'''

test_code_1 = '''
test(100,1)
'''

test_code_2 = '''
test(100,99)
'''

test_code_3 = '''
test(500,1)
'''

test_code_4 = '''
test(500,250)
'''

test_code_5 = '''
test(500,499)
'''

test_code_6 = '''
test(900,1)
'''

test_code_7 = '''
test(900,450)
'''

test_code_8 = '''
test(900,899)
'''


if __name__ == '__main__':
    print(timeit.timeit(setup=setup_code, stmt=test_code_1, number=10))
    print(timeit.timeit(setup=setup_code, stmt=test_code_2, number=10))
    print(timeit.timeit(setup=setup_code, stmt=test_code_3, number=10))
    print(timeit.timeit(setup=setup_code, stmt=test_code_4, number=10))
    print(timeit.timeit(setup=setup_code, stmt=test_code_5, number=10))
    print(timeit.timeit(setup=setup_code, stmt=test_code_6, number=10))
    print(timeit.timeit(setup=setup_code, stmt=test_code_7, number=10))
    print(timeit.timeit(setup=setup_code, stmt=test_code_8, number=10))
