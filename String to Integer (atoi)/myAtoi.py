def myAtoi(s: str) -> int:

    """Return the value of myAtoi function, as in C and C++.

        >>> print(myAtoi("42"))
        42
        >>> print(myAtoi("  42"))
        42
        >>> print(myAtoi("+-12"))
        0
        >>> print(myAtoi("+"))
        0
        >>> print(myAtoi("  "))
        0
        """        


    if s=='':
        return 0
    if len(s)==1 and not s.isdigit():
        return 0
    
    n=''
    for i in range(len(s)):
        if s[i]==' ':
            while i<len(s) and s[i]==' ':
                i+=1
            if i==len(s):
                return 0
                
        if s[i] not in "+-" and not s[i].isdigit():
            return 0
            
        elif s[i]=='-':
            i+=1
            if not s[i].isdigit():
                return 0
            else:
                while i<len(s) and s[i].isdigit():
                    n+=s[i]
                    i+=1
                y=int(n)
                y=y-(2*y)
                if y<=-2**31:
                    return -2**31
                elif y>(2**31)-1:
                    return (2**31)-1
                else:
                    return y
                    
        elif s[i]=='+':
            i+=1
            if not s[i].isdigit():
                return 0
            else:
                while i<len(s) and s[i].isdigit():
                    n+=s[i]
                    i+=1
                y=int(n)
                if y<=-2**31:
                    return -2**31
                elif y>(2**31)-1:
                    return (2**31)-1
                else:
                    return y
                    
        else:
            while i<len(s) and s[i].isdigit():
                n+=s[i]
                i+=1
            y=int(n)
            if y<=-2**31:
                return -2**31
            elif y>(2**31)-1:
                return (2**31)-1
            else:
                return y



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    
