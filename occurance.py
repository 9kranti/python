"""
22. Take 2 lists and print only matching number the number of time it matches
"""

def occurrence():
    try:
        list1 = [1,2,3,4,5,6]
        list2 = [2, 4, 6, 6]
        count = 0
        count_list = []
        number_occurred = []
        for x in list1:
            for y in list2:
                if x == y:
                    count = count + 1
            if count > 0:
                number_occurred.append(x)
                count_list.append(count)
            count = 0

        print(number_occurred)
        print(count_list)
        print("Below is the result we get in pair where 1st element is occured element and 2nd element is occurrence number")
        print(list(zip(number_occurred, count_list)))
    except Exception as e:
        print("Got an error saying ", str(e))

occurrence()
