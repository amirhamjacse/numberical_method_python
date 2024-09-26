x = [5,6,9,11]
y = [12,13,14,16]

itaration = len(x)
xp = 10
result = 0

for i in range(itaration):
    term = y[i]
    for j in range(itaration):
        if i!=j:
            term = term*(xp-x[j])/(x[i]-x[j])
    result+=term
print("result: ",result)
