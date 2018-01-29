f = open('Resources/flying.txt', 'r')

wordcount = 0
sentence_count = 0

reader = f.read()
words = reader.split()
n_words = len(words)
n_sentences = reader.count('.')
avg_words = sum(len(word) for word in words) / n_words

print('\nParagraph Analysis')
print('------------------')
print('Approximate word count: {}'.format(n_words))
print('Approximate sentence count: {}'.format(n_sentences))
print('Average Letter Count: {}'.format(avg_words))