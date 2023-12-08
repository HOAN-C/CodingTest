# IBX(2안)
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

    def cross(self, parents: List[Chromosome]) -> Chromosome:
        p1, p2 = parents[0], parents[1]
        r1_idx = self.select_route(p1)
        r1 = p1.routes[r1_idx]
        centroid = r1[len(r1) // 2]
        log.debug(f"Centroid : {centroid}\tfrom {r1}")

        # Use the construct_child_route method
        child_route = self.construct_child_route(p1, p2, r1_idx, centroid)

        # Create a new Chromosome with the child route
        child_chromosome = Chromosome(
            permutation=self.route_to_permutation(child_route))

        return child_chromosome
