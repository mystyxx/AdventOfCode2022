number = []
sum = 0
sumsum = []
max = 0

with open('doc.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]
    for i in range(len(calories)):
        if calories[i] != '':
            sum = sum + int(calories[i])
        else:
            sumsum.append(sum)
            sum=0

    sumsum.append(sum)
    i=+1

    for i in range(len(sumsum)):
        if max < sumsum[i]:
            max = sumsum[i]
    print(max)
    sumsum.remove(max)
    sumsum2 = sumsum

    max = 0

    for i in range(len(sumsum2)):
        if max < sumsum2[i]:
            max = sumsum2[i]
    print(max)
    sumsum2.remove(max)
    sumsum3 = sumsum2

    max = 0

    for i in range (len(sumsum3)):
        if max < sumsum3[i]:
            max = sumsum3[i]
    print(max)
