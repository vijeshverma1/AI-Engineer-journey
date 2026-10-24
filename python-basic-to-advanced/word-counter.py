word=input("Enter your sentance : ")
count=0
for ch in word:
    if(ch==" "):
        continue;
    else:
        count+=1
# print(count);
sentance=word.split()
print(f"the count of words in sentance {len(sentance)} and the numbers of letter in this sentence is {(count)}")