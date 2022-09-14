def order(sentence):
  d ={i+1:v for i in list(range(len(sentence.split()))) for v in sentence.split() if str(i+1) in v}
  return(' '.join([d[l] for l in d]))
  # one string method:
  # return(' '.join([{i+1:v for i in list(range(len(sentence.split())))
  #       for v in sentence.split() if str(i+1) in v}[l]
  #       for l in {i+1:v for i in list(range(len(sentence.split())))
  #       for v in sentence.split() if str(i+1) in v}]))

  # one more method:
  # return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

print(order("4of Fo1r pe6ople g3ood th5e the2"))


