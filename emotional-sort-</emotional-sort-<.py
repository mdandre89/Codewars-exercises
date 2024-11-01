def sort_emotions(arr, order):
    so = ['T_T',':(',':|',':)',':D']
    return sorted(arr,key=lambda x: so.index(x)) if not order else sorted(arr,key=lambda x: so[::-1].index(x))