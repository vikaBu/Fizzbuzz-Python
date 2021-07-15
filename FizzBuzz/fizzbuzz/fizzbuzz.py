import time


def fizzbuzz(start, end):
    def int_to_fizzbuzz(i):
        entry = ''
        if i%3 == 0:
            yield "fizz"
        if i%5 == 0:
            yield "buzz"
        if i%3 != 0 and i%5 != 0:
            yield "fizzbuzz"

    yield (int_to_fizzbuzz(i) for i in range(start, end+1))



if __name__ == "__main__":
    start = int(input("Start Value:"))
    end = int(input("End Value:"))
    for i in fizzbuzz (start, end):
        print (list(i))
