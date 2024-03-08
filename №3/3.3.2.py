from sklearn.feature_extraction import DictVectorizer

x = [{"Двуногое": 2,},
     {"без перьев": 3}]
dictVectorizer = DictVectorizer(sparse = False)
y = dictVectorizer.fit_transform(x)
print(y)
