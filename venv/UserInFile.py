def write_read_lines(self):
    write_read = open('newfile.txt', "w")
    write_read.write(str(list))
    write_read.close()
    # read_files = open('newfile.txt', "r")
    # print(read_files.readlines())
    return read_files