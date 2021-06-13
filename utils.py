def write_to_file(path, output):
    f = open(path + "/output.txt", "w")
    file = open(path + "/output.txt", "a")
    for i in range(1, len(output) + 1):
        file.write(str(i) + " " + str(output[i - 1]) + "\n")
    pass
