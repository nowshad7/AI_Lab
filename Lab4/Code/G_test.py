import random
import sys

def random_selection(population, fitness_fn, goal_fit):
	selection = None
	current_amount = 0
	fitness_total = []
	selection = []
	for i in range(len(population)):
		current_amount += fitness_fn(population[i], goal_fit)
		fitness_total.append(current_amount)
	prob = random.uniform(0, fitness_total[-1])
	for i in range(len(population)):
		if fitness_total[i] > prob:
			return population[i]


def mutation(child):
	return switch(1, child)


def reproduce(x):
	return switch(2, x)


def compute_goal_fit(n):
	goal_fit = 0
	for i in range(n):
		goal_fit += i
	return goal_fit


def switch(n, target):
    print(target)
    for i in range(n):   
        j = random.randint(0, 15)   
        k = random.randint(0, 15)   
        target[j], target[k] = target[k], target[j]  
    return target 


def gen_alg(population, fitness):
	nmax = 100000
	n = nmax
	goal_fit = compute_goal_fit(len(random.choice(population)))
	print ("\nproblem dimension: ", len(random.choice(population)), "x", len(random.choice(population)))
	print ("population size: ", len(population))
	print ("max generations: ", n)
	print ("\nrunning...")
	while n > 0: 
		new_population = []
		for i in range(len(population)):
			x = random_selection(population, fitness_fn, goal_fit)
			child = reproduce(x)
			if random.uniform(0,1) < 1.0:
				child = mutation(child)
			if fitness(child, goal_fit) >= goal_fit:
				print ("...done. \n\nresult ", child," found in ", nmax-n, " generations.\n")
				return child	
			new_population.append(child)
		population = new_population	
		n -= 1
	print ("\nno solution found in ", nmax, " generations, try again.\n")
	return None



def fitness_fn(individual, goal_fit):
	fitness_value = goal_fit
	for i in range(len(individual)):
		j = 1
		while j < len(individual)-i:
			if (individual[i] == individual[i+j]+j) or (individual[i] == individual[i+j]-j):
				fitness_value -= 1
			j += 1
	return fitness_value



n = 16
population = []
base = n
for i in range(10):
	population.append(switch(5, base))
gen_alg(population, fitness_fn)

