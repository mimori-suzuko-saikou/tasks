#!/usr/bin/env python3
# coding=utf-8
# Author:梁枫

import random

nums=[random.randint(0,99) for i in range(50)]
nums.sort()
nums=[str(num) for num in nums]

f=open('list file','a+')
f.write(','.join(nums)+'\n')
f.seek(0,0)
print(f.read())
nums.reverse()
f.write(','.join(nums)+'\n')
f.close()