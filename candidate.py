import pandas as pd     
data = pd.read_csv('es.csv')
instance = data.drop(columns=['enjoy_sport']).values.tolist()
target = data['enjoy_sport'].values.tolist()
sh = ['null']*len(instance[0])
gh=[['?']*len(instance[0]) for _ in range(len(instance[0]))]

i = 0
while i < len(instance):
    if target[i] == "yes":
        if 'null' in sh:
            sh = instance[i].copy()
        else:
            for x in range(len(sh)):
                if sh[x]!=instance[i][x]:
                    sh[x]= '?'
    else:
        for x in range(len(instance[0])):
            if instance[i][x]!=sh[x]:
                gh[x][x]=sh[x]

    i+=1
for x in range(len(instance[0])):
    if gh[x][x]!=sh[x]:
        gh[x][x] = '?'
for x in range(len(instance[0])):
    if gh[x][x]!='?':
        for y in range(len(instance[0])):
            if y!=x:
                gh[x][y]= '?'
print("Final Output: ")
print("\n Specific Hypothesis")
print(sh)
print("\n General Hypothesis")
for a in gh:
    flag = 0
    for s in a :
        if s!='?':
            flag =1
            break
    if flag == 1:
        print(a)
