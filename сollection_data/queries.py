queries = [
  "смотреть сериалы онлайн", 
  "новости спорта", 
  "афиша кино", 
  "курс доллара",
  "сериалы этим летом", 
  "курс по питону", 
  "сериалы про спорт",
  "кто же я",
  "я же точно",
  "я же",
  "я",
  "кто"
  
]

queries_new = {}
for i in queries:
	l = len(i.split(" "))
	queries_new[l] = queries_new.get(l, -1)+1
queries_new = {f"{k} Строк(и) с одинаковым количеством слов ":
               f"{s/sum(queries_new.values()):.2%}" 
               for k,s in queries_new.items()}
print(queries_new)