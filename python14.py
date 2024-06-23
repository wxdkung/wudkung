"""
#
# Part Python PIP
# 
"""

# pip List
# pip install --upgrade pip
# pip install camelcase
# pip uninstall camelcase

import camelcase
camel = camelcase.CamelCase()
txt = "hello wolrd"
print(camel.hump(txt))