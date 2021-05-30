def helper(s,i):
    l=len(s)
    s1=""
    for i in range(i,l):
        if(s[i].isdigit()):
            s1+=s[i]
        else:
            break
            
    if s1=="":
        s1=0

    n=int(s1)

    if s[0]=='-':
        n=-n
        
    if n<(-2)**31:
        return (-2)**31
    elif (2**31)-1<=n:
        return (2**31)-1
        #clamp the integer
    else:
        return n


def myAtoi_optimisation_1(s) -> int:
    s=s.lstrip() #Step-1

    l=len(s)

    if l==0:
        return 0
    else:
        s1=""
        #while l>0:
        if not(s[0].isdigit() or s[0]=='-' or s[0]=='+'):
            return 0
        elif s[0]=='-' or s[0]=='+':
            res=helper(s,1)
        elif s[0].isdigit():
            res=helper(s,0)

        return res
        

if __name__=="__main__":
    print(myAtoi_optimisation_1("42")) # 42
    print(myAtoi_optimisation_1("-42")) # -42
    print(myAtoi_optimisation_1("4193 with words")) # 4193
    print(myAtoi_optimisation_1("words and 987")) # 0
    print(myAtoi_optimisation_1("-91283472332")) # -2147483648
    print(myAtoi_optimisation_1("3.14159")) # 3
    print(myAtoi_optimisation_1(".1")) # 0
    print(myAtoi_optimisation_1("21474836460")) # 2147483647
    print(myAtoi_optimisation_1("+-12")) # 0
