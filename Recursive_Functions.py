import os
def r(p):
    if os.path.isdir(p):
        print 'directory', p
        content = os.listdir(p)
        for a in content:
            r(os.path.join(p,a))

    else:
        print 'file', p

root = '/Users/hb'
r(root)