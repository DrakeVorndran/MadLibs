s =  ['''A %s in %s was arrested this morning after he %s a %s in from of %s . %s , had a history of %s , but no one, not even his %s ever imagined he'd %s with a %s stuck in his %s . “I always thought he was %s , but I never thought he'd do something like this. Even his %s was surprised.” After a brief %s , cops followed him to a %s , where he reportedly %s in the fry machine. In %s, a woman was charged with a similar crime. But rather than %s with a %s , she %s with a %s . Either way, we imagine that after witnessing him %s with a %s there are probably a whole lot of %s''', ['noun', 'Wacky_State', 'verb', 'noun', 'noun', 'proper_name', 'verb', 'noun', 'verb','noun', 'part_of_the_body', 'adjective', 'Relative', 'activity', 'chain_restaurant', 'Past_tense_adjective', 'month', 'verb', 'noun', 'Past_tense_verb', 'Adjective', 'verb', 'noun', 'plural_noun']]
for x in range(len(s[1])):  s[1][x] = (input(s[1][x]+':'))
print (s[0] % tuple(s[1]))
