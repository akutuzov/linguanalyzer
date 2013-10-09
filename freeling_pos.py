#!/bin/python
# coding: utf-8
# Extracting POS marks of words with Freeling
# author: Andrey Kutuzov
# GPL v 3.0
from __future__ import division
import sys
import subprocess as sp

language = sys.argv[1]

config = u'/usr/local/share/freeling/config/%s.cfg' % language

counter = 0
for line in sys.stdin:
	tagset = []
	tagged = sp.Popen([u'threaded_analyzer', u'-f', config], stdin=sp.PIPE, stdout=sp.PIPE).communicate(line)[0]
	tagged = tagged.strip().split('\n')
	for word in tagged:
		word = word.split()
		if word:
		# and word[0] != ',' and word[0] != '.' and word[0] != '?' and word[0] != '!':
			tagset.append(word[2])
	tagset = "\n".join(tagset)
	print tagset
	print "============="