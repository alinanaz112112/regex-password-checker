print('python')# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

pattern = r"[a-zA-Z0-9#$@%]{8,}\d"
password = "hello12khgjggggggguy"

a = re.fullmatch(pattern, password)
if a:
    print('Password is correct')
else:
    print('try again')
