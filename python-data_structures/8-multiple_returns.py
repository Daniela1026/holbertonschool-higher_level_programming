#!/usr/bin/python3
def multiple_returns(sentence):
    sent = ()
    if len(sentence) == 0:
        sent = 0, "None"
    else:
        sent = len(sentence), sentence[0]
    return sent
