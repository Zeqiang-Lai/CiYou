
class WordModel:

    def __init__(self, spell):
        self.spell = spell
        self.word_meaning_list = {}

        self.word_meaning_list['abandon'] = {
            'spell': 'abandon',
            'phone': 'E5bAndEn',
            'meaning': 'n. 放纵： carefree, freedom from constraint'
        }
        self.word_meaning_list['abase'] = {
            'spell': 'abase',
            'phone': 'E5beIs',
            'meaning': 'v. 降低（地位、职位、威望或尊严）： to lower in rank, office, prestige, or esteem'
        }
        self.word_meaning_list['abash'] = {
            'spell': 'abash',
            'phone': 'E5bAF',
            'meaning': 'vt. 使尴尬，使羞愧： to destroy the self-possession or self-confidence of ,disconcert, embarrass'
        }
        self.word_meaning_list['abate'] = {
            'spell': 'abate',
            'phone': 'E5beIt',
            'meaning': 'v. 减轻（程度或者强度）： to reduce in degree or intensity'
        }
        self.info = self.word_meaning_list[self.spell]

    def get_comments(self):
        """
        :return:
        :rtype: CommentModel
        """
        pass

    def get_info(self):
        """
        返回单词的信息
        :return: 一个字典,包含以下字段
        {
            "spell": str
            "phone": str
            "meaning": [
                {
                    "basic": str
                    "example": str
                    "jin": str
                    "fan": str
                    "pai": str
                },
                {
                    "basic": str
                    "example": str
                    "jin": str
                    "fan": str
                    "pai": str
                },
                ...
            ]
        }
        """
        # TODO:
        return self.info


class CommentModel:
    pass


class StoryModel:
    pass

