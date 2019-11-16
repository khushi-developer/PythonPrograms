# def searcher():
#     import time
#     book="This is book on harry and code with harry and good"
#     time.sleep(4)# 4 sec time consuming task
#
#     while True:
#         text = (yield)
#         if text in book:
#             print("Your text in the book")
#         else:
#             print("Text not in the book")
#
# search = searcher()
# print("search started")
# next(search)
# print("next method run")
# search.send("harry")
# input("press any key")
# search.send("harry and")
# search.send("this and")
# search.send("that")
# search.close()
# print("closed")

print("==========================================================================================")

def Dea():
    book="This is khushi and khushi is the owner of vthe multinational company and khushi " \
         "is the best rapper nd she is too famous she is also expert in computer"
    import time
    time.sleep(3)

    while True:
        text=(yield)
        if text in book:
            print("name is present")
        else:
            print("name is not present")

D=Dea()
print("reading started")
next(D)
print("next method run")
D.send("khushi")