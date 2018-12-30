from api import db

from api.models.word import WordModel

class BookModel:

    def __init__(self, id):
        self.id = id

        if id == 1:
            self.basic_info = {
                "id": 1,
                "name": "Book1",
                "description": "Description1"
            }
        elif id == 2:
            self.basic_info = {
                "id": 2,
                "name": "Book2",
                "description": "Description2"
            }

        # for testing
        self.test_word_list = ['abandon', 'abase', 'abash', 'abate',
                               'abandon', 'abase', 'abash', 'abate',
                               'abandon', 'abase', 'abash', 'abate']


    def get_review_list(self, word_num):
        """
        获取要复习的单词列表
        :param word_num: 复习量
        :return: [str]
        """
        # TODO:
        return self.test_word_list[:word_num]

    def get_info(self):
        """
        根据 self.id 获取词书的基本信息
        :return: 一个字典,包含以下字段
        {
            'basic': {
                'id': str --- 词书ID
                'name': str --- 词书名称
                'description': str --- 词书简介
                'tags': [str] --- 词书标签
            }
            'progress': {
                'total': int --- 总背词量
                'done': int --- 已背单词量
                'familiar': int --- 熟记量
                'raw': int --- 模糊量
            }
        }
        """
        # TODO:
        return self.basic_info

    def get_word_list(self, st_idx, length):
        """
        获取词书的单词列表
        :param st_idx: 起始位置
        :param length: 长度
        :return:
        :rtype [WordModel]
        """
        # TODO:
        word_list = [WordModel(word) for word in self.test_word_list[:2]]
        return word_list
