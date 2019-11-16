try:
    f1=open("does.txt")

except EOFError as e:
    print(e)

except IOError as e:
    print("Io Exception",e)

else:
    print("execute only if except block is not executed")

finally:
    print("run anyways")
    try:
        f1.close()
    except Exception as e:
        print("file not openend",e)

print("Important stuff")