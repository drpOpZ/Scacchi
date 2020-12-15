import re

pattern = '^[RDTAC]?x?[a-h][1-8]$'

def check_chess_syntax(text):
    # TODO:IMPLEMENTARE
    pass


# TEST
for text in [
    # VALID SAMPLES
    'a2','xc5','0-0','Tg8','Rxb7',
    # INVALID SAMPLES
    'a9','Ga2','sbricci','']:
    try:
        check_chess_syntax(text)
    except:
        print("'{}' is INVALID:".format(text))
    else:
        print("'{}' is a valid move".format(text))

# Solo i primi cinque input devono risultare validi
