import os, sys
try:
    __import__("bot").bot()
except Exception as e:
    exit(str(e))
