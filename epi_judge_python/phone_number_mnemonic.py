from test_framework import generic_test, test_utils


# 6.7 Compute ALL MNEMoNICS FoR A pHoNE NUMBER
# Write a program which takes as input a phone number, specified as a string of digits, and returns
# all possible character sequences that correspond to the phone number. The cell phone keypad is
# specified by a mapping that takes a digit and returns the corresponding set of characters. The
# character sequences do not have to be legal words or phrases.
MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

# really difficult. try to reproduce the steps of the algorithm
def phone_mnemonic (phone_number) :
    print(phone_number)
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number):
            mnemonics.append("".join(partial_mnemonic))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                phone_mnemonic_helper(digit + 1)    

    mnemonics, partial_mnemonic = [] , [0] * len(phone_number)
    phone_mnemonic_helper(0)
    print(mnemonics)
    return mnemonics

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
