import re
import textwrap as tw
from more_itertools import sliced

def main():
    number = [[] for i in range(5)]
    for i in range(5):
        number[i] = input()
        #number[i] = re.findall('....', number[i])
        #number[i] = map(''.join, zip(*[iter(number[i])]*4))
        number[i] = list(sliced(number[i], 4))
        """for j in range(len(number[i])):
            p_holder = list(number[i][j])
            p_holder.pop()
            number[i][j] = "".join(p_holder)"""

    new = zip(number[0], number[1], number[2], number[3], number[4])
    all_digits = tuple(new)
    #print(all_digits)

    explode = None
    digit = None
    given_num = ""
    for x in all_digits:
        match x:
            case ('***', '* *', '* *', '* *', '***')|('*** ', '* * ', '* * ', '* * ', '*** '):
                digit = "0"
            case ('  *', '  *', '  *', '  *', '  *')|('  * ', '  * ', '  * ', '  * ', '  * '):
                digit = "1"
            case ('***', '  *', '***', '*  ', '***')|('*** ', '  * ', '*** ', '*   ', '*** '):
                digit = "2"
            case ('***', '  *', '***', '  *', '***')|('*** ', '  * ', '*** ', '  * ', '*** '):
                digit = "3"
            case ('* *', '* *', '***', '  *', '  *')|('* * ', '* * ', '*** ', '  * ', '  * '):
                digit = "4"
            case ('***', '*  ', '***', '  *', '***')|('*** ', '*   ', '*** ', '  * ', '*** '):
                digit = "5"
            case ('***', '*  ', '***', '* *', '***')|('*** ', '*   ', '*** ', '* * ', '*** '):
                digit = "6"
            case ('***', '  *', '  *', '  *', '  *')|('*** ', '  * ', '  * ', '  * ', '  * '):
                digit = "7"
            case ('***', '* *', '***', '* *', '***')|('*** ', '* * ', '*** ', '* * ', '*** '):
                digit = "8"
            case ('***', '* *', '***', '  *', '***')|('*** ', '* * ', '*** ', '  * ', '*** '):
                digit = "9"
            case _:
                return "BOOM!!"
        given_num += digit

    if int(given_num)%6 == 0:
        return "BEER!!"
    else:
        return "BOOM!!"

print(main())




