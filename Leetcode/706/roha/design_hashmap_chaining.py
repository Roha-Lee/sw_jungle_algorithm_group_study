class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 1000
        self.data = [[] for _ in range(self.capacity)]
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_val = key % self.capacity 
        self.remove(key)
        self.data[hash_val].append((key, value))
        return 
        
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_val = key % self.capacity 
        for k, v in self.data[hash_val]:
            if k == key:
                return v
        return -1
                                        
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_val = key % self.capacity 
        for i in range(len(self.data[hash_val])):
            if self.data[hash_val][i][0] == key:
                self.data[hash_val].pop(i)
                return 
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)