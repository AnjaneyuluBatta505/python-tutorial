class A:
    def who_are_you(self):
        print("I'm A")


class B:
    def who_are_you(self):
        print("I'm B")

    def say_name(self):
        print("Wow B")


class C:
    def who_are_you(self):
        print("I'm C")
    
    def say_name(self):
        print("Wow C")


class D(B, C, A):
    pass


class E(B, C, A):
    def who_are_you(self):
        print("I'm E")


class F(A, B, C):
    pass


print("class F")
f = F()
f.say_name()
# ouput: I'm A
