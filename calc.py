#!/usr/bin/env python

# Copyright 2016 -- Levi Starrett & Jay Hankins
# for educational purposes only
#
# For use in CS 190: https://github.com/Purdue-CSUSB/CS-190-F2016/
#
# Calculator -- a four function calculator commandline tool

import sys

# -------------------------------------------------------- #
# -- CALCULATOR FUNCTIONS -------------------------------- #
# -------------------------------------------------------- #

# Add function
# a -- addend
# b -- augend
def calc(P, I, J, K):
    return (P*I*J/K)/100

# Subtract function
# a -- minuend
# b -- subtrahend

def msg():
   return "Hello Master!"
# -------------------------------------------------------- #


# -------------------------------------------------------- #
# -- MAIN FUNCTIONAILTY -- DO NOT EDIT ------------------- #
# -------------------------------------------------------- #
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
        op = None

    # decide function
        #print "Invalid operation..."
    print "result", calc(P, I, J ,K)
    #print "yo", msg()
    #print K
    q = raw_input("Quit? [y/n] ")
    if (q == "y" or q == "Y"):
        break

# -------------------------------------------------------- #
