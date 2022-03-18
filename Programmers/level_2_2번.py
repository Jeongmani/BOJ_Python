def solution(bridge_length, weight, truck_weights):
    bridge=[0 for _ in range(bridge_length)]
    time=bridge_length
    i=0
    while True:
        if i==len(truck_weights):
            break
        time+=1
        del bridge[0]
        if sum(bridge)+truck_weights[i]<=weight:
            car=truck_weights[i]
            bridge.append(car)
            i+=1
        else:
            bridge.append(0)
    return time