class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = s.lower()
        arr = [char for char in ls if char.isalnum()]
        l = len(arr)
        for i in range(0, int(l/2)):
            if arr[i] != arr[l-i-1]:
                return False
        return True
