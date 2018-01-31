f = open('Resources/flying.txt', 'r')

reader = f.read()
words = reader.split()
n_words = len(words)
n_sentences = reader.count('.')
avg_words = sum(len(word) for word in words) / n_words

sents = reader.split('.')

avg_sents = sum(float(len(sent.split(' '))) for sent in sents) / float(len(sents))
print('\nParagraph Analysis')
print('------------------')
print('Approximate word count: {}'.format(n_words))
print('Approximate sentence count: {}'.format(n_sentences))
print('Average Letter Count: {}'.format(avg_words))
print('Average Sentence Length: {}'.format(avg_sents))
