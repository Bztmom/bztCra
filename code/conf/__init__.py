#coding=utf-8

import os

__all__ = filter(lambda filename: not filename.startswith("__"),[filename.split(".")[0] for filename in os.listdir("./conf") if filename.endswith(".py")])
print __all__