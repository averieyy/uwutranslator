def translate(msg:str):
    msg = msg.replace('l', 'w')
    msg = msg.replace('r', 'w')
    msg = msg.replace(':)', ':3')
    msg = msg.replace(':D', ':3')
    msg = msg.replace('.', '')
    msg = msg.replace(',', '')
    spacesplit = msg.split(' ')
    for i in range(len(spacesplit), 0, -1):
        if len(spacesplit[i-1]) >= 7 and 'u' in spacesplit[i-1]:
            usplit = spacesplit[i-1].split('u')
            result = usplit[:-2]
            result.append('uwu'.join(usplit[-2:]))
            spacesplit[i-1] = 'u'.join(result)
            break
    msg = ' '.join(spacesplit)
    msg += ' uwu'
    return msg

if __name__ == '__main__':
    print(translate(input('wat to translate > ')))