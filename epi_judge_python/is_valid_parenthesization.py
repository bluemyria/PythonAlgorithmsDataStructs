from test_framework import generic_test

# 8.3 Test a String over "{,},(,),[,]" for well-formdness
# Write a program that tests if a string made up of the characters [, ], {, }, (, ) is well-formed
def is_well_formed(s):
    # SOS!!!! do not compare ch w/ par_st.pop()
    # use par_st.pop() as index for the dictionary
    par_st = []
    pars = {"[":"]","{":"}","(":")"}
    for ch in s:
        if ch in pars.keys():
            par_st.append(ch)
        else:
            if par_st == [] or ch != pars[par_st.pop()]:
                return False
    return False if par_st != [] else True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
