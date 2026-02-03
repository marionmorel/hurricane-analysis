# Hurricane Analysis
## Data Scientist: Analytics - Codecademy

### Overview

This project is slightly different than others you have encountered thus far on Codecademy. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you’ll be building. There are many possible ways to correctly fulfill all of these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

In order to complete this project, you should have completed the Loops and Dictionaries sections of the Learn Python 3 Course. 

### Project Goals

You will work to write several functions that organize and manipulate data about Category 5 Hurricanes, the strongest hurricanes as rated by their wind speed. Each one of these functions will use a number of parameters, conditionals, lists, dictionaries, string manipulation, and return statements.

### Tasks

1. Hurricanes, also known as cyclones or typhoons, are one of the most powerful forces of nature on Earth. Due to climate change caused by human activity, the number and intensity of hurricanes has risen, calling for better preparation by the many communities that are devastated by them. As a concerned environmentalist, you want to look at data about the most powerful hurricanes that have occurred.

Begin by looking at the <code>damages</code> list. The list contains strings representing the total cost in USD($) caused by <code>34</code> category 5 hurricanes (wind speeds ≥ 157 mph (252 km/h )) in the Atlantic region. For some of the hurricanes, damage data was not recorded (<code>"Damages not recorded"</code>), while the rest are written in the format <code>"Prefix-B/M"</code>, where </code>B</code> stands for billions (</code>1000000000</code>) and <code>M</code> stands for millions (<code>1000000</code>).

Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as <code>"Damages not recorded"</code>.

Test your function with the data stored in <code>damages</code>.

2. Additional data collected on the <code>34</code> strongest Atlantic hurricanes are provided in a series of lists. The data includes:

* <code>names</code>: names of the hurricanes
* <code>months</code>: months in which the hurricanes occurred
* <code>years</code>: years in which the hurricanes occurred
* <code>max_sustained_winds</code>: maximum sustained winds (miles per hour) of the hurricanes
* <code>areas_affected</code>: list of different areas affected by each of the hurricanes
* <code>deaths</code>: total number of deaths caused by each of the hurricanes

The data is organized such that the data at each index, from <code>0</code> to <code>33</code>, corresponds to the same hurricane.

For example, <code>names[0]</code> yields the “Cuba I” hurricane, which ouccred in <code>months[0]</code> (October) <code>years[0]</code> (1924).

Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (<code>Name</code>, <code>Month</code>, <code>Year</code>, <code>Max Sustained Wind</code>, <code>Areas Affected</code>, <code>Damage</code>, <code>Death</code>) about the hurricane.

Thus the key "Cuba I" would have the value: <code>{'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}</code>.

Test your function on the lists of data provided.

3. In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year.

Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.

For example, the key <code>1932</code> would yield the value: <code>[{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United States'], 'Damage': 'Damages not recorded', 'Deaths': 16}, {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}]</code>.

Test your function on your hurricane dictionary.

4. You believe that knowing how often each of the areas of the Atlantic are affected by these strong hurricanes is important for making preparations for future hurricanes.

Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.

Test your function on your hurricane dictionary.

5. Write a function that finds the area affected by the most hurricanes, and how often it was hit.

Test your function on your affected area dictionary.

6. Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.

Test your function on your hurricane dictionary.

7. Just as hurricanes are rated by their windspeed, you want to try rating hurricanes based on other metrics.

Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating.

```
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
```

For example, a hurricane with a <code>1</code> mortality rating would have resulted in greater than <code>0</code> but less than or equal to <code>100</code> deaths. A hurricane with a <code>5</code> mortality rating would have resulted in greater than <code>10000</code> deaths.

Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating.

Test your function on your hurricane dictionary.

8. Write a function that finds the hurricane that caused the greatest damage, and how costly it was.

Test your function on your hurricane dictionary.

9. Lastly, you want to rate hurricanes according to how much damage they cause.

Write a function that rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating.

```
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
```

For example, a hurricane with a <code>1</code> damage rating would have resulted in damages greater than <code>0</code> USD but less than or equal to <code>100000000</code> USD. A hurricane with a <code>5</code> damage rating would have resulted in damages greater than <code>50000000000</code> USD (talk about a lot of money).

Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating.

Test your function on your hurricane dictionary.