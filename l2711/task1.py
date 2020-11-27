nl = []
for x in range(1500, 2701):
    if x % 35 == 0:
        nl.append(str(x))

print(', '.join(nl))