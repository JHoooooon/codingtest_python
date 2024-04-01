"""
*   트리순회

이진 트리를 표현한 리스트 nodes 를 인자로 받는다
해당 이진 트리에 대해서 전위순회, 중위순회, 후위순회를 반환하는 solution 함수를 구현

*   코드풀이

-   preorder 함수선언

    -   부모노드 -> 왼쪽 자식노드 -> 오른쪽 자식노드

-   inorder 함수선언

    -   왼쪽 자식노드 -> 부모노드 -> 오른쪽 자식노드

-   postorder 함수 선언

    -   왼쪽 자식노드 -> 오른쪽 자식노드 -> 부모노드

"""

def solution(nodes: list):
    answer = []

    def preorder(nodes, idx):
        if idx < len(nodes):
            node = str(nodes[idx]) + " "
            node += preorder(nodes, idx * 2 + 1);
            node += preorder(nodes, idx * 2 + 2);
            return node
        else:
            return ""

    def inorder(nodes, idx):
        if idx < len(nodes):
            node = ""
            node += inorder(nodes, idx * 2 + 1);
            node += str(nodes[idx]) + " ";
            node += inorder(nodes, idx * 2 + 2);
            return node
        else:
            return ""

    def postorder(nodes, idx):
        if idx < len(nodes):
            node = ""
            node += postorder(nodes, idx * 2 + 1);
            node += postorder(nodes, idx * 2 + 2);
            node += str(nodes[idx]) + " "
            return node
        else:
            return ""

    answer = [preorder(nodes, 0)[:-1], inorder(nodes, 0)[:-1], postorder(nodes, 0)[:-1]]

    return answer

solution([1,2,3,4,5,6,7])