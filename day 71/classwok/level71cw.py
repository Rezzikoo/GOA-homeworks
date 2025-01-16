def match_husband(usefulness, months_since_signup):
    husband_usefulness = sum(usefulness)
    first_needs = 100
    decay = 0.15
    decayed_needs = first_needs * (1 - decay) ** months_since_signup
    if husband_usefulness >= decayed_needs:
        return "match"
    else:
        return "no match"
