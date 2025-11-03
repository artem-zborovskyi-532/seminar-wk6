# Exercise 2:
    # Write in pseudo code a function merge(listA: List, listB: List) that returns a
    # sorted list containing the elements of both list where listA and listB are two sorted lists
    # of integers. If an element exists in both lists, it must appear multiple times in the returned list.
    # For example:
        # >>> merge([1,3,4,7],[2,3,5])
        # [1,2,3,3,4,5,7]

def merge(listA:list[int], listB:list[int]) -> list[int]:
    # Make sure that listA stores the list that is bigger
    if len(listB) > len(listA):
        return merge(listB, listA)
    
    res = listA.copy()
    shift = 0
    for elB in listB:
        for index, elA in enumerate(listA):
            if elA >= elB:
                res.insert(index + shift, elB)
                shift += 1
                break

    return res