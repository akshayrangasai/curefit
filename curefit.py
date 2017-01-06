def GenerateSequence(Codon):
    loopsize = len(Codon)+1
    finalarray = []
    for i in range(1,loopsize):
        for j in range(1,loopsize):
            for k in range(1,loopsize):
                    finalarray.append(Codon[i-1]+Codon[j-1]+Codon[k-1])
    print ' '.join(finalarray)
    print len(finalarray)
    return finalarray

def Translate(code,keyarray,splicelength):
    message = []
    for i in range(0,len(code),splicelength):
        try:
            DNA = code[i]+code[i+1]+code[i+2]
            DNA = ''.join(DNA)
            print keyarray[DNA],
            message.append(keyarray[DNA])
        except:
            print
    return message

Key = GenerateSequence('TCAG')
Pair = ['&','*']
ABCD = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
NUMBERS = "0 1 2 3 4 5 6 7 8 9"
SPECIALS = "~ ! @ # $ % ^ & * ( ) + - { } \ / < > , . ? : ; `"
SPACE = ' '
Pair+=ABCD.split() + NUMBERS.split() + SPECIALS.split()
Pair.append(SPACE)
Decode = dict(zip(Key,Pair))
#print Decode
FILE = open('Read.TXT','r+')
#print FILE
code = FILE.readline()

message = Translate(code,Decode,3)
FILE.write(''.join(message))
