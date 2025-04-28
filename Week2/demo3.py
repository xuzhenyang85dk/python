
fst_paragraph = """asdfjasklfasjklfajsfksajfklajsalæfjaælsdfasdfjasklfasjklfajsfksajfklajsalæfjaælsdfasdfjasklfasjklfajsfksajfklajsalæfjaælsdfasdfjasklfasjklfajsfksajfklajsalæfjaælsdf."""

count = {}
for character in fst_paragraph.split(' '):
    count.setdefault(character, 0) 
    count[character] += 1
#print(count)
#det gør at man add defaul key value i listen, så vi får ikke fejl

import pprint

def expand(rule):
    print(rule)
expand('_S')

def expand2(rule,a_value, b_value):
    print(a_value + b_value)
expand2(3,'a','b')

