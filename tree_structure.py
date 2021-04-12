'''
木構造
id k c1 ... ckの情報が付与されたときに
節点の情報をその番号が小さい順に出力する
node id, parent , depth, left-child
左子右兄弟表現(left-child, right-sibling representation)を用いる
'''


import dataclasses

@dataclasses.dataclass
class Node:
    parent: int=None
    left_child: int=None
    right_sibling: int=None
    depth: int=None

def rec(r,d):
    Tree_list[r].depth = d
    if Tree_list[r].right_sibling != None:
        print(r,d)
        rec(Tree_list[r].right_sibling,d)
    if Tree_list[r].left_child != None:
        print(r,d)
        rec(Tree_list[r].left_child,d+1) 

if __name__ == "__main__":
    input_data = []

    input_data.append("0 3 1 4 10")
    input_data.append("1 2 2 3")
    input_data.append("2 0")
    input_data.append("3 0")
    input_data.append("4 3 5 6 7")
    input_data.append("5 0")
    input_data.append("6 0")
    input_data.append("7 2 8 9")
    input_data.append("8 0")
    input_data.append("9 0")
    input_data.append("10 2 11 12")
    input_data.append("11 0")
    input_data.append("12 0")

    N = len(input_data)
    Tree_list = [Node() for i in range(N)]
    print(Tree_list)
    
    for data_str in input_data:
        data =list(map(int,data_str.split()))
        tree_id = data[0]
        tree_degree = data[1]

        if tree_degree>0:
            Tree_list[tree_id].left_child=data[2]
            Tree_list[data[2]].parent=tree_id

            for i in range(tree_degree-1):
                Tree_list[data[i+2]].right_sibling=data[i+3]
                Tree_list[data[i+3]].parent=tree_id


    for i in range(len(Tree_list)):
        if Tree_list[i].parent==None:
            r_index=i

    rec(r_index,0)

    print(Tree_list)
