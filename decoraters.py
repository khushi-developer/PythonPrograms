def dec(fun):
    def nowexec():
        print("This is decorater")
        fun()
        print("Executing")
    return nowexec()

@dec
def gon():
    print("this is gon")


# =======================================================
# def function1():
#     print("this is multinational owner khushi")
#
# func2=function1
# func2()

# =========================================================
#
# def func1(num):
#     if num==1:
#         return sum
#     if num==0:
#         return int
# print(func1(0))

# ===========================================================

# def func1(func2):
#     func2("This is me")
#
#
# func1(print)