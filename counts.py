# Instructions:
#
#   Implement each of the functions below to satisfy the problem, considering
#   the following:
#
#     1. does your solution work?
#     2. is your code clear and concise? is it readable?
#     3. is your code performant?
#
#   When you are done, upload your code to Github and send a link to
#   connor@fishtownanalytics.com.


from multiprocessing import Process
#import time

inlist = []

def process(i):
    """
    process() takes a single integer as an argument and does
    some background processing on it.
    process() should execute in constant time.
    """
    # multiprocessing.current_process().i

    # used for testing purposes 
    #print ("Starting %s \n" %name)
    #time.sleep(3)
    #print ("Exiting %s \n" %name)
    
    # process list by updating collection w/ passed in single ints
    inlist.append(i)
    
def min():
    """
    min() returns the minimum of all of the integers passed
    to process() so far.
    process() should execute in constant time.
    """
    # check if collection passed to process() so far is empty
    #assert len(process(s)) > 0, "process() arg is empty sequence"

    # assign tmp the first val inside collection 
    tmp = inlist[0]
    # for loop to iterate through collection to find minimum 
    for item in inlist:
        if item < tmp:
            tmp = item   
    return tmp   # return the minimum of all int

    """
    process(1)
    process(2)
    process(2)
    process(4)
    print(min())
    """

def avg():
    """
    avg() returns the average of all of the integers passed
    to process() so far.
    avg() should execute in constant time.
    """

    # call sum method to add up the values in the collection & div by the num of items
    # call len method to compute the # of vals in collection which is divided by sum total 
    mean = sum(inlist) / len(inlist)
    return mean  

    # alternate method would be calling the reduce method with lamda 
    # return reduce(lambda a, b: a + b, inlist) / len(inlist)


def mode():
    """
    mode() returns the mode (most frequently occurring) of
    all of the integers passed to process() so far.
    what's the execution time of mode? can mode() run in constant time?
    """

    # assumption: if more than 1 mode is found, return list of modes instead of single item

    # use dictionary to track occurance for each int w/ key rep int, val rep occurance count
    countdict = {}

    for item in inlist:
        # to process each int, check if int already exists in dict as a key
        if item in countdict: 
            # int already exists - increment the associated count (occurance count)
            countdict[item] = countdict[item]+1
        else: 
            # int does not exist - make new entry in dict for first occurance of new key
            countdict[item] = 1


  
    # call values method to return a list of val in dict
    countlist = countdict.values()

    maxcount = max(countlist)

    modelist = []
    # itering though the dict keys looking for a key w/ a val that matches max count
    for item in countdict:
         # when found such a key, place that key in the mode list 
        if countdict[item] == maxcount:
            # key/s assoc w/ count, appended to list of modes
            modelist.append(item)

    # check num of modes in collection if there's only one mode - output single item
    if len(modelist) <= 1:
        # for single mode - output single mode
        for item in modelist:
            return item
    else:   
        # more than 1 mode in collection - output list of modes
        return modelist

def median():
    """
    median() returns the median (50th percentile) of
    all of the integers passed to process() so far.
    what's the big-O execution time of median()?
    """

    # make copy of list using slice operator  
    copylist = inlist[:] 

    # sort list items in order by calling sort method from list class
    copylist.sort()

    # make deciion about whether there is even or odd num of items - using modulo operator 
    if len(copylist)%2 == 0:  
        # even length of num in collection
        rightmid = len(copylist)//2
        leftmid = rightmid - 1 
        median = (copylist[leftmid] + copylist[rightmid])/2.0
    else:   
        # odd length of num in collection 
        mid = len(copylist)//2
        median = copylist[mid]
    # use int method to truncate towards 0 (outputs int not decimal)
    return int(median) 


if __name__ == '__main__':
    process(1)
    process(2)
    process(2)
    process(4)

    p = Process(target=process, args=(int,))
    p.start()
    p.join()
    
    #background_process = multiprocessing.Process\
    #                     (name='background_process',\
    #                     target=process, args=(int,))
    #background_process.daemon = True
    
    #background_process.start()


print(min())  # should print "1"
print(avg())  # should print "2.25"
print(mode())  # should print "2"
print(median())  # should print "2"