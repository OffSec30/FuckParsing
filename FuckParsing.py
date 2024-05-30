import os as _0
import re as _1
import random as _2

def _3(_4):
    return [ _5 for _5 in _0.listdir(_4) if _5.endswith('.txt') ]

def _6(_7, _4):
    while _7:
        _8 = _2.choice(_7)
        _7.remove(_8)
        _9 = _0.path.join(_4, _8)
        
        try:
            with open(_9, 'r', encoding='utf-8') as _a:
                for _b in _a:
                    yield _8, _b
        except UnicodeDecodeError:
            with open(_9, 'r', encoding='latin-1') as _a:
                for _b in _a:
                    yield _8, _b

def _c(_d, _e):
    return _1.findall(_e, _d)

def _f(_10, _11, _12):
    with open(_10, 'a', encoding='utf-8') as _a:
        for _b in _11:
            _a.write(f"{_12}: {_b}\n")

def _13():
    _4 = r'G:\yourgoogledrivehere\Logs'
    _e = r'https?://[^\s:]+:[^\s:]+:[^\s:]+'
    _10 = 'results.txt'
    
    _7 = _3(_4)
    _14 = input("Enter the Keyword to search in logs: ")
    _15 = set()

    for _12, _b in _6(_7, _4):
        _11 = _c(_b, _e)
        for _16 in _11:
            if _14 in _16 and _16 not in _15:
                _15.add(_16)
                print(f"Result found in {_12}: {_16}")
                _f(_10, [_16], _12)

if __name__ == '__main__':
    _13()
