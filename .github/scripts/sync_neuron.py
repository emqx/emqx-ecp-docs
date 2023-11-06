import os
import sys
import json

import requests

docs_path = sys.argv[1]

DIR_DICT = {
    'cn': f'{docs_path}/zh_CN',
    'en': f'{docs_path}/en_US'
}

def get_files(language, dir_config):
    url_list = []
    for i in dir_config:
        md_name = i.get('path')
        if md_name == './':
            md_name = 'index'

        if i.get('url'):
            md_path = f'{DIR_DICT[language]}/{md_name}.md'
            if not os.path.exists(os.path.dirname(md_path)):
                os.makedirs(os.path.dirname(md_path))

            response = requests.get(i['url'])
            if response.status_code == 200:
                with open(md_path, 'w') as f:
                    f.write(response.text)
            else:
                print(f'Error: {i["url"]} not found')
                exit(1)
        if i.get('children'):
            get_files(language, i['children'])

    return url_list


if __name__ == '__main__':
    r = open(f'{docs_path}/directory.json', 'r')
    directory_config = json.load(r)
    for lang, directory_list in directory_config.items():
        print(f'lang: {lang}')
        get_files(lang, directory_list)
