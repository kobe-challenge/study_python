
# 2.3
name = 'Eric'
print(f'Hello {name}, would you like to learn some Python today?')

# 2.4
name = 'Stephen Young'
print(name.lower())
print(name.upper())
print(name.title())

# 2.5
name = 'Albert Einstein'
quote = 'A person who never made a mistake never tried anything new.'
print(f'{name} once said, "{quote}"')

# 2.6
famous_person = 'Albert Einstein'
message = f'{famous_person} once said, "{quote}"'
print(message)

# 2.7
name = ' \tStephen Young\n \t'
print(name)
print(name.lstrip())
print(name.rstrip())
name = name.strip()
print(name)

# 2.8
filename = 'python_notes.txt'
print(filename)
print(filename.removeprefix('python_'))
print(filename.removesuffix('.txt'))