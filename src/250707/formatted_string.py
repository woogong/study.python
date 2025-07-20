import math

print(f"the value of PI is approximately {math.pi:.8f}")

table = {'Dongun': 2007, "Yeongun": 2009, "Goeun": 2012}
for name, year in table.items():
    print(f"{name:8} : {year:5}")

height = "177.2(cm)"
weight = "67(kg)"
name = "Woogong"
print(f"{name=} {height=} {weight=}")