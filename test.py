'''This test.py file is used to test/check mehtods those defined in the assignmnet.py file
    make sure you import the file and intialize it's class- Assignmenrt instance by creating an object.'''

from assignment import Assignment
ass = Assignment()    #creating an object
""""Method calling, editing the method name, what you want to see/cehck. Having two schemas: 
   1). objectname.mehtodName() -->  this type of calling is used for methods those have a print function for their result.
   2). print(objectName.methodName()  --> this type of calling is used for methods those return their result. 
            you can assign there return value to a variable and print it.
"""
ass.reverse()       #sample method call for the "reverse" method.
