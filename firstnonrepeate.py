word=input("enter the word: ")
dict1={}

for le in word:
    if le in dict1:
        dict1[le]+=1
    else:
        dict1[le]=1
for le in word:
    if dict1[le]==1:
        print(le)
        break
