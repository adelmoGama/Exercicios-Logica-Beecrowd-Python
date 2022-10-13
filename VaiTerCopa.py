while True:
    N = int(input())
    try:
        if N == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
    except EOFError:
        break
