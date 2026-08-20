class Solution:
    def isPalindrome(self, s: str) -> bool:
        fixed = "".join(char.lower() for char in s if char.isalnum())
        reversed = fixed[::-1]
        if fixed == reversed:
            return True
        else:
            return False
        