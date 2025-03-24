import pprint


def get_obj_kind(o):
    if isinstance(o, str):
        return 'str'
    if o is None:
        return 'none'
    if isinstance(o, int):
        return 'int'
    # is method function or class
    if ' at 0x' in str(o):
        return str(o).split(' at 0x')[0] + '>'
    return str(o)


searched_kinds = []
searched_kinds_paths = []
strings = {}
ints = {}

def do_dir(o, path):
    for a in dir(o):
        this_path = path + '.' + a
        # print(this_path)
        try:
            v = getattr(o, a)
            if isinstance(v, str) and v not in strings.values():
                strings[this_path] = v
            if isinstance(v, int) and v not in ints.values():
                ints[this_path] = v

            obj_kind = get_obj_kind(v)
            if obj_kind not in searched_kinds:
                searched_kinds.append(obj_kind)
                searched_kinds_paths.append(this_path)
                do_dir(v, this_path)
        except AttributeError:
            print('AttributeError:', this_path)


do_dir(..., '...')
print(ints)

