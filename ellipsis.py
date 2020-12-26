#!/usr/bin/python3

import os
import sys
import re
import argparse

from pathlib import Path

'''
Replace instances of `...' with `…' in files within the current working
directory if they are not inside of
```
backticked code blocks.
```

Corner cases:
- Replaces sequences inside of `inline code elements`, which may not be
  desired.
- Doesn't work with nested code chunks.
'''

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--inplace', help='edit files in place', action='store_true')

args = parser.parse_args()

for x in os.walk('.'):
	for y in x[2]:
		print(Path(x[0])/Path(y))
		with open(Path(x[0])/Path(y)) as f:
			inside_code_block = False
			buff = ''
			for line in f:
				if re.compile('^```+\w*$').match(line):
					inside_code_block = not inside_code_block
				elif not inside_code_block:
					line = re.sub('\.\.\.', '…', line)
				buff += line
			# print(buff)
