# "methinks it is like a weasel"
import random

def makestring(n):
    chars = "abcdefghijklmnopqrstuvwxyz "
    mystr = ""
    for i in range(n+1):
        mystr = mystr + chars[random.randrange(0, 27)]
        # print(mystr)
    return mystr

def score(mainstr, genstr):
    score = 0
    for i in range(len(mainstr)):
        if mainstr[i]==genstr[i]:
            score = score + 1
    return score

def main():
    ourstr = "methinks it is like a weasel"
    length = len(ourstr)
    i = 0
    total_score = 0
    curr_score = 0
    best_str = ""
    while total_score < length:
        curr_str = makestring(length)
        curr_score = score(ourstr, curr_str)
        i = i + 1
        # print(i, curr_score, curr_str)
        if curr_score > total_score:
            total_score = curr_score
            best_str = curr_str
            # print(i, total_score, best_str)
        if (i%1000000 == 0):
            print("YES",i, total_score, best_str)


main()
