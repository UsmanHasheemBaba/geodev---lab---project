# This line is a comment. Python ignores it.
# print("Hello from Niger State")
# print(5000 * 4)
# print(20 / 4)

# State = "Niger State"
# print(State)
# State = "Kaduna State"
# print(State)

# population = 10000
# buffer_distance = 200
# ward_name = "Bosso LGA"
# print("ward_name, buffer_distance")

# ward_name = "Bosso LGA"
# ward_count = 999
# area_km2 = 5000.3
# is_capital = False
# print(type(ward_name), type(ward_count), type(area_km2), type(is_capital))

# case_1 = 10 + 10
# case_2 = "10" + "10"
# print(case_1, case_2)
# case_3 = "Bosso" + " LGA"
# print(case_1, case_2, case_3)

# area_text = "50.4"
# area_number = float(area_text)
# print(area_number * 2)

#LISTS
# lga = ["Bosso", "Chanchaga", "Paikoro", "Rafi"]
# print(lga)
# print(len(lga))
# print(lga[0])
# print(lga[1])
# lga.append("Shiroro")
# print(lga)

# lga = ["Bosso", "Chanchaga", "Paikoro", "Rafi"]

# for lga_name in lga:
#     print("Checking", lga_name)

# area = [2, 4, 6, 8, 10] #Bosso, Chanchaga, Paikoro, Rafi, Shiroro

# for area in area:
#     hecter = area * 10
#     print(area, "square kilometer is ", hecter, "hecters")
#     print("Done")

# lga = 1500

# if lga > 1500:
#     print("large lga")
# else:
#     print("small lga")
    
#Comparisms
# lga = "Bosso"
# print(lga == "Bosso")
# print(lga == "Chanchaga")
# print(lga != "Chanchaga")

# bosso_hectares = 200 * 2
# chanchage_hectares = 400 * 2
# paikoro_hectares = 600 * 2

# def km2_to_hectares(area):
#     return area * 2


# print(km2_to_hectares(200))
# print(km2_to_hectares(400))
# print(km2_to_hectares(600))

def describe(lga, count):
    return lga + " has " + str(count) + " wards"

print(describe("Bosso", 10))
