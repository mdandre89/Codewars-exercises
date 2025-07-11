from textwrap import wrap
def hex_string_to_RGB(hex_string):
    return {'rgb'[index] : int(value, 16) for index, value in enumerate( wrap( hex_string[1:], 2) ) }