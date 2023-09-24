
import random


def input_binary_array():
    while True:
        binary_array = input("10 길이의 이진 배열을 입력하세요 (예: 1010101010): ")
        if len(binary_array) == 10 and all(bit in '01' for bit in binary_array):
            return [int(bit) for bit in binary_array]
        else:
            print("올바르지 않습니다.")


print("첫 번째 부모:")
parent1 = input_binary_array()

print("두 번째 부모:")
parent2 = input_binary_array()

crossover_point = random.randint(1, 9)
child1 = parent1[:crossover_point] + parent2[crossover_point:]
child2 = parent2[:crossover_point] + parent1[crossover_point:]

print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child 1:", child1)
print("Child 2:", child2)
print("cutpoint:", crossover_point)
