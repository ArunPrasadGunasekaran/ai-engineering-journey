def add(a,b,c):
    return a+b+c
def average(a,b):
   return a/b
def rank(a):
   if a>= 90:
       return 'A'
   elif 75 <= a <= 89:
       return 'B'
   elif 60 <= a <= 74:
       return 'C'
   elif 50 <= a <= 59:
       return 'D'
   else:
       return 'F'
