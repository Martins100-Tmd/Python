#Comibination 
#nCr = n!/(n-r)! r!
#Combination - function
#@n - substitute for n in the combination formula
#@r - substitute for r in the combination formula
def Combination(n, r):
    sum=1
    diff=1
    R=1
    for i in range(n):
        sum*=(n-i)
    n_r = n-r
    for i in range(n_r):
        diff*=(n_r-i)
    for i in range(r):
        R*=(r-i)
    Upper_sequence_value=sum
    Lower_sequence_value=diff * R
    combination_Result=Upper_sequence_value/Lower_sequence_value
    return combination_Result
print(Combination(8,3))
    