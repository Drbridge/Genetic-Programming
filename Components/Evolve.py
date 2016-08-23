from Components.Tree import Tree
from Components.Fitness import Fitness
from random import random
from random import choice

import Kits.Operations as genop
import Kits.Functions as genfunc

class Evolve(object):
    def __init__(self, funcSet, termSet, fit, varDict, maxDeep = 3,
                 crosRate = 0.9, mutaRate = 0.1, size = 10, generation = 10):
        self.funcSet = funcSet
        self.termSet = termSet
        self.maxDeep = maxDeep
        self.crosRate = crosRate
        self.mutaRate = mutaRate
        self.size = size
        self.generation = generation
        self.fit = fit
        self.varDict = varDict
        self.population = []

    def init(self):
        for i in range(self.size):
            _ = Tree()
            deep = int(random() * self.maxDeep)
            _.makeTree(deep=deep, termSet=self.termSet, funcSet=self.funcSet)
            self.population.append(_)

    def evolve(self):
        for i in range(self.generation):
            for individual in self.population:
                individual.getDeep()
                individual.getSize()
                individual.calVal()
                individual.calFitness(fit=self.fit, varList=self.varDict)
            self.population.sort(cmp=genfunc.treeSort, reverse=True)
            _population = []
            for j in range(int(self.crosRate * self.size)):
                _ = genop.corssovers(self.population[j], self.population[j + 1])
                _population.append(_)
            for j in range(int(self.mutaRate * self.size)):
                _ = genop.mutation(tree=choice(self.population), termSet=self.termSet, funcSet=self.funcSet)
                _population.append(_)
            self.population = _population
        self.population.sort(cmp=genfunc.treeSort, reverse=True)
        return self.population[0]