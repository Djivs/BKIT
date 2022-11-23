# -*- coding: utf-8 -*-

from radish import before, after

from lab_1 import getEquationRoots

@before.each_scenario
def init_function(scenario):
    scenario.context.getEquationRoots = getEquationRoots