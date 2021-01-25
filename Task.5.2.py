import sys
print('Number of comamnd line args are : ',len(sys.argv))
print('Arguments are : ',str(sys.argv)) #argv[0] will be scrpt name, argv[1] will be the file name
try:
    fr = open(sys.argv[1]) #the default mode is read mode 'r'
except FileNotFoundError:
    print('file ', sys.argv[1],' doesnt exist')
else:
    print(sys.argv[1],' contents are')
    print(fr.read())