#the_database
data_base={"Red":[255,0,0],
           "Green":[0,255,0],
           "Blue":[0,0,255],
           "Dark_Red":[139,0,0],
           "Black":[0,0,0],
           "White":[255,255,255],
           "Grey":[82,82,82],
           "Brown":[48,34,15],
           "Forest Green":[41,97,37],
           "Light Green":[91,255,79],
           "Light Red":[255,91,91],
           "Orange": [255,170,0],
           "Magenta": [255,0,255],
           "Cyan": [0,255,255],
            "Yellow": [255,255,0] 
           }

def square_root(x):
    return x**(1/2)
def power(x,a):
    return x**a
 
def arrange(item, dimension,min,max):                                                #Normalize Function
    item_count = len(item)
    game_changer = item[:]

    for i in range(dimension):
        if(i < item_count):
            game_changer[i] = (game_changer[i] - min)*100/(max - min)
        else:
            game_changer[i] = 50*100/(max - min)
    return game_changer

def vectorSimilarity(A,B):                                                            #Similarity Function
    if len(A) != len(B):
        return -1
    else:
        len_ = len(A)
        total = 0
        for i in range(len_):
            total += power(B[i] - A[i], 2)
        distance = float(square_root(total))
        max_dist = 0
        for i in range(len_):
            max_dist += power(100,2)
        max_dist = square_root(max_dist)

        return 1- (distance/max_dist)
    return 0

def RGB_Similarity_Calculator(item1,item2):                                           #Limited Dimension Edition (3D)
    item1_1 = arrange(item1 ,3,0,255)
    item2_2 = arrange(item2 ,3,0,255)

    return vectorSimilarity(item1_1,item2_2)

print("Please write your 255-0 RGB value. For example-> Orange: [255,170,0]\n")
try:                                                                                  #user panel
    RGB_r = int(input("Red:"))
    RGB_g = int(input("Green:"))
    RGB_b = int(input("Blue:"))

except ValueError as V_error:
    print("We need three integer value between 255-0\n")

user_color = [RGB_r,RGB_g,RGB_b]

for i in user_color:
    if i >255:
        i = 255
    elif i<0:
        i = 0

Legend = [[colors, RGB_Similarity_Calculator(user_color,data_base[colors])] for colors in data_base]

max_rgb = max(Legend, key=lambda x: x[1])[0]
max_rgb_value = max(Legend, key=lambda x: x[1])
print("Closest color: ", max_rgb)
print("Similarity Rate: ", max_rgb_value) 






















