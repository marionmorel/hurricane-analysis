# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def update_damages(damages):
  conversion = {"M": 1000000,
                "B": 1000000000}
  updated_damages = []
  for damage in damages:
    if "B" in damage:
      updated_damages.append(float(damage[:-1]) * conversion["B"])
    elif "M" in damage:
      updated_damages.append(float(damage[:-1]) * conversion["M"])
    else:
      updated_damages.append(damage)
  return updated_damages

# test function by updating damages
updated_damages_list = update_damages(damages)
print(updated_damages_list)

# 2 
# Create a Table
def create_hurr_dict():
  hurricanes = {}
  for i in range(len(names)):
    hurricane = {"Name": names[i], "Month": months[i], "Year": years[i], "Max Sustained Wind": max_sustained_winds[i], "Areas Affected": areas_affected[i], "Damage": updated_damages_list[i], "Deaths": deaths[i]}
    hurricanes[names[i]] = hurricane
  return hurricanes;
  
# Create and view the hurricanes dictionary
hurricane_dictionary = create_hurr_dict()
print(hurricane_dictionary)

# 3
# Organizing by Year
def group_by_year(hurricanes):
  grouped_dict = {}
  for hurr in hurricanes:
    year = hurricanes[hurr]["Year"]
    hurr_data = hurricanes[hurr]
    if year not in grouped_dict:
      grouped_dict[year] = [hurr_data]
    else:
      grouped_dict[year].append(hurr_data)
  return grouped_dict

# create a new dictionary of hurricanes with year and key
hurricanes_by_year = group_by_year(hurricane_dictionary)
print(hurricanes_by_year)

# 4
# Counting Damaged Areas
def count_areas(hurricanes):
  area_count = {}
  for hurr in hurricanes:
    for area in hurricanes[hurr]["Areas Affected"]:
      if area not in area_count:
        area_count[area] = 1
      else:
        area_count[area] += 1
  return area_count

# create dictionary of areas to store the number of hurricanes involved in each area
area_count = count_areas(hurricane_dictionary)
print(area_count)

# 5 
# Calculating Maximum Hurricane Count
def most_hit_area(area_count):
  max_area = ""
  max_area_count = 0
  for area in area_count:
    if area_count[area] > max_area_count:
      max_area = area
      max_area_count = area_count[area]
    else:
      continue
  print("Most affected area: " + max_area + ", hit by " + str(max_area_count) + " hurricanes")

# find most frequently affected area and the number of hurricanes involved in
most_hit_area(area_count)

# 6
# Calculating the Deadliest Hurricane
def deathliest(hurricanes):
  max_deaths = 0
  deathliest_hurricane = ""
  for hurr in hurricanes:
    if hurricanes[hurr]["Deaths"] > max_deaths:
      deathliest_hurricane = hurr
      max_deaths = hurricanes[hurr]["Deaths"]
    else:
      continue
  print("Deadliest hurricane: " + deathliest_hurricane + ", " + str(max_deaths) + " deaths")

# find highest mortality hurricane and the number of deaths
deathliest(hurricane_dictionary)

# 7
# Rating Hurricanes by Mortality
def mortality_rate(hurricanes):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000,
                   5: 100000}
  grouped_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for hurr in hurricanes:
    death_toll = hurricanes[hurr]["Deaths"]
    data = hurricanes[hurr]
    for i in mortality_scale:
      if death_toll > mortality_scale[i]:
        continue
      else:
        grouped_by_mortality[i].append(data)
        break
  return grouped_by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_mortality_scale = mortality_rate(hurricane_dictionary)
print(hurricanes_mortality_scale)

# 8 Calculating Hurricane Maximum Damage
def costliest(hurricanes):
  max_cost = 0
  costliest_hurricane = ""
  for hurr in hurricanes:
    if hurricanes[hurr]["Damage"] == "Damages not recorded":
      hurricanes[hurr]["Damage"] = 0
    elif hurricanes[hurr]["Damage"] > max_cost:
      costliest_hurricane = hurr
      max_cost = hurricanes[hurr]["Damage"]
    else:
      continue
  print("Costliest hurricane: " + costliest_hurricane + ", $" + str(max_cost) + " in damages")

# find highest damage inducing hurricane and its total cost
costliest(hurricane_dictionary)

# 9
# Rating Hurricanes by Damage
def damage_severity(hurricanes):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  grouped_by_severity = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for hurr in hurricanes:
    damage = hurricanes[hurr]["Damage"]
    data = hurricanes[hurr]
    if damage == "Damages not recorded":
      grouped_by_severity[0].append(data)
    elif damage == damage_scale[0]:
      grouped_by_severity[0].append(data)
    elif damage > damage_scale[0] and damage <= damage_scale[1]:
      grouped_by_severity[1].append(data)
    elif damage > damage_scale[1] and damage <= damage_scale[2]:
      grouped_by_severity[2].append(data)
    elif damage > damage_scale[2] and damage <= damage_scale[3]:
      grouped_by_severity[3].append(data)
    elif damage > damage_scale[3] and damage <= damage_scale[4]:
      grouped_by_severity[4].append(data)
    elif damage > damage_scale[4]:
      grouped_by_severity[5].append(data)
  return grouped_by_severity
  
# categorize hurricanes in new dictionary with damage severity as key
hurricanes_severity_scale = damage_severity(hurricane_dictionary)
print(hurricanes_severity_scale)