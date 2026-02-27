"""
Practice 4.4: Python JSON
JSON数据处理练习
"""

import json                                            # 导入JSON模块
import os                                              # 导入操作系统模块

print("=" * 50)
print("1. Python to JSON (Python转JSON)")
print("=" * 50)

person = {                                              # 创建一个Python字典
    "name": "张三",                                     # 姓名
    "age": 25,                                          # 年龄
    "city": "北京",                                     # 城市
    "hobbies": ["读书", "游泳", "编程"],                 # 爱好列表
    "is_student": False                                 # 是否学生
}

print("Python dict (Python字典):")
print(person)                                           # 打印Python字典

json_str = json.dumps(person, ensure_ascii=False, indent=2)  # 转换为JSON字符串
print("\nJSON string (JSON字符串):")
print(json_str)                                         # 打印JSON字符串

print("\n" + "=" * 50)
print("2. JSON to Python (JSON转Python)")
print("=" * 50)

json_data = '{"name": "李四", "age": 30, "city": "上海"}'  # JSON格式字符串
print(f"JSON string (JSON字符串): {json_data}")

python_dict = json.loads(json_data)                      # 解析JSON为Python字典
print(f"Python dict (Python字典): {python_dict}")
print(f"Name (姓名): {python_dict['name']}")             # 获取姓名
print(f"Age (年龄): {python_dict['age']}")               # 获取年龄

print("\n" + "=" * 50)
print("3. Working with JSON Files (读写JSON文件)")
print("=" * 50)

data = {                                                 # 创建学生数据
    "students": [                                        # 学生列表
        {"name": "王小明", "score": 85},                  # 学生1
        {"name": "李小丽", "score": 92},                  # 学生2
        {"name": "张小华", "score": 78}                   # 学生3
    ]
}

with open("students.json", "w", encoding="utf-8") as f:  # 打开文件用于写入
    json.dump(data, f, ensure_ascii=False, indent=2)      # 将数据写入JSON文件
print("Data written to students.json (数据已写入students.json文件)")

if os.path.exists("students.json"):                       # 检查文件是否存在
    with open("students.json", "r", encoding="utf-8") as f:  # 打开文件读取
        loaded_data = json.load(f)                          # 从文件加载JSON数据
    
    print("\nData read from file (从文件读取的数据):")
    for student in loaded_data["students"]:                # 遍历每个学生
        print(f"{student['name']}: {student['score']}分")  # 打印学生信息

print("\n" + "=" * 50)
print("4. JSON Type Conversion (JSON类型转换)")
print("=" * 50)

conversion = {                                           # 类型对应表
    "Python": ["dict", "list", "str", "int", "float", "True/False", "None"],
    "JSON": ["object", "array", "string", "number", "number", "true/false", "null"]
}

print("Python to JSON conversion (Python到JSON类型转换):")
print("Python类型 → JSON类型")
for i in range(len(conversion["Python"])):
    print(f"{conversion['Python'][i]:<10} → {conversion['JSON'][i]}") 