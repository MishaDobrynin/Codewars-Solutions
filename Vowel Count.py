def get_count(sentence):
    return len([el for el in sentence.lower() if el in "aeiou"])