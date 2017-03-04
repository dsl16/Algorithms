# Uses python3
import sys

def gcd_standard(a,b):
    large = max([a,b])
    small = min([a,b])
    while large%small != 0:
        remain = large%small;
        large = small;
        small = remain;
    return small

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_standard(a,b):
    gcd = gcd_standard(a,b)
    
    return int(a*b/int(gcd))

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_standard(a, b))