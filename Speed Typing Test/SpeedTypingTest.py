from time import time
from random import randint
# calculate the accuracy of input prompt
def Errors(prompt):
    global iwords

    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        if i in (0, len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors +=1
        else:
            if iwords[i] == words[i]:
                if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

# calculate the speed in words per minute
def Speed(iprompt, Start_time, End_time):
    global time
    global iwords

    iwords = iprompt.split(" ")
    twords = len(iwords)
    speed = twords / ttime(Start_time, End_time)

    return speed

def ttime(Start_time, End_time):
    time = End_time - Start_time
    return time

if __name__ == '__main__':
    WordDict = [
        "The uncommon and speedy increase in Earth’s average temperature is called global warming. This growth has extensively been higher within the last century due to human intervention with nature"
        ,"The release of greenhouse gasses in the ecosystem has been one of the number one motives behind the boom in temperature. The multiplied intake of fossil fuels has extended the attention of greenhouse gasses."      
        ,"The effect of world Warming is a lot higher than just a sore in temperature."      
        ,"It modifies the rainfall pattern, intensifies coastal erosion, lengthens seasons in line with geography, the glaciers and ice caps are melting and will increase the range of continual and infectious illnesses."      
        ,"When atoms split, the process is called nuclear fission"
        ,"In nuclear fission a small amount of mass is converted into energy."
        ,"Women’s Day has been observed by SAARC (South Asian Association for Regional Cooperation) comprising seven countries namely India, Pakistan, Nepal, Bhutan, Bangladesh, Sri Lanka and Maldives"
        ,"Everyone knows that paper is made from trees. But when one looks at trees, one cannot imagine that something so soft and fragile as the paper is made is so hard and strong"
            ]

    prompt= WordDict[int(randint(0,6))]
    print("Type this:-\n\t", prompt, "'")

    input("Press ENTER when you are ready!\n\t")

    Start_time = time()
    iprompt = input("")
    End_time = time()

    # gather all the information returned from functions
    time = round(ttime(Start_time, End_time), 2)
    speed = Speed(iprompt, Start_time, End_time)
    errors = Errors(prompt)

    # printing all the required data
    print("Total Time elapsed : ", time, "s")
    print("Your Average Typing Speed was : ", speed, "words / minute")
    print("With a total of : ", errors, "errors")
