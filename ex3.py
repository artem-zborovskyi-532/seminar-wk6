# Exercise 3: reinventing the wheel!
    # For this question we are emulating the method split() from the type str. Write the
    # algorithm for a function splitText(text:String, delimiters:String) which
    # returns the list of the words by splitting the string text at each delimiters. The delimiters
    # themselves are discarded. An example is given below:
        # >>> sampleText = "As Python's creator, I'd like to say a
        # few words about its origins."
        # >>> splitText(sampleText, ", '.")
        # ['As', 'Python', 's', 'creator', 'I', 'd', 'like', 'to',
        # 'say', 'a', 'few', 'words', 'about', 'its', 'origins']
    # You can assume that a string has a method contains(Character) that returns true if the
    # character is in the string, false otherwise. This exercise is more challenging than it may look
    # like.

def splitText(text:str, delimiters:str) -> list[str]:
    res = []
    word = []
    for char in text:
        if char in delimiters:
            if word:
                res.append("".join(word))
                word = []
        else:
            word += char
    if word:
        res.append("".join(word))
    return res

sampleText = "As Python's creator, I'd like to say a few words about its origins."
print(splitText(sampleText, ", '."))