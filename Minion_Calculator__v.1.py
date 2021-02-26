time_between_Actions = 14.4
Your_Name = "Dianas"
"A s at the end"
Minions = 17
time_in_sec = 0
time_in_min = 0
time_in_hours = 0
time_in_days = 1
time_in_weeks = 0 
time_in_months = 0
time_in_years = 0
"Enter 4 for Clay ,if not enter 1"
blocks_per_Harvest = 1


One_Item = time_between_Actions * 2
Items_in_one_sec = 1 / One_Item
Time = time_in_sec + time_in_min * 60 + time_in_hours * 3600 + time_in_days * 86400 + time_in_weeks * 604876 + time_in_months * 2628000 + time_in_years * 31540000
Collection = Items_in_one_sec * Time * Minions * blocks_per_Harvest
collection_in_stacks = Collection / 64
Enchanted_Items = Collection / 160
Enchanted_Blocks = Enchanted_Items / 160 
Enchanted_Blocks_in_stacks = Enchanted_Blocks / 64
Enchanted_Items_in_stacks = Enchanted_Items / 64 


print("")
print(f"{Your_Name} Input")
print("")
print(f"{time_between_Actions} Sec between Actions")
print(f"{Minions} Minions" )
print(f"{Time} Sec")
print("")
print("Output")
print("")
print("Collection")
print(f"{Collection} Items")
print("In Stacks")
print(f"{collection_in_stacks} Stacks")
print("")
print("Enchanted Items")
print(f"{Enchanted_Items} Items")
print("In Stacks")
print(f"{Enchanted_Items_in_stacks} Stacks")
print("")
print("Enchanted Blocks")
print(f"{Enchanted_Blocks} Items")
print("In Stacks")
print(f"{Enchanted_Blocks_in_stacks} Stacks")
print("")
print("")
print("")
print("")
print("")
print("Made by Adrian John")





