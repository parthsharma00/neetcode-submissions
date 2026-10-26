class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mydict = {}

        for i in strs:
            x = "".join(sorted(i))
            if x in mydict:
                list = mydict[x] + [i]
                mydict[x] = list
            else:
                mydict[x] = [i]
        L = []
        for i in mydict:
            L = L + [mydict[i]]
        return L

            
            
                
            
            


                
            