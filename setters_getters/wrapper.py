import time
def say_main(func):

    def wrapper(*args):
        print("TIME", time.time())
        func(*args)
        print("End wrapper!")
    return wrapper


@say_main
def say_words(*args):
    print(sum(args))

say_words(1, 2, 5)