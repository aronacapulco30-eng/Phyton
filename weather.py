temperature = int(input("Enter the temperature in celsius"))

if temperature < 20:
 outfit = "jacket"
 print("It is cold.")
 print("Wear a", outfit)

else:
 outfit = "T shirt"
 print("It is hot")
 print("Go wear a", outfit)



is_raining = input("Is it raining today? (yes/no): " ) 

if is_raining == "yes":
 print("Bring an umbrella")

else:
 print("No, you done need an umbrella")


wind_speed = int(input("Enter the wind speed in km/h: "))

if wind_speed > 30:
 needs_windbreaker = "yes"
 print("YOU NEED A WINDBREAKER")

else:
 needs_windbreaker = "no"
 print("You dont need it")


has_puddles = input("Are there puddles on the ground? (yes/no): ")

if has_puddles == "yes":
 shoes = "Boots"
 print("You should wear", shoes)

else: 
 shoes = "Sandals"
 print("You can wear", shoes)


print("")

print("Weather check complete!")


print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", temperature)
print("Outfit Chosen:", outfit)
print("Raining:", is_raining)
print("Windbreaker Needed:", needs_windbreaker)
print("Shoes Chosen:", shoes)
print("===================================")
