"""
Practice 4.3: Python Math and Random
数学和随机数操作练习
"""

import math                                          # 导入数学模块
import random                                        # 导入随机模块
import string                                        # 导入字符串模块

print("=" * 50)
print("1. Built-in Math Functions (内置数学函数)")
print("=" * 50)

numbers = [5, 2, 8, 1, 9]                            # 创建一个数字列表
print(f"Numbers (数字列表): {numbers}")
print(f"Max (最大值): {max(numbers)}")               # 求最大值
print(f"Min (最小值): {min(numbers)}")               # 求最小值
print(f"Sum (总和): {sum(numbers)}")                  # 求和
print(f"Absolute (绝对值 -10): {abs(-10)}")          # 求绝对值
print(f"Round (四舍五入 3.14159): {round(3.14159, 2)}")  # 四舍五入保留2位小数
print(f"Power (幂运算 2³): {pow(2, 3)}")              # 2的3次方

print("\n" + "=" * 50)
print("2. Math Module (数学模块)")
print("=" * 50)

print(f"Pi (圆周率): {math.pi}")                      # 圆周率π
print(f"E (自然常数): {math.e}")                      # 自然常数e
print(f"Square root (平方根 √16): {math.sqrt(16)}")   # 平方根
print(f"Ceiling (向上取整 4.2): {math.ceil(4.2)}")    # 向上取整
print(f"Floor (向下取整 4.8): {math.floor(4.8)}")     # 向下取整
print(f"sin(90°): {math.sin(math.pi/2)}")            # 正弦90度
print(f"cos(0°): {math.cos(0)}")                      # 余弦0度

print("\n" + "=" * 50)
print("3. Random Module (随机模块)")
print("=" * 50)

print(f"Random (随机数 0-1): {random.random()}")      # 生成0-1随机小数
print(f"Random int (随机整数 1-10): {random.randint(1, 10)}")  # 1-10随机整数
print(f"Random choice (随机选择水果): {random.choice(['apple', 'banana', 'cherry'])}")

cards = ['A', '2', '3', '4', '5']                     # 创建扑克牌列表
print(f"Original (原顺序): {cards}")
random.shuffle(cards)                                  # 打乱列表顺序
print(f"Shuffled (打乱后): {cards}")

password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
print(f"Random password (随机8位密码): {password}")    # 生成随机密码 