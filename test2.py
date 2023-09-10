signal = input("Signal color? ")

if signal == "red":
    print("Stop!")
elif signal == "yellow":
    print("Slow down!")
elif signal == "blue" or signal == "green":
    print("Go!")
else:
    print("Invalid signal color...")
