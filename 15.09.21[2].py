list1=[1,2,3,4,5,6,7,8]
list2=[4, 5, 6, 7, 8, 9]
def intersection_lists(list1, list2):
 set_1 = set(list1)
 set_2 = set(list2)
 set_3 = set_1 & set_2
 return list(set_3)
print(intersection_lists(list1,list2))