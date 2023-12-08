# Crossover.py 수정
# def construct_child_route 구현
# PMX Crossover에 조건문 추가해 결과 노드 중복 방지

# 실행조건
# Generation:100
# MUTATION_RATE = 60

# Crossover.py 코드

import random

from abc import abstractmethod, ABCMeta
from typing import List

from domain.Chromosome import Chromosome
from log.log_config import log
from domain.Dataset import Dataset

class Crossover(metaclass=ABCMeta):
    @abstractmethod
    def cross(self, parents: List[Chromosome]) -> Chromosome:
        pass


class PMXCrossover(Crossover):
    def cross(self, parents: List[Chromosome]) -> Chromosome:
        p1, p2 = parents[0], parents[1]
        p1_perm = [customer for route in p1.routes for customer in route]
        p2_perm = [customer for route in p2.routes for customer in route]

        # 겹치지 않는 루트를 찾을 때까지 반복
        while True:
            # PMX 교차 수행
            points = sorted(random.sample(range(0, len(p1_perm)), 2))
            result = [0 for _ in range(len(p1_perm))]
            result[points[0]: points[1] + 1] = p1_perm[points[0]: points[1] + 1]

            for i, value in enumerate(result):
                if value == 0:
                    while (p2_value := p2_perm.pop(0)) in result:
                        pass
                    result[i] = p2_value

            # 루트가 겹치지 않는지 확인
            child_chromosome = Chromosome(result)
            if not self.routes_overlap(child_chromosome):
                return child_chromosome

    def routes_overlap(self, chromosome: Chromosome) -> bool:
        seen_customers = set()
        for route in chromosome.routes:
            for customer in route:
                if customer in seen_customers:
                    return True
                seen_customers.add(customer)
        return False


class IBXCrossover(Crossover):
    def construct_child_route(self, parent1: Chromosome, parent2: Chromosome, route_idx: int, centroid: int) -> List[int]:
        child_route = []
        visited_customers = set()

        current_time = parent1.customers[centroid].due_date
        current_x, current_y = parent1.customers[centroid].x, parent1.customers[centroid].y

        for i in range(1, len(parent1.routes[route_idx])):
            customer = parent1.routes[route_idx][i]

            if current_time + parent1.customers[customer].service_time > parent1.customers[customer].due_date:
                current_time = max(current_time + parent1.customers[customer].service_time, parent1.customers[customer].ready_time)
            else:
                if parent1.customers[customer].ready_time <= current_time <= parent1.customers[customer].due_date:
                    if abs(current_x - parent1.customers[customer].x) < 5 and abs(current_y - parent1.customers[customer].y) < 6:
                        current_time += parent1.customers[customer].service_time
                        current_x, current_y = parent1.customers[customer].x, parent1.customers[customer].y
                        child_route.append(customer)

                        if current_time > parent1.customers[customer].due_date:
                            log.warning(f"{route_idx} 경로의 {customer} 고객의 시간 제약이 위반되었습니다.")

        for i in range(1, len(parent1.routes[route_idx])):
            customer = parent1.routes[route_idx][i]
            if customer not in visited_customers:
                child_route.append(customer)
                visited_customers.add(customer)

        for i in range(len(parent2.routes[route_idx])):
            customer = parent2.routes[route_idx][i]
            if customer not in visited_customers:
                child_route.append(customer)
                visited_customers.add(customer)

        return child_route

    def nearest_neighbor(self, starting_customer, remaining_customers):
        min_distance = float('inf')
        nearest_customer = None

        for neighbor in remaining_customers:
            distance = self.calculate_distance(starting_customer, neighbor)
            if distance < min_distance:
                min_distance = distance
                nearest_customer = neighbor

        return nearest_customer, min_distance


    def nearest_neighbor_procedure(self, starting_customer, remaining_customers):
        current_customer = starting_customer
        path = [starting_customer]

        while remaining_customers:
            # Find adjacent neighbors
            adjacent_neighbors = [neighbor for neighbor in remaining_customers if neighbor in self.get_adjacent_nodes(current_customer)]
            
            # If there are adjacent neighbors, select one; otherwise, select the nearest neighbor
            if adjacent_neighbors:
                next_customer = random.choice(adjacent_neighbors)
            else:
                next_customer, _ = self.nearest_neighbor(current_customer, remaining_customers)
            
            path.append(next_customer)
            remaining_customers.remove(next_customer)
            current_customer = next_customer

        return path

    
    def cross(self, parents: List[Chromosome]) -> Chromosome:
        p1, p2 = parents[0], parents[1]
        r1_idx = self.select_route(p1)
        r1 = p1.routes[r1_idx]
        centroid = r1[len(r1) // 2]
        log.debug(f"Centroid: {centroid}\tfrom {r1}")

        # Construct child route using the modified insertion heuristic
        child_route = self.construct_child_route(p1, p2, r1_idx, centroid)

        # Apply Nearest-Neighbor Procedure for additional routes
        remaining_customers = set(customer for route in p1.routes if route != r1 for customer in route)
        additional_routes = []

        while remaining_customers:
            start_customer = random.choice(list(remaining_customers))
            path = self.nearest_neighbor_procedure(start_customer, remaining_customers)
            additional_routes.append(path)

        # Combine the constructed child route with additional routes to form the child chromosome
        child_routes = [child_route] + additional_routes

        # Create and return the child chromosome
        child_chromosome = Chromosome(routes=child_routes)
        return child_chromosome

   
