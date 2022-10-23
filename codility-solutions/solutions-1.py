def cost(scooter, sand):
    costs = [[20, 30], [5, 40]]
    return costs[scooter][sand]

def solution(R):
    n = len(R)
    ans = n*100

    for s in range(n+1):
        c = 0
        for i in range(n):
            c += cost(i < s, R[i] == 'S')
        ans = min(ans, c)
    
    return ans

assert solution('ASAASS')==115
assert solution('SSA')==80
assert solution('SSSSAAA')==175
