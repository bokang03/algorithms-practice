def solution(nodeList):
    tree = dict()

    for parent, left, right in nodeList:
        tree[parent] = (left, right)

    preOrder = []
    inOrder = []
    postOrder = []

    def pre(node):
        if node == ".":
            return
        left, right = tree[node]
        preOrder.append(node)
        pre(left)
        pre(right)

    def ino(node):
        if node == ".":
            return
        left, right = tree[node]
        ino(left)
        inOrder.append(node)
        ino(right)

    def post(node):
        if node == ".":
            return
        left, right = tree[node]
        post(left)
        post(right)
        postOrder.append(node)

    pre("A")
    ino("A")
    post("A")
    return [
        "".join(preOrder),
        "".join(inOrder),
        "".join(postOrder)
    ]