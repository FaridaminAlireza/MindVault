# You are given an array of integers heights[] representing
# the height of bars in a histogram. Each bar has a width of 1.
# Your task is to find the area of the largest rectangle that can
# be formed within the histogram.

# Ex heights = [2, 1, 5, 6, 2, 3] Output: 10

# Approach using hash map
def find_largest_rect_area(heights):

    max_area = 0
   

    for start_indx, end_indx, order in  (
        (0, len(heights),1), (len(heights)-1, -1,-1)):

        bar_tracker = dict()

        for i in range(start_indx, end_indx, order):
            bar_tracker.setdefault(heights[i], 0)
    
            for k in bar_tracker.keys():
                if k > heights[i]:
                    max_area = max(max_area, k * bar_tracker[k])
                    bar_tracker[k] = 0
                else:
                    bar_tracker[k] +=1

            # print(bar_tracker)
        for k in bar_tracker.keys():
            max_area = max(max_area, k * bar_tracker[k])
  
    return max_area

# heights = [2, 1, 5, 6, 2, 3]
# print(find_largest_rect_area(heights)) # Outputs 10
# heights = [2, 4, 8, 3]
# print(find_largest_rect_area(heights)) # Outputs 8
# heights = [2, 4]
# print(find_largest_rect_area(heights)) # Outputs 4
# heights = [6, 2, 5, 4, 5, 1, 6]
# print(find_largest_rect_area(heights)) # Outputs 12
# heights = [1, 1, 1, 1]
# print(find_largest_rect_area(heights)) # Outputs 4
# heights = [0, 9]
# print(find_largest_rect_area(heights)) # Outputs 9
# heights = [2, 1, 2]
# print(find_largest_rect_area(heights)) 

# Approach using stack    
def find_largest_rect_area(heights):

    max_area = 0
    if not heights:
        return 0

    for start_indx, end_indx, order in  (
        (1, len(heights),1),):
        #   (len(heights)-2, -1,-1)):
        
        stack_ls  = [(start_indx -1, heights[start_indx-1])]
   
        min_height_so_far = [0, heights[start_indx-1]]
        for i in range(start_indx, end_indx, order):

            if min_height_so_far[1] > heights[i]:
                min_height_so_far = [1+min_height_so_far[0] , heights[i]]
            else:
                min_height_so_far[0] = 1+ min_height_so_far[0]

            last_item =  stack_ls[-1]
            counter = 0
            while(len(stack_ls) and stack_ls[-1][1] > heights[i]):
                print('start check')
                counter +=1
                indx, item = stack_ls.pop()

                
                if item != last_item:
                    last_item = item 
                    # counter = 1

                if last_item <= min_height_so_far[1]:
                    s = counter + min_height_so_far[0]
                else:
                    s = counter

                last_item_area =  s * last_item 
                print(last_item,  min_height_so_far[1], counter)
                max_area =  max(max_area, last_item_area)
          

            stack_ls.append((i,heights[i]))
        

        last_item =  stack_ls[-1]
        counter = 0
 
        while(len(stack_ls)):
            indx, item = stack_ls.pop()
            counter += 1
            if item != last_item:
                last_item = item
                # counter = 1

            if last_item <= min_height_so_far[1]:
                s = counter + min_height_so_far[0]
            else:
                s = counter
          
            last_item_area = s * last_item 
            print(last_item, s, last_item)
            max_area =  max(max_area, last_item_area)
  
            
    return max_area
# print('-------------------')
# heights = [2, 1, 5, 6, 2, 3]
# print(find_largest_rect_area(heights)) # Outputs 10
# heights = [2, 4, 8, 3]
# print(find_largest_rect_area(heights)) # Outputs 8
# heights = [2, 4]
# print(find_largest_rect_area(heights)) # Outputs 4
heights = [6, 2, 5, 4, 5, 1, 6]
print(find_largest_rect_area(heights)) # Outputs 12
# heights = [1, 1, 1, 1]
# print(find_largest_rect_area(heights)) # Outputs 4
# heights = [0, 9]
# print(find_largest_rect_area(heights)) # Outputs 9
# heights = [2, 1, 2]
# print(find_largest_rect_area(heights)) 
