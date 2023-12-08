# mutation
import random
from domain.Chromosome import Chromosome
from typing import List


class Node:
    def __init__(self, solution, lower_bound):
        self.solution = solution
        self.lower_bound = lower_bound


def boundary(solution, distance_matrix, time_matrix):
    # 경계 함수 구현: 고객을 방문하는 비용을 합산하여 반환
    total_distance = calculate_total_distance(solution, distance_matrix)
    total_time = calculate_total_time(solution, time_matrix)

    # 간단한 형태로 삽입 비용과 위치 수를 고려한 경계 함수를 만들었습니다.
    # 실제로는 문제에 따라 더 복잡한 함수가 필요할 수 있습니다.
    cost = total_distance + total_time
    opportunities = len(solution)

    # 순위를 계산하고 반환
    rank = cost + opportunities
    return rank


def calculate_total_distance(solution, distance_matrix):
    # 총 이동 거리 계산 함수
    total_distance = 0
    for i in range(len(solution) - 1):
        from_customer = solution[i]
        to_customer = solution[i + 1]
        total_distance += distance_matrix[from_customer][to_customer]

    return total_distance


def calculate_total_time(solution, time_matrix):
    # 총 이동 시간 계산 함수
    total_time = 0
    for i in range(len(solution) - 1):
        from_customer = solution[i]
        to_customer = solution[i + 1]
        total_time += time_matrix[from_customer][to_customer]

    return total_time


def branch(node, distance_matrix, time_matrix):
    # 노드 분기 규칙 구현: 현재 순열에서 두 고객을 선택하여 위치를 교환하는 모든 가능한 자식 노드 생성
    children = []

    for i in range(len(node.solution)):
        for j in range(i + 1, len(node.solution)):
            # 교환
            child_solution = node.solution.copy()
            child_solution[i], child_solution[j] = child_solution[j], child_solution[i]

            # 경계 함수 계산
            child_lower_bound = boundary(
                child_solution, distance_matrix, time_matrix)

            # 자식 노드 생성
            child_node = Node(child_solution, child_lower_bound)
            children.append(child_node)

    return children


class Mutation:
    @abstractmethod
    def mutate(self, chromosome: Chromosome, distance_matrix, time_matrix) -> Chromosome:
        pass


class LNSBMutation(Mutation):
    def __init__(self, d=3, D=15):
        self.d = d  # Discrepancy factor
        self.D = D  # Parameter controlling determinism

    def mutate(self, chromosome: Chromosome, distance_matrix, time_matrix) -> Chromosome:
        # Copy the permutation from the given chromosome
        permutation = chromosome.routes_to_permutation(chromosome.routes)

        # Randomly select a customer to be inserted
        L = len(permutation)
        rand = random.uniform(0, 1)

        # Adjust selection based on the parameter D
        if self.D == 1:
            selected_customer = random.randint(0, L - 1)
        else:
            selected_customer = int(L * rand)

        # Perform branch-and-bound search over different insertion positions
        # using the LNSB-M(d) strategy
        tree_expansion_factor = random.choice([1, 2, 3])

        queue = [Node(permutation, boundary(
            permutation, distance_matrix, time_matrix))]
        best_solution = permutation
        best_value = float('inf')

        while queue:
            # Using FIFO queue for breadth-first search
            current_node = queue.pop(0)

            if current_node.lower_bound < best_value:
                if len(current_node.solution) == len(permutation):
                    current_value = objective_function(
                        current_node.solution, distance_matrix, time_matrix)
                    if current_value < best_value:
                        best_value = current_value
                        best_solution = current_node.solution

                else:
                    # Branch and generate child nodes
                    children = branch(
                        current_node, distance_matrix, time_matrix)
                    queue.extend(children)

        # Return the best solution found
        return Chromosome(best_solution)


def objective_function(solution, distance_matrix, time_matrix):
    # 목적 함수 계산 함수
    # 경계 함수를 포함하여 문제에 따라 적절한 방식으로 계산되어야 합니다.
    return boundary(solution, distance_matrix, time_matrix)
