##69.	Write a script that applies basic text analysis on a provided text file.

def text_analysis(filename):
    with open(filename, "r")as file:
        text = file.read()
    words = text.split()
    print(f"number of words : {len(words)}")
    print(f"number of lines : {text.count('\n')+1}")
    print(f"most common word: {max(set(words ), key=words.count)}")

text_analysis('69.txt')