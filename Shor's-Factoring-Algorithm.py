import random
import math
'''
Author: ジョシュアモル
Date: January, 10, 2020
Contact: devr4ndom@gmail.com
Version: 1.0
'''
def find_Period (g, minimum, N):
    match = pow(g, 1) % N
    print("[INFO]\tN = %d, g = %d, Searching for modulus matching: %d" % (N, g, match))
    for x in range(minimum, N):
        searching = pow(g, x) % N
        
        if searching == match:
            print("[Found]\t%d^%d %% %d = %d" % (g, x, N, searching))
            return x-1
    return -1

def calc_GCD(a, b, N):
    p = math.gcd(a, N)
    q = math.gcd(b, N)
    if p < 2:
        print("[INFO]\tIssues discovered with deriving GCD(a,N)\n[INFO]\tAttempting to resolve...")
        if q > 1 and q < N:
            p = N / q
            print("[Success]\tResolved discoved issue with deriving GCD(a,N)")
        else:
            p = -1
            print("[FAILED] Unable to solve issue deriving GCD(a,N)")
    elif q < 2:
        print("[INFO]\tIssues discovered with deriving GCD(b,N)\n[INFO]\tAttempting to resolve...")
        if p > 1 and p < N:
            q = N / p
            print("[Success]\tResolved discoved issue with deriving GCD(b,N)")
        else:
            q = -1
            print("[FAILED] Unable to solve issue deriving GCD(b,N)")
    return p, q

def return_Factor(t, N):
    if t == -1:
        print("[ERROR]\tUnable to find Period")
        return 0, 0
    elif t % 2 == 1:
        print("[ERROR]\tPeriod is odd, Unable to calculate a or b")
        return 0, 0
    e = t/2
    print("[INFO]\tt = %d, e = %d" % (t, e))
    a = pow(int(g), int(e), int(N))
    b = pow(int(g), int(e), int(N))
    a -= 1
    b += 1
    print("[INFO]\ta = %d, b = %d" % (a, b))
    p, q = calc_GCD(int(a), int(b), N)
    return p, q

'''
START OF PROGRAM:
'''
N = 221
minimum = 2
maximum = N-1
'''
Automation of guessing process 
'''
g = random.randint(minimum, maximum)

print("[INFO]\tguess: " + str(g))
t = find_Period(g, minimum, N)
p, q = return_Factor(t, N)
if p * q == N:
    print("[Success]\tp = %d, q = %d,  p * q = %d" % (p, q, p * q))
else:
    print("[ERROR]\tUnsuccessful Factoring")
    
