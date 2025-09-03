def generateLPS(pattern):
    lps=[0]*len(pattern)
    length=0
    i=1
    while i<len(pattern):
        if pattern[i]==pattern[length]:
            length+=1
            lps[i]=length
            i+=1
        else:
            if length!=0:
                length=lps[length-1]
            else:
                i+=1
    return lps
def lps(text,pattern):
    Lps=generateLPS(pattern)
    i=0
    j=0
    while i<len(text):
        if text[i]==pattern[j]:
            i+=1
            j+=1
        if j==len(pattern):
           print("pattern Found At :",i-j)
           j=Lps[j-1]
        elif text[i]!=pattern[j]:
            if j!=0:
                j=Lps[j-1]
            else:
                i+=1
lps('ABABABAB',"ABAB")
            
    