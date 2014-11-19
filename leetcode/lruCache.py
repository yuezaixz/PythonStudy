class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.data={}
        self.capacity=capacity
        self.head = LRUNode(-1,-1)
        self.tail = LRUNode(-1,-1)
        self.head.next = self.tail 
        self.tail.prev = self.head

    def moveToFirst( self, pnode ):
        # link current node's prev and next   
        if pnode.prev:
            pnode.prev.next = pnode.next
        if pnode.next:
            pnode.next.prev = pnode.prev
            # move it to first
            pnode.next = self.head.next
        if self.head.next:
            self.head.next.prev = pnode
            pnode.next = self.head.next
            self.head.next = pnode
            pnode.prev = self.head

    def removeLRU( self ):
        pdel = self.tail.prev
        pdel.prev.next = self.tail
        self.tail.prev = pdel.prev
        del self.data[ pdel.key ]
        del pdel

    def Insert( self, key, value ):
        newNode = LRUNode(key, value)
        self.data[key] = newNode
        self.moveToFirst(newNode)

    # @return an integer
    def get(self, key):
        if self.data.has_key(key):
            pvalue = self.data[key]
            value =  pvalue.value
            self.moveToFirst( pvalue )
            return value  
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.data.has_key(key):
            self.data[key].value = value
            self.moveToFirst( self.data[key] )
        else:
            self.Insert(key, value)
            if len(self.data) > self.capacity:
                self.removeLRU()
    
class LRUNode:
    def __init__(self,key,value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
       return str(self.key)+":"+str(self.value)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.set(2,1)
    cache.set(1,1)
    # print cache.head.next
    # print cache.tail.prev
    print cache.get(2)
    # print cache.head.next
    # print cache.tail.prev
    cache.set(4,1)
    print cache.get(1)
    print cache.get(2)
