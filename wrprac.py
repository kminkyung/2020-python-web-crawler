from wordcloud import WordCloud
import re
from PIL import Image
import numpy as np


text = ''
regexp = re.compile('(?<=",").+(?=")')


with open("kakao.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[1:]:
        sentence = regexp.search(line)
        if sentence is not None:
            s = sentence.group().replace('Emoticon', '').replace('Photo', '').replace('photos', '').replace('ㅋㅋ', '').replace('Search', '').replace('Boards', '').replace('Videos', '')
            text += s + '\n'


mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='/Users/minkyungkim/Library/Fonts/NanumBarunGothic.otf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")