#
# This script does simple arithmetic
#
# Use as follows, from the command line:
#
# python arith.py number operand number
#
# For example:
# 
# python arith.py 4 / 5
#
# 
#

import sys

def main():
    assert len(sys.argv) == 4, 'Enter a binary operation (operand1 operator operand2), e.g. 1 + 1 = 4'
    
    argument1 = str(float(sys.argv[1]))
    operator = sys.argv[2]
    argument2 = str(float(sys.argv[3]))
    
    result = eval(argument1 + operator + argument2)
    print result

main()    
