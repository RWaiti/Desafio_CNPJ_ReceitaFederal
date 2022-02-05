f = open("encoders.txt", "r")
lines = f.read().splitlines()
print(lines, len(lines))
f.close()

f = open("index.txt", "r", encoding="utf8")
lines = f.read().splitlines()
for i in range(len(lines)):
    lines[i] = lines[i].lower()
print(lines, len(lines))
f.close()