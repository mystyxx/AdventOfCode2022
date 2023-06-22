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

