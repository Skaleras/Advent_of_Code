import re
data = open('E:\code\AoC\day4\input.bat', 'r')
my_input = data.read()
pattern = '\n\n'
documents = re.split(pattern, my_input)
tag_counter=0
valid_passports=0

for document in documents:
    pattern = '\s'
    data=re.sub(pattern,',',document)
    #print('________________________________________________')
    if 'ecl' and 'pid' and 'eyr' and 'hcl' and 'byr' and 'iyr' and 'hgt' in data:
        data=data.split(',')
        #print(data)
        tag_counter=0
        for data_pieces in data:
            piece = data_pieces.split(':')
            if piece[0]== 'ecl':
                if piece[1] in ['amb','blu', 'brn','gry','grn','hzl','oth']:
                    tag_counter+=1
            elif piece[0]=='pid':
                if len(piece[1])==9:
                    tag_counter+=1
            elif piece[0]=='eyr':
                if int(piece[1]) in range(2020,2031):
                    tag_counter+=1
            elif piece[0]=='hcl':
                if re.match('#[a-f0-9]{6}',piece[1]):
                    tag_counter+=1
            elif piece[0]=='byr':
                if int(piece[1]) in range(1920,2003):
                    tag_counter+=1
            elif piece[0]=='iyr':
                if int(piece[1]) in range(2010,2021):
                    tag_counter+=1
            elif piece[0]=='hgt':
                if 'in' in piece[1] or 'cm' in piece[1]:
                    if 'cm' in piece[1]:
                        piece[1]= piece[1].replace('cm','')
                        if int(piece[1]) in range(150,194):
                            tag_counter+=1
                    if 'in' in piece[1]:
                        piece[1] = piece[1].replace('in','')
                        if int(piece[1]) in range(59,77):
                            tag_counter+=1
        if tag_counter==7:
            #print('Hay:',tag_counter, 'contadores de tags')
            valid_passports+=1
            tag_counter=0
    else:
        pass
print(valid_passports)
