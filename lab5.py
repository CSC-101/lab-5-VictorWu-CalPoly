from data import Time, Point
import math

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.

# Part 2
   # The function for Part 2 should be within the class in data.py.

# Part 3
def time_add(x:Time, y:Time) -> Time:
    total_hours = x.hour + y.hour           #add the hours from the inputted x and y objects
    total_minutes = x.minute + y.minute     #add the minutes from the inputted x and y objects
    total_seconds = x.second + y.second     #add the seconds from the inputted x and y objects
    while total_seconds >= 60:              #While seconds >= 60:
        total_seconds -= 60                 #Subtract 60 from sec.
        total_minutes += 1                  #Plus 1 to minutes

    while total_minutes >= 60:              #While minutes >= 60:
        total_minutes -= 60                 #Subtract 60 from min.
        total_hours += 1                    #Plus 1 to hours
    return Time(total_hours, total_minutes, total_seconds)

# Part 4
def is_descending(numbers:list[float]) -> list[float]:
    for idx in range(len(numbers) - 1):                 #For each object in the list from range(EX:5):
        for jdx in range(0, len(numbers) - idx - 1):    #AND for range[0,(5-0-1)] idx is 0, jdx is 0, range is 4 / Loop comparison
            if numbers[jdx] < numbers[jdx + 1]:         #Swaps if current number less than the adjacent number if necessary
                numbers[jdx], numbers[jdx + 1] = numbers[jdx + 1], numbers[jdx] #debug for #[2.2, 5.2, 3.3, 9.9, 1.1]
    return numbers

# Part 5
def largest_between(numbers:list[int],lower:int,upper:int) -> int:
    if lower > upper:           #Return none if lower is >= upper
        return None

    #Adjust if lower or upper out of bounds
    lower = max(0, lower)
    upper = min(len(numbers) - 1, upper)

    largest_value = None         #Storage/ Placeholder for the largest value
    largest_index = None         #Storage/ Placeholder for the largest index

    for x in range(lower, upper+1):   #Include the lower bound but the +1 is because range typically doesn't include the last value, this ensures its value is included.
        current_value = numbers[x]
        if largest_value is None or current_value > largest_value:  #(1st ITER) IF largest_value is a placeholder is None EX: 5 or (2nd ITER) current value > largest value EX: 6:
            largest_value = current_value                           #changes largest value to the current value is necessary
            largest_index = x                                       #changes largest index to the current largest value's index
    return largest_index

# Part 6
def furthest_from_origin(points:list[Point]) -> int:
    if not points:
        return None

    furthest_index = None               #storage for furthest index
    furthest_distance = 0               #storage for furthest distance

    for i in range(len(points)):        #range(3) so i = 0, 1, 2, which are the Point objects in list
        distance = math.sqrt(points[i].x ** 2 + points[i].y ** 2)   #for each Point object in the list grab their x and y values and find the distance from origin

        if distance > furthest_distance:                            #1st Iter: It will be true and replace 0 with Iter, now on Iter 2 if the new calculated distance > old furthest distance continue
            furthest_distance = distance                            #replacing eq
            furthest_index = i                                      #change the index because that's what we're trying to grab
    return furthest_index
