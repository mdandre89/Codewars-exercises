from collections import OrderedDict
class Array(object):
    def __init__(self, arr = []):
        self.arr = arr
    
    def num_elements(self):
        return len(self.arr)
    
    def num_values(self):
        return len(set(self.arr))  
    
    def start_end(self):
        return [self.arr[0], self.arr[-1]]
        
    def range_(self):
        return [min(self.arr),max(self.arr)]
        
    def largest_increas_subseq(self):
        arr = self.arr

        l = len(arr)  # l stores the length of the array
        i = 0  # initialize i, iterate from left of the array

        max = 1  # the max is always a one element array

        start = 0  # initialize start at the beginning of the array
        end = 0  # initialize end at the beginning of the array

        beststart = 0  # initialize beststart at the beginning of the array
        bestend = 0  # initialize bestend at the beginning of the array

        while i<l:
            if i+1 < l and arr[i+1]>arr[i]:
                end = end + 1  # increment end, as we found a longer array
                if (end-start+1) > max:
                    max = (end - start + 1)  # update max
                    beststart = start  # update beststart as we have the longest array till this point
                    bestend = end  # update bestend as we have the longest array till this point
            else:
                start = i+1  # re-initialize start
                end = i+1  # re-initialize end

            i = i + 1
        
        sub = arr[beststart:bestend+1]
        return sub if sub and len(sub)>=3 else 'No increasing subsequence'
        
    def largest_decreas_subseq(self):
        arr = self.arr

        l = len(arr)  # l stores the length of the array
        i = 0  # initialize i, iterate from left of the array

        max = 1  # the max is always a one element array

        start = 0  # initialize start at the beginning of the array
        end = 0  # initialize end at the beginning of the array

        beststart = 0  # initialize beststart at the beginning of the array
        bestend = 0  # initialize bestend at the beginning of the array

        while i<l:
            if i+1 < l and arr[i+1]<arr[i]:
                end = end + 1  # increment end, as we found a longer array
                if (end-start+1) > max:
                    max = (end - start + 1)  # update max
                    beststart = start  # update beststart as we have the longest array till this point
                    bestend = end  # update bestend as we have the longest array till this point
            else:
                start = i+1  # re-initialize start
                end = i+1  # re-initialize end

            i = i + 1
        
        sub = arr[beststart:bestend+1]
        return sub if sub and len(sub)>=3 else 'No decreasing subsequence'
        
    def __str__(self):
        d = OrderedDict()
        d.update({'1.number of elements': self.num_elements()})
        d.update({'2.number of different values': self.num_values()})
        d.update({'3.first and last terms': self.start_end()})
        d.update({'4.range of values': self.range_()})
        d.update({'5.increas subseq': self.largest_increas_subseq()})
        d.update({'6.decreas subseq': self.largest_decreas_subseq()})
        return str(d)