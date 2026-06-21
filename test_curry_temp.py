from returns.curry import curry

@curry
def add3(a: int, b: int = 1, c: int = 2) -> int:
    return a + b + c

# 测试1：只传一个参数
result1 = add3(10)
print(f'add3(10) = {result1}')
print(f'  type: {type(result1)}')

# 测试2：传两个参数
result2 = add3(10, 20)
print(f'add3(10, 20) = {result2}')
print(f'  type: {type(result2)}')

# 测试3：传所有参数
result3 = add3(10, 20, 30)
print(f'add3(10, 20, 30) = {result3}')

# 测试4：用关键字参数传默认值
result4 = add3(10, b=1)
print(f'add3(10, b=1) = {result4}')
print(f'  type: {type(result4)}')

# 测试5：看看能不能链式调用
try:
    result5 = add3(10)(20)
    print(f'add3(10)(20) = {result5}')
except Exception as e:
    print(f'add3(10)(20) 报错: {e}')

# 测试6：所有参数都有默认值的情况
@curry
def greet(name: str = 'world', greeting: str = 'Hello') -> str:
    return f'{greeting}, {name}!'

print()
result6 = greet()
print(f'greet() = {result6}')
print(f'  type: {type(result6)}')
