# a program that takes two input strings from the command line and generates the top 3 most suitable candidates for constructing a sentence consisting of three words
from collections import defaultdict, Counter

class SimpleTrigramModel:
    def __init__(self):
        self.trigrams = defaultdict(Counter)

    def train(self, text):
        words = text.split()
        for i in range(len(words) - 2):
            self.trigrams[(words[i], words[i+1])][words[i+2]] += 1

    def predict_next_words(self, word1, word2, n=3):
        next_words = self.trigrams.get((word1, word2), {})
        return [word[0] for word in next_words.most_common(n)]

# トレーニングデータ
text = "I love cats. I love Python programming. I love machine learning. I love deep learning."

model = SimpleTrigramModel()
model.train(text)

print("Enter two words separated by space:")
user_input = input().split()

if len(user_input) != 2:
    print("I'm sorry, but I can't predict based on the given input.")
else:
    word1, word2 = user_input
    predictions = model.predict_next_words(word1, word2)
    if predictions:
        print(f"After the words '{word1} {word2}', the most likely next words are: {predictions}")
    else:
        print("I'm sorry, but I can't provide predictions for the given word pair.")
