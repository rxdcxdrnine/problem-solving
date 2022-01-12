import heapq
from typing import List, Tuple


def reconstructQueue_0(people: List[List[int]]) -> List[List[int]]:

    sorted_people: List[List[int]] = sorted(people, key=lambda x: (x[1], -x[0]))
    answer: List[List[int]] = [sorted_people.pop(0)]

    for person in sorted_people:
        count: int = 0

        if person[1] == 0:
            answer.insert(0, person)

        else:
            for ind, other in enumerate(answer):
                # height
                if person[0] <= other[0]:
                    count += 1

                # key
                if count == person[1]:
                    break

            answer.insert(ind + 1, person)

    return answer


def reconstructQueue_1(people: List[List[int]]) -> List[List[int]]:
    heap = []
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))

    result = []
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])

    return result

if __name__ == "__main__":
    people: List[List[int]] = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    print(reconstructQueue_0(people))
