def is_even(k):
    if k == 0:
        return True
    while k > 2:
        k -= 2
    return k == 2 

def is_even2(k):
    if k == 0:
        return True
    div, mod = divmod(k, 2)
    return mod==0


if __name__ == '__main__':
    print(is_even(354352))
    print(is_even(3423451))
    print(is_even(1))
    print(is_even(0))

    print(is_even2(354352))
    print(is_even2(3423451))
    print(is_even2(1))
    print(is_even2(0))

    print(is_even2(9999999999999999999999999999))


