#   8Ball with a list
#
#
# -Bentley 8/6/2020

import random

messages = ['It is certain',
            'It is decidedly so',
            'Yes, Definitely',
            'Reply hazy try again later',
            'Ask again later',
            'Concentrate and ask again!',
            'My reply is no',
            'Outlook not so good',
            'Very Doubtful']

print(messages[random.randint(0, len(messages) -1)])