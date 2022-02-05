def toDict(result, row):
    dict(zip([c[0] for c in result.description], row))