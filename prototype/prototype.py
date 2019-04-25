from actors.smartcontract import *
from actors.patient import *
from actors.queue import *


def main():
    sm = Smartcontract()

    patients = create_test_patients()
    for p in patients:
        sm.register(p)

    queues = create_test_queues()
    sm.add_queues(queues)

if __name__ == '__main__':
    main()
