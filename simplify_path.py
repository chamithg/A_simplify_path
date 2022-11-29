class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        output =""
        
        pointer = 0
        if path[-1] != "/":
            path += "/"
        
        while pointer < len(path):
            if path[pointer] =="/":
                if output == "" or output[-1] != "/": 
                    output+="/"
            elif path[pointer] ==".":
                if path[pointer+1] == "." and path[pointer+2] != ".":
                    if output!= "":
                        output = output[:-2]
                    pointer +=1
                if path[pointer+1] == "." and path[pointer+2] == ".":
                    while path[pointer] == ".":
                        output += path[pointer]
                        pointer +=1
                    pointer -=1
            else:
                output += path[pointer]
            pointer +=1
        if len(output)>1 and output[-1] =="/":
            output = output[:-1]   
        return output
        
obj = Solution()

path = "/home//foo/"
path1 = "/../"
path2 ="/a/./b/../../c/" # /c
path3 = "/a//b////c/d//././/.."
path5 ="/.../fdsafd/"

print(obj.simplifyPath(path5))