def domain(url):
    if url[:7]=="http://":
        url=url[7:]
    elif url[:8]=="https://":
        url=url[8:]

    if url[:4]=="www":
        url=url[4:]

    domain_end=len(url)
    for i in range(len(url)):
        if url[i]=="/":
            domain_end=i
            break

    domain=url[:domain_end]
    return domain