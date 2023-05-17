from lru_cache import LRUCache

if __name__ == '__main__':
    cache = LRUCache(5)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    print("Output:", cache.get('Jesse'))
    cache.rem('Walter')
    print("Output:", cache.get('Walter'))

    cache.rem('Jesse')

    cache.set('1', 'Cache')
    cache.set('2', 'Test')
    cache.set('3', 'LRU')
    cache.set('4', 'Python')
    cache.set('5', '234')
    print("Output:", cache.get('1'))

    cache.set('6', 'failed')
    print("Output:", cache.get('4'))
    print("Output:", cache.get('1'))
    print("Output:", cache.get('6'))
    print("Output:", cache.get('5'))
    print(f"Output: {cache.get('-1')}")