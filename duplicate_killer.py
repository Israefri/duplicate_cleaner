import hashlib
print("""
           ###########    #          ###  #           #
           # XX   XX #    #     ##    #   #           #
           #    #    #    #   ##      #   #           #
           #    #    #    ###         #   #           #
           #---------#    #  ##       #   #           #
           ###########    #   ##     ###  ##########  ##########
          """)
output_path = input("Please enter the name of the new clean file")
input_path = input ("Please enter the input FULL path")
hash_lines = set()
output_file = open(output_path, "w")
for line in open (input_path,"r"):
    hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
    if hashValue not in hash_lines:
        output_file.write(line)
        hash_lines.add(hashValue)
output_file.close()
