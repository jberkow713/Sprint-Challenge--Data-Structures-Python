class RingBuffer:
    def __init__(self, capacity, data = []):
        self.index = 0
        self.capacity = capacity
        # data with a length = to capacity
        self._data = list(data)[-capacity:]
                     
        

    def append(self, item):

        if len(self._data) == self.capacity:
            self._data[self.index] = item 
        else:
            self._data.append(item)
        self.index = (self.index + 1) % self.capacity   
        
    def get(self):
        return self._data

'''
def __init__(self, size, data = []):
        """Initialization"""
        self.index = 0
        self.size = size
        self._data = list(data)[-size:]

    def append(self, value):
        """Append an element"""
        if len(self._data) == self.size:
            self._data[self.index] = value
        else:
            self._data.append(value)
        self.index = (self.index + 1) % self.size
        '''
        