from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


abay_kara_sozderi = open ('kara_sozder.txt',encoding="utf8").read()


stopwords = set(STOPWORDS)
stopwords.add('жоқ')
stopwords.add('деп')
stopwords.add('не')
stopwords.add('де')
stopwords.add('екен')
stopwords.add('деген')
stopwords.add('да')
stopwords.add('бір')
stopwords.add('ол')
stopwords.add('ма')
stopwords.add('бе')
stopwords.add('және')
stopwords.add('ба')
stopwords.add('еді')
stopwords.add('мал')
stopwords.add('керек')
stopwords.add('болса')
stopwords.add('бұл')
stopwords.add('болып')
stopwords.add('соң')
stopwords.add('осы')
stopwords.add('емес')
stopwords.add('адам')
stopwords.add('енді')
stopwords.add('әрбір')
stopwords.add('мен')
stopwords.add('екі')
stopwords.add('дейді')
stopwords.add('егер')
stopwords.add('десе')
stopwords.add('оның')
stopwords.add('болады')
stopwords.add('сол')
stopwords.add('оны')
stopwords.add('қылып')
stopwords.add('қалған')
stopwords.add('қылған')
stopwords.add('өз')
stopwords.add('я')
stopwords.add('десең')
stopwords.add('қай')
stopwords.add('ондай')
stopwords.add('келеді')
stopwords.add('бұлар')
stopwords.add('үшін')
stopwords.add('ешбір')
stopwords.add('соған')

abay = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords
)

abay.generate(abay_kara_sozderi)

fig = plt.figure(figsize=(14, 18))

plt.imshow(abay, interpolation='bilinear')
plt.axis('off')
plt.show()