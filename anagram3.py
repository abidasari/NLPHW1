#!/usr/bin/python
import sys
import math


fo = open("anagram_out.txt" , "w")
# out_list = []

def permute(prefix , str):
        n = len(str)
        if(n == 0):

            fo.write(prefix + "\n")
            return
            # print(prefix)
        else:
            for i in range(0,n):
                permute( prefix + str[i] , str[0:i] + str[i+1:n])

print (math.log(333))

input = str(sys.argv[1])
# print ("input: " + input)
string = ''.join(sorted(input))
# print ("string : " + string)
permute( prefix = "" , str = string)

# fo.writelines( out_list)

fo.close()
