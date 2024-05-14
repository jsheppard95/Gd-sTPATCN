FNAME = "sim-1bar/COLVAR"

time = []
Rg = []
alpha = []
abeta = []
pbeta = []
sasar = []
with open(FNAME, "r") as f:
    while True:
        f.readline()  # header line
        line = f.readline().split(" ")
        if line == "EOF":
            break
        print(line)
        time.append(line[1])
        Rg.append(line[2])
        alpha.append(line[3])
        abeta.append(line[4])
        pbeta.append(line[5])
        if FNAME != "sim-1bar/COLVAR":
            sasar.append(line[6])

print(time)