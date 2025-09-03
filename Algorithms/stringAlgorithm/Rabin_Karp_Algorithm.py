# 🔹 Rabin-Karp Algorithm (Simple Explanation)
    # Purpose: Find all occurrences of a pattern in a text using hashing.
# Idea:
    # Instead of comparing the pattern with every substring, we compare hash values.
    # If the hash matches, then we check the substring to avoid collisions.
    # We use rolling hash to update the hash in O(1) when sliding the window.
# 🔹 Steps
    # Compute hash of the pattern.
    # Compute hash of the first window of the text (same length as pattern).
    # Slide the window one character at a time:
    # If hash matches → compare substring to pattern.
    # Else → move window and update hash using rolling hash formula.
mod=10**9+7
def find_HashValue(pat):
    factor=1
    ans=0
    rabin=26
    for i in range(len(pat)-1,-1,-1):
        ans+=((ord(pat[i])-ord('a'))*factor)%mod
        factor=(factor*rabin)%mod
    return ans%mod
    
def rabin_Karp(text,pattern):
    patternHash=find_HashValue(pattern)
    textHash=0
    factor=1
    rabin=26
    Constant=(26**len(pattern))%mod
    left=0
    right=0
    for i in range(len(pattern)-1,-1,-1):
        textHash+=((ord(text[i])-ord('a'))*factor)%mod
        factor=(factor*rabin)%mod
        right+=1
    textHash=textHash%mod
    if textHash==patternHash:
            print("Find at index ",left)
    while right<len(text):
        textHash=(textHash*rabin-(ord(text[left])-ord('a'))*Constant+(ord(text[right])-ord('a')))%mod
        left+=1
        right+=1
        if textHash==patternHash:
            print("Find at index ",left)
rabin_Karp("ababab","abab")
        