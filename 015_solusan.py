#########TRANSPORTESAN MODE SLECTION#######
distence=5

if distence<3:
    transport="Walk"
elif distence<=15:
    transport="Bike"
else:
    transport="car"
print("jayaga:",transport)
    