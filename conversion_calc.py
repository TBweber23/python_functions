#Converting fahrenheit to celsius or vice versa
#Also converts lengths

#Conversion Functions
def inches_to_mm(length_in_inches):
    length_in_mm = length_in_inches * 25.4
    return length_in_mm

def mm_to_inches(length_in_mm):
    length_in_inches = length_in_mm / 25.4
    return length_in_inches

#get length from user

conversion_direction = input("Enter conversion direction (in>mm or mm>in): ")
length = float(input("Enter length: "))

#Convert length using appropriate function
#in>mm
if conversion_direction == "in>mm":
    #do inches to mm
    converted_len = inches_to_mm(length)
    print(f"{length} inches = {converted_len} mm")
elif conversion_direction == "mm>in":
    #do mm to in
    converted_len = mm_to_inches(length)
    print(f"{length} mm = {converted_len} inches")
else:
    print("Invalid conversion direction")


#Convert length to mm

#inches_to_mm(length_in_inches)

#print result


