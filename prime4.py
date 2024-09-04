import pyttsx3
p=pyttsx3.init()
p.getProperty("rate",150)
def speak(c):
    p.ay(c)
    p.runAndWait
speak("Enter the last number")
i=int(input("Enter the last no."))
speak("Enter the first number")
j=int(input("Enter the first no."))
m=[]
def main(sel):
    if sel<2:
        return False
    else:
        for j in range(2,sel//2+1):
        
            if sel%j==0:
                return False
    return True
for hero in range(j,i+1):
    if main(hero):
        m.append(hero)
print(f"{m } These are the prime numbers between {j} and {i}")