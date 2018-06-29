import pylangacq
import glob

files = glob.glob('cha/*')
broken_files = ('cha/roberts2.cha', 'cha/fusser11.cha')
good_files = tuple(f for f in files if f not in broken_files)

# HACK: loading takes a long time, so use fewer files for testing
# good_files = good_files[:2]

print "Loading corpus"
corpus = pylangacq.read_chat(*good_files)

trigrams = corpus.word_ngrams(3)
print "Most popular trigrams:"
trigram_items_by_freq = sorted(trigrams.items(), key=lambda item: item[1], reverse=True)
for trigram, freq in trigram_items_by_freq[:30]:
    print trigram, freq

print "Some sentences:"
for sentence in corpus.sents()[:10]:
    print u' '.join(sentence)
