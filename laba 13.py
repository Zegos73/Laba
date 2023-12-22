import csv
passengers_from_queenstown = 0
survived_from_queenstown_within_age = 0
median_age = 20 

with open('titanic.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        if row['Embarked'] == 'Q':
            passengers_from_queenstown += 1

            try:
                age = float(row['Age'])
                if median_age - 10 <= age <= median_age + 10:
                    if row['Survived'] == '1':  
                        survived_from_queenstown_within_age += 1
            except ValueError:
                pass

print(f"Количество пассажиров из порта Квинстауна: {passengers_from_queenstown}")
print(f"Количество выживших пассажиров в возрастном интервале медиана +- 10: {survived_from_queenstown_within_age}")
