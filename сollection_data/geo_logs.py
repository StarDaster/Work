geo_logs = [{"visit1": ["Москва", "Россия"]},
            {"visit2": ["Дели", "Индия"]},
            {"visit3": ["Владимир", "Россия"]},
            {"visit4": ["Лиссабон", "Португалия"]},
            {"visit5": ["Париж", "Франция"]},
            {"visit6": ["Лиссабон", "Португалия"]},
            {"visit7": ["Тула", "Россия"]},
            {"visit8": ["Тула", "Россия"]},
            {"visit9": ["Курск", "Россия"]},
            {"visit10": ["Архангельск", "Россия"]},
            ]

geo_logs_new = []

for visits in geo_logs:
    for countrys in visits.values():
        for capitals in range(len(countrys)):
            if countrys[capitals] == "Россия":
                geo_logs_new.append(visits)
print(geo_logs_new)
