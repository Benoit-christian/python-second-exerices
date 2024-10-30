def word_frequencies(sentence):
    words = sentence.split()
    frequency_dict = {}

    for word in words:
        word = word.lower()

        frequency_dict[word] = frequency_dict.get(word, 0)
        return frequency_dict