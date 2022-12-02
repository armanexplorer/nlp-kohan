from hazm import Normalizer


from hazm import Lemmatizer, Normalizer

lem = Lemmatizer()
normalizer = Normalizer()

# print(lem.lemmatize('رونده', pos="AJ"))
print(normalizer.normalize("می روم"))
