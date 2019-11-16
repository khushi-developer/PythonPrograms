#search Engine
#
# lis=["This is as good","python is as good as sneak","you have to learn python"]
# inp=input("Enter the String you have to search")
# matching=[s for s in lis if inp in s]
# print(matching)

def matchinwords(sentence1,sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == '__main__':
    # print(matchinwords("This is good" , "python is is good"))

    sentences = ["python is a good","This is snake","Harry is a good boy","Subscribe to code with harry"]
    query = input("Please enter the input string")
    scores = [matchinwords(query, sentence) for sentence in sentences]
    # print(scores)

    sortedSentScores = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True)]
    # print(sortedSentScores)

    print(f"{len(sortedSentScores)} results found!")
    for score, item in sortedSentScores:
        print(f"\"{item}\": with a score of {score}")
