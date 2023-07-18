# class A():
#     pass
# class B(A):
#     pass

# print(isinstance(B(),A))
# print(type(B()) == A)
# if 1 == True:
#     print( True)
# else:
#     print(not True)
def reverseWords(input): 
      
    inputWords = input.split(" ") 
    inputWords=inputWords[-1::-1] 

    output = ' '.join(inputWords) 

    print(ord("H"))
    print(ord("h"))
    return output 
  
if __name__ == "__main__": 
    input = 'I like runoob'
    rw = reverseWords(input) 
    print(rw)