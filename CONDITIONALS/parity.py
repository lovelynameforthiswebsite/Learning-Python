def main():
    """
    x = float(input("what's x ? "))
    if x % 2 == 0:
        print("even")
    else:
        print("odd")
    """
    x = float(input("what's x ? "))
    if is_even(x):
        print("even")
    else:
        print("odd")




def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False










main()
