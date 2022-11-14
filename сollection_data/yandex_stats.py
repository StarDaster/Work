stats = {"yandex": 120, "vk": 115, "google": 99, "email": 42, "ok": 98}

max_hesh = " "
for i in stats.keys():
	if stats[i]> stats.get(max_hesh,0):
		max_hesh = i
print(max_hesh.capitalize()) #capitalize для эстетики :)