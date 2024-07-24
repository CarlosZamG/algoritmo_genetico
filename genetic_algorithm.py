from typing import Callable, List
import numpy as np

PROBABILITY: float = 0.5

def initialization(init_size: int, left_endpoint: float,
                    right_endpoint: float) -> np.ndarray:
    
    # Generamos números aleatorios en nuestro intervalo para nuestra 
    # población inicial
    scalar: float = right_endpoint-left_endpoint
    population: np.ndarray = left_endpoint + scalar*np.random.rand(init_size)
    return population

def selection(population: np.ndarray,
                function: Callable[[float],float]) -> np.ndarray:
    
    np.random.shuffle(population)
    
    partition_1: np.ndarray = population[::2]
    partition_2: np.ndarray = population[1::2]
    evaluation_1: np.ndarray = function(partition_1)
    evaluation_2: np.ndarray = function(partition_2)
    
    size: int  = evaluation_1.size
    best_population: List[float] = []

    for index in range(size):
        e = evaluation_1[index]
        e2 = evaluation_2[index]
        
        if e < e2:
            i = 2*index
        else:
            i = 2*index+1
        
        best_population.append(population[i])
    
    return np.array(best_population)

def mutation(population: np.ndarray) -> np.ndarray:
    
    new_population: List[float] = []

    for i in range(population.size):
        value = np.random.rand(1)
        if value > PROBABILITY:
            # Aplicamos la mutación
            noise = np.random.normal()
            new_population.append(population[i] + noise)
        else:
            # NO aplicamos la mutación
            new_population.append(population[i])
    
    return np.array(new_population)


def crossover(population: np.ndarray) -> np.ndarray:
    values: np.ndarray = np.random.rand(int(population.size/2))
    
    term_1: np.ndarray = np.multiply(values, population[::2])
    term_2: np.ndarray = np.multiply((1-values), population[1::2])
    sons_1: np.ndarray = term_1 + term_2
    
    term_3: np.ndarray = np.multiply((1-values), population[::2])
    term_4: np.ndarray = np.multiply(values, population[1::2])
    sons_2: np.ndarray = term_3 + term_4
    
    return np.append(sons_1, sons_2)

def find_roots(function: Callable[[float],float],
                left_endpoint: float,
                right_endpoint: float,
                init_size: int,
                number_of_generations:int) -> np.ndarray:
    
    # Tamaño de la población inicial
    abs_function: Callable[[float],float] = lambda x: abs(function(x))
    population: np.ndarray = initialization(init_size, left_endpoint,
                                right_endpoint)
    
    for i in range(number_of_generations):
        parents_1: np.ndarray = selection(population, abs_function)
        parents_2: np.ndarray = selection(population, abs_function)
        all_parents: np.ndarray = np.append(parents_1, parents_2)
        sons: np.ndarray = crossover(all_parents)
        new_sons: np.ndarray = mutation(sons)
        parents_and_sons: np.ndarray = np.append(all_parents, new_sons)
        population: np.ndarray = selection(parents_and_sons, abs_function)
    
    return population







