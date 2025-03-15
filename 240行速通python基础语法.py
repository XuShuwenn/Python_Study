print("Hello,World!")
"""
演示字典的常用操作
字典有如下特点：
1.可以容纳多个数据
2.可以容纳不同数据类型的数据
3.每一份数据是key-value键值对
4.可以通过key获取到value,key不可以重复
5.不支持下标索引
6.可以修改
7.支持for循环，不支持while循环
"""
my_dict = {"zhoujielun": 33, "linjunjie": 88, "zhangxueyou": 77}
# 新增元素
print(f"字典经过更新后，结果：{my_dict}")
# 删除元素pop
score = my_dict.pop("zhoujielun")
print(f"字典中被移除了一个元素，结果：{my_dict},周杰伦的考试分数是：{score}")
# 清空元素clear
my_dict.clear()
print(f"字典被清空，结果：{my_dict}")
# 获取全部的key
my_dict = {"zhoujielun": 33, "linjunjie": 88, "zhangxueyou": 77}
keys = my_dict.keys()
print(f"字典的全部key是：{keys}")
# 遍历字典
# 方式1：通过获取全部的key来完成操作
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")
# 方式2：直接对字典进行for循环，每一次循环都直接得到key
for key in my_dict:
    print(f"字典的key:{key}")
    print(f"字典的value：{my_dict}")
# 统计字典内的元素数量len()函数
num = len(my_dict)
print(f"字典中的元素数量有{num}个")
"""
数据容器从以下视角进行分类：
1.是否支持下标索引：
    支持：列表、元组、字符串-序列类型
    不支持：集合、字典-非序列类型
2.是否可以修改：
    支持：列表、集合、字典
    不支持：字符串、元组
3.是否支持重复元素：
    支持：列表、元组、字符串-序列类型
    不支持：集合、字典

数据容器的通用操作：
1. len(容器)统计容器中的元素个数
max()统计最大元素
min()统计最小元素
字符串、字典关键字 会按照ASCII码的字典序比较大小
2. 通用类型转换：
list()转列表：其中list(字典)即将字典中的key取出
str()转字符串
tuple()转元组
set()转集合
因为缺失键值对，其他类型不能转字典
3.通用排序功能：
sorted(容器,[reverse=True])
将给定容器进行排序
"""
my_list = [2, 1, 9, 3, 8, 5, 4, 6, 7]
print(f"排序结果为：{sorted(my_list)}")

print(f"Hello,Python functions!")
"""
函数4种参数使用方式:
1.位置参数：
2.关键字参数：按照“键=值”形式传递
！！！注意：函数调用时，若有位置参数，位置参数必须在关键字参数前面，但关键字参数之间不存在先后顺序
3.缺省参数（或称为默认参数）：用于定义函数，为参数提供默认值，调用函数时可以不传入该默认参数的值
！！！注意：函数调用时，默认参数必须放在最后面
4.不定长参数
a. 位置不定长：传进的所有参数都会被args变量收集，根据位置先后合并成为一个元组，args是元组类型
b. 关键字不定长：被kwargs收集，根据键-值组成字典
"""
def user_info(name,age,gender):
    print(f"姓名是{name},年龄是{age},性别是{gender}")
#位置参数-默认使用形式
user_info('小明',20,'男')
#关键字参数
user_info(name='小王',gender='女',age=11)
#位置参数和关键字参数混用
user_info('甜甜',gender='女',age=10)

"""
函数作为参数传入：
lambda匿名函数
def关键字，定义带有名称的函数，可多次调用
lambda关键字，定义匿名函数（无名称），只可以临时使用一次
"""
#def关键字：
def test_func(compute):
    result=compute(1,2)
    print(result)
def compute(x,y):
    return x+y
test_func(compute)

#lambda关键字：
def test_func1(compute1):
    result1=compute(1,2)
    print(result1)
test_func1(lambda x,y:x+y)

"""
类和对象
class 类名称
    成员变量
    def 成员方法(self,参数列表):
    成员方法体

对象=类名称()
面向对象编程，就是使用对象进行编程
"""
class Student:
    name=None
    def say_hi(self):
        print(f"大家好，我是{self.name}")

stu=Student()
stu.name="周杰伦"
stu.say_hi()

"""
python类可以使用:__init__()方法，成为构造方法
可以实现：
1.在创建类对象（构造类）时，会自动执行
2.在创建类对象（构造类）时，将传入参数自动传递给__init__()方法使用
"""

class Student:
    name=None
    age=None
    tel=None
    def __init__(self,name,age,tel):#构造方法
        self.name=name
        self.age=age
        self.tel=tel
        print("Student类创建了一个类对象")
    def __str__(self):              #__str__字符串方法
        return f"Student类对象，name:{self.name},age:{self.age}"

stu=Student("周杰伦",31,"18963306029")
print(stu.name)
print(stu.age)
print(stu.tel)
"""
构造方法的作用：
1.构造类对象时候会自动执行
2.构建类对象的传参会传递给构造方法，给成员变量赋值

魔术方法：
1.__str__字符串方法
2.__lt__小于符号比较方法
3.__le__小于等于比较方法
4.__eq__相等比较方法

面向对象编程思想：“封装、继承、多态”
私有成员变量/私有成员方法:__开头
私有成员方法无法被类对象使用，私有变量无法赋值，也无法获取值
1.封装：将现实世界事物在类中描述为属性和方法，即为封装
  私有成员：类对象无法访问私有成员；类中其他成员可以访问私有成员
2.继承
class 类(父类1,父类2,...,父类N):
    类内容体/pass
3.多态：多种状态，使用不同对象会得到不同的状态
"""
class Phone:
    __current_voltage =0.5  #当前手机运行电压
    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print("5G通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5G通话，并已设置为单核运行进行省电")
phone=Phone()
phone.call_by_5G()
#单继承
class phone:
    IMEI=None #序列号
    producer="HW" #厂商
    def call_by_4G(self):
        print("4G通话")

class Phone2025(Phone): #父类
    face_id=10001  #面部识别id
    def call_by_5G(self):
        print("2025最新5G通话")
"""
多继承：一个类可以同时继承多个类
class 类名(父类1,父类2,父类3)
"""
class NFC_Reader:
    nfc_type="第五代"
    producer="HW"
    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")
class RemoteControl:
    rc_type="红外遥控"
    def control(self):
        print("红外遥控已开启")
class MyPhone(Phone,NFC_Reader,RemoteControl):#同名成员，左边优先
    pass  #使得语法正确
phone1=MyPhone()
phone1.call_by_5G()
phone1.read_card()
phone1.write_card()
phone1.control()
#复写：子类中重新定义父类中同名的属性或方法
"""
类型注解：在代码中涉及数据交互时，提供数据类型的注解（显式说明）
基础语法：变量：类型
var_1:int=10
class Student:
    pass
stu:Student=Student()

函数和方法的类型注解：
def 函数方法名(形参名:类型,形参名:类型,...)->list[Record]:
    pass
Union 类型：
from typing import Union
my_list:list[Union[str,int]]=[1,2,"inheima","itcast"]
Uinon[类型, 类型]

多态常作用在继承关系上
比如，1.函数（方法）形参声明接受父类对象
     2.实际传入父类的子类对象进行工作，获得同一行为的不同动作

抽象类（接口）：用来作顶层设计，并不直接使用
"""
