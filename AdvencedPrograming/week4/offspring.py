import random

populationSize = 30
chromosomeLength = 10

population = []  # population 배열 생성

# populationSize(30)개 chromosome 랜덤 생성.
for i in range(populationSize):
    chromosome = [random.randint(0, 1) for _ in range(chromosomeLength)]
    fitness = sum(chromosome)
    population.append((chromosome, fitness))
    print(f"{i}: {''.join(map(str, chromosome))} (f:{fitness})")


tournament_size = 0.5  # 토너먼트 크기


def tournament_selection(population, tournament_size):
    selected_parents = []

    for _ in range(2):  # 두 번 선택
        tournament = random.sample(population, int(
            tournament_size * populationSize))  # tournament_size 0.5 기준 15개 겹치지 않는 무작위 추출
        # fitness 사이즈 기준 tornament 내림차순으로 정렬
        tournament.sort(key=lambda x: x[1], reverse=True)
        selected_parent = tournament[0]  # 정렬 이후 0 index, 제일 처음 오는 값 추출.
        selected_parents.append(selected_parent)  # 선택부모에 추가.

    return selected_parents


# 위 tournament_selection 함수를 통해 2개 값 추춣
parent1, parent2 = tournament_selection(population, tournament_size)


def uniform_crossover(parent1, parent2):
    offspring = []
    for gene1, gene2 in zip(parent1[0], parent2[0]):
        if random.random() < 0.5:  # 랜덤값이 0.5 보다 크거나 작으면 gen1 or gen2 추가
            offspring.append(gene1)
        else:
            offspring.append(gene2)
    return offspring


print("\nTournament selection")
print(f"Parent 1: {''.join(map(str, parent1[0]))} (f:{parent1[1]})")
print(f"Parent 2: {''.join(map(str, parent2[0]))} (f:{parent2[1]})")


offspring = uniform_crossover(parent1, parent2)
offspring_fitness = sum(offspring)
print("\nUniform crossover")
print(f"Offspring: {''.join(map(str, offspring))} (f:{offspring_fitness})")
