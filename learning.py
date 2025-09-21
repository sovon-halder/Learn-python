s="money is power"
s2="love is everything"
s3="click here"
massage=input("enter your comment: ")
if((s in massage) or (s2 in massage) or (s3 in massage)):
    print("this is spam")
else:
    print("this is valid,you can go")
