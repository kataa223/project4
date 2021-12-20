class TestClass6:
    val = "クラス変数"
    def __init__(self, arg):
        self.val = arg
        
testClass6 = TestClass6("インスタンス変数1")
print(TestClass6.val)
print(testClass6.val)
del testClass6.val
del testClass6.val
print(testClass6.val)