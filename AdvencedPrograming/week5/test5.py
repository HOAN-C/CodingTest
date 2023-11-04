import random
TARGET_LENGTH = 20  # 문제 파라미터


# 개체 선택: 룰렛 휠 선택 , //토너먼트가 보통 많이 쓰이니 다음부턴 토너먼트 ㄱㄱ
def select_population(population, fitness, num_parents):
    selected_parents = []
    total_fitness = sum(fitness)
    for _ in range(num_parents):
        pick = random.uniform(0, total_fitness)
        current_sum = 0
        for i, ind in enumerate(population):
            current_sum += fitness[i]
            if current_sum >= pick:
                selected_parents.append(ind)
                break

    return selected_parents


def crossover(parent1, parent2):  # 교차: 두 부모로부터 두 자식 생성
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2


def mutate(individual, mutation_rate):  # 돌연변이: 랜덤 비트 뒤집기 //
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]


population_size = 29  # 초기 설정 # 29개의 개체
mutation_rate = 0.01
num_generations = 50

# 초기 개체 집합 생성
population = [[random.randint(0, 1) for _ in range(
    TARGET_LENGTH)] for _ in range(population_size)]

for generation in range(num_generations):
    fitness = [sum(ind) for ind in population]  # 개체 평가, 1의 개수 반환

    best_individual = population[fitness.index(max(fitness))]  # 가장 좋은 개체 선택
    print(f"- Generation {generation + 1}")
    # 튜플(tuple)로 돌리기 e.g (0, '10111111111111111111')
    for i, ind in enumerate(population):
        print(f"{i + 1:02}: {''.join(map(str, ind))} (F:{fitness[i]})")

    print("Best:", ''.join(map(str, best_individual)), f"(f:{max(fitness)})")

    # 새로운 개체 생성
    new_population = [best_individual]  # 엘리트 개체 보존

    while len(new_population) < population_size:
        parents = select_population(population, fitness, 2)  # 개체 선택: 룰렛 휠 선택
        child1, child2 = crossover(
            parents[0], parents[1])  # 교차: 두 부모로부터 두 자식 생성
        mutate(child1, mutation_rate)  # 돌연변이: 랜덤 비트 뒤집기
        mutate(child2, mutation_rate)
        new_population.extend([child1, child2])

    population = new_population

# 최종 결과 출력
best_individual = population[fitness.index(max(fitness))]
print("- Generation", num_generations)
print("Best:", ''.join(map(str, best_individual)), f"(F:{max(fitness)})")
