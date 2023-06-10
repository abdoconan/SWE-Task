import gensim
from gensim import corpora

documents = [['apple', 'banana', 'fruits'], ['bought', 'bicycle', 'recently', 'less', 'two', 'years', 'buy', 'bike'], 
             ['colour', 'apple', 'bicycle', 'red']]
mapping = corpora.Dictionary(documents)
data = [mapping.doc2bow(word) for word in documents]

print(data)

ldamodel = gensim.models.ldamodel.LdaModel(data, num_topics=2, id2word=mapping, passes=15)
topics = ldamodel.show_topics()
print(topics)


# Distribution of topics for the first document
print(ldamodel.get_document_topics(data[0]))