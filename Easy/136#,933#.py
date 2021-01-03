#933:
class RecentCounter(object):

    def __init__(self):
        self.slide_window = deque()

        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
         # step 1). append the current call
        self.slide_window.append(t)

        # step 2). invalidate the outdated pings
        while self.slide_window[0] < t - 3000:
            self.slide_window.popleft()

        return len(self.slide_window)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()


#136

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashtable = [[] for vals in range(0, 3*10**4)]
        
        for vals in nums:
            hash_key = vals 
            hash_function = hash_key % len(hashtable)
            hashtable[hash_function].append(vals)
        
        for x in hashtable:
            if (len(x) == 1):
                return(x[0])
            else:
                pass 
            
            
            
            
            
            
            
            
        
