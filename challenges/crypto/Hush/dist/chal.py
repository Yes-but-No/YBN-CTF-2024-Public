from secret import flag

class Hush:
    def __init__(self, size):
        self._size = size 
        self._keys = [None]*size 
        self._values = [None]*size

    def hushfunction(self, key):
        return key % self._size

    def rehush(self, oldhush):
        return (oldhush + 1) % self._size

    def put(self, key, data):
        hush_value = self.hushfunction(key)
        
        while self._keys[hush_value] is not None:
            hush_value = self.rehush(hush_value)
        
        self._keys[hush_value] = key
        self._values[hush_value] = data

    def data(self):
        return self._keys, self._values

hush = Hush(len(flag))
for i in range(len(flag)):
    char = flag[i]
    hush.put(ord(char) + i, char)

print(hush.data())