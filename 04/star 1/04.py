with open('doc.txt') as f:
    file_content = f.read()
    pairs = [i.replace(" ", "") for i in file_content.split("\n")]
    
    #separer les paires
    for i in range(len(pairs)):
        pairs.split(',')
    print(pairs)
