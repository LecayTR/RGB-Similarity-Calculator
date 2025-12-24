#the_database
red = [255,0,0]
green=[0,255,0]
blue =[0,0,255]
dark_red = [181, 25, 25]
black = [0,0,0]
white = [255, 255, 255]
grey = [82, 82, 82]
brown = [48, 34,15]


def square_root(x):
    return x**(1/2)
    
def power(x,a):
    return x**a

def arrange(item, dimension,min,max):      #Normalize Function
    item_count = len(item)

    for i in range(dimension):
        if(i <= item_count):
            item[i] = (item[i] - min)*100/(max - min)
        else:
            item[i] = 50*100/(max - min)
    return item

def vectorSimilarity(A,B):                 #Similarity Function
    if len(A) != len(B):
        return -1
    else:
        len_ = len(A)
        total = 0
        for i in range(len_):
            total += power((B[i] - A[i]), 2)
        distance = square_root(total)
        max_dist = 0
        for i in range(len_):
            max_dist += power(100,2)
        max_dist = square_root(max_dist)

        return 1 - (distance/max_dist)
    return 0
    
def RGB_Similarity_Calculator(item1,item2):       #Limited Dimension Edition (3D)
    item1 = arrange(item1 ,3,0,255)
    item2 = arrange(item2 ,3,0,255)
    
    return vectorSimilarity(item1,item2)


print(RGB_Similarity_Calculator(white,red))


    


    

    




        