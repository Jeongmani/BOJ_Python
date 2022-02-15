N=int(input())                      #N을 입력받는다.

def divide_sum(x):
    K=x                             #x를 임시적으로 저장할 K를 선언한다.  
    for i in range(len(str(x))):    #x를 문자열(str)로 바꾸고 K에 한자리씩 더한다
        K+=int(str(x)[i])

    if K==N:                        #실행한 결과가 N과 같다면 그 수는 N의 생성자이다.
        return x
    else:                           #그 수의 생성자가 아니라면 None를 리턴한다.
        return None
i=1
while True:                         #i를 1씩 증가시키며 확인한다.
    if divide_sum(i)!=None:         #None를 리턴하지 않는다면
        print(divide_sum(i))        #그 수를 출력한다.
        break
    i+=1
    if i>=N:
        print('0')                  #만약 i가 N보다 커지면 그 수는 생성자가 없으므로 0을 출력한다.
        break