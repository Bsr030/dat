import random

# Define the fitness function
f = lambda x: x**2

# Genetic Algorithm Parameters
pop, mut, gen, space = 100, 0.1, 100, (-10, 10)

# Initialize the initial population with random solutions within the search space
p = [random.uniform(*space) for _ in range(pop)]

# Main Genetic Algorithm Loop
for _ in range(gen):
    # Create a new population for the next generation
    new_population = []

    # Iterate through the current population
    for _ in range(pop):
        # Select two parents based on their fitness using random.choices
        parent1 = random.choices(p, [f(x) for x in p])[0]
        parent2 = random.choices(p, [f(x) for x in p])[0]

        # Create a child by averaging the parents' values
        child = (parent1 + parent2) / 2

        # Apply mutation to the child with a certain probability
        if random.random() < mut:
            child += random.uniform(-0.1, 0.1)

        # Add the child to the new population
        new_population.append(child)

    # Update the population with the new generation
    p = new_population

    #To print the species
    #print(p)

# Find the best solution in the final population
best_solution = min(p, key=f)
best_fitness = f(best_solution)

# Print the best solution and its fitness
print(f"Best Solution: {best_solution}")
print(f"Best Fitness: {best_fitness}")
