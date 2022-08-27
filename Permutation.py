#Comibination 
#nCr = n!/(n-r)! r!
#Permutation - function
#@n - substitute for n in the combination formula
#@r - substitute for r in the combination formula
def Permutation(n, r):
    sum=1
    R=1
    for i in range(n):
        sum*=(n-i)
    for i in range(r):
        R*=(r-i)
    permutation_Result=sum/R
    return permutation_Result
print(Permutation(7,3))