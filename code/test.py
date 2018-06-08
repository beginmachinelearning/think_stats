import nsfg
df = nsfg.ReadFemPreg()
df['birthwgt_lb'].value_counts()


def MakePregMap(df):
    d = defaultdict(list)
    for index, caseid in df.caseid.iteritems():
        d[caseid].append(index)
    return d