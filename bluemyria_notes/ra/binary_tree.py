def testEqual(actual,expected,places=5):
    '''
    Does the actual value equal the expected value?
    For floats, places indicates how many places, right of the decimal, must be correct
    '''
    if isinstance(expected,float):
        if abs(actual-expected) < 10**(-places):
            print('\tPass')
            return True
    else:
        if actual == expected:
            print('\tPass')
            return True
    print('\tTest Failed: expected {} but got {}'.format(expected,actual))
    return False

def buildTree():
    bt = BinaryTree('a')
    print(bt)
    insertLeft(bt, 'b')
    insertRight(bt, 'c')
    print(bt)
    print(getLeftChild(bt), ' d')
    print(getRightChild(bt), ' f')
    print(getRightChild(bt), ' e')

    
    insertRight(getLeftChild(bt), 'd')
    insertRight(getRightChild(bt), 'f')
    insertLeft(getRightChild(bt), 'e')
    return bt

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    print(root)
    print(newBranch)
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    print("***",root)
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    print("getLeftChild ", root[1])
    return root[1]

def getRightChild(root):
    print("getRightChild ", root)
    
    return root[2]



ttree = buildTree()
testEqual(getRootVal(getRightChild(ttree)),'c')
testEqual(getRootVal(getRightChild(getLeftChild(ttree))),'d')
testEqual(getRootVal(getRightChild(getRightChild(ttree))),'f')
