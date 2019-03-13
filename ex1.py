data = '''
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release.
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart.
'''
token = data.split("\n")
result = [token[i][0] for i in range(1, len(token) - 1)]
for char in result:
	print(char, end = " ")
#C R O S S M Y H E A R T