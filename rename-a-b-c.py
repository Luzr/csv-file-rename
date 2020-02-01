# change from [num]-name to, to [num]-a etc.

import os

_path = '.\\photos-a\\'

for filename in os.listdir(_path):
    name = filename.split("-")
    os.rename(_path+filename, _path + name[0] +'[name]'+'.jpg')