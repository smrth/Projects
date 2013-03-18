'''
Created on Mar 27, 2012

@author: Samarth
'''

import pragfunction
        
def tuples(field1,field2,field3,field4,field5,globalsem):
    if field2=='STARTPROGRAM':
        name=field1+'.asm'
        pragfunction.asmfileapp.append(name)
        pragfunction.prin(name)
        
        
    elif field2=='ENDPROGRAM':
        data = 'mov esp, ebp\npop dword ebp'
        pragfunction.asmfileapp.append(data)
        pragfunction.prin(data) 
        data = 'ret\n'
        pragfunction.asmfileapp.append(data)
        pragfunction.prin(data)
        prag=open(pragfunction.asmfileapp[0],'w+')
        pragfunction.asmfileapp.pop(0)
        prag.write('global main\nextern printf\n')
        for e in pragfunction.numberfororiginal :
            e = e + ':\tresd\t1'
            pragfunction.bss.append(e)
        for e in pragfunction.printdatasec :
            e = e + '\n'
            prag.write(e)
        for e in pragfunction.bss :
            e = e + '\n'
            prag.write(e)
        for e in pragfunction.asmfileapp :
            e = e + '\n'
            prag.write(e)
        prag.close()
    
    
    elif field2 == 'ENDDECLARATION' and globalsem == 0 :
        pragfunction.asmfileapp.append('SECTION .text\n')
        pragfunction.prin('SECTION .text\n')
        
            
    elif field2=='MEMORY' and globalsem == 0 and field5 == 'INTEGER':
        pragfunction.originalintnum.append(field1)
        if field3 == 1:
            data = field1+':\tresd\t'+str(field3)
            pragfunction.glprag.append(field1)
            pragfunction.bss.append(data)
            pragfunction.prin(data)
        elif field4 == 0:
            data = field1+':\tresd\t'+str(int(field3))
            pragfunction.glprag.append(field1)
            pragfunction.bss.append(data)
            pragfunction.prin(data)
        else:
            data = field1+':\tresd\t'+str(int(field3)*int(field4))
            pragfunction.glprag.append(field1)
            pragfunction.bss.append(data)
            pragfunction.prin(data)
            
        
    elif field2=='MEMORY' and globalsem == 1 and field5 == 'INTEGER':
        pragfunction.originalintegerroll.append(field1)
        if field3 == 1:
            z = pragfunction.assignmentvalues(field1,'0000')
            pragfunction.removeall(field1,'')
            pragfunction.assignmentvalues(field1,z)
            pragfunction.lcprag.append(field1)
            
            
    elif field2=='MEMORY' and globalsem == 0 and field5 == 'REAL':
        pragfunction.originalnum.append(field1)
        if field3 == 1:
            pragfunction.glprag.append(field1)
            pragfunction.numberfororiginal.append(field1)
    
    
    elif field2 == 'ENDPROCEDURE' :
        for ee in pragfunction.formalrparam :
            data = 'push\t'+pragfunction.registermany[pragfunction.dictvariable[ee]]
            pragfunction.asmfileapp.append(data)
            pragfunction.prin(data)
            pragfunction.removeall(ee,'')
        pragfunction.formalrparam = []
        pragfunction.reallyclear()
        data = 'mov esp, ebp\npop dword ebp'
        pragfunction.asmfileapp.append(data)
        pragfunction.prin(data) 
        data = 'ret'
        pragfunction.asmfileapp.append(data)
        pragfunction.prin(data)
    
    
    elif field2 == 'BEGINPROCEDURE' :
        data = field1+':\t'
        pragfunction.asmfileapp.append(data)
        pragfunction.prin(data)
        data = 'push ebp\nmov ebp, esp'
        pragfunction.asmfileapp.append(data)
        pragfunction.prin(data) 
    
    
    elif field2 == 'LABEL' :
        if field1 == 'MAIN' :
            data = field1.lower()+':\t'
            pragfunction.asmfileapp.append(data)
            pragfunction.prin(data) 
            data = 'push ebp\nmov ebp, esp'
            pragfunction.asmfileapp.append(data)
            pragfunction.prin(data) 
        else :
            data = field1+':\t'
            pragfunction.asmfileapp.append(data)
            pragfunction.prin(data)
    
    
    elif field2 == 'JUMP' :
        data = 'jmp\t'+field1
        pragfunction.asmfileapp.append(data)
        pragfunction.prin(data)
    
    
    elif field2 == 'CALL' :
        if field1 == 'PRINTF' :
            pragfunction.optimusprime  = 1
        else :
            data =field2+'\t'+field1
            pragfunction.asmfileapp.append(data)
            pragfunction.prin(data)
    
    
    elif field2 == 'ACTUALVALdasbsUESUBPARAMETER' :
        data =field2+'\t'+field1
        pragfunction.asmfileapp.append(data)
        pragfunction.prin(data)
        
    
    elif field2 == 'ISUB' :
        pragfunction.findfunc(field1)
        pragfunction.isub(field3,field4)
        pragfunction.assigningvalue(field1)
        triplez = pragfunction.fdprag.findall(field3)
        if triplez[0][2] != '' :
            pragfunction.removeall(field3,'')
        triplez = pragfunction.fdprag.findall(field4)
        if triplez[0][2] != '' :
            pragfunction.removeall(field4,'')
    
    
    elif field2 == 'IADD' :
        pragfunction.findfunc(field1)
        pragfunction.iadd(field3,field4)
        pragfunction.assigningvalue(field1)
        triplez = pragfunction.fdprag.findall(field3)
        if triplez[0][2] != '' :
            pragfunction.removeall(field3,'')
        triplez = pragfunction.fdprag.findall(field4)
        if triplez[0][2] != '' :
            pragfunction.removeall(field4,'')
    
    
    elif field2 == 'IMUL' :
        pragfunction.findfunc(field1)
        pragfunction.imul(field3,field4)
        pragfunction.assigningvalue(field1)
        triplez = pragfunction.fdprag.findall(field3)
        if triplez[0][2] != '' :
            pragfunction.removeall(field3,'')
        triplez = pragfunction.fdprag.findall(field4)
        if triplez[0][2] != '' :
            pragfunction.removeall(field4,'')
    
    
    elif field2 == 'IMULT' :
        pragfunction.findfunc(field1)
        pragfunction.imul(field3,field4)
        pragfunction.assigningvalue(field1)
        triplez = pragfunction.fdprag.findall(field3)
        if triplez[0][2] != '' :
            pragfunction.removeall(field3,'')
        triplez = pragfunction.fdprag.findall(field4)
        if triplez[0][2] != '' :
            pragfunction.removeall(field4,'')
        
    elif field2 == 'ISUBASSIGN' :
        pragfunction.findfunc(field1)
        pragfunction.subassign(field1,field3,field4)
        triplez = pragfunction.fdprag.findall(field3)
        if triplez[0][2] != '' :
            pragfunction.removeall(field3,'')
    
    
    elif field2 == 'SUBLOAD' :
        pragfunction.findfunc(field1)
        pragfunction.subload(field3,field4)
        pragfunction.assigningvalue(field1)
        triplez = pragfunction.fdprag.findall(field3)
        if triplez[0][2] != '' :
            pragfunction.removeall(field3,'')
        triplez = pragfunction.fdprag.findall(field4)
        if triplez[0][2] != '' :
            pragfunction.removeall(field4,'')
            
            
            
    elif field2 == 'ILT' :
        pragfunction.kudkomarahiya = 'lessthan'
        pragfunction.compartor(field3,field4)
            
            
            
    elif field2 == 'IGT' :
        pragfunction.kudkomarahiya = 'greaterthan'
        pragfunction.compartor(field3,field4)
            
            
            
    elif field2 == 'ILE' :
        pragfunction.kudkomarahiya = 'lessthanequal'
        pragfunction.compartor(field3,field4)
            
            
            
    elif field2 == 'IGE' :
        pragfunction.kudkomarahiya = 'greaterthanequal'
        pragfunction.compartor(field3,field4)
            
            
            
    elif field2 == 'IEQ' :
        pragfunction.kudkomarahiya = 'equal'
        pragfunction.compartor(field3,field4)
            
            
            
    elif field2 == 'INE' :
        pragfunction.kudkomarahiya = 'notequal'
        pragfunction.compartor(field3,field4)
    
    
    elif field2 == 'CJUMP' :
        if pragfunction.kudkomarahiya == 'lessthan' :
            data = 'jg\t'+field1
            pragfunction.asmfileapp.append(data)
            pragfunction.prin(data)
        elif pragfunction.kudkomarahiya == 'greaterthan' :
            data = 'jl\t'+field1
            pragfunction.asmfileapp.append(data)
            pragfunction.prin(data)
        elif pragfunction.kudkomarahiya == 'lessthanequal' :
            data = 'jge\t'+field1
            pragfunction.asmfileapp.append(data)
            pragfunction.prin(data)
        elif pragfunction.kudkomarahiya == 'greaterthanequal' :
            data = 'jle\t'+field1
            pragfunction.asmfileapp.append(data)
            pragfunction.prin(data)
        elif pragfunction.kudkomarahiya == 'equal' :
            data = 'jne\t'+field1
            pragfunction.asmfileapp.append(data)
            pragfunction.prin(data)
        elif pragfunction.kudkomarahiya == 'notequal' :
            data = 'je\t'+field1
            pragfunction.asmfileapp.append(data)
            pragfunction.prin(data)
        pragfunction.kudkomarahiya = ''
            
            
            
    elif field2 == 'FORMALVALUEPARAMETER' :
        z = pragfunction.assignmentvalues(field1,'0000')
        pragfunction.removeall(field1,'')
        pragfunction.assignmentvalues(field1,z)
        pragfunction.lcprag.append(field1)
        data = 'pop\tdword '+z
        pragfunction.asmfileapp.append(data)
        pragfunction.prin(data)
            
            
            
    elif field2 == 'FORMALREFERENCEPARAMETER' :
        1
            
            
            
    elif field2 == 'ACTUALVALUESUBPARAMETER' :
        pragfunction.actualparameter(field3) 
            
            
            
    elif field2 == 'ACTUALREFERENCESUBPARAMETER' :
        pragfunction.formalrparamclast.append(field3)
        pragfunction.actualparameter(field3)

            
                        
    elif field2 == 'BEGINACTUALPARAMETERLIST' :
        pragfunction.asmfileapp.pop()

               
            
    elif field2 == 'ENDACTUALPARAMETERLIST' :
        data ='call\t'+field1
        pragfunction.asmfileapp.append(data)
        pragfunction.prin(data)
        
        
    elif field2 == 'RADD' :
        pragfunction.findfunc(field1)
        pragfunction.alltypeinc = 'radd'
        pragfunction.variablerep = field3
        pragfunction.variablereprepag = field4
        triplez = pragfunction.fdprag.findall(field3)
        if triplez[0][2] != '' :
            pragfunction.removeall(field3,'')
        triplez = pragfunction.fdprag.findall(field4)
        if triplez[0][2] != '' :
            pragfunction.removeall(field4,'')
        
        
    elif field2 == 'RSUB' :
        pragfunction.findfunc(field1)
        pragfunction.alltypeinc = 'rsub'
        pragfunction.variablerep = field3
        pragfunction.variablereprepag = field4
        triplez = pragfunction.fdprag.findall(field3)
        if triplez[0][2] != '' :
            pragfunction.removeall(field3,'')
        triplez = pragfunction.fdprag.findall(field4)
        if triplez[0][2] != '' :
            pragfunction.removeall(field4,'')
        
        
    elif field2 == 'RSUBASSIGN' and field3[1] == '$' :
        pragfunction.findfunc(field1)
        if pragfunction.alltypeinc == 'radd' :
            pragfunction.forrealaddition(pragfunction.variablerep,pragfunction.variablereprepag,field1)
        elif pragfunction.alltypeinc == 'rsub' :
            pragfunction.forrealsubtraction(pragfunction.variablerep,pragfunction.variablereprepag,field1)
        triplez = pragfunction.fdprag.findall(field3)
        if triplez[0][2] != '' :
            pragfunction.removeall(field3,'')
        
        
    elif field2 == 'RSUBASSIGN' :
        pragfunction.findfunc(field1)
        if field1 in pragfunction.numberfororiginal :
            data = field1+':\t dd\t'+field3
            pragfunction.printdatasec.append(data)
            for eac in range(len(pragfunction.numberfororiginal)) :
                if pragfunction.numberfororiginal[eac] == field1 :
                    mm = eac
            pragfunction.numberfororiginal.pop(mm)
        triplez = pragfunction.fdprag.findall(field3)
        if triplez[0][2] != '' :
            pragfunction.removeall(field3,'')
    
    
    elif field2 == 'OUTPUTPARAMETER' :
        if field3 != '" "' and pragfunction.optimusprime == 1 :
            pragfunction.printdata(field3)
    
    
    elif field2 == 'OUTPUTSUBPARAMETER' :
        if field3 != '" "' and pragfunction.optimusprime == 1 :
            pragfunction.printingdatasub(field3,field4)
    
    
    elif field2 == 'ENDOUTPUTPARAMETERS' :
        pragfunction.optimusprime = 0
