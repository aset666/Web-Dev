"""
def solve(grams):
    ounces = grams / 28.3495231
    return ounces
    
grams = int(input())
print(solve(grams))
    """
    
def solve(far):
    c = (5 / 9) * (far - 32)
    return c

far = int(input())
print(solve(far))

def solve(numh, numl):
    for i in range(numh + 1):
        j = numh - i
        if 2 * j + 4 * i == numl:
            return i, j
    
numh, numl = int(input()), int(input())
print(solve(numh, numl))

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num%2 == 0:
        return False


    i = 3
    while i*i < num:
        if num%i == 0:
            return False
        i+=2
    return True

def filter_prime(nums: list[int]) -> list[int]:
    res = []
    for _ in nums:
        if is_prime(_): res.append(_)
    return res

running = 1

while running:
    try:
        l = map(int, input("Enter nums: ").split())
        t = filter_prime(l)
        print(t)
    except Exception as ex:
        break
    
from itertools import permutations

def solve(s):
    perm = permutations(s)
    
    for p in perm:
        print(''.join(p))
        
s = input()
solve(s)

def solve(s):
    w = s.split()
    ans = w[::-1]
    return ' '.join(ans)
    
s = input()
print(solve(s))

a = list(map(int, input().split()))
ok = False
for i in range(len(a) - 1):
    if a[i] == 3 and a[i + 1] == 3:
        ok = True
        break
print(ok)

def solve(a):
    ok = False
    for i in range(len(a) - 2):
        if a[i] == 0:
            if a[i + 1] == 0:
                if a[i + 2] == 7:
                    ok = True
                    break
    return ok
a = list(map(int, input().split()))
print(solve(a))

import math
def solve(r):
    ans = (4 / 3) * math.pi * r ** 3
    return ans
r = float(input())
print(solve(r))

def solve(a):
    ans = []
    for i in a:
        if i not in ans:
            ans.append(i)
    return ans

a = input().split()
print(solve(a))

def solve(s):
    ok = True
    for i in range((len(s) + 1) // 2):
        if s[i] != s[len(s) - 1 - i]:
            ok = False
            break
    return ok
s = input()
solve(s)
if solve(s) == True:
    print("Palindrome")
else:
    print("Not Palindrome")
    
    def solve(a):
        for i in range(a):
            print('*', end = "")
a = list(map(int, input().split()))
for i in a:
    solve(i)
    print()