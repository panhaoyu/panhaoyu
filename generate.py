import os

os.system('pelican')
os.system('git -C ../image1 ad')
os.system('git -C ../image1 ci "Auto Push"')
os.system('git -C ../image1 ph')
os.system('git ad')
os.system('git ci "Auto Push"')
os.system('git ph')
