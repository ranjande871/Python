#TestList = ["element1","element2","element3"]

#TestList = [0,1,2]

Scores = [70,80,90,67.5,95]
#print(Scores)
print(Scores[0])
print(Scores[1])
print(Scores[-1])
print(Scores[-2])


print(Scores[0:3])
print(Scores[1:3])
print(Scores[2:])

Scores[0] = 75
print(Scores)
Scores[1:3] = []
print(Scores)

Scores.append(82)
print(Scores)



