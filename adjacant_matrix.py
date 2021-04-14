def get_adjacant_matlix(data,n):
    adjacent_matrix=[[]]
    for i in range(n):
        temp=[0]*n
        k=adjacent_list[i][1]
        for j in range(k):
            index=adjacent_list[i][j+2]
            temp[index-1]=1
        adjacent_matrix.append(temp)

    del adjacent_matrix[0]

    return adjacent_matrix

if __name__=='__main__':

    # N=int(input())
    # adjacent_list=[list(map(int,input().split())) for i in range(N)]
    N=4
    adjacent_list=[[1, 2, 2, 4], [2, 1, 4], [3,0], [4,1,3]]

    adjacent_matrix=get_adjacant_matlix(adjacent_list,N)

    
    for line in adjacent_matrix:
        print(line)







