file = open('kaartnummers.txt', 'r')
fileRead = file.split(',')
fileRead = fileRead.replace('\n', '')
print(fileRead[1])
