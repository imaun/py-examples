import os

with os.scandir('../') as dirs:
    for d in dirs:
        if d.is_file():
            print(f'[file] {d.name}')
        else:
            print(f'[dir] {d.name}')

