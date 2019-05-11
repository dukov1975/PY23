import requests
import os

# API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
API_KEY = 'trnsl.1.1.20190502T142635Z.78342a3a8ef9e1da.225624bfb31ad38bba3ad3c8e39a794cf401cf76'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(text, from_lang,to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:

    """
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    # print(json_)
    return ''.join(json_['text'])

while True:
    print('Список доступных файлов для перевода:')
    for file_name in os.listdir():
        if file_name.endswith('.txt'):
            print(file_name)
    file_name = input('Имя файла:')
    from_lang = input('С какого перевести (de,es,fr):')
    to_lang = input('На какой перевести (ru,cz,it)')
    text_to_write = []
    with open(file_name) as source_file:
        for line in source_file:
            if line not in '\n':
                if to_lang != '':
                    text_to_write.append(translate_it(line, from_lang.lower(), to_lang.lower()))
                else:
                    text_to_write.append(translate_it(line, from_lang.lower()))
        write_file = f'{from_lang}_translate'
        with open(write_file, 'w+') as write_translate:
            for write_line in text_to_write:
                write_translate.write(write_line)



# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))


# requests.post('http://requestb.in/10vc0zh1', json=dict(a='goo', b='foo'))