# Problem: B - Distinct Digits - https://codeforces.com/gym/530187/problem/B

import sys
import threading
from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()

setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

def main():
    for _ in range(int(input())):
        n = int(input())
        ans = float('inf')
        
        def gen(sum, num, start):
            nonlocal ans
            if sum == n:
                ans = min(ans, int(num))
                return
            if sum > n:
                return
            
            for digit in range(start, 10):
                gen(sum + digit, num + str(digit), digit + 1)
        
        gen(0, "", 1)
        print(ans)



main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

