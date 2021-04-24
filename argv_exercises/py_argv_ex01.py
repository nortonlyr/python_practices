import sys

print("This is the name of the program: ", sys.argv[0])
print("Number of elements inlcuding the name of the program: ", len(sys.argv))
print("Number of elements excluding he name of the program: ", (len(sys.argv)-1))
print("Argument List: ", str(sys.argv))