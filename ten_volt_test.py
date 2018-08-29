import sys

def main():
    if len(sys.argv) != 4:
        sys.exit('You do not have the correct number of arguments')
    script = sys.argv[0]
    val1 = float(sys.argv[1])
    val2 = float(sys.argv[2])
    bit = float(sys.argv[3])
    ten_volt_test(val1, val2, bit)

def ten_volt_test(x, y, bit):
    x = abs(x)
    y = abs(y)
    val = (x+y)/2
    if bit==24:
        test_val = 2**24./40
    elif bit == 26:
        test_val = 2**26./40
    perc = (1 - (val/(test_val*10)))*100
    if perc <= 0.5 or perc >= -0.5:
        print('{:f} is within 0.5% of nominal value {:f}: {:4f}'.format(val/10, test_val, perc))
    else:
        print('{:f} is within 0.5% of nominal value {:f}: {:4f}'.format(val/10, test_val, perc))
    return round(perc, 4)

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
