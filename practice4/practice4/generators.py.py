"""
Practice 4.1: Iterators and Generators
迭代器和生成器练习
"""

print("=" * 50)
print("1. Python Iterators (迭代器)")
print("=" * 50)

# 1.1 iter() 和 next() 的基本使用
print("\n1.1 Using iter() and next():")

my_list = [1, 2, 3]              # 创建一个列表
my_iter = iter(my_list)            # 将列表转换为迭代器

print(next(my_iter))  # 1         # 获取迭代器的下一个元素
print(next(my_iter))  # 2         # 每次调用next()会返回下一个值
print(next(my_iter))  # 3         # 直到没有元素可返回

# 1.2 自定义迭代器
print("\n1.2 Custom Iterator (自定义迭代器):")

class Counter:                     # 定义一个计数器类
    def __init__(self, max):       # 初始化方法，传入最大值
        self.max = max             # 保存最大值
        self.n = 0                 # 初始化当前值为0
    
    def __iter__(self):            # 返回迭代器对象本身
        return self
    
    def __next__(self):            # 定义获取下一个元素的方法
        if self.n < self.max:      # 如果还没达到最大值
            self.n += 1             # 当前值加1
            return self.n           # 返回当前值
        else:                       # 已达到最大值
            raise StopIteration     # 抛出停止迭代异常

count = Counter(3)                  # 创建一个计数器，最大值为3
print("Counting to 3:")             # 打印提示
for i in count:                     # 遍历计数器
    print(i, end=" ")  # 1 2 3      # 打印1 2 3
print()

print("\n" + "=" * 50)
print("2. Python Generators (生成器)")
print("=" * 50)

# 2.1 yield 的基本使用
print("\n2.1 Using yield:")

def simple_gen():                   # 定义一个简单的生成器函数
    yield "Hello"                    # 返回"Hello"，暂停执行
    yield "World"                    # 返回"World"，暂停执行
    yield "!"                        # 返回"!"，结束

gen = simple_gen()                   # 创建生成器对象
print("Generator yields:")           # 打印提示
for word in gen:                     # 遍历生成器
    print(word, end=" ")  # Hello World !
print()

# 2.2 生成器表达式
print("\n2.2 Generator Expression:")

squares = (x*x for x in range(5))    # 生成器表达式：计算0-4的平方
print("Squares 0-4:", list(squares))  # 转换为列表并打印 [0, 1, 4, 9, 16]

# 2.3 实际应用：生成斐波那契数列
print("\n2.3 Fibonacci Generator:")

def fibonacci(n):                    # 生成前n个斐波那契数
    a, b = 0, 1                       # 初始化前两个数
    for _ in range(n):                 # 循环n次
        yield a                         # 返回当前数
        a, b = b, a + b                 # 计算下一个数

print("First 8 Fibonacci:", list(fibonacci(8)))  # [0, 1, 1, 2, 3, 5, 8, 13] 