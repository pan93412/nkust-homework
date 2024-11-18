def jaccard_similarity[T](s1: set[T], s2: set[T]):
    return len(s1.intersection(s2)) / len(s1.union(s2))

a_list = ['dog', 'cat', 'rat']
b_list = ['dog', 'cat', 'mouse']

print(jaccard_similarity(set(a_list), set(b_list)))
