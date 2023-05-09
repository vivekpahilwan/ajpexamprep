byte = int(input("Enter number in byte:"))
bit = byte/8
mb = bit/1024**2
gb = bit/1024**3
tb = bit/1024**4
print(mb, gb, tb)
