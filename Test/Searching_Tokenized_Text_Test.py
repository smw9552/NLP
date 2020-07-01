import nltk
from nltk.corpus import gutenberg, nps_chat

moby = nltk.Text(gutenberg.words('melville-moby_dick.txt'))
moby.findall(r"<a> (<.*>) <man>")