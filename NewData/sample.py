import json
import random

with open('outwithOC.json') as f:
    js = json.load(f)

nums = []
while len(nums) < 200:
    val = random.randrange(len(js))
    if(val not in nums):
        nums.append(val)

sample = []
print(nums)
for i in nums:
    sample.append(js[i])

with open("sampleOC.json", "w") as outfile:
    json.dump(sample, outfile)