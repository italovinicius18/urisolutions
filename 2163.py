def check_cordinate(i,j):
    point = mat[i][j]
    return point

def check_force(n,m,mat):
    
    for i in range(1,n-1):
        for j in range(1,m-1):
            if (mat[i][j] == 42):

                sd = check_cordinate(i-1,j-1)
                sm = check_cordinate(i-1,j)
                se = check_cordinate(i-1,j+1)
                me = check_cordinate(i,j-1)
                md = check_cordinate(i,j+1)
                ie = check_cordinate(i+1,j-1)
                im = check_cordinate(i+1,j)
                id = check_cordinate(i+1,j+1)

                res = [sd, sm, se, me, md, ie, im, id]
                if(res.count(7)==8):
                    print(i+1,j+1)
                    return

    print(0,0)

n,m = list(map(int,input().split()))

mat = []
for i in range(n):
    xs = list(map(int,input().split()))
    mat.append(xs)

check_force(n,m,mat)