score = 0

with open('doc.txt') as f:
    file_content = f.read().strip()

if file_content:
    rounds = [i.replace(" ", "") for i in file_content.split("\n")]
else:
    rounds = []
print(len(rounds))
for i in range(len(rounds)):
    if rounds[i][1] == 'X':
        if rounds[i][0] == 'A':
               score += 4
        if rounds[i][0] == 'B':
               score += 1
        if rounds[i][0] == 'C':
               score += 7
    if rounds[i][1] == 'Y':
        if rounds[i][0] == 'A':
            score += 8
        if rounds[i][0] == 'B':
               score += 5
        if rounds[i][0] == 'C':
               score += 2
    if rounds[i][1] == 'Z':
        if rounds[i][0] == 'A':
               score += 3
        if rounds[i][0] == 'B':
               score += 9
        if rounds[i][0] == 'C':
               score += 6
print(score)
