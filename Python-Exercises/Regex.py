# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
def solution(a, p):
    match = ""
    ZeroOrMore = False
    OneOrMOre = False
    curr = ""

    for i, val in enumerate(a): #

        if i > len(p)-1 and (OneOrMOre or ZeroOrMore):
            curr = match[-1]
        elif i > len(p)-1 and (not OneOrMOre and not ZeroOrMore): break
        else:
            curr = p[i]
        if OneOrMOre:
            match+= match[-1]
            continue
        elif ZeroOrMore:
            match+= match[-1]
            continue
        # print(i,val)
        if curr == val:
            match += val
        elif curr == ".":
            match += val
        elif curr == "+" and OneOrMOre == False:
            match += match[-1]
            OneOrMOre = True
        elif curr == "*" and ZeroOrMore == False:
            match += val
            ZeroOrMore = True
    print(match)
    return match==a

print(solution("abbbb", ".*"))
# solution("hel+, "h+")
