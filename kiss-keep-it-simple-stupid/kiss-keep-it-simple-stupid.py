def is_kiss(words):
    return "Good work Joe!" if len(words.split()) >= max(map(len, words.split())) else "Keep It Simple Stupid"