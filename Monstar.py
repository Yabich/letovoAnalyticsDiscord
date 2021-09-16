class A:
    def __str__(self):
        return 'a'
    def __add__(self, other):
        return other
    def __radd__(self, other):
        return other


b = A()
c=1
print(b)