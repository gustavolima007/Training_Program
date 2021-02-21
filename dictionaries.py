dict = {"k1": "Cat", "k2": "Dog", "k3": "Mouse", "k4": "Fish"}
print(dict)

print(dict["k1"])

print(dict["k3"])

dict["k5"] = "Parrot"
print(dict)

dict["k2"] = "Squirrel"
print(dict)


dep_workers = {"dep_1": "Peter", "dep_2": ["Jennifer", "Michael", "Tommy"]}
print(dep_workers["dep_2"])


Team = {}
Team["Point Guard"] = "Dirk"
Team["Shooting Guard"] = "Al"
Team["Small Forward"] = "Sean"
Team["Power Forward"] = "Alexander"
Team["Center"] = "Hector"
print(Team)

print(Team["Center"])

print(Team.get("Small Forward"))

print(Team.get("Coach"))]
