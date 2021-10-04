import isbn

code = input('Enter an ISBN code: ')
result = isbn.is_valid(code)

print(f'Is the ISBN code {code} valid? {result}')