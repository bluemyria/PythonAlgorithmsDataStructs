import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# LOG in FILE
# logging.basicConfig(filename='myLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# DEBUG, INFO, WARNING, ERROR, CRITICAL
#logging.disable(logging.CRITICAL)

logging.debug('Start of program')
def factorial(n):
    logging.debug(f'Start of factorial {n}')

    total = 1
    for i in range(1, n+1):

        total *= i
        logging.debug(f'i is {i}, total is {total}')
    
    logging.debug(f'Return value is {total}')
    return total

print(factorial(5))

logging.debug('End of program')
