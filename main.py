from operator import add

square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1

def __main__():
    print("lol")
    accumulate(add, 0, 5, identity)

def accumulate(combiner, base, n, term):
    to_return = 0
    nums = [base]
    if n > 1:
        for num in range(1, n + 1):
            nums.append(num)
    else:
        return base
    print(str(nums))
    while len(nums) > 1:
        fst = nums.pop(0)
        snd = nums.pop(0)
        print(fst, snd)
        to_return += combiner(term(fst), term(snd))
        print(to_return)
    return to_return

print(accumulate(add, 0, 5, identity))