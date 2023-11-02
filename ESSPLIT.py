adress = "192.168.0.1"
groups = adress.split(".")
groups = [int(group) for group in groups]
print(groups)
