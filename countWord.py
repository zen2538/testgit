source = '''
Lost in the sky
Clouds roll by and I roll with them
Arrows fly
Seas increase and then fall again
This world is spinning around me
This world is spinning without me and
Every day sends future to past
Every breath leaves me one less to my last
Watch the sparrow falling
Gives new meaning to it all
If not today nor yet tomorrow then some other day
I'll take seven lives for one
And then my only father's son
As sure as I did ever love him I am not afraid
This world is spinning around me
The whole world keeps spinning around me and
All life is future to past
Every breath leaves me one less to my last
Pull me under
Pull me under
Pull me under, I'm not afraid
All that I feel is honor and spite
All I can do is to set it right
Dust fills my eyes
Clouds roll by and I roll
'''
splitWord = []
cleanWord = []
countWord = {}
splitWord = source.split()
for word in splitWord:
    word = word.lower()
    word = word.strip()
    word = word.replace(",","")
    word = word.replace(".","")
    cleanWord.append(word)
for count in cleanWord:
    if count in countWord:
        countWord[count] += 1
    else :
        countWord[count] = 1

print(sorted(countWord.values(),reverse=True))
