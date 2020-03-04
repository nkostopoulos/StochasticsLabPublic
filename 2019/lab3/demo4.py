from __future__ import division
from simple_markov_chain_lib import markov_chain
import statistics as stat
from numpy import matmul
import numpy as np

def defineMarkovTable(): 
	p = 1/6
	markov_table = {
		1: {2: 1.},
		2: {2: 2/3, 3: 1/3},
		3: {1: p, 2: 1-p}
	}

	return markov_table

def defineNumpyTable():
	Pn = np.array([[0,1,0],
		       [0,2/3,1/3],
		       [1/6, 5/6, 0]])
	P0 = np.array([[1,0,0]])
	
	return Pn,P0

def multiplyNumpyTables(Pn,P0):
	for index in range(40):
		Pn = np.matmul(Pn,Pn)
	Pn = np.matmul(P0,Pn)
	return Pn

def defineInitDistribution():
	init_dist = {1: 1.}
	
	return init_dist

def calculateProbabilities(markov_table, init_dist):
	mc = markov_chain(markov_table, init_dist)
	experiments = 500000
	steps = 40
	visits = 0

	for index in range(experiments):
		mc.start()
		for j in range(steps):
			mc.move()
		if mc.running_state == 1: visits += 1

	probability = visits / experiments
	return probability

if __name__ == "__main__":
	markov_table = defineMarkovTable()
	init_dist = defineInitDistribution()

	probability = calculateProbabilities(markov_table, init_dist)
	print(probability)

	Pn,P0 = defineNumpyTable()
	realProbability = multiplyNumpyTables(Pn,P0)
	print(realProbability)
