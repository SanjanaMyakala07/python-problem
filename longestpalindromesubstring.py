class LongestPalindromicSubstringBruteForce:
    def longest_palindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""  

        longest = "" 
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]  
                if self.is_palindrome(substring):
                    if len(substring) > len(longest):
                        longest = substring
        return longest
    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False  
            left += 1
            right -= 1
        return True  
solution = LongestPalindromicSubstringBruteForce()
print(solution.longest_palindrome("babad"))  
print(solution.longest_palindrome("cbbd"))  
