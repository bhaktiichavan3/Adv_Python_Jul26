my_list = [1,2,3]
my_list[0] = 10

my_tuple = (1,2,3)

def pure_process(data):
    return data + (4,5,6)

original = (1,2,3)
processed = pure_process(original)

print(original)
print(processed)