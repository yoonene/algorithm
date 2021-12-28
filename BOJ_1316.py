N = int(input())
result = 0

for i in range(N):
    word = input()
    sorted_word = sorted(word, key=word.find)
    if sorted_word == list(word):
        result+=1
        
result

# sorted(word, key=word.find) : ex) (A,C,C,B,A) -> (A,A,B,C,C)
