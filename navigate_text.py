from map import Map
import os

datadir = 'data'

map = Map()
for xml in os.listdir(datadir):
    map.load(os.path.join(datadir, xml))

loc = map['dorm_inside']

running = True
while running:
    print('You are in ' + loc.text)
    print(loc.description)
    print()
    print('You can go:')
    print(' \n'.join([e.label for e in loc.exits.values()]))
    print()
    command = input('? ').split(' ')
    cmd = command[0]

    if cmd in ['q', 'quit', 'exit']:
        running = False
    elif cmd == 'go':
        loc = map[loc.exits[command[1]].to]
        if not loc:
            print('That is not a place. You got lost and returned to the promenade')
            loc = map['promenade']
