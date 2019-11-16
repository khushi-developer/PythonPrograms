from functools import lru_cache
import time
@lru_cache(maxsize=3) #3 means how much recent time delay save ,here we are saving maximum 3 latest value
def somework(n):
    time.sleep(n)#some task takes n time
    return n

if __name__ == '__main__':
    print("now running some work")
    somework(5)
    print("done....calling again")
    somework(5)
    print("called again")


