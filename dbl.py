
def log(string):
    file = open('logs.txt', 'a+', encoding='utf-8')
    file.write(str(get_string(string)))
    file.write("\n")
    file.close()


def get_string(string):
    if isinstance(string, str):
        return string
    elif isinstance(string, list):
        strings = []
        strings.append("\n\nObject of type list:")
        strings.append("\n======\n")
        for s in string:
            strings.append(get_string(s))
        strings.append("===\nEnd object\n\n")
        return '\n'.join(strings)
    elif isinstance(string, dict):
        strings = []
        strings.append("\n\nObject of type dict")
        strings.append("\n======\n")
        for s in string.keys():
            strings.append(s + "=>" + get_string(string[s]))
        strings.append("===\nEnd object\n\n")
    else:
        return dump(string)

def logint(inte):

    file = open('logs.txt', 'ab+')

    file.write(inte)

    file.write("\n")

    file.close()


def dump(obj):
    strings = []
    strings.append("\n\nObject of type %s"%str(type(obj)))
    strings.append("\n======\n")

    for attr in dir(obj):
        if attr.find('__') > -1:
            continue
        strings.append("obj.%s = %r" % (attr, getattr(obj, attr)))

    strings.append("===\nEnd object\n\n")
    return '\n'.join(strings)