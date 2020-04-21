'''
You are given an array of desired filenames in the order of their creation. Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].

'''
def fileNaming(names):
    dic = {}
    new_names=[]
    for i in range(0, len(names)):
        if not names[i] in dic:
            dic[names[i]]=0
        dic[names[i]]+=1
        
        if dic[names[i]]>1:
            new_name=names[i]+"(" + str(dic[names[i]]-1) + ")"

            count_loop=0
            while new_name in dic:
                count_loop+=1
                new_name=names[i]+"(" + str(dic[new_name]+count_loop-1) + ")"

            names[i]=new_name
            if not new_name in dic:
                dic[new_name]=0
            dic[new_name]+=1
            
    return names