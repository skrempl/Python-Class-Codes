import random

basses = ["Schecter RIOT 5",
        "MTD Custom",
        "Fender Pbass",
        "Fender Jazz",
        "Carvin",
        "Upright bass",
        "Electric Upright"]

type = ["jazz",
        "rock",
        "motown",
        "R&B",
        "pop",
        "church",
        "swing"]

random_bass = random.choice(basses)
random_type = random.choice(type)

print(f"How about you take the {random_bass} to the {random_type} gig?")
