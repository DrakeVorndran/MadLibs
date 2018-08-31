s = ['''Pizza was invented by a %s %s chef named  %s. To make a pizza, you need to take a lump of %s, and make a thin, round %s %s. Then you cover it with %s sauce, %s cheese, and fresh chopped %s. Next you have to bake it in a very hot %s. When it is done, cut it into %s %s. Some kids like %s pizza the best, but my favorite is the %s pizza. If I could, I would eat pizza %s times a day!.''' ,["adjective","nationality","person","noun","adjective","noun","adjective","adjective","plural noun","noun","number","shapes","food","food","number"]]
for x in range(len(s[1])):
    s[1][x] = (input(s[1][x]+''': '''))
print (s[0] % tuple(s[1]))
