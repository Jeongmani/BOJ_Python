import sys
card_plus=[0]*10000001                                  #카드가 10000000가지의 수가 있는 양수 리스트를 선언한다.
card_minus=[0]*10000001                                 #카드가 10000000가지의 수가 있는 음수 리스트를 선언한다.

N=int(sys.stdin.readline().rstrip())                    #가지고 있는 카드의 개수를 입력받는다
have_list=list(map(int,sys.stdin.readline().split()))   #가지고 있는 카드를 리스트 자료형으로 입력받는다
for i in have_list:
    if i>=0:                                            #카드를 입력 받아서 양수인 경우 그 수를 양수 카드를 저장하는 리스트에 i번째 인덱스에 1을 추가한다.
        card_plus[i]+=1
    else:
        card_minus[-i]+=1                               #카드를 입력 받아서 음수인 경우 그 수를 음수 카드를 저장하는 리스트에 -i번째 인덱스에 1을 추가한다.

M=int(sys.stdin.readline().rstrip())                    #찾고자 하는 카드의 개수를 입력받는다
in_list=list(map(int,sys.stdin.readline().split()))     #찾고자 하는 카드의 번호를 입력받는다 
for i in in_list:
    if i>=0:
        print(card_plus[i],end=' ')                     #입력받은 카드의 번호 번째 인덱스 값을 호출한다
    else:
        print(card_minus[-i],end=' ')
