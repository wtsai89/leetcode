class Jar:
    def __init__(self, capacity=2):
        self.capacity = capacity
    
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    def poopy(self, butts):
        print(butts)

def main():
    jar = Jar()
    a = [1,2,3,4]
    print(a[-2:])

main()