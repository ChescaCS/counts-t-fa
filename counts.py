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
import time
# import os - used for testing purposes 

inlist = []

def process(i):
    """
    process() takes a single integer as an argument and does
    some background processing on it.
    process() should execute in constant time.
    """

    startTime = time.time()

    inlist.append(i)

    print('process() runtime: ', time.time() - startTime)

def min():
    """
    min() returns the minimum of all of the integers passed
    to process() so far.
    process() should execute in constant time.
    """

    startTime = time.time()

    # check if collection passed to process() so far is empty
    assert len(inlist) > 0, "process() is empty collection"

    # assign tmp the first val inside collection 
    tmp = inlist[0]
    # for loop to iterate through collection to find minimum 
    for item in inlist:
        if item < tmp:
            tmp = item   
    print('min() runtime: ', time.time() - startTime)
    return tmp   # return the minimum of all int

def avg():
    """
    avg() returns the average of all of the integers passed
    to process() so far.
    avg() should execute in constant time.
    """

    startTime = time.time()

    # call sum method to add up the values in the collection & div by the num of items
    # call len method to compute the # of vals in collection which is divided by sum total 
    mean = sum(inlist) / len(inlist)
    print('avg() runtime: ', time.time() - startTime)
    return mean  

    # alternate method would be calling the reduce method with lamda 
    # return reduce(lambda a, b: a + b, inlist) / len(inlist)

def mode():
    """
    mode() returns the mode (most frequently occurring) of
    all of the integers passed to process() so far.
    what's the execution time of mode? can mode() run in constant time?

    -      -      -
    fk answer: the execution time of mode is 1.0013580322265625e-05

    for mode() to run in constant time, it would need to consist of simple statements (basic ops) 
    in order to have the time for each statement beconstant & the total time also be constant O(1)
    """

    startTime = time.time()

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
            print('mode() runtime: ', time.time() - startTime)
            return item

    else:   
        print('mode() runtime: ', time.time() - startTime)
        # more than 1 mode in collection - output list of modes
        return modelist

def median():
    """
    median() returns the median (50th percentile) of
    all of the integers passed to process() so far.
    what's the big-O execution time of median()?
    -      -      -
    fk answer: big-O execution time of median() is in linear-time : O(N) 
    when executing the provided process calls with four calls to 1,2,2,4
    the execution time of median() consisted of: 1.4066696166992188e-05 

    when tested w/ five, six or more input integers (passed in from process()): 
    execution time gradually increased as follows: 3.814697265625e-06, 4.0531158447265625e-06,...n^k+

    Besides testing execution time of testing scenerios, can determine time complexity as follows:

    In median func utilized if-then-else statement, thus if:
    if(...) seq 1 else seq 2...either sequence 1 will execute, or sequence 2 will execute 
    Therefore, the worst-case time is the slowest of the two possibilities: max(time(sequence 1), time(sequence 2))
    For ex, if sequence 1 is O(N) and sequence 2 is O(1)- worst-case time complete if-then-else statement would be O(N)
    """
    # for testing purposes - to test execution time
    # startTime = time.time()  

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

    # for testing purposes only - testing execution time
    #print('median() runtime: ', time.time() - startTime)

    # use int method to truncate towards 0 (outputs int not decimal)
    return int(median) 


# testing function to check run time
def calcRunTime(function, *args):  
    """
    running a function & returning run time w/ result of function
    for func like process which require arg, can be passed in for testing purposes
    """

    startTime = time.time()

    result = function(*args)

    return time.time() - startTime, result


if __name__ == '__main__': 
    p = Process(target=process, args=(int,))
    p.start()
    p.join()


process(1)
process(2)
process(2)
process(4)


print(min())  # should print "1"
print(avg())  # should print "2.25"
print(mode())  # should print "2"
print(median())  # should print "2"