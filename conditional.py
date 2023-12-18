import csv
a= []
with open("hello.csv","r") as csvfile:
    next(csvfile)
    for row in csv.reader(csvfile):
        a.append(row)
total_tr = len(a)
golf = 0
sgmr = 0
mr = 0
for i in range(len(a)):
    if(a[i][1]=='golf'):
        golf+=1
for i in range(len(a)):
    if(a[i][3]=='single' and a[i][6]=='medRisk'):
        sgmr+=1

for i in range(len(a)):
    if(a[i][6]=='medRisk'):
        mr+=1

print("Probability of golf = ", end="")
print(golf/total_tr)
print("Probability of single and med risk = ", end=" ")
print(sgmr/total_tr)
print("Probability of medrisk = ", end=" ")
print(mr/total_tr)
print("Probability of single given medrisk = ", end=" ")
print(sgmr/mr)
