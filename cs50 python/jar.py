class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity,int) or capacity < 0:
            raise ValueError("capacity is not a non-negative int")
        self.cap = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        self.cookies += n
        if self.cookies > self.cap:
            raise ValueError("cookies exceed the capacity allowed")

    def withdraw(self, n):
        if self.cookies < n:
            raise ValueError("not enough cookies to withdraw")
        self.cookies -= n

    @property
    def capacity(self):
        return self.cap

    @property
    def size(self):
        return self.cookies

def main():
    jar = Jar()
    jar.deposit(2)
    print(str(jar))

main()