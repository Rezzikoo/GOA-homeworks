def is_anagram(test, original):
    if len(test) != len(original):       #tu testi ar udris originals mashin gamoitanos false
        return False

    joined = (test + original).lower()       #joined=testi da originali ertad patara asoebit

    for char in joined:         
        if joined.count(char) % 2 != 0:         #tu joined gayofili 2ze ar udris nols mashin gamoitanos false
            return False