lijst = ['a', 'b', 'c']
print(lijst)

def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')
    lijst = letterlijst

wijzig(lijst)
print(lijst)