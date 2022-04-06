def solution(s):
    dp_odd=[0 for _ in range(len(s))]
    dp_even=[0 for _ in range(len(s))]
    for standard1 in range(len(s)):
        i=1
        result=1
        check=True
        while True:
            if standard1-i<0:
                dp_odd[standard1]=result
                break
            if standard1+i==len(s):
                dp_odd[standard1]=result
                break
            if s[standard1-i]==s[standard1+i]:
                result+=2
            else:
                dp_odd[standard1]=result
                break
            i+=1
        
    
    for standard2 in range(len(s)-1):
        i=1
        if s[standard2]==s[standard2+1]:
            result=2
        else:
            continue
        while True:
            if standard2-i<0:
                dp_even[standard2]=result
                break
            if standard2+1+i==len(s):
                dp_even[standard2]=result
                break
            if s[standard2-i]==s[standard2+1+i]:
                result+=2
            else:
                
                dp_even[standard2]=result
                break
            i+=1
    else:
        return max(max(dp_odd),max(dp_even))
