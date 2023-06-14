'''
One-line solution to Question 2
'''

print(
    " ".join(
        map(
            str,
            (
                (a + b) & 1  # Basically = (a + b) % 2. When the final bit is 1, it is odd.
                for a, b in zip(map(int, input().split()), map(int, input().split()))
                #           zip - Combine two iterators into one iterator.
                #           For example, zip([1, 2, 3], [4, 5, 6]) -> [(1, 4), (2, 5), (3, 6)]
            ),
        )
    )
)
