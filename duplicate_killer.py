import hashlib
print("""
           ###########    #          ###  #           #
           # XX   XX #    #     ##    #   #           #
           #    #    #    #   ##      #   #           #
           #    #    #    ###         #   #           #
           #---------#    #  ##       #   #           #
           ###########    #   ##     ###  ##########  ##########
          """)
output_path = input("Please enter the name of the new clean file: ")
input_path = input("Please enter the input FULL path: ")
hash_lines = set()
#opens the new file with the given name.
output_file = open(output_path, "w")
#running through the lines of the file
for line in open (input_path,"r"):
    #hashing
    hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
    #checking the set
    if hashValue not in hash_lines:
        output_file.write(line)
        hash_lines.add(hashValue)
output_file.close()
