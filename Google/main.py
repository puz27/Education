import os

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just",
    "on", "not", "in", "to"]


with open("worlds.txt", 'r') as file:
    data = file.read().split()
    file.close()

def check_punctuations(word):
    new_word = ''
    for i in word:
        if i not in punctuations:
            new_word = new_word + i
    return new_word

def check_all(data):
    convert_data = []
    for word in data:
        convert_data.append(check_punctuations(word))
    for i in convert_data:
        if i in uninteresting_words:
            convert_data.remove(i)
    return convert_data

def create_dik(d):
    dik = {}
    for word in d:
        dik[word] = dik.get(word, 0) + 1
    return dik
print(check_all(data))
print(create_dik(check_all(data)))
