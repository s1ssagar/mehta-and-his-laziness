import math
def gcd(num1,num2):
    if num1 <= 1 or num2 <= 1:
        return 1
    if num1 < num2:
        num2,num1 = num1,num2
    while num1 % num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num2
        
def prime_factors(num):
    prime_fac = {}
    count = 0
    while num % 2 == 0:
        num /= 2
        count += 1
    if count > 0:
        prime_fac[2] = count
    for divisor in range(3,int(math.sqrt(num))+1,2):
        count = 0
        while num % divisor == 0:
            count += 1
            num /= divisor
        if count > 0:
            prime_fac[divisor] = count
    if num > 2:
        prime_fac[num] = 1
    num_factors = 1
    for key,value in prime_fac.iteritems():
        num_factors *= (value+1)
    return num_factors-1

def mehta_i_saved_you():
    perfect_squares = [x*x for x in range(2,3164)]
    tc = input()
    while tc > 0:
        num = input()
        num_fac = prime_factors(num)
        count = 0
        div_count = 0
        if num % 2 == 0:
            while perfect_squares[count] <= num/2:
                if num % perfect_squares[count] == 0 and perfect_squares[count] % 2 == 0:
                    div_count += 1
                count += 1
            if div_count != 0:
                div = gcd(div_count,num_fac)
                if div != 1:
                    print str(div_count/div)+'/'+str(num_fac/div)
                else:
                    print str(div_count)+'/'+str(num_fac)
            else:
                print 0
        else:
            print 0
        tc -= 1

mehta_i_saved_you()