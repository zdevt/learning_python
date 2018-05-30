import re
import operator

fin = open( '../../tinyxml2/tinyxml2.cpp', 'r' )
str = fin.read( )
reObj = re.compile( '\b?(\w+)\b?' )
words = reObj.findall( str )
wordDict = dict( )

for word in words:
    if word.lower( ) in wordDict:
        wordDict[word.lower( )] += 1
    else:
        wordDict[word] = 1

a = sorted( wordDict.items( ), key = lambda iterm: iterm[1], reverse = True )

# for k, v in wordDict.items( ):
#     print("%s:%s" % (k, v))

for e in a:
    print(e)
