import re
from operator import itemgetter
import flag
import semantics

n_pro=0
n_sym=0
n_non=0
each=0
redno=0
rl=0
rhs1=''

# Dictionary function which stores tokens

dictic = {'start':'1', 'prog':'2', 'body':'3', 'declpart':'4', 'decllist':'5', 'declstat':'6', 'type':'7', 'procpart':'8', 'proclist':'9', 'proc':'10', 'prochead':'11', 'procname':'12', 'fparmlist':'13', 'calltype':'14', 'execpart':'15', 'exechead':'16', 'statlist':'17', 'stat':'18', 'input1stat':'19', 'outputstat':'20', 'callstat':'21', 'callname':'22', 'aparmlist':'23', 'ifstat':'24', 'ifthen':'25', 'ifhead':'26', 'whilestat':'27', 'whileexpr':'28', 'whilehd':'29', 'astat':'30', 'bexpr':'31', 'andexpr':'32', 'notexpr':'33', 'relexpr':'34', 'aexpr':'35', 'term':'36', 'primary':'37', 'constant':'38'};

file12=open("/Users/Samarth/Downloads/827/wpfile")
f=file12.readline().strip().split(' ')

s=re.compile('[0-4]')
p=re.compile('\d+')
n_pro=f[0]
n_sym=f[5]
n_non=f[10]

ostack=[]
production=[]
production1=[]
symbols=[]
matrix=[]
stack1=[]
inputline=[]
rh1=[]

for i in range(int(n_sym)):
    j=file12.readline().strip().split(' ')
    symbols.append(j)


for i in range(int(n_pro)):
    j=p.findall(file12.readline())
    production.append(j)
    production1.append(j)

production.sort(key=itemgetter(0),reverse=True)

for i in range(int(n_sym)):
    j=s.findall(file12.readline().strip())
    matrix.append(j)

# Code for Reduction

def reduc(stack,input1,line):
    #print 'lineis',line
    inputline[:] = input1[:]
    ostack[:]=stack[:]
    ol=len(ostack)
    rl=len(stack)
    if (len(stack)==0):
        stack.append(input1[0])
        rh1.append(line[0])
        stack1.append(symbols[int(input1[0])-1][0]);
        del input1[0]
        del line[0]
    
    while (len(input1) >= 1):
        a = int (stack[len(stack) - 1]) - 1
        b = int (input1[0]) - 1
        if (flag.flag9 == 1):
            data1="Top of Stack"+symbols[a][0];
            print '{:>60}'.format(data1)
            data2="input1 Symbol"+symbols[b][0];
            print '{:>60}'.format(data2)
            if (int(matrix[a][b]) == 3):
                data3="Relation between "+symbols[a][0]+" and "+ symbols[b][0]+" is Less Than";
                print '{:>60}'.format(data3)
            elif (int(matrix[a][b]) == 1):
                data3="Relation between "+symbols[a][0]+" and "+ symbols[b][0]+" is Equal";
                print '{:>60}'.format(data3)
            elif (int(matrix[a][b]) == 2):
                data3="Relation between "+symbols[a][0]+" and "+ symbols[b][0]+" is Greater Than";
                print '{:>60}'.format(data3)
    
        if (matrix[a][b] == '0'):
            print "Character Pair Error in line ",flag.lcount," between ",symbols[a][0]," and ",symbols[b][0]
            data = "Symbols ignored:"
            for ab in range(len(input1)):
                data = data+" " + str(symbols[int(input1[ab])-1][0]) 
            print data
            diff=len(stack)-rl
            data4 = 'Symbols popped: '
            for ae in range(diff):
                data4= data4+ " "+str(symbols[int(stack[len(stack)-1])-1][0])
                stack.pop()
                stack1.pop()
            data4= data4+" "+str(stack1[len(stack1)-1])
            print data4 
            stack[:]=ostack[:]
            data1 = "Stack is: "
            for ac in range(len(ostack)):
                data1 = data1+" " + str(symbols[int(stack[ac])-1][0])
            print data1
            break

        if (matrix[a][b] == '3' or matrix[a][b] == '1'):
            stack.append(input1[0])
            stack1.append(symbols[int(input1[0])-1][0]);
            rh1.append(line[0])
            del line[0]
            #print 'stack1',stack1
            del input1[0]
    
        if (matrix[a][b] == '2'):
            for each in production:
                j = 10
                l = len(each) - 2
                if int(each[l]) == int(each[l]):
                    for i in range(int(each[0])):
                        if int(each[l-i]) != int(stack[len(stack)-i-1]):
                            break
                        else :
                            j=i
        
                if (int(each[0])-1) == j:
                    redno=0
                    for sublist in production1:
                        redno=redno+1
                        if sublist == each:
                            break
                    if (flag.flag8 == 1 or flag.flag12 == 1):
                        data = "Stack Before Reduction: "
                        for ad in range(len(stack1)):
                            data = data+" " + str(stack1[ad]) 
                        print data
                    rhs=''
                    rhs1=''
                    if redno == 16 or redno == 17 :
                        LOCAL = []
                        LST = []
                    semantics.seman(rhs,redno,rh1)
                    rh1.append('')
                    for jj in range(int(each[0])):
                        rhs=rhs+' '+symbols[int(stack[len(stack)-1])-1][0]
                        del stack[len(stack)-1]
                        del stack1[len(stack1)-1]
                        del rh1[len(rh1)-1]
                        #print 'rhs1',rhs1,rh1,rhs
                    stack.append(each[l+1])
                    #rh1.insert(0,each[l+1])
                    lhs=''
                    lhs=symbols[int(each[l+1])-1][0]
                    stack1.append(symbols[int(each[l+1])-1][0]);
                    rl=len(stack1)
                    #print 'redno',redno
                    if (flag.flag7 == 1):
                        #print
                        data = "Reduction # "+str(redno)+" : "+lhs+" <---- "+rhs
                        print '{:>60}'.format(data)
                    if (flag.flag10 == 1):
                        data = "Handle is: "+rhs
                        print '{:>60}'.format(data)
                    if (flag.flag8 == 1 or flag.flag12 == 1):
                        data = "Stack After Reduction: "
                        for ad in range(len(stack1)):
                            data = data+" " + str(stack1[ad]) 
                        print data
                    break
                
# Code for Reduction when input is empty but the stack is not

def red1(stack,line):
    ostack=stack
    while (len(stack) > 0):
        if (len(stack)==1 and stack[0]=='1'):
            break
        #print 'prod',production
    
        for each in production:
            j = 10
            l = len(each) - 2
            if int(each[l]) == int(each[l]):
                for i in range(int(each[0])):
                    if int(each[l-i]) != int(stack[len(stack)-i-1]):
                        break
                    else :
                        j=i
        
            if (int(each[0])-1) == j:
                redno=0
                for sublist in production1:
                    redno=redno+1
                    if sublist == each:
                        break
                #print 'redno',redno
                if (flag.flag8 == 1 or flag.flag12 == 1):
                    data = "Stack Before Reduction: "
                    for ad in range(len(stack1)):
                        data = data+" " + str(stack1[ad]) 
                    print data
                rhs=''
                rhs1=''
                if redno == 16 or redno == 17 :
                    LOCAL = []
                    LST = []
                semantics.seman(rhs,redno,rh1)
                rh1.append('')
                for jj in range(int(each[0])):
                    rhs=rhs+' '+symbols[int(stack[len(stack)-1])-1][0]
                    rhs1 = rhs1+' '+rh1[0]  
                    del stack[len(stack)-1]
                    del stack1[len(stack1)-1]
                    del rh1[len(rh1)-1]
                stack.append(each[l+1])
                #rh1.append(each[l+1])
                lhs=''
                lhs=symbols[int(each[l+1])-1][0]
                stack1.append(symbols[int(each[l+1])-1][0]);
                rl=len(stack1)
                #print 'rhs',rhs1,rh1,rhs
                if (flag.flag7 == 1):
                    #print
                    data = "Reduction # "+str(redno)+" : "+lhs+" <---- "+rhs
                    print '{:>60}'.format(data)
                if (flag.flag10 == 1):
                    data = "Handle is: "+rhs
                    print '{:>60}'.format(data)
                if (flag.flag8 == 1 or flag.flag12 == 1):
                    data = "Stack After Reduction: "
                    for ad in range(len(stack1)):
                        data = data+" " + str(stack1[ad]) 
                    print data
                    #break 
        if(stack==ostack):
            break               
