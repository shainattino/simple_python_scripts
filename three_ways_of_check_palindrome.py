import os
import time
def compare(word):
    if (len(word)==1):
        return False
    for i in range(int(len(word)/2)):
        if word[i]!=word[0-1-i]:
            return False
    return True

def compare2(word):
    if word==reversed(word):
        return 1
    return 0

def compare3(word):
    if word==word[::-1]:
        return 1
    return 0


def test(function):
    path="/Users/shaina"
    start=time.time()
    for root,dirs,files in os.walk(path):
        for file in files:
            name, ext=os.path.splitext(file)
            if function(name):
                print(name)
    end=time.time()
    return("%.1f"%(end-start))

l=[]
l.append(test(compare))
l.append(test(compare2))
l.append(test(compare3))
print(l)