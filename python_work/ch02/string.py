"This is a string."
'This is also a string.'

'I told my friend, "Python is my favorite language!"'
'The language "Python" is named after Monty Python, not the snake.'
"One of Python's strengths is its diverse and supportive community."

# 字符串可以用单引号，也可以用双引号，这样就能在字符串中包含引号。

name = "ada lovelace"
print(name.title()) # 将字符串s中的每个单词的首字母大写

name = "Ada Lovelace"
print(name.upper()) # 将字符串s中的所有字母大写
print(name.lower()) # 将字符串s中的所有字母小写

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name # 字符串拼接
full_name = f'{first_name} {last_name}' # f-string 推荐使用方法。
print(full_name)

print(f'Hello, {full_name.title()}!')
message = f'Hello, {full_name.title()}!'
print(message)

print("Python")
print("\tPython") # \t制表符
print("Languages:\nPython\nC\nJavaScript") # \n换行符
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip()) # 删除字符串末尾的空白
print(favorite_language.lstrip()) # 删除字符串开头的空白
print(favorite_language.strip()) # 删除字符串两端的空白

#
nostarch_url = 'http://www.nostarch.com'
print(nostarch_url)
nostarch_url.removeprefix('http://')
print(nostarch_url)
simple_url = nostarch_url.removesuffix('http://')