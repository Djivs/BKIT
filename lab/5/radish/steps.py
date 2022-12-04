# -*- coding: utf-8 -*-

from radish import given, when, then

import math

def getEquationRoots(A, B, C):
    D = B*B - 4*A*C
    if A == 0:
        if B == 0:
            return []
        else:
            return [-math.sqrt(math.abs(-C/B)), math.sqrt(math.abs(-C/B))]
    if D < 0:
        return []
    elif D == 0:
        try:    
            X1 = -math.sqrt( (-B)/(2 * A) )
            X2 = math.sqrt( (-B)/(2*A) )
        except:
            return []
        return list(set([X1, X2]))
    else:
        result = []
        firstPair = True
        secondPair = True
        try:
            X1 = -math.sqrt((-B + math.sqrt(D))/(2 * A))
            X2 = math.sqrt((-B + math.sqrt(D))/(2 * A))
        except:
            firstPair = False
        try:
            X3 = -math.sqrt((-B - math.sqrt(D))/(2 * A))
            X4 = math.sqrt((-B - math.sqrt(D))/(2 * A))
        except:
            secondPair = False
        
        if firstPair:
            result.append(X1)
            result.append(X2)
        if secondPair:
            result.append(X3)
            result.append(X4)
        return list(set(result))

@given("I have the numbers {A:g}, {B:g} and {C:g}")
def have_numbers(step, A, B, C):
    step.context.A = A
    step.context.B = B
    step.context.C = C

@when("I solve the equation with those numbers")
def sum_numbers(step):
    step.context.N = len(getEquationRoots( \
       step.context.A, step.context.B, step.context.C))

@then("I expect to get {N:g} roots")
def expect_result(step, N):
    assert step.context.N == N