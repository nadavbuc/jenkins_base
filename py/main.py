import sys
if sys.argv[1] <= '2':
    if sys.argv[1] == '2':
        print ("Jenkins job name: " + str(sys.argv[2]))
    else:
        print (sys.argv[1])
        print (sys.argv[2])
        abc
elif sys.argv[1] > '3':
    if (int(sys.argv[1]) + 1) % '3' == '0':
        print ("Jenkins job name: " + str(sys.argv[2]))
else:
    print (sys.argv[1])
    print (sys.argv[2])