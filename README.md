```python
! pip install nltk
! pip install tqdm
! pip install numpy
! pip install pandas
```

    Requirement already satisfied: nltk in d:\education\master\semesters\semester 3\nlp\hws\2\kohan\venv\lib\site-packages (3.4)
    Requirement already satisfied: six in d:\education\master\semesters\semester 3\nlp\hws\2\kohan\venv\lib\site-packages (from nltk) (1.16.0)
    Requirement already satisfied: singledispatch in d:\education\master\semesters\semester 3\nlp\hws\2\kohan\venv\lib\site-packages (from nltk) (3.7.0)
    Requirement already satisfied: tqdm in d:\education\master\semesters\semester 3\nlp\hws\2\kohan\venv\lib\site-packages (4.64.1)
    Requirement already satisfied: colorama in d:\education\master\semesters\semester 3\nlp\hws\2\kohan\venv\lib\site-packages (from tqdm) (0.4.6)
    Requirement already satisfied: numpy in d:\education\master\semesters\semester 3\nlp\hws\2\kohan\venv\lib\site-packages (1.23.5)
    Requirement already satisfied: pandas in d:\education\master\semesters\semester 3\nlp\hws\2\kohan\venv\lib\site-packages (1.5.2)
    Requirement already satisfied: python-dateutil>=2.8.1 in d:\education\master\semesters\semester 3\nlp\hws\2\kohan\venv\lib\site-packages (from pandas) (2.8.2)
    Requirement already satisfied: numpy>=1.20.3 in d:\education\master\semesters\semester 3\nlp\hws\2\kohan\venv\lib\site-packages (from pandas) (1.23.5)
    Requirement already satisfied: pytz>=2020.1 in d:\education\master\semesters\semester 3\nlp\hws\2\kohan\venv\lib\site-packages (from pandas) (2022.6)
    Requirement already satisfied: six>=1.5 in d:\education\master\semesters\semester 3\nlp\hws\2\kohan\venv\lib\site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)
    


```python
import nltk
import codecs
import tqdm

# Read text
GAZALS_FILE_PATH = 'all_qazals_mesra.txt'
mesra_collection = codecs.open(GAZALS_FILE_PATH,'rU','utf-8').readlines()

# Select part of that
mesra_collection = mesra_collection[40:100]
```


```python
from hazm import Normalizer

# Normalizer on qazals collection
normalizer = Normalizer(token_based=True, kohan_style=True)
mesra_normalized = [normalizer.normalize(x) for x in tqdm.tqdm(mesra_collection)]
mesra_normalized
```

    100%|?????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????| 60/60 [00:00<00:00, 191.08it/s]
    




    ['?????? ?????????? ???????????? ?? ?????? ?????????? ?????? ????????',
     '???????? ?????? ????\u200c???????? ???? ?????? ?????????? ????',
     '?????????? ?????? ???? ???????? ???? ???? ?????? ????????\u200c???? ??????????',
     '???????????? ???????????????? ?????? ?????? ???????? ????',
     '???????? ???? ???????? ?? ???? ???? ?? ?????? ?????? ???????? ????',
     '???? ???? ?????????? ?? ???????????? ???? ???????? ?????? ???????? ????',
     '?????? ???????? ?? ???? ???????? ?????? ?? ?????? ?????????? ????????',
     '???? ???? ?????? ???? ???????????? ?????? ?????? ???????? ????',
     '?????? ???? ?????? ?????? ???? ???????? ???????? ????',
     '???? ???? ???? ?????? ?? ???????????? ???? ????????\u200c???? ???? ????',
     '?????????????? ???? ???????? ???????? ?????? ??????',
     '?????????? ???????? ???????? ?????????? ????',
     '???????? ???????? ?????????? ?????? ???????? ???? ????',
     '???? ?????????? ???????? ???????????? ???????? ????',
     '???? ?????? ?? ?????? ???????? ?????? ?????? ?????? ??????',
     '???? ?????? ?? ?????? ???????????? ?????? ???????? ????',
     '?????????? ???? ???? ?????? ?????? ???????????? ????????',
     '?????? ???????? ?????? ?????? ?????? ???????? ????',
     '???? ???? ???????? ?????????? ?? ???????? ????????????',
     '???? ?????? ?????? ?????????? ?????????????? ????',
     '???? ?????? ?????? ?????????? ?????? ???? ???????? ???? ??????',
     '???? ?????? ?????? ?? ?????? ???????? ?????? ???????? ????',
     '???? ?????????? ???? ?????? ?????? ???? ???????? ????????',
     '???????? ???????? ???? ?????? ???????? ?????????? ????',
     '???? ????\u200c?????? ???? ???????? ???????? ???????? ?????? ????',
     '???????? ???? ?????? ?????????? ?????????? ???? ????????????',
     '???????? ?????????????????? ???? ?????? ???????? ??????????',
     '???????? ???? ???????????????? ?????????? ???????? ????',
     '???? ???????? ?????? ?????????? ???????????? ?????? ?? ??????????',
     '???????? ???? ?????? ?????????? ???????? ???????? ????????',
     '???? ???????? ???? ?? ???? ?????? ?????????? ?????? ????????',
     '?????? ???????????? ???????? ???? ???????? ??????????????',
     '???? ???????? ?????????? ???????????? ??????????',
     '???????? ?????????? ???? ?????????? ????\u200c?????? ????',
     '?????????? ???? ???????? ?????????? ?????? ???? ?????? ??????',
     '???? ???????????? ???????? ???? ???????????? ??????????',
     '???? ?????? ??????\u200c???????? ???? ???? ?????? ????????????',
     '?????? ???? ??????\u200c?????????? ?????????? ???? ?????? ????',
     '???? ?????? ???? ???? ???????? ???? ???????????????? ??????????',
     '???????? ?????? ?? ???????? ???? ???????? ??????????????',
     '?????????? ?????????????? ???? ?????? ?????? ?? ????????',
     '???? ?????? ???????????? ???????? ?????????? ?????? ?????? ????',
     '???????? ?????? ???? ?????? ?????? ???? ?????????? ??????????',
     '???????? ???? ???? ???? ???? ?????? ?????? ?????? ????????',
     '?????????? ?????????? ?????? ???? ?????? ????????',
     '???? ???? ???? ???????? ???????? ?????????? ?????? ????????',
     '?????????? ??????????\u200c???? ???????????????? ??????????',
     '???????? ?????? ?????????? ?????????? ?????????? ????',
     '???????? ???? ?????? ???????????? ?????? ???????? ???? ????????',
     '???? ?????? ?????????????? ?????????? ?????? ???? ????',
     '???? ?????????????? ?????????? ???? ?????????? ?????? ?????? ????',
     '???? ???? ?????? ?????????????? ???? ?????? ???????? ?????? ????',
     '???? ???????? ?????????????? ???? ???????? ?????? ??????????',
     '?????? ???? ???????? ???????? ???????? ?????? ?????? ????',
     '?????? ?????????? ?????? ?????? ???? ?????? ???? ??????????',
     '???? ???????? ???? ???????????? ?? ?????? ?????? ??????????',
     '???? ?????????? ?????????? ???? ???????? ??????????????',
     '???? ???? ?????? ???? ?????? ???????? ???? ??????\u200c?????? ??????????',
     '?????? ???? ???? ?????? ?????????? ???? ???????? ??????????????',
     '???? ???????? ?????????????? ???????????? ???????? ????']




```python
# Normalizer on special cases
n = [
    normalizer.normalize('??????????????'),
    normalizer.normalize('???? ?????????? ????'),
    normalizer.normalize('???? ?????????? ????'),
    normalizer.normalize('?????? ???????? ????'),
    normalizer.normalize('?????? ??????????')
]
print('\n'.join(n))
```

    ??????????????
    ????????????????????????
    ????????????????????????
    ????????????????????????
    ???????????????????
    


```python
from hazm import Lemmatizer

# Lemmatizer on Kohan verbs
lemmatizer = Lemmatizer()
l = [
    lemmatizer.lemmatize('????????????????'),
    lemmatizer.lemmatize('????????????'),
    lemmatizer.lemmatize('?????????????????'),
    lemmatizer.lemmatize('?????????????????????'),
]
print('\n'.join(l))

```

    ??????????#??????
    ????????#??????
    ??????????#??????
    ?????????????????????
    


```python
# Combine lemmitizing with normalizing
n1 = normalizer.normalize('?????? ??????????')
l1 = lemmatizer.lemmatize(n1)

n2 = normalizer.normalize('?????? ????????????????')
l2 = lemmatizer.lemmatize(n2)

print(l1,l2)
```

    ??????????#?????? ??????????#??????
    


```python
# add Kohan conjugations
lemmatizer.conjugations('??????????#??????')
```




    ['????????????',
     '????????????',
     '??????????',
     '??????????????',
     '??????????????',
     '??????????????',
     '??????????????',
     '??????????????',
     '????????????',
     '????????????????',
     '????????????????',
     '????????????????',
     '??????????????',
     '??????????????',
     '????????????',
     '????????????????',
     '????????????????',
     '????????????????',
     '????????????\u200c????',
     '????????????\u200c????',
     '???????????? ??????',
     '????????????\u200c??????',
     '????????????\u200c??????',
     '????????????\u200c??????',
     '??????????????\u200c????',
     '??????????????\u200c????',
     '?????????????? ??????',
     '??????????????\u200c??????',
     '??????????????\u200c??????',
     '??????????????\u200c??????',
     '??????????????\u200c????',
     '??????????????\u200c????',
     '?????????????? ??????',
     '??????????????\u200c??????',
     '??????????????\u200c??????',
     '??????????????\u200c??????',
     '????\u200c????????????',
     '????\u200c????????????',
     '????\u200c??????????',
     '????\u200c??????????????',
     '????\u200c??????????????',
     '????\u200c??????????????',
     '??????\u200c????????????',
     '??????\u200c????????????',
     '??????\u200c??????????',
     '??????\u200c??????????????',
     '??????\u200c??????????????',
     '??????\u200c??????????????',
     '??????\u200c????????????',
     '??????\u200c????????????',
     '??????\u200c??????????',
     '??????\u200c??????????????',
     '??????\u200c??????????????',
     '??????\u200c??????????????',
     '??????\u200c??????????????',
     '??????\u200c??????????????',
     '??????\u200c????????????',
     '??????\u200c????????????????',
     '??????\u200c????????????????',
     '??????\u200c????????????????',
     '????\u200c??????????????',
     '????\u200c??????????????',
     '????\u200c????????????',
     '????\u200c????????????????',
     '????\u200c????????????????',
     '????\u200c????????????????',
     '??????????????',
     '??????????????',
     '????????????',
     '????????????????',
     '????????????????',
     '????????????????',
     '????????????????',
     '????????????????',
     '??????????????',
     '??????????????????',
     '??????????????????',
     '??????????????????',
     '????????',
     '????????',
     '????????',
     '??????????',
     '??????????',
     '??????????',
     '??????????',
     '??????????',
     '??????????',
     '????????????',
     '????????????',
     '????????????',
     '??????????',
     '??????????',
     '??????????',
     '????????????',
     '????????????',
     '????????????',
     '????\u200c????????',
     '????\u200c????????',
     '????\u200c????????',
     '????\u200c??????????',
     '????\u200c??????????',
     '????\u200c??????????',
     '??????\u200c????????',
     '??????\u200c????????',
     '??????\u200c????????',
     '??????\u200c??????????',
     '??????\u200c??????????',
     '??????\u200c??????????',
     '??????\u200c????????',
     '??????\u200c????????',
     '??????\u200c????????',
     '??????\u200c??????????',
     '??????\u200c??????????',
     '??????\u200c??????????',
     '??????????',
     '??????????',
     '??????????',
     '????????????',
     '????????????',
     '????????????',
     '??????\u200c????????',
     '??????\u200c????????',
     '??????\u200c????????',
     '??????\u200c??????????',
     '??????\u200c??????????',
     '??????\u200c??????????',
     '??????????????',
     '??????????????',
     '????????????',
     '????????????????',
     '????????????????',
     '????????????????',
     '??????\u200c??????????',
     '??????\u200c??????????',
     '??????\u200c??????????',
     '??????\u200c????????????',
     '??????\u200c????????????',
     '??????\u200c????????????',
     '????\u200c??????????',
     '????\u200c??????????',
     '????\u200c??????????',
     '????\u200c????????????',
     '????\u200c????????????',
     '????\u200c????????????',
     '????????',
     '????????',
     '????????']




```python
from hazm.utils import stopwords_list

# Add more stopwords according to the Kohan texts
print(stopwords_list())
```

    ['????\u200c????????', '??????', '??????????', '??????', '????????', '??????', '??????????', '????', '??????', '??????????', '????????????', '????????', '????????', '????????', '??????', '??????????', '????', '????????', '????????_??????', '????????', '????????', '??????????', '??????????', '??????', '??????', '????????', '????????????', '????????', '??????', '??????', '????', '??????', '??????', '??????????', '??????', '??????', '????????', '??????????', '????????', '????', '????????', '????', '??????????', '??????', '????????', '??????', '????????', '????????????', '????????', '????????', '??????', '????', '??????', '??????????', '????????', '??????', '??????????', '????????', '????', '????', '????', '??????', '????????', '????????', '??????????', '??????', '????', '??????????', '??????', '????????', '??????', '??????????_??????', '????????????', '????\u200c????????????', '??????\u200c??????', '????????', '??????', '????????', '????????', '??????', '??????', '??????', '????????????', '??????', '????', '????\u200c??????', '????', '????????', '??????', '????????', '????????', '????????', '??????????', '??????????', '??????', '????????????', '??????', '????????', '??????', '??????', '??????', '??????', '????????', '??????', '????????', '????????', '????', '??????', '????', '??????????', '????????', '????????', '??????', '??????????', '??????????', '??????????', '??????', '??????????', '??????', '??????????????', '????????', '????????', '????????', '????????', '????', '??????????', '????????', '??????', '????????', '??????', '????????', '????\u200c??????????', '????????', '????????', '????', '??????_??????', '??????', '??????', '??????????', '??????????', '??????????', '??????????_??????', '????????', '????????', '??????', '????????', '????', '????????', '????????', '??????', '????????', '????????_??????', '????????', '????????', '??????????', '????\u200c????????', '??????', '????????', '??????????', '??????????', '????????', '????????', '????', '??????????', '??????????', '??????', '????????', '????', '????????', '????????', '????????', '????????', '????????????', '??????', '??????????', '??????_??????', '????????', '????????', '????????', '??????', '??????????_??????', '????', '??????', '??????', '??????????', '????????????', '????????', '??????', '????\u200c????????', '????????', '??????????', '????????', '????', '????\u200c????', '??????????', '??????', '??????', '????????', '????????', '????????', '????????', '??', '????', '????????', '??????????', '????????', '????\u200c????????', '??????', '????????', '????????', '????????????????', '??????????', '????\u200c??????', '????????', '????\u200c????????', '??????????', '??????????_??????', '????????????', '??????????', '????????', '????', '????????', '??????', '??????', '??????', '??????????', '????', '??????', '????\u200c????????', '??????', '????????', '????????', '????????', '????????', '????????', '????', '????????_??????', '??????????', '??????', '??????????', '????', '????????????????', '??????????', '??????????', '??????', '????\u200c??????', '??????', '????????', '????\u200c??????', '????????', '??????', '????', '??????????', '????????', '??????????', '????', '????\u200c????????', '??????', '????????????', '??', '????????', '????????', '????????', '??????', '??????????_????????', '??????????_????', '????????', '????????????', '????', '????????', '??????', '????\u200c????????', '??????', '??????', '??????', '??????', '????????', '??????????', '??????????', '????????', '????????????????', '????', '????????', '??????', '????', '????????', '????', '??????', '??????', '??????', '??????', '??????????', '????', '????????', '????', '????', '????', '????', '????????', '????\u200c??????????', '????????', '??????', '????????', '??????', '??????????', '??????', '??????????', '??????', '??????????', '??????', '????????_??????', '????????????', '????\u200c??????????', '??????', '??????????', '??????????', '????????', '????????', '????????????', '????', '??????', '??????????', '??????', '??????????', '????????', '????????', '??????\u200c??????', '??????', '????\u200c????????', '????????', '??????', '????????_??????', '??????_??????', '????????', '??????', '????', '????????', '????', '????????', '??????????', '????????', '????????', '????????', '????????', '????????', '??????????', '????\u200c??????', '??????????', '????????', '????????', '????????', '????????', '????\u200c??????', '????\u200c??????', '????????????', '????????', '????????', '????????', '??????', '????', '??????????', '????????', '????????????', '????????????', '??????????_??????', '??????', '??????', '??????', '??????????', '????????', '??????', '??????', '??????', '????????????', '????????', '????', '??????', '??????????', '??', '????????????', '????\u200c??????', '??????????', '????????', '????????', '????????', '??????', '????????', '????????????', '????????????', '??????', '????????', '??????', '??????', '????????_??????', '????', '??????????_??????????', '????????', '????????']
    


```python
# Detected stopwords of Kohan qazals
tokens = normalizer.tokenizer.tokenize(''.join(mesra_normalized))
stopword_tokens_in_qazals = {t for t in tokens if t in stopwords_list()}
stopword_tokens_in_qazals
```




    {'????',
     '????????',
     '????',
     '??????',
     '????',
     '??????',
     '??????',
     '????',
     '????',
     '????',
     '??????????',
     '????',
     '??????',
     '??????',
     '??????',
     '????????',
     '????',
     '??????',
     '????',
     '????',
     '??????',
     '??????',
     '????',
     '????????',
     '????',
     '????',
     '????',
     '????\u200c??????',
     '??????',
     '????',
     '????????',
     '??',
     '????',
     '??????',
     '??????',
     '????',
     '??????',
     '????',
     '??????',
     '????????',
     '????'}




```python

```
