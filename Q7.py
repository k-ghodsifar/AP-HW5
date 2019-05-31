[print(j,end=' ') for j in sorted([eval(i) for i in input().split()[5::6] if eval(i)%6==0])]
