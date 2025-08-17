url = input()

urls = url.replace(':', '')
result = urls.split('/')

print(f"protocol: {result[0]}")
print(f"host: {result[2]}")
print(f"others: {result[3]}")