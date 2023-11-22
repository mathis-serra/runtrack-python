def time_to_text(minutes):
    heures = minutes // 60
    minutes = minutes % 60
    print(heures, "heures et", minutes, "minutes")
time_to_text(32)
