ids = {
    "user1": [213, 213, 213, 15, 213],
    "user2": [54, 54, 119, 119, 119],
    "user3": [213, 98, 98, 35]
}
ids_new = list(ids["user1"] + ids["user2"] + ids["user3"])
ids_new = set(ids_new)
ids_new = list(ids_new)
print(ids_new)
