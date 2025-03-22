def reverse_words(sent):
    words = sent.split(" ") 
    reversed_words = [word[::-1] for word in words]  
    return " ".join(reversed_words)  



