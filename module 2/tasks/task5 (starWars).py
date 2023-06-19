import requests
nums = [0, 1, 2, 4, 7]
url = 'https://swapi.dev/api/'
response = requests.get(url).json()
starships_api = response.get('starships')
response = requests.get(starships_api).json()
Max = int(response['results'][nums[0]]["max_atmosphering_speed"])
max_num = 0
for num in nums[1:]:
    if Max <= int(response['results'][num]["max_atmosphering_speed"]):
        Max = int(response['results'][num]["max_atmosphering_speed"])
        max_num = num
print(response['results'][max_num]["name"])
