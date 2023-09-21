def replaceWords(dictionary: list[str], sentence: str) -> str:
    res = []
    dictionary.sort(key=lambda x: (x, len(x)))
    for word in sentence.split():
        flag = True
        for root in dictionary:
            if word.startswith(root):
                res.append(root)
                flag = False
                break
        if flag:
            res.append(word)
    return ' '.join(res)
