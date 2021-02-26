time_between_Actions = 14.4
Minions = 17
time_in_sek = 0
time_in_min = 0
time_in_hours = 0
time_in_days = 1
time_in_weeks = 0 
time_in_months = 0
time_in_years = 0

One_Item = time_between_Actions * 2
Items_in_one_sek = 1 / One_Item
Time = time_in_sek + time_in_min * 60 + time_in_hours * 3600 + time_in_days * 86400 + time_in_weeks * 604876 + time_in_months * 2628000 + time_in_years * 31540000
Collection = Items_in_one_sek * Time * Minions
collection_in_stacks = Collection / 64
Enchanted_Items = Collection / 160
Enchanted_Blocks = Enchanted_Items / 160 
Enchanted_Blocks_in_stacks = Enchanted_Blocks / 64
Enchanted_Items_in_stacks = Enchanted_Items / 64 

print("")
print("Your Input")
print("")
print("Time between Actions")
print(time_between_Actions)
print("Minions")
print(Minions)
print("Time in Sek")
print(Time)
print("")
print("Output")
print("")
print("Collection")
print(Collection)
print("In Stacks")
print(collection_in_stacks)
print("")
print("Enchanted Items")
print(Enchanted_Items)
print("In Stacks")
print(Enchanted_Items_in_stacks)
print("")
print("Enchanted Blocks")
print(Enchanted_Blocks)
print("In Stacks")
print(Enchanted_Blocks_in_stacks)
print("")
print("")
print("")
print("")
print("")
print("Made by Adrian John")
