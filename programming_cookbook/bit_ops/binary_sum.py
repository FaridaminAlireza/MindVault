# You are not allowed to use the + or - operators.
# Given two integers a and b, return their sum using bitwise operations only.

def bitwise_sum(a, b):
   
    num_a = a
    num_b = b
    hold_over_bit = 0
    sum_result = 0
    offset = 1
    i = 0

    while (num_a or num_b):

        num_a =  (a >> i) 
        num_b =  (b >> i)

        num_a_bit = num_a & 1
        num_b_bit = num_b & 1

        result_bit = (num_a_bit ^ num_b_bit) ^ hold_over_bit

        hold_over_bit = ((num_a_bit & num_b_bit) |
                         ((num_a_bit ^ num_b_bit) & hold_over_bit))
        
    
        # sum_result += offset * result_bit
        #offset *= 2

        sum_result |= result_bit << i
        # note that Bitwise OR is not a replacement for addition.
        # It only sets bits that are 1 in either number.
      
        i += 1

    return sum_result


print(bitwise_sum(1, 255))
        

# with minor change in implementation         
def bitwise_sum_v2(a, b):
    sum_result = 0
    carry = 0
    i = 0

    while (a >> i) > 0 or (b >> i) > 0 or carry:
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1

        # sum of current bits + carry
        sum_bit = bit_a ^ bit_b ^ carry

        # compute new carry
        carry = (bit_a & bit_b) | ((bit_a ^ bit_b) & carry)

        # add sum_bit to the result
        sum_result |= (sum_bit << i)

        i += 1

    return sum_result


print(bitwise_sum_v2(1, 255))
        