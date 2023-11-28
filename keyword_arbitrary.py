def build_profile(first, last, **info):
    info["First name"] = first
    info["Last name"] = last

    return info
profile = build_profile("Matthew", "Fernandez", Section="ICT-1103", Fav_sub="Math", Location="Muntinlupa city")

for k, v in profile.items():
    print(f"The {k} is {v}")