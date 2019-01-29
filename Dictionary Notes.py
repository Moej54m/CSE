states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Alaska",
    "GA": "Georgia"
}
nested_dictionary ={
    "CA": {
         "NAME": "California",
        "POPULATION": 39500000
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000

    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000

    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000

    }
}

print(nested_dictionary["GA"]["POPULATION"])
print(nested_dictionary["FL"]["POPULATION"])

georgia = nested_dictionary["GA"]

states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Alaska",
    "GA": "Georgia"
}
nested_dictionary ={
    "CA": {
         "NAME": "California",
        "POPULATION": 39500000
        "Cities": [
        "Fresno",
        "San Francisco",
        "Los Angeles"
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000,
        "CITIES": [
            "Miami",
            "Orlando",
            "Tampa",
            "Jacksonville"
        ]

    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000,
        "CITIES": [
            "Anchorage"
            "Fairbanks"
            "Juneau"
        ]
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000,
        "CITIES": [
            "Atlanta",
            "Savannah",
            "Augusta"
        ]

    }
}

print(nested_dictionary["GA"]["POPULATION"])
print(nested_dictionary["FL"]["POPULATION"])

georgia = nested_dictionary["GA"]
