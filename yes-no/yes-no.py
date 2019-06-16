while True:
    print('(Y/n)')
    ok = input()

    if ok in ('y', None):
        print('gucci')
        break
    
    if ok in ('n'):
        print('no gucci')

    print('invalid response')
