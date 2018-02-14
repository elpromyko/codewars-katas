"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps
Notes:

the returned string should only contain lowercase letters
"""


def kebabize(string):
    return ''.join([i for i in ['-{}'.format(i) if i.isupper() else i for i in string] if not i.isdigit()]).lower().lstrip('-')
