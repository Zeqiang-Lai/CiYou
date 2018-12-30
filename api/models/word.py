
class WordModel:

    def __init__(self, spell):
        self.spell = spell
        self.word_meaning_list = {}

        self.word_meaning_list['abandon'] = {
            'spell': 'abandon',
            'phone': 'E5bAndEn',
            'meaning': [{'basic': 'n. 放纵： carefree, freedom from constraint',
                         'example': 'added spices to the stew with complete abandon   肆无忌惮地向炖菜里面加调料',
                         'jin': 'unconstraint, uninhibitedness, unrestraint',
                         'fan': '',
                         'pai': ''},
                        {'basic': 'v. 放弃： to withdraw from often in the face of danger or encroachment',
                         'example': 'abandon the ship/homes	弃船，离家',
                         'jin': 'salvage   救援',
                         'fan': '',
                         'pai': ''}
                        ]
        }
        self.word_meaning_list['abase'] = {
            'spell': 'abase',
            'phone': 'E5beIs',
            'meaning': [{'basic': 'v. 降低（地位、职位、威望或尊严）： to lower in rank, office, prestige, or esteem',
                         'example': 'was unwilling to abase himself by pleading guilty to a crime that he did not '
                                    'commit 不愿意屈就自己去承认一个莫须有的罪名',
                         'jin': 'debauch, degrade, profane, vitiate, discredit, foul, smirch, take down',
                         'fan': 'elevate, ennoble, uplift, aggrandize, canonize, deify, exalt   使高贵，使有声望',
                         'pai': ''}]

        }
        self.word_meaning_list['abash'] = {
            'spell': 'abash',
            'phone': 'E5bAF',
            'meaning': [{'basic': 'vt. 使尴尬，使羞愧： to destroy the self-possession or self-confidence of ,disconcert, embarrass',
                         'example': 'Nothing could abash him.	没有什么可以使他感到难堪。',
                         'jin': 'discomfit, disconcert, discountenance, faze, fluster, nonplus, mortify',
                         'fan': 'embolden 使大胆',
                         'pai': ''}]
        }
        self.word_meaning_list['abate'] = {
            'spell': 'abate',
            'phone': 'E5beIt',
            'meaning': [{'basic': 'v. 减轻（程度或者强度）： to reduce in degree or intensity',
                         'example': 'added spices to the stew with complete abandon   肆无忌惮地向炖菜里面加调料',
                         'jin': 'moderate, recede, subside, remit, wane, die (away or down or out),let up, '
                                'phase down, ratchet (down)，taper off',
                         'fan': 'intensify',
                         'pai': ''}]
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

