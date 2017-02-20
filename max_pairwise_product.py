# Uses python3

import numpy as np

def Slow_Sure_Solution(a):
    values = []
    a = np.array(a)
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j:
                values.append(a[i]*a[j])
            else:
                values.append(0)
    return(np.array(values).max())
    
def Fast_Experimental_Solution(a):
    a = np.array(a)
    result = np.array(a).max()*np.delete(a,a.argmax()).max()
    return result

# Std Output
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

print(Fast_Experimental_Solution(a))

'''
# Stress Test
while True:
    n = np.random.randint(2,10)
    a = np.random.randint(0,1000,size=n)
    if Slow_Sure_Solution(a) != Fast_Experimental_Solution(a):
        print(a)
        print(Slow_Sure_Solution(a))
        print(Fast_Experimental_Solution(a))
        break
    else:
        print('OK')
'''