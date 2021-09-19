# Python-CV-Neon-Light-effect
This is a set of codes poorly optimize and without any error handling, feel free to improve it and teach me how, the main pourpuse is to give a neon light effect to your images, and it does just that. The neon effect can be improved by changing some paramenters in the functions so feel free to do so.
For this to work you need to have Photoshop installed on your computer.
There are 5 functions to make this possible, all of them need to be on your computer but you only need to call the GetLines function.
Inside the GetLines.py program other functions are called. You can install this package using pip install NeonLightEffect

## GetLines:
This is the main function that will recive the arguments given by the user and transmit the necessary information for the remaining functions. This function recives 7 arguments, (Edges, Background, Lradius, Iradius, line_color, light_color, SavePath).
It will also determinate the region where you want to apply the neon light effect.

### 1st argument
The first argument is an image with the lines where we want to apply the effect, for this to work properly the lines need to be on a black background. To get this lines I use normally use the cv2.Canny() funtion but other methods can be used.

### 2nd argument
The second argument is the background where you want to put the neon light.

### 3rd argument
The third argument is the size of line that will the center and source of the neon light, if 1 (px) is given the actual size will be 2 (px). This needs to be an integer.

### 4th argument
The fourth argument is the size of inner glow if 1 (px) the actual size will be 1 (px).

### 5th argument
The fifth argument is the color of the source of light, white is recommended, but it can support a list of colors and even a list of colors created using the colour library. The format of each individual the color must be [.. , .. , ..].

### 6th argument
The sixth argument is the color of the inner and outer glow, it supports only one color, a list of colors and a list of colors create using the colour library. The format of each individual the color must be [.. , .. , ..].

### 7th argument
The seventh argument is th path to place where the different will images will be saved and final result. It needs to be a string

## InnerGlow
This function in the Inner_glow script will give the inner glow of the neon light effect, all it's arguments are given by the GetLines function. 
This inner glow is made with the help of the cv2.circle() function. And depending on the size of the inner glow as it aproaches the middle of the light it's itensity decreases.
This function will save a JPEG file in your computer named InnerGlow in the path the user provided and return this new image.

## AddLine
This function in the AddLine script will give the source of light of the neon light, all it's arguments are given by the GetLines function. It will increase the thickness of the lines passed to the GetLines funtion and write it on top of the image given by the InnerGlow function. The increase in thickness is due to the use of cv2.circle() function.
This function will save a JPEG file in your computer named Line in the path the user provided and return this new image.

## OuterGlow
This function in the Outer_glow script will give the outer glow of the neon light effect, all it's arguments are given by the GetLines function. It will create a transparent image where the outer glow will be written
This outer glow is also made with the help of the cv2.circle() function. And two layers will be create with different sizes, the opacity of thsi two layers will be changed with the cv2.addWeighted() function and two PNG images will be created and saved in your computer named OuterGlow1 for the smaller and more bright glow and OuterGlow2 for the larger and less bright glow. The Eraser funtion is called to erase all the color of this two images over the source of light and inner glow.

## PyPS
This funtions runs a script that will use Photoshop to put everything together, and give all the effects necessary to create the effect, it will make use of the files saved previously and save the final result as JPEG file in your computer named NeonLight in the
path the user provided. All it's arguments are given by the GetLines function. 


