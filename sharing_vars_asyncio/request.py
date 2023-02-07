

data_id = [1, 2, 3, 4, 5]
print(data_id)
req = {data_id[i]: [True] for i in range(len(data_id))}
print(req)

global req

def