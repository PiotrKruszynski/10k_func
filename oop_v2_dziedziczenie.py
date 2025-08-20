class A:
    def magic(self):
        print(f'class A')


class B:
    def magic(self):
        print(f'class B')


class C(A):
    def magic(self):
        print(f'class C')


class X(B, C, A):
    pass
    # @staticmethod
    # def magic(self):
    #     print(f'class {type(self)}')


x = X()
print(X.__mro__)
x.magic()


# print(dir('ala ma kota'))
# print(help("ala".capitalize))


#print(dir((1,)))
#print(help(dir((1,))))