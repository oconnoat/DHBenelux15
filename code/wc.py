import nltk

rawtext = open('example.txt').read().decode('utf-8').lower()

text = nltk.Text(nltk.word_tokenize(rawtext))
freq = nltk.FreqDist(text)

print freq.freq('math')
freq.plot(20, cumulative=False)



