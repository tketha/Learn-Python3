'''Define a function which can generate a list where the values are
square of numbers between 1 and 20 (both included). Then the function
needs to print the last 5 elements in the list.'''
def printList():
        li=list()
        for i in range(1,21):
                li.append(i**2)
        print(li[-5:])
printList()