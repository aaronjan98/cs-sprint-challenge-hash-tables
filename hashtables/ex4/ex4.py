match = {}

def has_negatives(a):
    # only positive numbers will be set into match dict
    match = {a[i]: False for i in range(len(a)) if a[i] > 0}

    # loop through the list
    for num in a:
        # if num is negative and its pair is in match
        if num < 0 and abs(num) in match:
            match.update({abs(num): True})

    pairs_only = []
    for key, value in match.items():
        if value == True:
            pairs_only.append(key)
    return pairs_only


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
