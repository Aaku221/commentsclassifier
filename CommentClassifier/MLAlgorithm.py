import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

comments = pd.read_csv('E:/Code/CommentClassifier/DataSet/attack_annotated_comments.tsv', sep = '\t', index_col = 0)
annotations = pd.read_csv('E:/Code/CommentClassifier/DataSet/attack_annotations.tsv', sep ='\t')

len(annotations['rev_id'].unique())

labels = annotations.groupby('rev_id')['attack'].mean() > 0.5

comments['attack'] = labels

comments['comment'] = comments['comment'].apply(lambda x: x.replace("NEWLINE_TOKEN", " "))
comments['comment'] = comments['comment'].apply(lambda x: x.replace("TAB_TOKEN", " "))

print(comments.query('attack')['comment'].head())

train_comments = comments.query("split=='train'")
test_comments = comments.query("split=='test'")

clf = Pipeline([
    ('vect', CountVectorizer(max_features = 10000, ngram_range = (1,2))),
    ('tfidf', TfidfTransformer(norm = 'l2')),
    ('clf', LogisticRegression()),
])
clf = clf.fit(train_comments['comment'], train_comments['attack'])
auc = roc_auc_score(test_comments['attack'], clf.predict_proba(test_comments['comment'])[:, 1])
#print('Algorithm efficiency: %.3f' %auc)

def classify(comment):
    res=clf.predict([comment])
    final=res[0]
    #print(final)
    if(final == True):
        return "Abusive"
    else:
        return "Not abusive"

#print(classify("Go to hell"))
