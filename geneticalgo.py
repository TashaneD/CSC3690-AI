import random

pop_size = 10  # Population size
string_length = 6  # Length of each binary string
mutation_rate = 0.1  # Probability of mutation
generations = 5  # Number of generations

# Define the fitness function
def fitness(individual):
    # Fitness is the number of '1's in the binary string
    return sum(individual)


# Generate a random population of binary strings
def generate_population(size, length):
    return [[random.choice([0, 1]) for _ in range(length)] for _ in range(size)]


def select_parents(population, fitness_fn, tournament_size=3):
    def tournament():
        # Randomly select tournament size
        tournament_contestants = random.sample(population, tournament_size)
        # Return the one with the highest fitness
        return max(tournament_contestants, key=fitness_fn)

    # Select two parents
    parent1 = tournament()
    parent2 = tournament()
    return parent1, parent2



# Perform single point crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)  # Select crossover point
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


# Perform mutation- to flip a random bit
def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Flip the bit (0 becomes 1, 1 becomes 0)
    return individual


# Genetic algorithm main loop
def genetic_algorithm(pop_size, length, mutation_rate, generations):
    # Generate initial population
    population = generate_population(pop_size, length)

    for generation in range(generations):
        # Evaluate fitness
        population_fitness = [fitness(ind) for ind in population]
        best_fitness = max(population_fitness)
        print(f"Generation {generation}: Best fitness = {best_fitness}")

        # If best possible solution is found , then we break
        if best_fitness == length:
            break

        # In order to create next generation
        next_population = []
        for _ in range(pop_size // 2):  # Create half as many pairs
            # Selection
            parent1, parent2 = select_parents(population, fitness)

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)

            # Add to next generation
            next_population.extend([child1, child2])

        # Replace old population with the new
        population = next_population

    # Return the best individual
    best_individual = max(population, key=fitness)
    return best_individual


best_solution = genetic_algorithm(pop_size, string_length, mutation_rate, generations)
print(f"Best solution: {best_solution}, fitness = {fitness(best_solution)}")
