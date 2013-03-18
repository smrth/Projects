'''
Created on Mar 3, 2012

@author: Samarth
'''
import parser
import redfile
import pragmatics
import flag
import re
inputsem=''
rhs = ''
m = 0
global l
l=0
shape = ''
count =0
proname=[]
stackif={}
jig = [0,1,2,3,4,5,6,7,8,9]
semancopy=[]
tmstk=[]
LOCAL=[]
GLOBAL = []
LST = []
GST = []
FLST = []
data=[]
error=[]
n=0
globe = 0
m=0

vic = re.compile('([a-z][a-zA-Z0-9_]*)|([I][$][0-9]+)|([R][$][0-9]+)|([-+]?\d+\.\d+)|([+-]*[0-9]+)')

def findshape(var1):
    type1 = ''
    check = vic.findall(var1)
    if check[0][0]!='':
        if check[0][0] in LOCAL:
            for e in LST :
                if e[0] == check[0][0]:
                    type1=e[2]
        elif check[0][0] in GLOBAL:
            for e in GST :
                if e[0] == check[0][0]:
                    type1=e[2]
        else:
            s=1
    else:
        a=1  
    return type1                            


def findrc(var1):
    type1 = ''
    type2 = ''
    check = vic.findall(var1)
    if check[0][0]!='':
        if check[0][0] in LOCAL:
            for e in LST :
                if e[0] == check[0][0]:
                    type1=e[3]
                    type2=e[4]
        elif check[0][0] in GLOBAL:
            for e in GST :
                if e[0] == check[0][0]:
                    type1=e[3]
                    type2=e[4]
        else:
            s=1
    else:
        a=1  
    return type1,type2                            


def findtype(var1,var2):
    #print 'var',var1,var2
    type1 = ''
    type2 = ''
    check = vic.findall(var1)
    #print LOCAL,GLOBAL
    #print 'check',check[0][0]
    if check[0][0]!='':
        if check[0][0] in LOCAL:
            for e in LST :
                #print 'e',e
                if e[0] == check[0][0]:
                    type1=e[1]
        elif check[0][0] in GLOBAL:
            for e in GST :
                #print 'e',e
                if e[0] == check[0][0]:
                    type1=e[1]
        else:
            print 'NO VARIABLE '+check[0][0]               
    elif check[0][1]!='' or check[0][4]!='':
        type1 = 'INTEGER'
    elif check[0][2]!='' or check[0][3]!='':
        type1 = 'REAL'
    check = vic.findall(var2)
    #print 'check',check
    if check[0][0]!='':
        if check[0][0] in LOCAL:
            for e in LST :
                if e[0] == check[0][0]:
                    type2=e[1]
        elif check[0][0] in GLOBAL:
            for e in GST :
                if e[0] == check[0][0]:
                    #print e
                    type2=e[1]
        else:
            print 'NO VARIABLE '+check[0][0]               
    elif check[0][1]!='' or check[0][4]!='':
        type2 = 'INTEGER'
    elif check[0][2]!='' or check[0][3]!='':
        type2 = 'REAL'
    #print 'type',type1,type2
    return type1,type2
        
def tuple(tup):
    if (flag.flag13 == 1):
        data =  'TUPLE IS : ( '+str(tup[0])+' , '+str(tup[1])+' , '+str(tup[2])+' , '+str(tup[3])+' )'
        print '{:>60}'.format(data)
    #pragmatics.tuples(tup,globe)

def seman(rh1,red,inputsem):
    if red!='':
        redfile.func(red,inputsem)
        list1 = redfile.freak
        if list1 != [] :
            #print 'this is list1',inputsem,list1,red,tmstk
            #print "hasg",red
            #print stackif
            type1=''
            type2=''
            row = ''
            col = ''
            global n
            global m
            global shape
            global globe
            global LST
            global LOCAL
            if red == 1 :
                data = [inputsem[-3], 'ENDPROGRAM','#','#']
                tuple(data)
                pragmatics.tuples(inputsem[-3], 'ENDPROGRAM','#','#','#',globe)
                if (flag.flag16 == 1):
                    print 'Global ST'
                    print
                    for ia in range(len(GST)):
                        print 'ST Entry [Name:'+GST[ia][0]+' Type:'+GST[ia][1]+' Shape:'+GST[ia][2]+' Rows:'+str(GST[ia][3])+' Cols:'+str(GST[ia][4])+' ]'
                    print
            elif red == 2 :
                data = [inputsem[-1],'STARTPROGRAM','#','#']
                tuple(data)
                pragmatics.tuples(inputsem[-1],'STARTPROGRAM','#','#','#',globe)
                inputsem[-2] = inputsem[-1]
            elif red == 5:
                data = ["#","ENDDECLARATION","#","#"]
                tuple(data)
                pragmatics.tuples("#","ENDDECLARATION","#","#",'#',globe)
            elif red == 11 :
                inputsem[-1] = 'INTEGER'
            elif red == 12 :
                inputsem[-1] = 'REAL'
            elif red == 16 :
                data = [inputsem[-4],'ENDPROCEDURE','#','#']
                tuple(data)
                pragmatics.tuples(inputsem[-4],'ENDPROCEDURE','#','#','#',globe)
                if (flag.flag14 == 1):
                    global count
                    print
                    count=len(LST)
                    for js in range(len(LST)):
                        print 'LT Entry [Name:'+LST[js][0]+' Type:'+LST[js][1]+' Shape:'+LST[js][2]+' Rows:'+str(LST[js][3])+' Cols:'+str(LST[js][4])+'Call Type:'+ LST[js] [5]+' ]'
                    print
            elif red == 17 :
                data = [inputsem[-3],'ENDPROCEDURE','#','#']
                tuple(data)
                pragmatics.tuples(inputsem[-3],'ENDPROCEDURE','#','#','#',globe)
                if (flag.flag14 ==1 ):
                    global count1
                    count1=len(LST)-count
                    print
                    for js in range(count1):
                        print 'LT Entry [Name:'+LST[js+count][0]+' Type:'+LST[js+count][1]+' Shape:'+LST[js+count][2]+' Rows:'+str(LST[js+count][3])+' Cols:'+str(LST[js+count][4])+'Call Type:'+ LST[js+count] [5]+' ]'
                    print
            elif red == 18 :
                data = ['#','ENDFORMALPARAMETERLIST','#','#']
                tuple(data)
                pragmatics.tuples('#','ENDFORMALPARAMETERLIST','#','#','#',globe)
            elif red == 19 :
                data = ['#','NOFORMALPARAMETERS','#','#']
                tuple(data)
                pragmatics.tuples('#','NOFORMALPARAMETERS','#','#','#',globe)
            elif red == 20 :
                globe = 1
                data = [inputsem[list1[0]],list1[1],list1[2],list1[3]]
                inputsem[-2] = inputsem[-1]
                tuple(data)
                pragmatics.tuples(inputsem[list1[0]],list1[1],list1[2],list1[3],'#',globe)
                temp1 = [inputsem[list1[0]],'PROCEDURE','N/A',0,0,'N/A']
                temp = [inputsem[list1[0]],'PROCEDURE','N/A',0,0]
                LST.append(temp1)
                GST.append(temp)
                global proname
                proname.append(inputsem[list1[0]])
            elif red == 21 :
                LOCAL.append(inputsem[-1])
                temp = [inputsem[-1],inputsem[-2],'SCALAR',1,0,inputsem[-3]]
                LST.append(temp)
                data = [inputsem[-1],'FORMAL'+inputsem[-3]+'PARAMETER',1,0]
                stackif[inputsem[-2]] = inputsem[-3]
                tuple(data)
                pragmatics.tuples(inputsem[-1],'FORMAL'+inputsem[-3]+'PARAMETER',1,0,'#',globe)
            elif red == 22 :
                LOCAL.append(inputsem[-2])
                temp = [inputsem[-2],inputsem[-3],'VECTOR',inputsem[-1],0,inputsem[-4]]
                LST.append(temp)
                data = [inputsem[-2],'FORMAL'+inputsem[-4]+'PARAMETER',inputsem[-1],0]
                tuple(data)
                pragmatics.tuples(inputsem[-2],'FORMAL'+inputsem[-4]+'PARAMETER',inputsem[-1],0,'#',globe)
                stackif[inputsem[-2]] = inputsem[-3]
            elif red == 23 :
                LOCAL.append(inputsem[-4])
                temp = [inputsem[-4],inputsem[-5],'MATRIX',inputsem[-3],inputsem[-1],inputsem[-6]]
                LST.append(temp)
                data = [inputsem[-4],'FORMAL'+inputsem[-6]+'PARAMETER',inputsem[-3],inputsem[-1]]
                tuple(data)
                pragmatics.tuples(inputsem[-4],'FORMAL'+inputsem[-6]+'PARAMETER',inputsem[-3],inputsem[-1],'#',globe)
                stackif[inputsem[-4]] = inputsem[-5]
            elif red == 24 :
                LOCAL.append(inputsem[-1])
                temp = [inputsem[-1],inputsem[-2],'SCALAR',1,0,inputsem[-3]]
                LST.append(temp)
                data = ['#' ,'BEGINPARAMETERLIST','#','#']
                tuple(data)
                pragmatics.tuples('#' ,'BEGINPARAMETERLIST','#','#','#',globe)
                data = [inputsem[-1],'FORMAL'+inputsem[-3]+'PARAMETER',1,0]
                tuple(data)
                pragmatics.tuples(inputsem[-1],'FORMAL'+inputsem[-3]+'PARAMETER',1,0,'#',globe)
            elif red == 25 :
                LOCAL.append(inputsem[-2])
                temp = [inputsem[-2],inputsem[-3],'VECTOR',inputsem[-1],0,inputsem[-4]]
                LST.append(temp)
                data = ['#','BEGINPARAMETERLIST','#','#']
                tuple(data)
                pragmatics.tuples('#','BEGINPARAMETERLIST','#','#','#',globe)
                data = [inputsem[-4],'FORMAL'+inputsem[-4]+'PARAMETER',inputsem[-1],0]
                tuple(data)
                pragmatics.tuples(inputsem[-4],'FORMAL'+inputsem[-4]+'PARAMETER',inputsem[-1],0,'#',globe)
            elif red == 26 :
                LOCAL.append(inputsem[-4])
                temp = [inputsem[-4],inputsem[-5],'MATRIX',inputsem[-3],inputsem[-1],inputsem[-6]]
                LST.append(temp)
                data = ['#','BEGINPARAMETERLIST','#','#']
                tuple(data)
                pragmatics.tuples('#','BEGINPARAMETERLIST','#','#','#',globe)
                data = [inputsem[-4],'FORMAL'+inputsem[-6]+'PARAMETER',inputsem[-3],inputsem[-1]]
                tuple(data)
                pragmatics.tuples(inputsem[-4],'FORMAL'+inputsem[-6]+'PARAMETER',inputsem[-3],inputsem[-1],'#',globe)
            elif red == 27:
                inputsem[-2] = 'VALUE'
            elif red == 28:
                inputsem[-2] = 'REFERENCE'
            elif red == 30 :
                data = ["MAIN","LABEL","#","#"]
                tuple(data)
                pragmatics.tuples("MAIN","LABEL","#","#",'#',globe)
            elif red == 36 :
                data = ['#','ENDOFINPUTPARAMETERS','#','#']
                tuple(data)
                pragmatics.tuples('#','ENDOFINPUTPARAMETERS','#','#','#',globe)
                data = ['SCANF','ENDINPUTPARAMETERS','#','#']
                tuple(data)
                pragmatics.tuples('SCANF','ENDINPUTPARAMETERS','#','#','#',globe)
            elif red == 37 :
                data = ["PRINTF","ENDOUTPUTPARAMETERS","#","#"]
                tuple(data)
                pragmatics.tuples('PRINTF','ENDOUTPUTPARAMETERS','#','#','#',globe)
            elif red == 39 :
                shape = findshape(inputsem[-1])
                if shape == 'SCALAR' :
                    data = ['#','INPUTPARAMETER',inputsem[-1],'#']
                    tuple(data)
                    pragmatics.tuples('#','INPUTPARAMETER',inputsem[-1],'#','#',globe)
                else:
                    print 'Error'
            elif red == 40 :
                type1,type2 = findtype(inputsem[-2],'0')
                shape = findshape(inputsem[-4])
                if shape == 'VECTOR' and type1 == 'INTEGER' :
                    data = ['#','INPUTSUBPARAMETER',inputsem[-4],inputsem[-2]]                                                   
                    tuple(data)
                    pragmatics.tuples('#','INPUTSUBPARAMETER',inputsem[-4],inputsem[-2],'#',globe)
                else :
                    print 'Error'
            elif red == 41 :
                type1,type2 = findtype(inputsem[-4],inputsem[-2])
                shape = findshape(inputsem[-6])
                if shape == 'MATRIX' and type1 == 'INTEGER' and type2 == 'INTEGER':
                    n=n+1
                    row,col=findrc(inputsem[-6])
                    data = ['I$'+str(n),'IMULT',col,inputsem[-4]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n),'IMULT',col,inputsem[-4],'#',globe)
                    data = ['I$'+str(n+1),'IADD','I$'+str(n),inputsem[-2]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n+1),'IADD','I$'+str(n),inputsem[-2],'#',globe)
                    n=n+1
                    data = ['#','INPUTSUBPARAMETER',inputsem[-6],'I$'+str(n)]
                    tuple(data)
                    pragmatics.tuples('#','INPUTSUBPARAMETER',inputsem[-6],'I$'+str(n),'#',globe)
                else :
                    print 'Error'
            elif red == 42 :
                data = ['SCANF','CALL','#','#']
                tuple(data)
                pragmatics.tuples('SCANF','CALL','#','#','#',globe)
                data = ['#','INPUTPARAMETER',inputsem[-1],'#']
                tuple(data)
                pragmatics.tuples('#','INPUTPARAMETER',inputsem[-1],'#','#',globe)
            elif red == 43 or red == 44 :
                data = ["#","OUTPUTPARAMETER",inputsem[-1],"#"]
                tuple(data)
                pragmatics.tuples("#","OUTPUTPARAMETER",inputsem[-1],"#",'#',globe)
            elif red == 45 :
                type1,type2 = findtype(inputsem[-2],'0')
                shape = findshape(inputsem[-4])
                if shape == 'VECTOR' and type1 == 'INTEGER' :
                    data = ['#','OUTPUTSUBPARAMETER',inputsem[-4],inputsem[-2]]                                                   
                    tuple(data)
                    pragmatics.tuples('#','OUTPUTSUBPARAMETER',inputsem[-4],inputsem[-2],'#',globe)
                else :
                    print 'Error'
            elif red == 46 :
                type1,type2 = findtype(inputsem[-4],inputsem[-2])
                shape = findshape(inputsem[-6])
                if shape == 'MATRIX' and type1 == 'INTEGER' and type2 == 'INTEGER':
                    n=n+1
                    row,col=findrc(inputsem[-6])
                    data = ['I$'+str(n),'IMULT',col,inputsem[-4]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n),'IMULT',col,inputsem[-4],'#',globe)
                    data = ['I$'+str(n+1),'IADD','I$'+str(n),inputsem[-2]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n+1),'IADD','I$'+str(n),inputsem[-2],'#',globe)
                    n=n+1
                    data = ['#','OUTPUTSUBPARAMETER',inputsem[-6],'I$'+str(n)]
                    tuple(data)
                    pragmatics.tuples('#','OUTPUTSUBPARAMETER',inputsem[-6],'I$'+str(n),'#',globe)
                else :
                    print 'Error'
            elif red == 47 :
                data = ['PRINTF','CALL','#','#']
                tuple(data)
                pragmatics.tuples('PRINTF','CALL','#','#','#',globe)
                data = ['#','OUTPUTPARAMETER',inputsem[-1],'#']
                tuple(data)
                pragmatics.tuples('#','OUTPUTPARAMETER',inputsem[-1],'#','#',globe)
            elif red == 48 :
                data = [inputsem[list1[0]],list1[1],list1[2],list1[3]]
                tuple(data)
                pragmatics.tuples(inputsem[list1[0]],list1[1],list1[2],list1[3],'#',globe)
            elif red == 49 :
                data = ['#','NOACTUALPARAMETER','#','#']
                tuple(data)
                pragmatics.tuples('#','NOACTUALPARAMETER','#','#','#',globe)
            elif red == 50 :
                if inputsem[-1] in proname:
                    data = [inputsem[-1],'CALL','#','#']
                    inputsem[-2] = inputsem[-1]    
                    tuple(data)
                    pragmatics.tuples(inputsem[-1],'CALL','#','#','#',globe)
                else:
                    print 'No such Procedure name'
            elif red == 51 :
                shape = findshape(inputsem[-1])
                if shape == 'SCALAR' :
                    n = n + 1
                    data = ['#','ACTUAL'+inputsem[-2]+'SUBPARAMETER',inputsem[-1],'I$'+str(n)]
                    tuple(data)
                    pragmatics.tuples('#','ACTUAL'+inputsem[-2]+'SUBPARAMETER',inputsem[-1],'I$'+str(n),'#',globe)
                else :
                    print 'Error'
            elif red == 52 :
                type1,type2 = findtype(inputsem[-2],'0')
                shape = findshape(inputsem[-4])
                if shape == 'VECTOR' and type1 == 'INTEGER' :
                    n = n + 1
                    data = ['#','ACTUAL'+inputsem[-5]+'SUBPARAMETER',inputsem[-4],'I$'+str(n)]
                else :
                    print 'Error'
            elif red == 53 :
                type1,type2 = findtype(inputsem[-4],inputsem[-2])
                shape = findshape(inputsem[-6])
                if shape == 'MATRIX' and type1 == 'INTEGER' and type2 == 'INTEGER':
                    n=n+1
                    data = ['I$'+str(n),'IMULT',inputsem[-2],inputsem[-4]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n),'IMULT',inputsem[-2],inputsem[-4],'#',globe)
                    data = ['I$'+str(n+1),'IADD','I$'+str(n),inputsem[-2]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n+1),'IADD','I$'+str(n),inputsem[-2],'#',globe)
                    n=n+1
                    data = ['#','ACTUAL'+inputsem[-7]+'SUBPARAMETER',inputsem[-6],'I$'+str(n)]
                    tuple(data)
                    pragmatics.tuples('#','ACTUAL'+inputsem[-7]+'SUBPARAMETER',inputsem[-6],'I$'+str(n),'#',globe)
                else :
                    print 'Error'
            elif red == 54 :
                shape = findshape(inputsem[-1])
                if shape == 'SCALAR' :
                    data = ['#','BEGINACTUALPARAMETERLIST','#','#']
                    tuple(data)
                    pragmatics.tuples('#','BEGINACTUALPARAMETERLIST','#','#','#',globe)
                    n = n + 1
                    data = ['#','ACTUAL'+inputsem[-2]+'SUBPARAMETER',inputsem[-1],'I$'+str(n)]
                    tuple(data)
                    pragmatics.tuples('#','ACTUAL'+inputsem[-2]+'SUBPARAMETER',inputsem[-1],'I$'+str(n),'#',globe)
                else :
                    print 'Error'
            elif red == 55 :
                type1,type2 = findtype(inputsem[-2],'0')
                shape = findshape(inputsem[-4])
                if shape == 'VECTOR' and type1 == 'INTEGER' :
                    data = ['#','BEGINACTUALPARAMETERLIST','#','#']
                    tuple(data)
                    pragmatics.tuples('#','BEGINACTUALPARAMETERLIST','#','#','#',globe)
                    n = n + 1
                    data = ['#','ACTUAL'+inputsem[-5]+'SUBPARAMETER',inputsem[-4],'I$'+str(n)]
                    tuple(data)
                    pragmatics.tuples('#','ACTUAL'+inputsem[-5]+'SUBPARAMETER',inputsem[-4],'I$'+str(n),'#',globe)
                else :
                    print 'Error'
            elif red == 56 :
                type1,type2 = findtype(inputsem[-4],inputsem[-2])
                shape = findshape(inputsem[-6])
                if shape == 'MATRIX' and type1 == 'INTEGER' and type2 == 'INTEGER':
                    n=n+1
                    data = ['#','BEGINACTUALPARAMETERLIST','#','#']
                    tuple(data)
                    pragmatics.tuples('#','BEGINACTUALPARAMETERLIST','#','#','#',globe)
                    data = ['I$'+str(n),'IMULT',inputsem[-2],inputsem[-4]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n),'IMULT',inputsem[-2],inputsem[-4],'#',globe)
                    data = ['I$'+str(n+1),'IADD','I$'+str(n),inputsem[-2]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n+1),'IADD','I$'+str(n),inputsem[-2],'#',globe)
                    n=n+1
                    data = ['#','ACTUAL'+inputsem[-7]+'SUBPARAMETER',inputsem[-6],'I$'+str(n)]
                    tuple(data)
                    pragmatics.tuples('#','ACTUAL'+inputsem[-7]+'SUBPARAMETER',inputsem[-6],'I$'+str(n),'#',globe)
                else:
                    print "Error"
            elif red == 57 :
                    x=tmstk.pop()
                    data = ['L'+str(x),'LABEL','#','#']
                    tuple(data)
                    pragmatics.tuples('L'+str(x),'LABEL','#','#','#',globe)
            elif red == 58 :
                    x=tmstk.pop()
                    data = ['L'+str(x),'LABEL','#','#']
                    tuple(data)
                    pragmatics.tuples('L'+str(x),'LABEL','#','#','#',globe)
            elif red == 59 :
                    data = ['L'+str(m),'JUMP','#','#']
                    tuple(data)
                    pragmatics.tuples('L'+str(m),'JUMP','#','#','#',globe)
                    x=tmstk.pop()
                    data = ['L'+str(x),'LABEL','#','#']
                    tmstk.append(m)
                    m=m+1
                    tuple(data)
                    pragmatics.tuples('L'+str(x),'LABEL','#','#','#',globe)
            elif red == 60 :
                    data = ['L'+str(m),'CJUMP',inputsem[-3],'#']
                    tuple(data)
                    pragmatics.tuples('L'+str(m),'CJUMP',inputsem[-3],'#','#',globe)
                    tmstk.append(m)
                    m=m+1
            elif red == 61 :
                    data = ['L'+str(tmstk[-2]),'JUMP','#','#']
                    tuple(data)
                    pragmatics.tuples('L'+str(tmstk[-2]),'JUMP','#','#','#',globe)
                    data = ['L'+str(tmstk[-1]),'LABEL','#','#']
                    tuple(data)
                    pragmatics.tuples('L'+str(tmstk[-1]),'LABEL','#','#','#',globe)
                    tmstk.pop()
                    tmstk.pop()
            elif red == 62 :
                vwhile=inputsem[-3]
                type1,type2 = findtype(inputsem[-3],'0')
                vwhile
                if (vwhile[0] == 'B' and vwhile[1] == '$') or (type1 == '1' or type1 == '0'):
                    vwhile='BOOLEAN'
                else :
                    print 'Not Boolean'
                data = ['L'+str(m),'CJUMP',inputsem[-3],'#']
                tuple(data)
                pragmatics.tuples('L'+str(m),'CJUMP',inputsem[-3],'#','#',globe)
                tmstk.append(m)
                m=m+1
            elif red == 63 :
                    data = ['L'+str(m),'LABEL','#','#']
                    tuple(data)
                    pragmatics.tuples('L'+str(m),'LABEL','#','#','#',globe)
                    tmstk.append(m)
                    m=m+1
            elif red == 64 :
                n=n+1
                type1,type2 = findtype(inputsem[-3],inputsem[-1])
                if type1!=type2 :
                    type2 = type1
                    data =  [type1[0]+'$'+str(n),type1,inputsem[-1],'#']
                    tuple(data)
                    pragmatics.tuples(type1[0]+'$'+str(n),type1,inputsem[-1],'#','#',globe)
                    inputsem[-1] = type1[0]+'$'+str(n)
                    #n = n + 1
                data = [inputsem[-3],type1[0]+'SUBASSIGN',inputsem[-1],'#']
                tuple(data)
                pragmatics.tuples(inputsem[-3],type1[0]+'SUBASSIGN',inputsem[-1],'#','#',globe)
                inputsem[-3] = inputsem[-1]
            elif red == 65 :
                type1,type2 = findtype(inputsem[-4],'0')
                if type1 == 'INTEGER':
                    n=n+1
                    type1,type2 = findtype(inputsem[-6],inputsem[-1])
                    if type1!=type2 :
                        type2 = type1
                        data =  [type1[0]+'$'+str(n),type1,inputsem[-1],'#']
                        tuple(data)
                        pragmatics.tuples(type1[0]+'$'+str(n),type1,inputsem[-1],'#','#',globe)
                        inputsem[-1] = type1[0]+'$'+str(n)
                        #n = n + 1
                    data = [inputsem[-6],type1[0]+'SUBASSIGN',inputsem[-1],inputsem[-4]]
                    tuple(data)
                    pragmatics.tuples(inputsem[-6],type1[0]+'SUBASSIGN',inputsem[-1],inputsem[-4],'#',globe)
                    inputsem[-6] = inputsem[-1]
                else :
                    print "Index is not Integer"
            elif red == 66 :
                type1,type2 = findtype(inputsem[-6],inputsem[-4])
                row,col=findrc(inputsem[-8])
                if type1 == 'INTEGER' and type2 == 'INTEGER':
                    n=n+1
                    type1,type2 = findtype(inputsem[-8],inputsem[-1])
                    if type1!=type2 :
                        type2 = type1
                        data =  [type1[0]+'$'+str(n),type1,inputsem[-1],'#']
                        tuple(data)
                        pragmatics.tuples(type1[0]+'$'+str(n),type1,inputsem[-1],'#','#',globe)
                        inputsem[-1] = type1[0]+'$'+str(n)
                    data = ['I$'+str(n),'IMULT',col,inputsem[-6]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n),'IMULT',col,inputsem[-6],'#',globe)
                    data = ['I$'+str(n+1),'IADD','I$'+str(n),inputsem[-5]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n+1),'IADD','I$'+str(n),inputsem[-5],'#',globe)
                    n=n+1
                    data = [inputsem[-8],type1[0]+'SUBASSIGN',inputsem[-1],'I$'+str(n)]
                    tuple(data)
                    pragmatics.tuples(inputsem[-8],type1[0]+'SUBASSIGN',inputsem[-1],'I$'+str(n),'#',globe)
                    inputsem[-8] = inputsem[-1]
                else :
                    print "Indices are not Integer"
            elif red == 67 :
                n=n+1
                type1,type2 = findtype(inputsem[-4],inputsem[-2])
                if type1!=type2 :
                    type2 = type1
                    data =  [type1[0]+'$'+str(n),'CONVERTTO'+type1[0],inputsem[-2],'#']
                    tuple(data)
                    pragmatics.tuples(type1[0]+'$'+str(n),'CONVERTTO'+type1[0],inputsem[-2],'#','#',globe)
                    inputsem[-2] = type1[0]+'$'+str(n)
                    #n = n + 1
                data = [inputsem[-4],type1[0]+'SUBASSIGN',inputsem[-2],'#']
                tuple(data)
                pragmatics.tuples(inputsem[-4],type1[0]+'SUBASSIGN',inputsem[-2],'#','#',globe)
                inputsem[-4] = inputsem[-2]
            elif red == 68 :
                type1,type2 = findtype(inputsem[-5],'0')
                if type1 == 'INTEGER':
                    n=n+1
                    type1,type2 = findtype(inputsem[-7],inputsem[-2])
                    if type1!=type2 :
                        type2 = type1
                        data =  [type1[0]+'$'+str(n),'CONVERTTO'+type1[0],inputsem[-2],'#']
                        tuple(data)
                        pragmatics.tuples(type1[0]+'$'+str(n),'CONVERTTO'+type1[0],inputsem[-2],'#','#',globe)
                        inputsem[-2] = type1[0]+'$'+str(n)
                        #n = n + 1
                    data = [inputsem[-7],type1[0]+'SUBASSIGN',inputsem[-2],inputsem[-5]]
                    tuple(data)
                    pragmatics.tuples(inputsem[-7],type1[0]+'SUBASSIGN',inputsem[-2],inputsem[-5],'#',globe)
                    inputsem[-7] = inputsem[-2]
                else:
                    print "Index is not Integer"
            elif red == 69 :
                type1,type2 = findtype(inputsem[-7],inputsem[-5])
                row,col=findrc(inputsem[-9])
                if type1 == 'INTEGER' and type2 == 'INTEGER':
                    n=n+1
                    type1,type2 = findtype(inputsem[-9],inputsem[-2])
                    if type1!=type2 :
                        type2 = type1
                        data =  [type1[0]+'$'+str(n),type1,inputsem[-2],'#']
                        tuple(data)
                        pragmatics.tuples(type1[0]+'$'+str(n),type1,inputsem[-2],'#','#',globe)
                        inputsem[-2] = type1[0]+'$'+str(n)
                    data = ['I$'+str(n),'IMULT',col,inputsem[-7]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n),'IMULT',col,inputsem[-7],'#',globe)
                    data = ['I$'+str(n+1),'IADD','I$'+str(n),inputsem[-5]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n+1),'IADD','I$'+str(n),inputsem[-5],'#',globe)
                    n = n+1
                    data = [inputsem[-9],type1[0]+'SUBASSIGN',inputsem[-2],'I$'+str(n)]
                    tuple(data)
                    pragmatics.tuples(inputsem[-9],type1[0]+'SUBASSIGN',inputsem[-2],'I$'+str(n),'#',globe)
                    inputsem[-9] = inputsem[-2]
                else :
                    print "Indices are not Integer"
            elif red == 70 :
                n=n+1
                if (inputsem[-1] == '0' or inputsem[-1] == '1' ) and ( inputsem[-3] == '0' or inputsem[-3] == '1') :  
                    data = ['B$'+str(n),'OR',inputsem[-3],inputsem[-1]]
                    tuple(data)
                    pragmatics.tuples('B$'+str(n),'OR',inputsem[-3],inputsem[-1],'#',globe)
                else :
                    print "Operands are not of type Boolean"

            elif red == 72 :
                n=n+1
                if (inputsem[-1] == '0' or inputsem[-1] == '1' ) and ( inputsem[-3] == '0' or inputsem[-3] == '1') :  
                    data = ['B$'+str(n),'AND',inputsem[-3],inputsem[-1]]
                    tuple(data)
                    pragmatics.tuples('B$'+str(n),'AND',inputsem[-3],inputsem[-1],'#',globe)
                else :
                    print "Operands are not of type Boolean"
            elif red == 74 :
                n=n+1
                if (inputsem[-1] == '0' or inputsem[-1] == '1' ) :  
                    data = ['B$'+str(n),'NOT',inputsem[-1],"#"]
                    tuple(data)
                    pragmatics.tuples('B$'+str(n),'NOT',inputsem[-1],"#",'#',globe)
                else :
                    print "Operands are not of type Boolean"

            elif red == 76 :
                n=n+1
                type1,type2 = findtype(inputsem[-3],inputsem[-1])
                if type1 != type2 :
                    if type1 == 'REAL': 
                        type2 = type1   
                        data = ['B$'+str(n),type1[0]+'LT',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type1[0]+'LT',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)
                    else:
                        type1 = type2      
                        data = ['B$'+str(n),type2[0]+'LT',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type2[0]+'LT',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)   
                else :  
                    data = ['B$'+str(n),type1[0]+'LT',inputsem[-3],inputsem[-1]]
                    tuple(data)
                    pragmatics.tuples('B$'+str(n),type1[0]+'LT',inputsem[-3],inputsem[-1],'#',globe)
                    inputsem[-3] = 'B$'+str(n)
            elif red == 77 :
                n=n+1
                type1,type2 = findtype(inputsem[-3],inputsem[-1])
                if type1 != type2 :
                    if type1 == 'REAL': 
                        type2 = type1   
                        data = ['B$'+str(n),type1[0]+'LE',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type1[0]+'LE',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)
                    else:
                        type1 = type2      
                        data = ['B$'+str(n),type2[0]+'LE',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type2[0]+'LE',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)   
                else :  
                    data = ['B$'+str(n),type1[0]+'LE',inputsem[-3],inputsem[-1]]
                    tuple(data)
                    pragmatics.tuples('B$'+str(n),type1[0]+'LE',inputsem[-3],inputsem[-1],'#',globe)
                    inputsem[-3] = 'B$'+str(n)
            elif red == 78 :
                n=n+1
                type1,type2 = findtype(inputsem[-3],inputsem[-1])
                if type1 != type2 :
                    if type1 == 'REAL': 
                        type2 = type1   
                        data = ['B$'+str(n),type1[0]+'GT',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type1[0]+'GT',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)
                    else:
                        type1 = type2      
                        data = ['B$'+str(n),type2[0]+'GT',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type2[0]+'GT',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)   
                else :  
                    data = ['B$'+str(n),type1[0]+'GT',inputsem[-3],inputsem[-1]]
                    tuple(data)
                    pragmatics.tuples('B$'+str(n),type1[0]+'GT',inputsem[-3],inputsem[-1],'#',globe)
                    inputsem[-3] = 'B$'+str(n)
            elif red == 79 :
                n=n+1
                type1,type2 = findtype(inputsem[-3],inputsem[-1])
                if type1 != type2 :
                    if type1 == 'REAL': 
                        type2 = type1   
                        data = ['B$'+str(n),type1[0]+'GE',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type1[0]+'GE',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)
                    else:
                        type1 = type2      
                        data = ['B$'+str(n),type2[0]+'GE',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type2[0]+'GE',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)   
                else :  
                    data = ['B$'+str(n),type1[0]+'GE',inputsem[-3],inputsem[-1]]
                    tuple(data)
                    pragmatics.tuples('B$'+str(n),type1[0]+'GE',inputsem[-3],inputsem[-1],'#',globe)
                    inputsem[-3] = 'B$'+str(n)
            elif red == 80 :
                n=n+1
                type1,type2 = findtype(inputsem[-3],inputsem[-1])
                if type1 != type2 :
                    if type1 == 'REAL': 
                        type2 = type1   
                        data = ['B$'+str(n),type1[0]+'EQ',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type1[0]+'EQ',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)
                    else:
                        type1 = type2      
                        data = ['B$'+str(n),type2[0]+'EQ',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type2[0]+'EQ',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)   
                else :  
                    data = ['B$'+str(n),type1[0]+'EQ',inputsem[-3],inputsem[-1]]
                    tuple(data)
                    pragmatics.tuples('B$'+str(n),type1[0]+'EQ',inputsem[-3],inputsem[-1],'#',globe)
                    inputsem[-3] = 'B$'+str(n)
            elif red == 81 :
                n=n+1
                type1,type2 = findtype(inputsem[-3],inputsem[-1])
                if type1 != type2 :
                    if type1 == 'REAL': 
                        type2 = type1   
                        data = ['B$'+str(n),type1[0]+'NE',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type1[0]+'NE',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)
                    else:
                        type1 = type2      
                        data = ['B$'+str(n),type2[0]+'NE',inputsem[-3],inputsem[-1]]
                        tuple(data)
                        pragmatics.tuples('B$'+str(n),type2[0]+'NE',inputsem[-3],inputsem[-1],'#',globe)
                        inputsem[-3] = 'B$'+str(n)   
                else :  
                    data = ['B$'+str(n),type1[0]+'NE',inputsem[-3],inputsem[-1]]
                    tuple(data)
                    pragmatics.tuples('B$'+str(n),type1[0]+'NE',inputsem[-3],inputsem[-1],'#',globe)
                    inputsem[-3] = 'B$'+str(n)  
            elif red == 83:
                n=n+1
                type1,type2 = findtype(inputsem[-1],inputsem[-3])
                if type1 != type2 :
                    if type1 == 'REAL': 
                        type2 = type1   
                        data = ['R$'+str(n),'CONVERTITOR',inputsem[-3],'#']
                        tuple(data)
                        pragmatics.tuples('R$'+str(n),'CONVERTITOR',inputsem[-3],'#','#',globe)
                        inputsem[-3] = 'R$'+str(n)
                    else:
                        type1 = type2      
                        data = ['R$'+str(n),'CONVERTITOR',inputsem[-1],'#']
                        tuple(data)
                        pragmatics.tuples('R$'+str(n),'CONVERTITOR',inputsem[-1],'#','#',globe)
                        inputsem[-1] = 'R$'+str(n)    
                data = [type1[0]+'$'+str(n),type1[0]+'ADD',inputsem[-3],inputsem[-1]]        
                tuple(data)
                pragmatics.tuples(type1[0]+'$'+str(n),type1[0]+'ADD',inputsem[-3],inputsem[-1],'#',globe)
                inputsem[-3] = type1[0]+'$'+str(n)
            elif red == 84:
                n=n+1
                type1,type2 = findtype(inputsem[-1],inputsem[-3])
                if type1 != type2 :
                    if type1 == 'REAL': 
                        type2 = type1   
                        data = ['R$'+str(n),'CONVERTITOR',inputsem[-3],'#']
                        tuple(data)
                        pragmatics.tuples('R$'+str(n),'CONVERTITOR',inputsem[-3],'#','#',globe)
                        inputsem[-3] = 'R$'+str(n)
                    else:
                        type1 = type2      
                        data = ['R$'+str(n),'CONVERTITOR',inputsem[-1],'#']
                        tuple(data)
                        pragmatics.tuples('R$'+str(n),'CONVERTITOR',inputsem[-1],'#','#',globe)
                        inputsem[-1] = 'R$'+str(n)    
                data = [type1[0]+'$'+str(n),type1[0]+'SUB',inputsem[-3],inputsem[-1]]        
                tuple(data)
                pragmatics.tuples(type1[0]+'$'+str(n),type1[0]+'SUB',inputsem[-3],inputsem[-1],'#',globe)
                inputsem[-3] = type1[0]+'$'+str(n)
            elif red == 85:
                n=n+1
                type1,type2 = findtype(inputsem[-1],'0')
                if type1 != type2 : 
                    type2 = type1   
                    data = ['R$'+str(n),'CONVERTITOR','0','#']
                    tuple(data)
                    pragmatics.tuples('R$'+str(n),'CONVERTITOR','0','#','#',globe)
                    #inputsem[-3] = 'R$'+str(n) 
                    n=n+1   
                data = [type1[0]+'$'+str(n),type1[0]+'SUB','0',inputsem[-1]]        
                tuple(data)
                pragmatics.tuples(type1[0]+'$'+str(n),type1[0]+'SUB','0',inputsem[-1],'#',globe)
                inputsem[-2] = type1[0]+'$'+str(n)
            elif red == 87:
                n=n+1
                type1,type2 = findtype(inputsem[-1],inputsem[-3])
                #print 'type',type1,type2
                if type1 != type2 :
                    if type1 == 'REAL': 
                        type2 = type1   
                        data = ['R$'+str(n),'CONVERTITOR',inputsem[-3],'#']
                        tuple(data)
                        pragmatics.tuples('R$'+str(n),'CONVERTITOR',inputsem[-3],'#','#',globe)
                        inputsem[-3] = 'R$'+str(n)
                    else:
                        type1 = type2      
                        data = ['R$'+str(n),'CONVERTITOR',inputsem[-1],'#']
                        tuple(data)
                        pragmatics.tuples('R$'+str(n),'CONVERTITOR',inputsem[-1],'#','#',globe)
                        inputsem[-1] = 'R$'+str(n)
                #print type1#type1[0]
                data = [type1[0]+'$'+str(n),type1[0]+'MUL',inputsem[-3],inputsem[-1]]        
                tuple(data)
                pragmatics.tuples(type1[0]+'$'+str(n),type1[0]+'MUL',inputsem[-3],inputsem[-1],'#',globe)
                inputsem[-3] = type1[0]+'$'+str(n)
            elif red == 88:
                n=n+1
                type1,type2 = findtype(inputsem[-1],inputsem[-3])
                if type1 != type2 :
                    if type1 == 'REAL': 
                        type2 = type1   
                        data = ['R$'+str(n),'CONVERTITOR',inputsem[-3],'#']
                        tuple(data)
                        pragmatics.tuples('R$'+str(n),'CONVERTITOR',inputsem[-3],'#','#',globe)
                        inputsem[-3] = 'R$'+str(n)
                    else:
                        type1 = type2      
                        data = ['R$'+str(n),'CONVERTITOR',inputsem[-1],'#']
                        tuple(data)
                        pragmatics.tuples('R$'+str(n),'CONVERTITOR',inputsem[-1],'#','#',globe)
                        inputsem[-1] = 'R$'+str(n)   
                n=n+1 
                data = [type1[0]+'$'+str(n),type1[0]+'DIV',inputsem[-3],inputsem[-1]]        
                tuple(data)
                pragmatics.tuples(type1[0]+'$'+str(n),type1[0]+'DIV',inputsem[-3],inputsem[-1],'#',globe)
                inputsem[-3] = type1[0]+'$'+str(n)
            elif red == 90 :
                inputsem[-3] = inputsem[-2]
            elif red == 91 :
                type1,type2 = findtype(inputsem[-4],inputsem[-2])
                typevar,tpy0=findtype(inputsem[-6],'0')
                shape = findshape(inputsem[-6])
                if shape == 'MATRIX' and type1 == 'INTEGER' and type2 == 'INTEGER':    
                    n=n+1
                    row,col=findrc(inputsem[-6])
                    data = ['I$'+str(n),'IMULT',col,inputsem[-4]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n),'IMULT',col,inputsem[-4],'#',globe)
                    data = ['I$'+str(n+1),'IADD','I$'+str(n),inputsem[-2]]
                    tuple(data)
                    pragmatics.tuples('I$'+str(n+1),'IADD','I$'+str(n),inputsem[-2],'#',globe)
                    n=n+1
                    data = [typevar[0]+'$'+str(n+1),'SUBLOAD',inputsem[-6],'I$'+str(n)]
                    tuple(data)
                    pragmatics.tuples(typevar[0]+'$'+str(n+1),'SUBLOAD',inputsem[-6],'I$'+str(n),'#',globe)
                    inputsem[-6] = typevar[0]+'$'+str(n+1)
                    n=n+1
                else :
                    print 'Indices not integer and Shape mismatch'
            elif red == 92 :
                type1,type2 = findtype(inputsem[-2],'0')
                typevar,typ=findtype(inputsem[-4],'0')
                shape = findshape(inputsem[-4])
                if shape == 'VECTOR' and type1 == 'INTEGER' :
                    n=n+1
                    data = [typevar[0]+'$'+str(n),'SUBLOAD',inputsem[-4],inputsem[-2]]
                    tuple(data)
                    pragmatics.tuples(typevar[0]+'$'+str(n),'SUBLOAD',inputsem[-4],inputsem[-2],'#',globe)
                    inputsem[-4] = typevar[0]+'$'+str(n)
                else :
                    print 'Error'
                
            elif list1[1] == 'MEMORY':
                temp = []
                if list1[2] == 1:
                    temp = [inputsem[list1[0]],inputsem[-2],'SCALAR',list1[2],list1[3]]
                    temp1 = [inputsem[list1[0]],inputsem[-2],'SCALAR',list1[2],list1[3],'N/A']
                    if globe == 0:
                        #print list1,inputsem
                        GLOBAL.append(inputsem[list1[0]])
                        GST.append(temp)
                    else:
                        LOCAL.append(inputsem[list1[0]])
                        LST.append(temp1)
                    temp = [inputsem[list1[0]],'MEMORY',list1[2],list1[3],inputsem[-2]]
                    shape = findshape(inputsem[list1[0]])
                    tuple(temp)
                    pragmatics.tuples(inputsem[list1[0]],'MEMORY',list1[2],list1[3],inputsem[-2],globe)
                elif list1[3] == 0:
                    temp = [inputsem[list1[0]],inputsem[-3],'VECTOR',inputsem[list1[2]],list1[3]]
                    temp1 = [inputsem[list1[0]],inputsem[-3],'VECTOR',inputsem[list1[2]],list1[3],'N/A']
                    if globe == 0:
                        GLOBAL.append(inputsem[list1[0]])
                        GST.append(temp)
                    else:
                        LOCAL.append(inputsem[list1[0]])
                        LST.append(temp1)
                    temp = [inputsem[list1[0]],'MEMORY',inputsem[list1[2]],list1[3],inputsem[-3]]
                    tuple(temp)
                    pragmatics.tuples(inputsem[list1[0]],'MEMORY',inputsem[list1[2]],list1[3],inputsem[-3],globe)
                else:
                    temp = [inputsem[list1[0]],inputsem[-5],'MATRIX',inputsem[list1[2]],inputsem[list1[3]]]
                    temp1 = [inputsem[list1[0]],inputsem[-5],'MATRIX',inputsem[list1[2]],inputsem[list1[3]],'N/A']
                    if globe == 0:
                        GLOBAL.append(inputsem[list1[0]])
                        GST.append(temp)
                    else:
                        LOCAL.append(inputsem[list1[0]])
                        LST.append(temp1)
                    temp = [inputsem[list1[0]],'MEMORY',inputsem[list1[2]],inputsem[list1[3]],inputsem[-5]]
                    tuple(temp)
                    pragmatics.tuples(inputsem[list1[0]],'MEMORY',inputsem[list1[2]],inputsem[list1[3]],inputsem[-5],globe)
                #print LOCAL,GLOBAL
