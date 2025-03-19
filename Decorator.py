"""
装饰器的本质是高阶函数（函数作为参数 或 返回值），它接受一个函数作为参数，并返回一个新的函数。
"""

#1.函数装饰器
#装饰器（Decorator）是Python 中的一种高级功能，本质上是一个函数，
#用于在不修改原函数代码的情况下，增强或修改其功能。
#装饰器广泛用于日志记录、权限验证、性能监测、缓存等场景。
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"函数 `{func.__name__}` 开始执行，参数：{args}, {kwargs}")
        result = func(*args, **kwargs)  # 调用原函数
        print(f"函数 `{func.__name__}` 执行完成，返回值：{result}")
        return result
    return wrapper

@log_decorator #调用装饰器
def add(x, y):
    return x + y

result = add(3, 5)
#2.多个装饰器：
#允许多个装饰器层层嵌套，装饰器的执行顺序是 自下而上（先执行离函数最近的装饰器）
#3.带参数的装饰器
def repeat(n):  # 额外包一层用于接收参数 n
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):  # 控制执行次数
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)  # 让函数执行 3 次
def greet():
    print("Hello, world!")

greet()

#4.实际应用举例：计算函数执行时间

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} 执行时间: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("函数执行完毕")

slow_function()

