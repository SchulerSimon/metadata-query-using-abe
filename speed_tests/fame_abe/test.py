from charm.toolbox.pairinggroup import PairingGroup, GT
from charm.toolbox.secretutil import SecretUtil
from ac17 import AC17CPABE
import timeit


def test(number_of_attr, split_attributes):
    group = PairingGroup('MNT224')
    msg = group.random(GT)

    cpabe = AC17CPABE(group, 1)
    (public_key, master_secret_key) = cpabe.setup()

    attr_list = ['ATTR' + str(n) for n in range(number_of_attr)]
    policy = '(' + ' and '.join(attr_list[:split_attributes]) + \
        ') and (' + ' or '.join(attr_list[split_attributes:]) + ')'

    secret_key = cpabe.keygen(public_key, master_secret_key, attr_list)
    cypher_text = cpabe.encrypt(public_key, msg, policy)

    dec_msg = cpabe.decrypt(public_key, cypher_text, secret_key)
    if not msg == dec_msg:
        print('Failed decryption')


setup_code = '''
from __main__ import test
'''

test_code_1 = '''
test(100, 1)
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
