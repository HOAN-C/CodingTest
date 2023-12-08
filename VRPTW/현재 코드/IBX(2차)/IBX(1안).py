# IBX(1안)
class IBXCrossover(Crossover):
    @staticmethod
    def select_route(chromosome: Chromosome) -> int:
        # Select Randomly One of P1's Routes by waiting time
        point = random.random()
        total_waiting_time = sum(chromosome.waiting_time)
        point *= total_waiting_time
        sum_val = 0
        for i in range(len(chromosome.routes)):
            sum_val += chromosome.waiting_time[i]
            if point < sum_val:
                return i

    def construct_child_route(self, parent1: Chromosome, parent2: Chromosome, route_idx: int, centroid: int) -> List[int]:
        # Solomon의 영감을 받은 수정된 삽입 휴리스틱의 구현
        child_route = [centroid]  # 중심으로 시작

        # Set to track visited customers for all vehicles
        visited_customers = set([centroid])

        for i in range(1, len(parent1.routes[route_idx])):
            # 만약 해당 고객이 아직 방문되지 않았다면 해당 고객을 자식 경로에 추가
            customer = parent1.routes[route_idx][i]
            if customer not in visited_customers:
                child_route.append(customer)
                visited_customers.add(customer)

        # 이미 자식 경로에 없는 경우 parent2에서 고객을 추가
        for i in range(len(parent2.routes[route_idx])):
            customer = parent2.routes[route_idx][i]
            if customer not in visited_customers:
                child_route.append(customer)
                visited_customers.add(customer)

        return child_route

    def nearest_neighbor_procedure(self, starting_customer, remaining_customers):
        current_customer = starting_customer
        path = [starting_customer]

        while remaining_customers:
            # Find adjacent neighbors
            adjacent_neighbors = [neighbor for neighbor in remaining_customers if
                                  neighbor in self.get_adjacent_nodes(current_customer)]

            # If there are adjacent neighbors, select one; otherwise, select the nearest neighbor
            if adjacent_neighbors:
                next_customer = random.choice(adjacent_neighbors)
            else:
                next_customer, _ = self.nearest_neighbor(
                    current_customer, remaining_customers)

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
        remaining_customers = set(
            customer for route in p1.routes if route != r1 for customer in route)
        additional_routes = []

        while remaining_customers:
            start_customer = random.choice(list(remaining_customers))
            path = self.nearest_neighbor_procedure(
                start_customer, remaining_customers)
            additional_routes.append(path)

        # Combine the constructed child route with additional routes to form the child chromosome
        child_routes = [child_route] + additional_routes

        # Create and return the child chromosome
        # Waiting time 정보가 누락되어 있어 None으로 처리
        child_chromosome = Chromosome(routes=child_routes, waiting_time=None)
        return child_chromosome
