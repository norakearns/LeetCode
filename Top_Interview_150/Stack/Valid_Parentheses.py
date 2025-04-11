class Solution:
    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

        Input: s = "()"
        Output: true
        """
        if len(s) == 1:
            return False
        
        stack = []

        for char in s: 
            if char == '(' or char == '{' or char == '[':
                stack.append(char) 
            else:
                if stack:
                    prev_char = stack.pop()
                    if char == "}" and prev_char != "{":
                        return False
                    elif char == "]" and prev_char != "[":
                        return False
                    elif char == ")" and prev_char != "(":
                        return False
                else:
                    return False
        
        if stack:
            return False
        else:
            return True


