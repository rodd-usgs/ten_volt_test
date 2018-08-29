#!/usr/bin/python

from ten_volt_test import ten_volt_test

def main():
    check_ten_volt_test()


def check_ten_volt_test():
    perc = ten_volt_test(16774130, -16772780, 26)
    if perc == 0.0224:
        print('TEST1: TEN_VOLT_TEST PASSED')
    else:
        print('TEST1: TEN_VOLT_TEST FAILED: CHECK CODE')
    perc = ten_volt_test(0, 0, 26)
    if perc == 100.0000:
        print('TEST2: TEN_VOLT_TEST PASSED')
    else:
        print('TEST2: TEN_VOLT_TEST FAILED: CHECK CODE')
    perc = ten_volt_test(4197580, -4197314, 24)
    if perc == -0.0749:
        print('TEST3: TEN_VOLT_TEST PASSED')
    else:
        print('TEST3: TEN_VOLT_TEST FAILED: CHECK CODE')
    perc = ten_volt_test(0, 0, 24)
    if perc == 100.0000:
        print('TEST4: TEN_VOLT_TEST PASSED')
    else:
        print('TEST4: TEN_VOLT_TEST FAILED: CHECK CODE')


if __name__ == '__main__':
    main()
