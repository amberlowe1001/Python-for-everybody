<<<<<<< Updated upstream
fname = input("mbox.txt ")
=======
fname = input("Enter file name: ")
>>>>>>> Stashed changes
if len(fname) < 1 : fname = "mbox.txt"
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From:"): continue
    line = line.strip().split()
    print(line[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
