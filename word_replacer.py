def word_replacement():
    while True:
        str = "Hello, how are you doing, My name is Kazzi.tech and i am a Python Developer"
        print("\n \n Below is the word of the day.")
        print(str)
        word1 = input("Enter word to be replaced:")
        word2 = input("Enter word you wish to replace with:")
        if word1 in str:
            print(str.replace(word1, word2))
        else:
            print("Select a word present in the above sentence to replace, take note of the capital and small letters.")

word_replacement()