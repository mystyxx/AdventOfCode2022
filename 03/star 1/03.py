from collections import *
import string

answer = 0
res_first, res_second = [], []
lettersInCommon, lettervalue = [], []


for letter in string.ascii_lowercase:
    lettervalue.append(letter)
for letter in string.ascii_uppercase:
    lettervalue.append(letter)

with open('doc.txt') as f:
    file_content = f.read()
    rucksacks = [i.replace(" ", "") for i in file_content.split("\n")] 

#separer chaque partie du sac a dos
    for i in range(len(rucksacks)):
        res_first.append(rucksacks[i][:len(rucksacks[i])//2])
        res_second.append(rucksacks[i][len(rucksacks[i])//2:])

#mettre tout les caracteres dans les deux parties dans une liste
    for i in range(len(res_first)):
        for j in range(len(res_first[i])):
            if res_first[i][j] in res_second[i]:
                lettersInCommon.append(res_first[i][j])
                break

#calculer la somme des valeurs des caracteres en commun
    for i in range(len(lettersInCommon)):
        answer += lettervalue.index(lettersInCommon[i])+1
    print(answer)
