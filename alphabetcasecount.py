word=input("enter the word: ")
upper=word.upper()
lower=word.lower()
upper_count=0
lower_count=0
for le in word:
    if le in upper:
        upper_count+=1
    else:
        lower_count+=1
print(f'upper case letters: {upper_count}')
print(f'lower case letters: {lower_count}')




