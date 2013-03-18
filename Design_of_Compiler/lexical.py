import re
import math
import flag
import parser
import datetime
digits=0            # variable digits to count significant no of digits
data_int=''         # Temporary variable
data=''             # Temporary variable
flag_pound=False    # flag to check for ##
flag_multi=False    # flag to check for multi line comments
flag_single=False   # flag to check for single line comments
flag_double=True    # flag to check for double quotes
stack = []
inline=[]
# Code to print date time & partner information
now = datetime.datetime.now()
print "Partners:Jinen Gandhi and Samarth Shah"
print "E-mail id: jgandhi@clemson.edu and samarts@clemson.edu"
print "Time:",now.strftime("%m-%d-%Y %H:%M:%S");


# Function to find significant no of digits
def find_sigfigs(x):    
    x = x.lower()
    if ('e' in x):       
        myStr = x.split('e')
        return len( myStr[0] ) - 1 
    else:       
        n = ('%.*e' %(8, float(x))).split('e')        
        if '.' in x:
            s = x.replace('.', '')            
            l = len(s) - len(s.rstrip('0'))            
            n[0] = n[0].rstrip('0') + ''.join(['0' for num in xrange(l)])
        else:            
            n[0] = n[0].rstrip('0')        
    return find_sigfigs('e'.join(n))

# Dictionary function which stores tokens
def dictionary(arg1):
    dictic = {'END':'39', 'PROGRAM':'40','var':'41','DECLARE':'42',';':'43','integer':'44','::':'45', 'INTEGER':'46', 'REAL':'47', '}':'48', 'PROCEDURE':'49', ',':'50', '{':'51', 'VALUE':'52', 'REFERENCE':'53', 'MAIN':'54', '[':'55', ']':'56', ':':'57', 'INPUT':'58', 'string':'59', 'OUTPUT':'60', 'CALL':'61', 'ELSE':'62', 'IF':'63', '(':'64',')':'65', 'THEN':'66', 'DO':'67', 'WHILE':'68', '<-':'69', '|':'70','&':'71', '!':'72', '<':'73', '<=':'74', '>':'75', '>=':'76', '==':'77', '!=':'78', '+':'79', '-':'80', '*':'81', '/':'82','real':'83'};
    return dictic[arg1],arg1

# Code to find the group of word word
conditions=re.compile('(\".*?\")|(##|/\*|\*/|//|")|([-+]?\d+\.\d+)|([+-]?\d+)|(==|!=|<=|>=|<-|::)|(;|:|,|\[|\]|\(|\)|<|>|!|\+|\-|\*|/|{|}|\||&)|([a-z][a-zA-Z0-9_]+|[a-z])|([A-Z]+)|(\.|`|~|@|^|=)')
for line in open("/Users/Samarth/Documents/Dropbox/testdata/arithmetic.txt"):
    flag.lcount=flag.lcount+1
    
    if "##" in line:
        p=re.compile('\##|[+|-]\d+')
        m=p.findall(line)
    for ii in m: 
        if ii=="+1":
            flag.flag1=1
        elif ii=="-1":
            flag.flag1=0
        elif ii=="+2":
            flag.flag2=1
        elif ii=="-2":
            flag.flag2=0
        elif ii=="+7":
            flag.flag7=1
        elif ii=="-7":
            flag.flag7=0
        elif ii=="+8":
            flag.flag8=1
        elif ii=="-8":
            flag.flag8=0
        elif ii=="+9":
            flag.flag9=1
        elif ii=="-9":
            flag.flag9=0
        elif ii=="+10":
            flag.flag10=1
        elif ii=="-10":
            flag.flag10=0
        elif ii=="+12":
            flag.flag12=1
        elif ii=="-12":
            flag.flag12=0
        elif ii=="+13":
            flag.flag13=1
        elif ii=="-13":
            flag.flag13=0
        elif ii=="+14":
            flag.flag14=1
        elif ii=="-14":
            flag.flag14=0
        elif ii=="+15":
            flag.flag15=1
        elif ii=="-15":
            flag.flag15=0
        elif ii=="+16":
            flag.flag16=1
        elif ii=="-16":
            flag.flag16=0
        
            
    if flag.flag1==1:
        #print
        print line
    A=[]
    kk = 0;
    if 1==1:
        line_check = conditions.findall(line)
        for word_line in line_check:
            i=1;
            for word in word_line:
                if(word!=''):
                    break;
                i=i+1;
            if(word=="##"):
                if flag_pound==False:
                    flag_pound=True
                else:
                    flag_pound=False
            if(word=='"'):
                if flag_double==True:
                    flag_double=False
                else:
                    flag_double=True            
            if(word=="/*"):
                flag_multi=True
            if(word=="*/"):
                flag_multi=False
            if(word=="//"):
                break;
            if i==1 :
                inline.append(word)
                data="Token Code of "+word+" is 59";
                if flag.flag2==1:
                    print '{:>60}'.format(data)
                A.append('59')
                kk =1

            if i==3 and flag_multi==False and flag_pound==False and flag_double==True:  # Group 1 is Real numbers group
                if "+" in word:
                    word=word.split('+')
                    word=word[1]
                    data="Token Code of + is 79";
                    if flag.flag2==1:
                        print '{:>60}'.format(data)
                    A.append('79')
                    inline.append(word)
                    kk=1
                y=find_sigfigs(word)
                if y<=7:
                    a,b=dictionary('real')
                    data="Token Code of "+word+" is "+a;
                    if flag.flag2==1:
                        print '{:>60}'.format(data)
                    A.append(a)
                    inline.append(word)
                    kk=1
                else:
                    print '{:>60}'.format("Significant digits are greater than 7");
                    
                    
            if i==4 and flag_multi==False and flag_pound==False and flag_double==True:  # Group 2 is Integers group
                data_int=word
                if "+" in word:
                    word=word.split('+')
                    word=word[1]
                    data="Token Code of + is 79";
                    if flag.flag2==1:
                        print '{:>60}'.format(data)
                    A.append('79')
                    inline.append(word)
                    kk=1
                    digits = len(word)
                if "-" in data_int:
                    digits = len(data_int)-1
                if digits<=9:
                    a,b=dictionary('integer')
                    data="Token Code of "+word+" is "+a;
                    if flag.flag2==1:
                        print '{:>60}'.format(data)
                    A.append(a)
                    inline.append(word)
                    kk=1
                else:
                    data="Bad Integer "+word;
                    if flag.flag2==1:
                        print '{:>60}'.format(data);
                    

            if i==5 and flag_multi==False and flag_pound==False and flag_double==True:  # Group 3 is Multi Ascii characters group
                    a,b=dictionary(word)
                    data="Token Code of "+b+" is "+a;
                    if flag.flag2==1:
                        print '{:>60}'.format(data)
                    A.append(a)
                    inline.append(word)
                    kk=1
            if i==6 and flag_multi==False and flag_pound==False and flag_double==True:  # Group 4 is Single Ascii character group
                    a,b=dictionary(word)
                    data="Token Code of "+b+" is "+a;
                    if flag.flag2==1:
                        print '{:>60}'.format(data)
                    A.append(a)
                    inline.append(word)
                    kk=1
            if i==7 and flag_multi==False and flag_pound==False and flag_double==True:  # Group 5 is identifiers group
                if len(word)<=16:
                    a,b=dictionary('var')
                    data="Token Code of "+word+" is "+a;
                    if flag.flag2==1:
                        print '{:>60}'.format(data)
                    A.append(a)
                    inline.append(word)
                    kk=1
                else:
                    data="Invalid Idetifier "+word;
                    if flag.flag2==1:
                        print '{:>60}'.format(data);
                    
            if i==8 and flag_multi==False and flag_pound==False and flag_double==True:  # Group 6 is keywords group
                list1=['END','PROGRAM','DECLARE','REAL','INTEGER','PROCEDURE','VALUE','REFERENCE','MAIN','INPUT','OUTPUT','CALL','ELSE','IF','THEN','DO','WHILE']
                if word in list1:
                    a,b=dictionary(word)
                    data="Token Code of "+b+" is "+a;
                    if flag.flag2==1:
                        print '{:>60}'.format(data)
                    A.append(a)
                    inline.append(word)
                    kk=1
                else:
                    data="Invalid Keyword "+word;
                    if flag.flag2==1:
                        print '{:>60}'.format(data);
           
            if i==9 and flag_multi==False and flag_pound==False and flag_double==True: # Group 7 is invalid ascii characters group
                    data="Invalid Ascii Character"+word;
                    if flag.flag2==1:
                        print '{:>60}'.format(data)
    if kk == 1:
        parser.reduc(stack, A,inline)
        kk=0
        A = []
        inline = []
parser.red1(stack,inline)
