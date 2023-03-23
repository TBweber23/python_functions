#Converting fahrenheit to celsius or vice versa
#Also converts lengths

#Conversion Functions
def inches_to_mm(length_in_inches):
    length_in_mm = length_in_inches * 25.4
    return length_in_mm

def mm_to_inches(length_in_mm):
    length_in_inches = length_in_mm / 25.4
    return length_in_inches

def feet_to_meters(length_in_feet):
    length_in_meters = length_in_feet * 0.3048
    return length_in_meters

def meters_to_feet(length_in_meters):
    length_in_feet = length_in_meters / 0.3048
    return length_in_feet

def f_to_c(temp_in_f):
    temp_in_c = (temp_in_f -32) * 5/9
    return temp_in_c

def c_to_f(temp_in_c):
    temp_in_f = (temp_in_c * 9/5 + 32)
    return temp_in_f

def perform_conversion(value, conversion_direction):
    if conversion_direction == "in>mm":
        #do inches to mm
        converted_value = inches_to_mm(value)
        print(f"{value} inches = {converted_value} mm")
    elif conversion_direction == "mm>in":
        #do mm to in
        converted_value = mm_to_inches(value)
        print(f"{value} mm = {converted_value} inches")
    #ft to m
    elif conversion_direction == "ft>mm":
        converted_value = feet_to_meters(value)
        print(f"{value} ft = {converted_value} meters")
    elif conversion_direction == "mm>ft":
        converted_value = feet_to_meters(value)
        print(f"{value} mm = {converted_value} meters")
    else:
        print("Invalid conversion direction")

#get length from user

while True:

    conversion_direction = input("Enter conversion direction (in>mm, mm>in, f>c, or c>f) or 'q' to quit: ")
    
    #exit loop if user types q
    if conversion_direction == "q":
        break
    
    value = float(input("Enter length: "))

    #Convert length using appropriate function
    #in>mm
    #value = float(input("enter value to be converted: "))

    perform_conversion(value, conversion_direction)
print ("Thanks for using the calc!")

#Convert length to mm

#inches_to_mm(length_in_inches)

#print result


