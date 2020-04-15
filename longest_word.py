'''
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
longestWord(text) = "steady".

best solution by dnl-blkv:
	return max(re.split('[^a-zA-Z]', text), key=len)
'''
def longestWord(text):
    rex='[\[\],!@#$%¨&{}+-=~^´`´_*/:()<>|?*]|(\\\)'
    m=None
    w=None
    text=re.sub(rex, ' ',text)
    for word in text.split():
        word=re.sub(rex, '',word)
        if m==None or m<len(word):
            m=len(word)
            w=word
    return w
print(longestWord('Ready, steady, go!'))