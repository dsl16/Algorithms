# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_standard(n,m):
    if n <= 1:
        return n
    
    previous = 0
    current  = 1
    
    whole = [0,1]; copy = []; j = 0;
    for i in range(n - 1):
        previous, current = current % m, (previous + current) % m
        whole.append(current)
        if (whole[j] == current) & (j == 0):
            copy.append(current)
            start = i
            j += 1
        elif (whole[j] == current):
            copy.append(current)
            j += 1
        else:
            copy = [];
            j = 0;
        if j == start:
            break
    return current
    
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
