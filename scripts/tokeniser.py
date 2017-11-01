# Program for segmenting the Silesian Wikipedia and keeping track of article names and paragraph/sentence IDs

import sys 

title = ''

for blokk in sys.stdin.read().split('\n\n'): 
	paragraphs = blokk.split('\n')
	if len(paragraphs) < 2: 
		continue
	title = paragraphs[0].strip().replace(' ', '_')
	for line in paragraphs[1:]:
		# Deal with abbreviations 
		sentences = line.replace('. ', '.\n').split('\n')
		sentIdx = 1
		for sent in sentences:
			sent = sent.strip()
			if sent == '':
				continue
			print('# sent_id = %s%d' % (title, sentIdx));
			print('# text = %s' % (sent))
			# Deal with abbreviations and punctuation
			tokens = sent.split(' ')
			tokIdx = 1
			for token in tokens:
				print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (tokIdx, token, '_','_','_','_','_','_','_','_'))
				tokIdx += 1
			print()
			sentIdx += 1
	
