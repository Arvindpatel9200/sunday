                        # dictionary is a collection of  key value pair.......{}
                        #unorderd ..........creat with the help of {}
                        # we are creat nested dictionary
                        #its a mutable (we can change)
                        # con not cantain duplcate keys.....

mydict={
    "arvind":"gentalman","mahi":"lovely person",
    "both":"02",1:2,                                            #we can write umeric value as a string
    "anotherdict":{"love":"understanding"}
    
}

print(mydict['anotherdict']['love'])
print(mydict['both'])

                            #dictionary method 

print(list(mydict.keys()))                #view all keys whos present in dictionary
print(list(mydict.values()))              #view all value whos present in dictionary
print(list(mydict.items()))               #view all items(key-value) whos present in dictionary

mydictupadate={
    "abhi":"dog",
    "ravi":"cat"
}
mydict.update(mydictupadate)
print(mydict.get(1))
print(mydict[1])
print(mydict)
