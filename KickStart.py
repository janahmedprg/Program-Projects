import collections
T = input()
T = int(T)
for t in range(0,T):
    cases = 0
    row1 = input()
    row2 = input()
    row3 = input()
    g = []
    row2 = row2.split()
    row2.insert(1,0)
    g.append(row1.split())
    g.append(row2)
    g.append(row3.split())
    for i in range(0,3):
        for j in range(0,3):
            g[i][j] = int(g[i][j])
    lst = []
    if (g[0][0] + g[2][2])%2==0:
        lst.append(g[0][0] + g[2][2])
    if (g[2][0]+g[0][2])%2==0:
        lst.append(g[2][0]+g[0][2])
    if (g[1][0]+g[1][2])%2==0:
        lst.append(g[1][0]+g[1][2])
    if (g[0][1]+g[2][1])%2 == 0:
        lst.append(g[0][1]+g[2][1])
    if len(lst) != 0:
        occurrences = collections.Counter(lst)
        all_values = occurrences.values()
        max_value = max(all_values)
        for k, v in occurrences.items():
            if v == max_value:
                g[1][1] = int(k/2)
                break
    for i in range(0,3):
        if 2*g[i][1] - g[i][0] == g[i][2]:
            cases += 1
    for j in range(0,3):
        if 2*g[1][j] - g[0][j] == g[2][j]:
            cases += 1
    if 2*g[1][1] - g[0][0] == g[2][2]:
        cases += 1
    if 2*g[1][1] - g[0][2] == g[2][0]:
        cases += 1
    print('Case #'+str(t+1)+': '+ str(cases))
