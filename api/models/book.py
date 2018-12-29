from api import db


class BookModel():

    def __init__(self):
        # for testing
        self.test_word_list = ['abandon', 'abase', 'abash', 'abate',
                               'abandon', 'abase', 'abash', 'abate',
                               'abandon', 'abase', 'abash', 'abate']
        self.word_meaning_list = {}

        self.word_meaning_list['abandon'] = {
            'spell': 'abandon',
            'phone': 'E5bAndEn',
            'meaning': 'n. 放纵： carefree, freedom from constraint'
        }
        self.word_meaning_list['abase'] = {
            'spell': 'abase',
            'phone': 'E5beIs',
            'meaning': [
                {'basic': 'v. 降低（地位、职位、威望或尊严）： to lower in rank, office, prestige, or esteem',
                 'example': '',
                 'jinyi': '',
                 'tongyi': '',
                 'paishen': ''
                },
                {},
                {}
            ]
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

    def get_review_list(self, word_num):
        # TODO:
        return self.test_word_list[:word_num]

    def get_word(self, word_spell):
        # TODO:
        if word_spell in self.word_meaning_list.keys():
            return self.word_meaning_list[word_spell]
        return {
            'spell': 'error',
            'phone': 'error',
            'meaning': 'error'
        }
