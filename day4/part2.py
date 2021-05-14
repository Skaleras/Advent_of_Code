import re
data = open('E:\code\AoC\day4\input.bat', 'r')
my_input = data.read()
pattern = '\n\n'
documents = re.split(pattern, my_input)
counter=0
tag_checklist = ['ecl','pid','eyr','hcl','byr', 'iyr', 'hgt', 'cid']
tag_counter = 0
for document in documents:
    pattern = '\s'
    data=re.sub(pattern,',',document)
    print('________________________________________________')
    data=data.split(',')
    #print(data)
    for tag in tag_checklist:
        for data_pieces in data:
            if tag in data_pieces:
                piece = data_pieces.split(':')
                if piece[0]== 'ecl':
                    if piece[1] in ['amb','blu', 'brn','gry','grn','hzl','oth']:
                        tag_counter+=1
                    else:
                        pass
                elif piece[0]=='pid':
                    if len(pieces[1])==9:
                        tag_counter+=1
                    else:
                        pass
                elif piece[0]=='eyr':
                    if int(pieces[1]) in list(range(2020,2031)):
                        tag_counter+=1
                    else:
                        pass
                elif piece[0]=='hcl':
                    pass #WIP
    
    counter+=1
    if counter == 10: break