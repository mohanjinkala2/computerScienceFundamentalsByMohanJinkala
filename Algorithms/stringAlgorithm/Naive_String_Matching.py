#🔹Problem
    # We’re given:
    # Text (T) of length n
    # Pattern (P) of length m
    # We want to find all occurrences of P inside T.
#🔹Example
    # Text:
    # T = "ABABABAB"
    # Pattern:
    # P = "ABAB"
    # Shifts:(Explanation)
        # s=0 → T[0:4] = "ABAB" ✅ match
        # s=1 → T[1:5] = "BABA" ❌ no
        # s=2 → T[2:6] = "ABAB" ✅ match
        # s=3 → T[3:7] = "BABA" ❌ no
        # s=4 → T[4:8] = "ABAB" ✅ match
        # So matches at indices [0,2,4].
T="ABABABAB"
P="ABAB"
# this is Normal
# def Naive_String_Matching(s1,s2):
#     i=0
#     j=len(s2)-1
#     while j<len(s1):
#         if s1[i:j+1]==s2:
#             print("Pattern found at index", i)  
#         j+=1
#         i+=1
#using pure coding
def Naive_String_Matching(s1,s2):
    for i in range(len(s1)-len(s2)+1):#Time complexity is O((len(s1)-len(s2)+1)*len(s2))
        j=0
        while j<len(s2) and s1[i+j]==s2[j]:
            j+=1
        if j==len(s2):
            print("Pattern found at index", i)   
Naive_String_Matching(T,P)
    