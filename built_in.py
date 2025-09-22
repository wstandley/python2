"""
    This is for Assignment OOP 2.9 Inheriting Properties from built in Classes
"""

class VowelString(str):
    def __new__(cls, name):
        return super().__new__(cls, name)

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        count = 0
        for char in self:
            if char in vowels:
                count += 1
        return count
    
name = VowelString("William Standley")
vowel_count = name.count_vowels()

print(f"The number of vowels in '{name}' is: {vowel_count}")