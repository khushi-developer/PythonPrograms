import re

str='''
khushipadadune@gmail.com she is from
gp nd scsmcoe
nd not a topper of the university
khushi was too clever nd she got marks as ususal to afford good colleage
her friends go in gr8 colleages where have grood compus placements but she still in nagar
nd dont go in colleage where have big campuses
she decided to develope a company
japmnies@yahoo.com
nd today all gr8 colleage students are employee of her company
nd she is owner of the company
so colleage dont decide your future
sunenahgsjg@eqqu.com
if u sble for successs dosent matter anything colleage percentage not even degree
u got success
so choose ur habit carefully they decide ur future
niti@gmail.com
sammi@dea.com
'''

email=re.findall(r"[a-zA-Z0-9._+%]+@[a-zA-z0-9._+%]+[.]+[a-zA-Z0=9._+%]",str)
print(email)