def create_user(username, stage_level, money, troop_storage, spell_storage, castle_storage, other_storage):
    """
    example of troop storage:
    {'warrior': [(boolean - unlocked?), (integer - level_of_troop)],
    'archer' :[(boolean - unlocked?), (integer - level_of_troop)]...}
    same for spell_storage, castle_storage and other_storage
    """

    all_data = {
        "username": username,
        "stage_level": stage_level,  # can be list if you want else just integer
        "money": money,  # money that the user have
        "troop_storage": troop_storage,
        "spell_storage": spell_storage,
        "castle_storage": castle_storage,
        "other_storage": other_storage
    }
    return all_data

username = "Ewen"
stage_level = 5
money = 1000
troop_storage = {
    "warrior": [True, 2],
    "archer" :[True, 3],
    "wizard":[False, 1],
    "sparta":[True,1],
    "giant":[False,2]
}
spell_storage = {
    "rage":[True,1],
    "healing":[True,2],
    "freeza":[False,1]
}
castle_storage = {
    "default_castle":[True,1,1]   # two upgrade
}
other_storage = {
}

user1 = create_user(username,stage_level,money,troop_storage,spell_storage,castle_storage,other_storage)
# print(user1)
# you guys can do changes on the data based on what you need, just change to what you want
# here is just the idea of data, you can use them in your python file.
