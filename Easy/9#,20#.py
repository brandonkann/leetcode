class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        val = str(x)
        if (val[:: -1] == val): 
            return True 
        else:
            return False 

        
class Solution1(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack =  Stack()
        
        for val in s:
            if (val == '{' or val == '[' or val == '(' ):
                stack.push(val)
            elif (stack.isEmpty() and val == ']'):
                return False
            elif (stack.isEmpty() and val == '}'):
                return False
            elif (stack.isEmpty() and val == ')'):
                return False
            else:
                return True
        
    
    

class Stack: 
    def __init__ (self):
        self.items = []
        
    def pop(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        return (self.items.append(item))

    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[0]


    

            
        