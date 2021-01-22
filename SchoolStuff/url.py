import requests

hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
for a in hexa:
    for b in hexa:
        for c in hexa:
            for d in hexa:
                for e in hexa:
                    for f in hexa:
                        for g in hexa:
                            request = requests.get(f'http://cdn1.vikaa.fi:38341/photos/108dadc6/8b88ef005f7{a}{b}{c}{d}{e}20ffff010b000034{f}{g}.png')
                            if request.status_code == 200:
                                print(f'http://cdn1.vikaa.fi:38341/photos/108dadc6/8b88ef005f7{a}{b}{c}{d}{e}20ffff010b000034{f}{g}.png')
                            elif request.status_code == 429:
                                print('429')
                            #elif request.status_code == 404:
                                #print('not found')
