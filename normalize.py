def normalize(txt)
    if txt.isupper()
        return txt[0].title() + txt[1].lower() + !
    else
        return txt[0].title() + txt[1].lower()


print(normalize(Let us stay calm, no need to panic.))
