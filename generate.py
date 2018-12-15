import os

os.system('pelican')
os.system('git -C ../images1 ad')
os.system('git -C ../images1 ci "Auto Push"')
os.system('git -C ../images1 ph')
os.system('git ad')
os.system('git ci "Auto Push"')
os.system('git ph')
os.system('ghp-import -p output')
