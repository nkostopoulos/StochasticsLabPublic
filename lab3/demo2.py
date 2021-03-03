from __future__ import division
from simple_markov_chain_lib import markov_chain
import numpy as np
import matplotlib.pyplot as plt

def defineMarkovTable(): 
	markov_table = {
		0: {0: 0.6, 1: 0.2, 5: 0.2},
		1: {0: 0.2, 1: 0.6, 2: 0.2},
		2: {1: 0.2, 2: 0.6, 3: 0.2},
		3: {2: 0.2, 3: 0.6, 4: 0.2},
		4: {3: 0.2, 4: 0.6, 5: 0.2},
		5: {0: 0.2, 4: 0.2, 5: 0.6}
        }

	return markov_table

def defineInitDistribution():
	init_dist = {0: 1.}
	
	return init_dist

def calculateFrequencyTable(markov_table,init_dist):
	total_runs = 10000

	visits = list()
	visits = [0] * len(markov_table)

	for index in range(total_runs):
		mc.move()
		visits[mc.running_state] += 1
	
	frequency = [v/total_runs for v in visits]
	
	return frequency

def printFrequencies(frequency, markov_table):
	for state in range(0, len(markov_table)) :
		print(str(state) + ": ", str(frequency[state]))
	
	return None

def plotFrequencies(frequency):
	objects = ('1', '2', '3', '4', '5', '6')
	y_pos = np.arange(len(objects))
	
	plt.bar(y_pos, frequency, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel('States')
	plt.title('Frequencies')
	plt.show()
	
	return None

if __name__ == "__main__":
	markov_table = defineMarkovTable()
	init_dist = defineInitDistribution()
	mc = markov_chain(markov_table, init_dist)
	mc.start()

	frequency = calculateFrequencyTable(markov_table, init_dist)
	printFrequencies(frequency, markov_table)
	plotFrequencies(frequency)
