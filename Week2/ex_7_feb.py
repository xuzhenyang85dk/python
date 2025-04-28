import random
grammar = {
      "_S"  : ["_N _V"],
      "_N"  : ["developer", "teacher", "student"],
      "_V"  : ["learns", "trains", "tests", "is", "studies", "asks"]
  }

_N = random.choice(grammar['_N'])
_V = random.choice(grammar['_V']) 

grammar['_S'] = _N +' ' + _V
print(grammar['_S'])


import random
grammar = {
      "_S"  : ["_NP _VP"],
      "_NP" : ["_N",
               "_A _NP _P _A _N"],
      "_VP" : ["_V",
               "_V _NP"],
      "_N"  : ["developer", "teacher", "student"],
      "_A"  : ["smart", "interesting", "nice", "desperate", "anoying"],
      "_P"  : ["about", "near"],
      "_V"  : ["learns", "trains", "tests", "is", "studies", "asks"]
  }

_N = random.choice(grammar['_N'])
_A = random.choice(grammar['_A'])
_P = random.choice(grammar['_P'])
_V = random.choice(grammar['_V'])

def expandNP(a_value,b_value):
    print(a_value + ',' + b_value)
print(_N)