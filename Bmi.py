Geschlecht = input ('Geben Sie ihre Geschlecht ein : W or M' )
if Geschlecht =='W':
    print('Weblich')
else:
    print('Männlich')    
Größe = int(input('Geben Sie ihre Größe ein:'))
Gewicht = int (input('Geben Sie ihre Gewicht ein:')) 
Bmi = (Gewicht / (Größe*Größe))*10000
print(Bmi)

if Bmi <= 18.5:
    print(	'Untergewicht')
elif  Bmi> 18.5 and Bmi<= 24.9:
    print('Normalgewicht ')
elif Bmi>= 30 and Bmi<= 34.9 :
    print('Adipositas Grad I ')
elif Bmi >=35 and Bmi<= 39.9 :
    print('Adipositas Grad II ')
else :
    print('Adipositas Grad III ')    
