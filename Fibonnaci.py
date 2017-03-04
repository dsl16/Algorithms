# Uses python3
"""
Created on Fri Mar  3 17:17:03 2017

@author: Darrin Lim
"""

import time

def clock(function,*args):
    t1 = time.time()
    answer = function(*args)
    t = time.time() - t1
    return answer, t

def calc_fib(n):
    if n <= 1:
        return n
    a = 0; b = 1;
    for i in range(n-1):
        answer = a + b;
        a = b;
        b = answer;

    return answer

if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))