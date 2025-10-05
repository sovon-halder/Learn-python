
def rem(l, word):
    for item in l:
         l.remove(word)
         return l


l=["sovon","rohit","subha","nekhil"]

print(rem(l,"sovon"))