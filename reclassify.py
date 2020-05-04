# EGS Favorability
def Reclass(arg):
    if (arg >= 1 and arg < 2):
        return 1
    elif (arg >= 2 and arg < 3):
        return 0.75
    elif (arg >= 3 and arg < 4):
        return 0.50
    elif (arg >= 4 and arg < 5):
        return 0.25
    else:
        return 0


# GDR Submissions
def Reclass(arg):
    if (arg < 1):
        return 1
    elif (arg >= 1 and arg < 3):
        return 0.75
    elif (arg >= 3 and arg < 10):
        return 0.50
    elif (arg >= 10 and arg < 50):
        return 0.25
    else:
        return 0


# Operating Geothermal Stations
def Reclass(arg):
    if (arg == 0):
        return 1
    else:
        return 0

# Developing Geothermal Stations
def Reclass(arg):
    if (arg == 0):
        return 1
    else:
        return 0

# Research Potential
((0.35 * !EGS_Favorability!) + (0.35 * !GDR_Submissions!) + (0.15 * !Operating_Stations!) + (0.15 * !Developing_Stations!))
