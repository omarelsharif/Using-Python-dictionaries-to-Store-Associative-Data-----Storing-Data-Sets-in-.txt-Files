

# Omar El-Sharif 

'''After reading file1.txt (input this as the name of the first file)
and file2.txt (input this as the name of the second file),
this script does the following without using set operators.

• Lists of all the unique words contained in the first file.
• Lists of all the unique words contained in the second file.
• Lists of all the unique words contained in both files.
• Lists of the words that appear in both files.
• Lists of the words that appear in the first file but not the second file.
• Lists of the words that appear in the second file but not the first file.
• Lists of the words that appear in either the first or second file but not both files.
• Creates a frequency table of words counts in each file

'''


def read_file(file):

    file_ = open(file,'r')
    file1list = []
    for line in file_:
        line = line.split()
        for i in line:
            file1list.append(i)
    return file1list

def unique(n):
    
    emptyList = []
    for i  in n:
        if i in emptyList:
            continue
        emptyList.append(i)

    return emptyList

def countWordFile1(n):
    
    blankDict = {}
    for i in n:
        if i not in blankDict:
            blankDict[i] = 1
        else:
            blankDict[i] = blankDict[i] + 1
    return blankDict

 

def union(x,y):
    
    emptyList = []
    for i in x:
        if i in emptyList:
            continue
        emptyList.append(i)
        
    for i in y:
        if i in emptyList:
            continue
        
        emptyList.append(i)
        
    return emptyList

def intersect(x,y):

    v = unique(x)
    emptyList = []

    for i in v:
        if i in y:
            emptyList.append(i)
    return emptyList

def file1NotFile2(x,y):
    
    emptyList = []
    
    for i in x:
        if i in y:
            continue
        emptyList.append(i)
    return emptyList

def write_file(uw_file1,uw_file2,union,intersect,firstNotSec,secNotFirst,symmetricDiffrence,wordCount1,wordCount2):

    FileAnalysis = open('FileAnalysis.txt','w')
    FileAnalysis.write("Unique words in file 1: ")
    
    for i in uw_file1:
        FileAnalysis.write(i+' ')
    FileAnalysis.write('\n')
    FileAnalysis.write("Unique words in file 2: ")
    
    for i in uw_file2:
        FileAnalysis.write(i+' ')
    FileAnalysis.write('\n')

    
    FileAnalysis.write('Union of the words in files 1 and 2: ')
    for i in union:
        FileAnalysis.write(i+' ')
    FileAnalysis.write('\n')
    FileAnalysis.write('Intersection of the words in files 1 and 2: ')

    for i in intersect:
        FileAnalysis.write(i+' ')
    FileAnalysis.write('\n')
    FileAnalysis.write('Words in file 1 but not in file 2: ')

    for i in firstNotSec:
        FileAnalysis.write(i+' ')
    FileAnalysis.write('\n')

    FileAnalysis.write('Words in file2 but not in file 1: ')
    for i in secNotFirst:
        FileAnalysis.write(i+' ')
    FileAnalysis.write('\n')
    FileAnalysis.write('Words in file 1 but not in file 2 and words in file 2 but not in file 1: ')

    for i in symmetricDiffrence:
        FileAnalysis.write(i+' ')
        
    FileAnalysis.write('\n')
    FileAnalysis.write('\n')

    FileAnalysis.write('Frequency table for file 1: ')
    FileAnalysis.write('\n')
    FileAnalysis.write('{0:<20s} {1:s}'.format('Word','Count'))
    FileAnalysis.write('\n')

    for i in wordCount1:
        FileAnalysis.write('{0:<20s} {1:d}'.format(i,wordCount1[i]))
        FileAnalysis.write('\n')

    FileAnalysis.write('\n')
    FileAnalysis.write('Frequency table for file 2:')
    FileAnalysis.write('\n')
    FileAnalysis.write('{0:<20s} {1:s}'.format('Word','Count'))
    FileAnalysis.write('\n')

    for i in wordCount2:
        FileAnalysis.write('{0:<20s} {1:d}'.format(i,wordCount2[i]))
        FileAnalysis.write('\n')
        
    FileAnalysis.write('\n')

def main():

    file1 = input('Enter the name of the first file: ')
    file2 = input('Enter the name of the second file: ')
    list_file1,list_file2 = read_file(file1),read_file(file2)
    uwfile1,uwfile2 = unique(list_file1),unique(list_file2)
    union_ = union(list_file1,list_file2)
    intersect_ = intersect(list_file1,list_file2)
    firstNotSecond,secondNotFirst = file1NotFile2(list_file1,list_file2),file1NotFile2(list_file2,list_file1)
    symmetricDiffrence = firstNotSecond+secondNotFirst
    wordCount1 = countWordFile1(list_file1)
    wordCount2 = countWordFile1(list_file2)
    write_file(uwfile1,uwfile2,union_,intersect_,firstNotSecond,secondNotFirst,symmetricDiffrence,wordCount1,wordCount2)

    print('Data is saved in fileAnalysis.txt')

main()

 

