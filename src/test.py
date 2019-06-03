def load_results():
    name = "venkatesh"
    file_name = name+".txt"
    text_file = open(file_name, "r")
    items = text_file.read().split()
    text_file.close()
    return items

print(load_results())

def save_results(arr):
    name = "ven"
    file_name = name+".txt"
    text_file = open(file_name, "w")
    for item in arr:
      text_file.write(str(item)+ " ")
    text_file.close()

save_results(["a","b","c","d","e"])    