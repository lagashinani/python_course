file_names = ["1.txt", "2.txt"]
result_file = "3.txt"

files = []

for file_name in file_names:
    with open(file_name) as i:
        files.append((i.readlines(), file_name))

files = sorted(files, key=lambda x: len(x[0]))

with open(result_file, "w") as o:
    for file in files:
        print(file[1], file=o)
        print(len(file[0]), file=o)
        print("".join(file[0]), file=o)