def solution(numbers):
    zigzag = []
    for i in range(len(numbers)-2):
        a = numbers[i]
        b = numbers[i+1]
        c = numbers[i + 2]
        if a > b and b < c:
            zigzag.append(1)
        elif a< b and b> c:
            zigzag.append(1)
        else:
            zigzag.append(0)
    print(zigzag)
    return zigzag



solution([1,2,1,3,4,7,3,5,7,3,6])
