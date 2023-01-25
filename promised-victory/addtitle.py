# adds a fontmatter field named "title" every .md file in folder
# if the file already has a title, do nothing
# if the file has no title, add a title based on the filename


import os
import re
#for yaml parsing:
import yaml
# get all .md files in nested folder
def get_files(path):
    files = []
    #ignore .obsidian folder
    ignore = ['.obsidian']
    for r, d, f in os.walk(path):
        for file in f:
            if '.md' in file and not any(x in r for x in ignore):
                files.append(os.path.join(r, file))

            
    return files

#get files from current dir
files = get_files(os.getcwd())
print(files)

# for each file, check if it has a title
for file in files:
    print(file)
    # folder could have emojis
    # to avoide  � error, open file in 
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        #check if first line is ---
        if content.startswith('---'):
            #get lines untill second ---
            lines = content.split('---')[1].splitlines()
            #load as yaml
            data = yaml.load('\n'.join(lines), Loader=yaml.FullLoader)
            #check if title exists
            if 'title' in data:
                print('title exists')
            else:
                #add title
                print('title does not exist')
                #get filename
                filename = os.path.splitext(os.path.basename(file))[0]
                #add title
                data['title'] = filename
                with open(file, 'w', encoding='utf-8') as f:
                    f.write('---\n')
                    yaml.dump(data, f, default_flow_style=False)
                    f.write('\n---\n')
                    f.write(''.join(content.split('---')[2:]))
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x8f in position 2089: character maps to <undefined>
# to fix this error, open the file in notepad++ and save it as utf-8