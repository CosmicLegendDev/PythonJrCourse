# Reading file line by line.
my_bio_file = open("my_bio.txt", "r")
is_continue = True
while(is_continue):
    line = my_bio_file.readline()
    if line:
        print(line)
    else:
        is_continue = False

my_bio_file.close()