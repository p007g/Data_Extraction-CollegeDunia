l1 = [0,1,3,5,7,9]
l2 = [1,2,4,5,6]
l3 = [0,3,5,8]
l4 = [3,4,6,7,9]

lst = [1,2,3,4]


all = [l1, l2, l3, l4]

# for l in all:
#     r1 = []
#     for a in lst:
#         found = False
#         for i in l:
#             if a == i:
#                 r1.append(a)
#                 found = True
#                 break
#         if found == False:
#             r1.append("")
#     print(r1)
    
    
for l in all:
    empt = ["", "", "", ""]
    for b in l:
        if b == 1:
            empt[0] = 1
        elif b ==2:
            empt[1] = 2
        elif b ==3:
            empt[2] = 3
        elif b ==4:
            empt[3] = 4
    print(empt)
    
    
    
# var lit1 = new List<int> { 0, 1, 3, 5, 7, 9 };
#  List<int> list2 = new List<int>();
#  for(int j = 1; j < 5; j++)
#  {
#      bool found= false;
#      foreach (var i in lit1)
#      {
#          if (i == j)
#          {
#              list2.Add(j);
#              found = true;
#              break;
#          }                    
#      }
#      if (!found)
#      {
#          list2.Add(0);
#      }

#  }

            
        # if i == 1:
        #     r1.append(i)
        #     continue
        # elif i == 2:
        #     r1.append(i)
        #     continue
        # elif i == 3:
        #     r1.append(i)
        #     continue
        # elif i == 4:
        #     r1.append(i)
        #     continue
        # else:
        #     continue
    
    # if 1 in l:
    #     r1.append(1)
    # else:
    #     r1.append("")
    # if 2 in l:
    #     r1.append(2)
    # else:
    #     r1.append("")
    # if 3 in l:
    #     r1.append(3)
    # else:
    #     r1.append("")
    # if 4 in l:
    #     r1.append(4)
    # else:
    #     r1.append("")
    
    
    # for i in l:
        
    #     if i == 1:
    #         r1.append(1)
    #         continue
        # else:
        #     r1.append("")
        # if i == 2:
        #     r1.append(2)
        # else:
        #     r1.append("")
        # if i == 3:
        #     r1.append(3)
        # else:
        #     r1.append("")
        # if i == 4:
        #     r1.append(4)
        # else:
        #     r1.append("")
            
    # print(r1)