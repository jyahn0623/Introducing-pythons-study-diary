from collections import Counter, OrderedDict
def solution(genres, plays):
    answer = []
    _dict = {}
    _number = { k : [] for k in set(genres) }
    rank = []
    i = 0
    # 통합 데이터
    for k, v in zip(genres, plays):
        _number[k].append((i, v))
        try:
            _dict[k] += v
        except:
            _dict[k] = 0
            _dict[k] += v
            rank.append(k)
        i+=1
    
    # 순위 
    for i, k in enumerate(rank):
        for j, v in enumerate(rank):
            if _dict[k] > _dict[v]:
                tmp = rank[i]
                rank[i] = rank[j]
                rank[j] = tmp
    
    # 베스트 앨범 출시
    for i in rank:
        __rank = []
        _list = _number[i]
        c = OrderedDict(Counter(dict(_list)).most_common())
        j = 0
        for v in c:
            if j < 2:
                answer.append(v)
                j+=1
    return answer

solution(['a', 'b', 'a', 'b', 'a', 'c'], [200, 300, 400, 40, 200, 1000])
