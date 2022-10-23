def cost(scooter, sand):
    costs = [[20, 30], [5, 40]]
    return costs[scooter][sand]

def solution(R):
    n = len(R)
    foot = [0] * (n+1)
    for i in range(n-1, -1, -1):
        foot[i] = foot[i+1] + cost(False, R[i] == 'S')

    ans = foot[0]
    c = 0
    for i in range(n):
        c += cost(True, R[i] == 'S')
        ans = min(ans, c + foot[i+1])
    return ans

assert solution('ASAASS')==115
assert solution('SSA')==80
assert solution('SSSSAAA')==175
