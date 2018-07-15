class Life:
    def __init__(self,num,p):
        self.num=num
        self.p=p
    def set_map(self):
        a=[]
        for i in range(0,self.num):
            a.append([])
            for j in range(0,self.num):
                a[i].append('*')
        self.a=a
    def set_pattern(self):
        b=self.a[:]
        if self.p==1:
            x=int((self.num-1)/2)
            for i in range(x,x+3):
                b[x-1][i-1]=0
            b[x][x-1]=0
            b[x+1][x]=0
        else:
            x=int((self.num-1)/2)
            for i in range(x,x+3):
                b[x-1][i-1]='*'
            b[x][x-1]='*'
            b[x+1][x]='*'
        self.b=b
    def display(self):
        for i in range(0,self.num):
            for j in range(0,self.num):
                print(self.b[i][j],end=' ')
            print('')

x=Life(7,0)
x.set_map()
x.set_pattern()
x.display()
