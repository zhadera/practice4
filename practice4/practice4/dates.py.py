"""
Practice 4.2: Python Dates and Time
日期和时间操作练习
"""

from datetime import datetime, date, timedelta  # 导入日期时间模块
import time                                      # 导入时间模块

print("=" * 50)
print("1. Current Date & Time (当前日期和时间)")
print("=" * 50)

now = datetime.now()                              # 获取当前日期时间
print(f"Now (现在): {now}")                       # 打印当前时间
print(f"Date (日期): {now.date()}")                # 打印当前日期
print(f"Time (时间): {now.time().strftime('%H:%M:%S')}")  # 打印当前时间

print("\n" + "=" * 50)
print("2. Date Formatting (日期格式化)")
print("=" * 50)

print(f"YYYY-MM-DD: {now.strftime('%Y-%m-%d')}")  # 格式：年-月-日
print(f"DD/MM/YYYY: {now.strftime('%d/%m/%Y')}")  # 格式：日/月/年
print(f"Full (完整格式): {now.strftime('%A, %B %d, %Y')}")  # 星期, 月份 日, 年
print(f"Time (时间): {now.strftime('%H:%M:%S')}")  # 格式：时:分:秒

print("\n" + "=" * 50)
print("3. Date Calculations (日期计算)")
print("=" * 50)

new_year = datetime(2025, 1, 1)                    # 创建2025年1月1日对象
today = datetime.now()                              # 获取当前时间

days_left = (new_year - today).days                 # 计算相差天数
print(f"Days until 2025 New Year (距离2025年元旦还有): {days_left} 天")

tomorrow = today + timedelta(days=1)                # 当前时间加1天
yesterday = today - timedelta(days=1)                # 当前时间减1天
print(f"Tomorrow (明天): {tomorrow.strftime('%Y-%m-%d')}")
print(f"Yesterday (昨天): {yesterday.strftime('%Y-%m-%d')}")

birthday = date(2000, 1, 1)                          # 创建生日日期
today_date = date.today()                            # 获取今天日期
age = today_date.year - birthday.year                 # 计算大致年龄
print(f"Age (年龄): {age} 岁") 