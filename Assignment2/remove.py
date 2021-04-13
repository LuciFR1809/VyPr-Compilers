import os
import sys
def remove():
    fname = sys.argv[1]
    fd=open(fname,"r")
    d=fd.read()
    fd.close()
    m=d.split("\n")
    s="\n".join(m[:-1])
    fd=open(fname,"w+")
    for i in range(len(s)):
        fd.write(s[i])
    fd.close()
if __name__ == '__main__':
	remove()