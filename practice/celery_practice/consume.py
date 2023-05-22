from tasks import add

res = add.delay(2, 3)
print(res)
