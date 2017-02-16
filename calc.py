import sys

def calc(P, I, J, K):
    return (P*I*J/K)/100

def msg():
   return "k"
# P - initial deposit money
# S - resulting money
# K - days in year
# I - interest rate
# J- capitalisation period days
P = None
S = None
K = 365
I = None
J = None

while (True):
    # get input values
    P = raw_input("Enter Inintial money amount P: ")
    I = raw_input("Enter Interest Rate: ")
    J = raw_input("Enter capitalisation period: ")
    try:
        P = int(P)
        I = int(I)
        J = int(J)
    except ValueError:
        print "Invalid number argument..."


    # decide function
        #print "Invalid operation..."
    print "result", calc(P, I, J ,K)
    #print "yo", msg()
    #print K
    q = raw_input("Quit? [y/n] ")
    if (q == "y" or q == "Y"):
        break

# -------------------------------------------------------- #

import unittest

class TestStringMethods(unittest.TestCase):

    def test_msg(self):
        self.assertEqual(msg(), 'kf')


if __name__ == '__main__':
    unittest.main()

