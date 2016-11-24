import os

root = '/Users/hb'
a = os.listdir(root)
print a

for b in (a):
    c = os.path.join(root,b)
    if os.path.isdir(c):
        print 'Directory', c
    else:
        print c

