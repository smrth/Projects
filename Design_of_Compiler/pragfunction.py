'''
Created on Apr 4, 2012

@author: Samarth
'''


import re
fdprag = re.compile('([a-z][a-zA-Z0-9]*)|([0-9]+)|([IR$]+[0-9]+)')
divprag = re.compile('[a-z][a-zA-Z0-9]+')
asmfileapp=[]
dictvariable = {}
lcprag = []
glprag = []
originalnum = []
originalintnum = []
originalintegerroll = []
alltypeinc = ''
formalrparam =[]
formalrparamclast = []
numberfororiginal = []
printdatasec = ['SECTION .data\nformati:\tdb "%d",10,0,\nformatr:\tdb "%f",10,0']
bss = ['SECTION .bss\nz1:    resd    1']
variablerep = ''
variablereprepag = ''
optimusprime = 0
registermany = {'eax':'','ebx':'','ecx':'','edx':'','esp':'','ebp':'','esi':'','edi':''}
registerless = ['ebx','ecx','esi','edi','ebp','esp']
kudkomarahiya = ''

def printdata(name):
    if name in lcprag :
        if name in originalintnum or name in originalintegerroll :
            data='push\tdword [z1]'
            asmfileapp.append(data)
            prin(data)
            data='push formati'
            asmfileapp.append(data)
            prin(data)
            data='call printf'
            asmfileapp.append(data)
            prin(data)
        elif name in originalnum :
            data='push formatr'

    elif name in glprag :
        if name in originalintnum or name in originalintegerroll :
            data='push\tdword ['+ name +']'
            asmfileapp.append(data)
            prin(data)
            data='push formati'
            asmfileapp.append(data)
            prin(data)
            data='call printf'
            asmfileapp.append(data)
            prin(data)
        elif name in originalnum :
            data='push formatr'
 
    else :
        if name in originalintnum or name in originalintegerroll :
            data='push\t[z1]'
            asmfileapp.append(data)
            prin(data)
            data='push formati'
            asmfileapp.append(data)
            prin(data)
            data='call printf'
            asmfileapp.append(data)
            prin(data)
        elif name in originalnum :
            data='push formatr'

            
def printingdatasub(name,index):
    if name in glprag :
        if name in originalintnum or name in originalintegerroll :
            if index in lcprag :
                data='mov\teax,'+ registermany[dictvariable[index]]
                asmfileapp.append(data)
                prin(data)
                data='imul\teax,4'
                asmfileapp.append(data)
                prin(data)
            elif index in glprag :
                data='mov\teax,['+index+']'
                asmfileapp.append(data)
                prin(data)
                data='imul\teax,4'
                asmfileapp.append(data)
                prin(data) 
            else :
                data='mov\teax,' + index
                asmfileapp.append(data)
                prin(data)
                data='imul\teax,4'
                asmfileapp.append(data)
                prin(data)  
            data='push\tdword ['+ name +' + eax]'
            asmfileapp.append(data)
            prin(data)
            data='push formati'
            asmfileapp.append(data)
            prin(data)
            data='call printf'
            asmfileapp.append(data)
            prin(data)
        elif name in originalnum :
            data='push formatr'
  

def in_global(var):
    data = 'mov\teax,'+'['+var+']'
    asmfileapp.append(data)
    prin(data)           

def prin(data):
    print data

def removeall(nam,var):
    registermany[dictvariable[nam]] = ''
    dictvariable.pop(nam)    
 
def reallyclear():
    global dictvariable
    dictvariable = {}
    global lcprag
    lcprag = []
    global registermany
    registermany = {'eax':'','ebx':'','ecx':'','edx':'','esi':'','edi':'','ebp':'','esp':''}    


def assigningvalue(name):
    if name in lcprag :
        data='mov\t'+ registermany[dictvariable[name]] + ',eax'
        asmfileapp.append(data)
        prin(data)
    elif name in glprag :
        data='mov\tdword ['+ name + '],eax'
        asmfileapp.append(data)
        prin(data)
    else :
        z = assignmentvalues(name,'0000')
        data='mov\t'+ z + ',eax'
        asmfileapp.append(data)
        prin(data)
        
        
def assignmentvalues(nam,var):
    for e in registerless:
        if registermany[e] == '':
            registermany[e] = var
            dictvariable[nam] = e
            return e


def subassign(name,value,index):
    if index == '#' :
        if name in lcprag :
            if value in lcprag :
                data='mov\t'+registermany[dictvariable[name]]+','+ registermany[dictvariable[value]]
                asmfileapp.append(data)
                prin(data)
                data='mov\tdword [z1],'+ registermany[dictvariable[value]]
                asmfileapp.append(data)
                prin(data)
            elif value in glprag :
                data='mov\t'+registermany[dictvariable[name]]+',['+value+']'
                asmfileapp.append(data)
                prin(data)
                data='mov\tdword [z1],['+value+']'
                asmfileapp.append(data)
                prin(data)
            else :
                data='mov\t'+registermany[dictvariable[name]]+','+ value
                asmfileapp.append(data)
                prin(data)
                data='mov\tdword [z1],'+ value
                asmfileapp.append(data)
                prin(data)
        elif name in glprag :
            if value in lcprag :
                data='mov\tdword ['+name+'],'+ registermany[dictvariable[value]]
                asmfileapp.append(data)
                prin(data)
            elif value in glprag :
                in_global(value)
                data='mov\tdword ['+name+'],eax'
                asmfileapp.append(data)
                prin(data)
            else :
                data='mov\tdword ['+name+'],'+ value
                asmfileapp.append(data)
                prin(data)
        else :
            z=assignmentvalues(name,'0000')
            if value in lcprag :
                data='mov\t'+z+','+ registermany[dictvariable[value]]
                asmfileapp.append(data)
                prin(data)
                data='mov\tdword [z1],'+ registermany[dictvariable[value]]
                asmfileapp.append(data)
                prin(data)
            elif value in glprag :
                in_global(value)
                data='mov\t'+z+',eax'
                asmfileapp.append(data)
                prin(data)
                data='mov\tdword [z1],eax'
                asmfileapp.append(data)
                prin(data)
            else :
                data='mov\t'+z+','+ value
                asmfileapp.append(data)
                prin(data)
                data='mov\tdword [z1],'+ value
                asmfileapp.append(data)
                prin(data)
    else :
        if name in glprag :
            if index in lcprag :
                data='mov\teax,'+ registermany[dictvariable[index]]
                asmfileapp.append(data)
                prin(data)
                data='imul\teax,4'
                asmfileapp.append(data)
                prin(data) 
            elif index in glprag :
                data='mov\teax,['+index+']'
                asmfileapp.append(data)
                prin(data)
                data='imul\teax,4'
                asmfileapp.append(data)
                prin(data)
            else :
                data='mov\teax,' + index
                asmfileapp.append(data)
                prin(data)
                data='imul\teax,4'
                asmfileapp.append(data)
                prin(data)
                
            if value in lcprag :
                data='mov\tdword ['+name+' + eax],'+ registermany[dictvariable[value]]
                asmfileapp.append(data)
                prin(data)
            elif value in glprag :
                data='mov\tedx,['+value+']'
                asmfileapp.append(data)
                prin(data)
                data='mov\tdword ['+name+' + eax],edx'
                asmfileapp.append(data)
                prin(data)
            else :
                data='mov\tdword ['+name+' + eax],'+ value
                asmfileapp.append(data)
                prin(data)    
                
                
def subload(name,index) :
    if name in glprag :
        if index in lcprag :
            data='mov\teax,'+ registermany[dictvariable[index]]
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,4'
            asmfileapp.append(data)
            prin(data)
            data='mov\teax,['+ name +' + eax]'
            asmfileapp.append(data)
            prin(data)
        elif index in glprag :
            data='mov\teax,['+index+']'
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,4'
            asmfileapp.append(data)
            prin(data)
            data='mov\teax,['+ name +' + eax]'
            asmfileapp.append(data)
            prin(data)
        else :
            data='mov\teax,' + index
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,4'
            asmfileapp.append(data)
            prin(data)
            data='mov\teax,['+ name + ' + eax]'
            asmfileapp.append(data)
            prin(data)

def rsubassign(name,value) :
    if name in glprag :
        z = assignmentvalues(name, '0000')
        removeall(name,'')
        assignmentvalues(name,z)
        data = 'mov\t'+z+','+name
        asmfileapp.append(data)
        prin(data)        
        if value in lcprag :
            11111
        else :
            data = 'mov\tqword ['+z+'],'+ value
            asmfileapp.append(data)
            prin(data)
        removeall(name,'')
        
def actualparameter(name):
    if name in lcprag :
        data='push\t'+ registermany[dictvariable[name]]
        asmfileapp.append(data)
        prin(data)
    elif name in glprag :
        z = assignmentvalues(name,'0000')
        data='mov\t'+z+','+ name
        asmfileapp.append(data)
        prin(data)
        data='mov\teax,['+z+']'
        asmfileapp.append(data)
        prin(data)
        data='push\teax'
        asmfileapp.append(data)
        prin(data)
        removeall(name,'')
    else :
        data='mov\teax,'+ name
        asmfileapp.append(data)
        prin(data)
        data='push\teax'
        asmfileapp.append(data)
        prin(data)
        
        
def endactualparameter():
    for ee in range(len(formalrparamclast)) :
        xx = formalrparamclast[len(formalrparamclast)-1-ee]
        if xx in lcprag :
            data='pop\tdword '+ registermany[dictvariable[xx]]
            asmfileapp.append(data)
            prin(data)
        elif xx in glprag :
            z = assignmentvalues(xx,'0000')
            data='mov\t'+z+','+ xx
            asmfileapp.append(data)
            prin(data)
            data='pop\tdword ['+z+']'
            asmfileapp.append(data)
            prin(data) 
        
            
def isub(var1,var2):
    if var1 in lcprag :
        if var2 in lcprag :
            data='mov\teax,'+ registermany[dictvariable[var1]]
            asmfileapp.append(data)
            prin(data)
            data='sub\teax,'+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='mov\teax,'+ registermany[dictvariable[var1]]
            asmfileapp.append(data)
            prin(data)
            data='sub\teax,['+var2+']' 
            asmfileapp.append(data)
            prin(data)
        else :
            data='mov\teax,'+ registermany[dictvariable[var1]]
            asmfileapp.append(data)
            prin(data)
            data='sub\teax,'+ var2
            asmfileapp.append(data)
            prin(data)
    elif var1 in glprag :
        if var2 in lcprag :
            data='mov\teax,['+ var1 +']'
            asmfileapp.append(data)
            prin(data)
            data='sub\teax,'+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='mov\teax,['+var1+']'
            asmfileapp.append(data)
            prin(data)
            data='sub\teax,['+ var2 +']'
            asmfileapp.append(data)
            prin(data)
        else :
            data='mov\teax,['+ var1 +']'
            asmfileapp.append(data)
            prin(data)
            data='sub\teax,'+ var2
            asmfileapp.append(data)
            prin(data)
    else :
        if var2 in lcprag :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='sub\teax,'+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='sub\teax,['+var2+']' 
            asmfileapp.append(data)
            prin(data)
        else :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='sub\teax,'+ var2
            asmfileapp.append(data)
            prin(data)        
        

        
        
def imul(var1,var2):
    if var1 in lcprag :
        if var2 in lcprag :
            data='mov\teax,'+ registermany[dictvariable[var1]]
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,'+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='mov\teax,'+ registermany[dictvariable[var1]]
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,['+var2+']' 
            asmfileapp.append(data)
            prin(data)
        else :
            data='mov\teax,'+ registermany[dictvariable[var1]]
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,'+ var2
            asmfileapp.append(data)
            prin(data)
    elif var1 in glprag :
        if var2 in lcprag :
            data='mov\teax,['+ var1 +']'
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,'+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='mov\teax,['+var1+']'
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,['+ var2 +']'
            asmfileapp.append(data)
            prin(data)
        else :
            data='mov\teax,['+ var1 +']'
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,'+ var2
            asmfileapp.append(data)
            prin(data)
    else :
        if var2 in lcprag :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,'+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,['+var2+']' 
            asmfileapp.append(data)
            prin(data)
        else :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='imul\teax,'+ var2
            asmfileapp.append(data)
            prin(data)        
        


def iadd(var1,var2):
    if var1 in lcprag :
        if var2 in lcprag :
            data='mov\teax,'+ registermany[dictvariable[var1]]
            asmfileapp.append(data)
            prin(data)
            data='add\teax,'+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='mov\teax,'+ registermany[dictvariable[var1]]
            asmfileapp.append(data)
            prin(data)
            data='add\teax,['+var2+']' 
            asmfileapp.append(data)
            prin(data)
        else :
            data='mov\teax,'+ registermany[dictvariable[var1]]
            asmfileapp.append(data)
            prin(data)
            data='add\teax,'+ var2
            asmfileapp.append(data)
            prin(data)
    elif var1 in glprag :
        if var2 in lcprag :
            data='mov\teax,['+ var1 +']'
            asmfileapp.append(data)
            prin(data)
            data='add\teax,'+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='mov\teax,['+var1+']'
            asmfileapp.append(data)
            prin(data)
            data='add\teax,['+ var2 +']'
            asmfileapp.append(data)
            prin(data)
        else :
            data='mov\teax,['+ var1 +']'
            asmfileapp.append(data)
            prin(data)
            data='add\teax,'+ var2
            asmfileapp.append(data)
            prin(data)
    else :
        if var2 in lcprag :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='add\teax,'+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='add\teax,['+var2+']' 
            asmfileapp.append(data)
            prin(data)
        else :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='add\teax,'+ var2
            asmfileapp.append(data)
            prin(data)
            
               
def forrealaddition(var1,var2,var3) :
    if var1 in glprag :
        data = 'fld\tdword ['+var1+']'
        asmfileapp.append(data)
        prin(data)
    data = 'fld\tdword ['+var2+']'
    asmfileapp.append(data)
    prin(data)
    data = 'faddp\tst1,st0\nsub\tesp,8\nfstp\tqword [esp]\npush\tformatr\ncall\tprintf\nadd\tesp,12'
    asmfileapp.append(data)
    prin(data)
            
   
def forrealsubtraction(var1,var2,var3) :
    if var1 in glprag :
        data = 'fld\tdword ['+var1+']'
        asmfileapp.append(data)
        prin(data)
    data = 'fld\tdword ['+var2+']'
    asmfileapp.append(data)
    prin(data)
    data = 'fsubp\tst1,st0\nsub\tesp,8\nfstp\tqword [esp]\npush\tformatr\ncall\tprintf\nadd\tesp,12'
    asmfileapp.append(data)
    prin(data)

def compartor(var1,var2) :
    if var1 in lcprag :
        if var2 in lcprag :
            global dictvariable
            data='cmp\t'+registermany[dictvariable[var1]]+','+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='cmp\t'+registermany[dictvariable[var1]]+',['+var2+']' 
            asmfileapp.append(data)
            prin(data)
            removeall(var2,'')
        else :
            data='cmp\t'+registermany[dictvariable[var1]]+','+ var2
            asmfileapp.append(data)
            prin(data)
    elif var1 in glprag :
        if var2 in lcprag :
            data='cmp\t['+var1+'],'+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='mov\teax,['+var1+']'
            asmfileapp.append(data)
            prin(data)
            data='cmp\teax,['+ var2 +']'
            asmfileapp.append(data)
            prin(data)
        else :
            data='cmp\tdword ['+var1+'],'+ var2
            asmfileapp.append(data)
            prin(data)
    else :
        if var2 in lcprag :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='cmp\teax,'+ registermany[dictvariable[var2]]
            asmfileapp.append(data)
            prin(data)
        elif var2 in glprag :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='cmp\teax,['+ var2+']'
            asmfileapp.append(data)
            prin(data)
        else :
            data='mov\teax,'+ var1
            asmfileapp.append(data)
            prin(data)
            data='cmp\teax,'+ var2
            asmfileapp.append(data)
            prin(data)
    
    triplez = fdprag.findall(var1)
    if triplez[0][2] != '' :
        removeall(var1,'')
    triplez = fdprag.findall(var2)
    if triplez[0][2] != '' :
        removeall(var2,'')

def findfunc(name):
    if name in lcprag :
        111
    elif name in glprag :
        222
    else :
        lcprag.append(name)
        z = assignmentvalues(name,'0000')
        removeall(name,'')
        assignmentvalues(name,z)