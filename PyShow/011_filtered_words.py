# -*- coding: utf-8 -*-


word_filter = set( )

with open( '011_filtered_words.txt' ) as f:
    for w in f.readlines( ):
        word_filter.add( w.strip( ) )

# for x in word_filter:
#     print(x)

s = raw_input( "please input:" )

if s in word_filter:
    print ("fxxx")
else:
    print("goodaa")
