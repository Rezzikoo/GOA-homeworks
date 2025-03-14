def jaccard_similarity(a, b):

    gadakveta = []
    gaertianeba = []
#gadakveta
    for element in a:
        if element in b and element not in gadakveta:
            gadakveta.append(element)
#gaertianeba
    for element in a:
        if element not in gaertianeba:
            gaertianeba.append(element)
    for element in b:
        if element not in gaertianeba:
            gaertianeba.append(element)

    gadakvetis_size = len(gadakveta)
    gaertianebis_size = len(gaertianeba)

    return gadakvetis_size / gaertianebis_size 


a = [1,2,4,6,7]
b = [2,3,4,7]

print(jaccard_similarity(a, b))  
