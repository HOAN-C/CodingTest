#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

// one-point crossover 함수
void onePointCrossover(int parent1, int parent2, int& child1, int& child2) {
    // 랜덤한 cut point 결정
    int numBits = sizeof(int) * 8; // int의 비트 수
    int cutPoint = rand() % (numBits - 1) + 1; // 1부터 (numBits - 1) 사이의 랜덤한 숫자

    // cut point 이전의 비트를 자식 1에 복사
    child1 = (parent1 >> cutPoint) << cutPoint;
    child1 |= (parent2 & ((1 << cutPoint) - 1));

    // cut point 이전의 비트를 자식 2에 복사
    child2 = (parent2 >> cutPoint) << cutPoint;
    child2 |= (parent1 & ((1 << cutPoint) - 1));
}

int main() {
    srand(static_cast<unsigned int>(time(nullptr))); // 랜덤 시드 설정

    int parent1, parent2, child1, child2;
    
    cout << "Enter parent1: ";
    cin >> parent1;
    cout << "Enter parent2: ";
    cin >> parent2;

    onePointCrossover(parent1, parent2, child1, child2);

    cout << "Child 1: " << child1 << endl;
    cout << "Child 2: " << child2 << endl;

    return 0;
}
