#Excercise-1: create a dictionary , take input from user and fetch its meaning

oxfordDict={"set":"collection of all data",
            "glad":"Happy",
            "Awesome":"Amazing",
            "Dustbin":"thing which is removable",
            "criteria":"Minimum Limit"}

print("Enter the word you have to search its meaning=")
word=input()

print("you have search word", word, "and its meaning is",
      oxfordDict[word])