import os
import traceback

#################################################
# EXCEPTIONS & TRACEBACK
#################################################
def boxPrint(symbol, width, height):
    
    try:
        if len(symbol) != 1:
            raise Exception('"symbol" must be a string of length 1')
        if width < 3 or height < 3:
            raise Exception('"width" and "height" must be greater than 2')
    except:
        errorFile = open('error_log.txt', 'a')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('the traceback was written in error_log.txt')
    print(symbol * width)

    for _ in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol )

    print(symbol * width)

boxPrint('&', 15, 8)
boxPrint('O', 5, 20)
boxPrint('**', 5, 20)
boxPrint('*', 2, 20)
boxPrint('*', 3, 2)

#################################################
# ASSERTIONS
#################################################

market_2nd = {'ns': 'green', 'ew':'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)


