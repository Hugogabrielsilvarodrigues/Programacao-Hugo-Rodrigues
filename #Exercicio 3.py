#Exercicio 3
smallestword = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
biggestword = "a"
words = ["computer","peanut","rapture","salamander","hippopotamus"]
for word in words:
    if len(word) < len(smallestword) :
        smallestword = word
    if len(word) > len(biggestword) :
        biggestword = word
print ("maior palavra: ", biggestword)
print ("menor palavra: ", smallestword)

