import collections 
def most_frequent_item_count(ls):
    return max(collections.Counter(ls).values()) if ls else 0