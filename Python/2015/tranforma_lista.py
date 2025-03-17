def transforma(a):

    b = a.splitlines()
    for c in b:
        print(f'"{c}",')

a = '''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
'''

transforma(a)

   