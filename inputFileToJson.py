import json

input_file = "input.txt"
dataList = []
data = {}
key =  ''
value = ''
with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        key, value = line.split(maxsplit=1)
        # Remove quotes from key
        key = key.strip('"')


        value = value.strip('"')
        data[key] = value
dataList.append(data)        
print(json.dumps(data, indent=4))
print(dataList)