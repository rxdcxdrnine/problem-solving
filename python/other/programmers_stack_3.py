def solution(bridge_length, weight, truck_weights):
    answer = 0
    before = [i for i in range(len(truck_weights))]
    count = [0] * len(truck_weights)
    bridge = []
    after = []

    while before or bridge:

        for index in bridge:
            count[index] += 1

        while bridge:
            next = bridge[0]
            if count[next] == bridge_length:
                after.append(truck_weights[bridge.pop(0)])
            else:
                break

        current_weight = 0
        for index in bridge:
            current_weight += truck_weights[index]

        if before:
            next = before[0]
            if current_weight + truck_weights[next] <= weight \
                    and len(bridge) + 1 <= bridge_length:
                bridge.append(before.pop(0))

        answer += 1

    return answer


if __name__ == "__main__":
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    print(solution(bridge_length, weight, truck_weights))
