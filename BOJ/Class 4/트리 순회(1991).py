import sys
input=sys.stdin.readline

def preorder(x):                                #전위 순회 함수 (루트>왼쪽노드>오른쪽노드)
    if x =='.':                                 #'.'을 입력받는경우 무시한다.
        return  
    print(x,end='')                             #제일먼저 루트를 탐색하고
    preorder(tree[x][0])                        #왼쪽 노드에서 preorder를 진행한다.
    preorder(tree[x][1])                        #오른쪽 노드에서 preorder를 진행한다.


def inorder(x):                                 #중위 순회 함수 (왼쪽노드>루트>오른쪽노드)
    if x =='.':                                 #'.'을 입력받는경우 무시한다.
        return
    inorder(tree[x][0])                         #제일먼저 왼쪽노드에서 inorder를 진행한다.
    print(x,end='')                             #이후 루트를 탐색하고 
    inorder(tree[x][1])                         #마지막으로 오른쪽노드에서 inorder를 진행한다.

def postorder(x):                               #후위 순회 탐색 (왼쪽노드>오른쪽노드>루트)
    if x =='.':                                 #'.'을 입력받는경우 무시한다.
        return
    postorder(tree[x][0])                       #왼쪽노드에서 postoreder를 진행한다.
    postorder(tree[x][1])                       #이후 오른쪽노드에서 postorder를 진행하고
    print(x,end='')                             #마지막으로 루트를 탐색한다.

N=int(input())
tree={}                                         #딕셔너리 자료형으로 저장
for i in range(N):
    root,left,right=map(str,input().split())
    tree[root]=(left,right)                     #딕셔너리 자료형의 node: (left,right)

preorder('A')
print()
inorder('A')
print()
postorder('A')
