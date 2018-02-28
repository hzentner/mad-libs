mad_libs = open("example.txt", "r")
mad_libs_str = mad_libs.read()
words = mad_libs_str.split(" ")
final_string = ""
 
for i in range (0, len(words)):
