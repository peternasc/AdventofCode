import hashlib

chave = 'yzbqklnj'
num = 0

while True:
    teste = f'{chave}{num}'.encode()
    md5 = hashlib.md5(teste).hexdigest()
    if md5.startswith('000000'):
        print(num)
        break
    num += 1