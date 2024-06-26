#!/usr/bin/env python
#-*- coding: utf-8 -*-
import requests

import re

from deep_translator import GoogleTranslator

from ..githubcontroller import GitHubController
from ..base import Base


class ThreatHuntingBook(GitHubController, Base):
    """
    Data Source: https://github.com/12306Bro/Threathunting-book

    Authors:
        - 12306Bro

    This class is a wrapper for the above data set
    """

    __URL = 'https://raw.githubusercontent.com/12306Bro/Threathunting-book/master/{}'
    __REPO = '12306Bro/Threathunting-book'

    def __init__(self):
        super(ThreatHuntingBook, self).__init__()
        self.translator = GoogleTranslator(source='auto', target='en')
        self.session = requests.Session()
        self._dataset = []
        self.__temp_attack_paths = []

    def get(self):
        return_list = []
        repo = self.github.get_repo(self.__REPO)
        contents = repo.get_contents("")
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            else:
                if file_content.path.endswith('.md') and file_content.path.split('/')[-1].startswith('T'):
                    content = self.__download_raw_content(file_content.download_url)
                    try:
                        translated = self.translator.translate(content)
                        template = self.__parse_markdown(translated.text)
                        if template:
                            return_list.append(template)
                    except:
                        pass
        return return_list

    def _parse_code_blocks(self, content, technique_id):
        regexp = re.compile(r"((.*\n){2})`` `([^`]*)`` `")
        found = re.findall(regexp, content)
        name = None
        type_name = None
        for item in found:
            if isinstance(item, tuple):
                for match in item:
                    stripped_match = match.rstrip('\r\n')
                    if stripped_match:
                        for line in stripped_match.splitlines():
                            if line.startswith('## '):
                                if 'test' in line:
                                    name = line.strip('## ').strip()
                                    break
                                if 'detection rules' in line:
                                    name = line.strip('## ').strip()
                                    break
                        if name and name not in stripped_match:
                            if 'test' in name:
                                for line in stripped_match.splitlines():
                                    type_name = line
                                    break
                                if type_name:
                                    self.generated_data.add_command(
                                        technique_id=technique_id,
                                        source=self.__URL,
                                        name=type_name,
                                        command=stripped_match
                                    )
                                else:
                                    self.generated_data.add_command(
                                        technique_id=technique_id,
                                        source=self.__URL,
                                        name='',
                                        command=stripped_match
                                    )
                            if 'detection rules' in name:
                                for line in stripped_match.splitlines():
                                    type_name = line
                                    break
                                if type_name:
                                    self.generated_data.add_possible_queries(
                                        technique_id=technique_id,
                                        product=self.__URL,
                                        content=stripped_match,
                                        name=type_name
                                    )
                                else:
                                    self.generated_data.add_command(
                                        technique_id=technique_id,
                                        source=self.__URL,
                                        name='',
                                        command=stripped_match
                                    )

    def __parse_markdown(self, content):
        technique_id = None
        if content.strip():
             for line in content.splitlines():
                if line.startswith('# '):
                    if line.strip('# ').split('-')[0].startswith('T'):
                        technique_id = line.strip('# ').split('-')[0].strip()
                        break
        self._parse_code_blocks(content, technique_id)

    def __download_raw_content(self, url):
        response = self.session.get(url.encode('utf-8'))
        if response.status_code == 200:
            return response.text