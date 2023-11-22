"""
Question1
"""

word = input("Please enter a word:")
wordCount = len(word)
endR = wordCount - 1

if word.lower() != "wow":
    print(word[0],word[endR])
