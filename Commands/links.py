links = {  # add the links here
    'rickroll': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
    'memes': 'https://www.reddit.com/r/memes/',
    'porn': 'woah take a step back there, buddy',
}
result = None


def link_message(linkname):
    if linkname in links.keys():
        return links.get(linkname)
    else:
        return 'Link does not exist in the database'

def link_list():
    linklist = ''
    for x in links.keys():
        linklist += f'{x}\n'
    return linklist