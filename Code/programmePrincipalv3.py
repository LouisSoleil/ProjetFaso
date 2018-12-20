#Fonctions
#initialisation ecran : 
import time,sys
if sys.platform == 'uwp':
	import winrt_smbus as smbus
	bus = smbus.SMBus(1)
else:
	import smbus
	import RPi.GPIO as GPIO
	rev = GPIO.RPI_REVISION
	if rev == 2 or rev == 3:
		bus = smbus.SMBus(1)
	else:
		bus = smbus.SMBus(0)

# this device has two I2C addresses
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e

# set backlight to (R,G,B) (values from 0..255 for each)
def setRGB(r,g,b):
	bus.write_byte_data(DISPLAY_RGB_ADDR,0,0)
	bus.write_byte_data(DISPLAY_RGB_ADDR,1,0)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xaa)
	bus.write_byte_data(DISPLAY_RGB_ADDR,4,r)
	bus.write_byte_data(DISPLAY_RGB_ADDR,3,g)
	bus.write_byte_data(DISPLAY_RGB_ADDR,2,b)

# send command to display (no need for external use)    
def textCommand(cmd):
	bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)

# set display text \n for second line(or auto wrap)     
def setText(text):
	textCommand(0x01) # clear display
	time.sleep(.05)
	textCommand(0x08 | 0x04) # display on, no cursor
	textCommand(0x28) # 2 lines
	time.sleep(.05)
	count = 0
	row = 0
	for c in text:
   		if c == '\n' or count == 16:
         		count = 0
         		row += 1
         		if row == 2:
             			break
         		textCommand(0xc0)
         		if c == '\n':
             			continue
     		count += 1
     		bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))

#Update the display without erasing the display
def setText_norefresh(text):
	textCommand(0x02) # return home
	time.sleep(.05)
	textCommand(0x08 | 0x04) # display on, no cursor
	textCommand(0x28) # 2 lines
	time.sleep(.05)
	count = 0
	row = 0
	while len(text) < 32: #clears the rest of the screen
     		text += ' '
		for c in text:
			if c == '\n' or count == 16:
        	 		count = 0
         			row += 1
         			if row == 2:
             				break
         			textCommand(0xc0)
         			if c == '\n':
             				continue
			count += 1
			bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))
#bouton
# Importons les packs
import time
import grovepi
import datetime 


# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
button=3

grovepi.pinMode(button,"INPUT")

potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")
buzzer = 4 
grovepi.pinMode(buzzer,"OUTPUT")
fin = 1
r = 0
p = 0
ultrasonic_ranger = 2
date = str(datetime.datetime.now())




def recommencer() :
        fin=1
        r=0
        p=0
        setRGB(250,0,250)
        time.sleep(.1)
        setText("Combien de pompes ?")
        while p != 1:
              sensor_value = grovepi.analogRead(potentiometer)
              time.sleep(0.8)
              nb = (int)((sensor_value)/10)
              setText_norefresh("Nombre de pompe : {} ".format(str(nb)))
              time.sleep(.1)
              if grovepi.digitalRead(button)==1 :
                      p = p+1
        time.sleep(0.1)
        nbe = ("Nombre de pompe : " + str(nb))
        debut=9
        //faire la mesure avec le capteur de temperature avant leffort
        avant = "temperature corporelle avant effort : str(tavant)"
        while debut != 0 :
                setText_norefresh("Debut de seance dans {}".format(str(debut)))
                debut=debut-1
                time.sleep(1)
        textCommand(0x01)
        time.sleep(0.1)
        setRGB(250,0,0)
        time.sleep(0.1)
        setText_norefresh("{} pompes restantes".format(str(nb)))
        time.sleep(.5)
        cpt = nb #nombre de pompe a faire au depart 
        while cpt!=0: 
                if grovepi.ultrasonicRead(ultrasonic_ranger)<15:
				cpt=cpt-1
				setText_norefresh("{} pompes restantes".format(str(cpt))) 
				time.sleep(.1)
				grovepi.digitalWrite(buzzer,1)
				time.sleep(.2)
				grovepi.digitalWrite(buzzer,0)
				time.sleep(.1)
				time.sleep(0.5)
        grovepi.digitalWrite(buzzer,1)
        time.sleep(.8)
        grovepi.digitalWrite(buzzer,0)
        //faire la messure avec le capteur de température après leffort
        apres = "temperature corporelle apres effort : str(tapres)"
        fichier = open("valeur.txt", "a")
        fichier.write(date + " ; " + nbe + "\n")
        time.sleep(.4)
        setText("Voulez-vous recommencez ?")
        time.sleep(2)
        setText("Si oui maintenez le bouton")
        while r != 4 :
                r = r+1
                time.sleep(1)
                if grovepi.digitalRead(button)==1 :
                        recommencer()
                        r=4











while fin!=0: 
	if grovepi.digitalRead(button)==1 : 
		setRGB(250,0,250)
		setText("Bonjour Louis")
		time.sleep(3)
		setText("combien de pompes ?")
		while p != 1:
                      sensor_value = grovepi.analogRead(potentiometer)
                      time.sleep(0.8)
                      nb = (int)((sensor_value)/10)
                      setText_norefresh("Nombre de pompe : {} ".format(str(nb)))
                      time.sleep(.1)
                      if grovepi.digitalRead(button)==1 :
                              p = p+1
                nbe = (" Nombre de pompe :"+" "+str(nb)
		time.sleep(0.1)
        nbe = ("Nombre de pompe : " + str(nb))
		debut=9
        //faire la mesure avec le capteur de temperature avant leffort
        avant = "temperature corporelle avant effort : str(tavant)"
		while debut != 0 :
                        setText_norefresh("Debut de seance dans {}".format(str(debut)))
                        debut=debut-1
                        time.sleep(1)
                textCommand(0x01)
                time.sleep(.1)
                setRGB(250,0,0)
		setText_norefresh("{} pompes restantes".format(str(nb)))
		time.sleep(.5)
                cpt = nb #nombre de pompe a faire au depart 
		while cpt!=0: 
			if grovepi.ultrasonicRead(ultrasonic_ranger)<15:
				cpt=cpt-1
				setText_norefresh("{} pompes restantes".format(str(cpt))) 
				time.sleep(.1)
				grovepi.digitalWrite(buzzer,1)
				time.sleep(.2)
				grovepi.digitalWrite(buzzer,0)
				time.sleep(.1)
				time.sleep(0.5)
		time.sleep(0.5)
		grovepi.digitalWrite(buzzer,1)
		time.sleep(.8)
		grovepi.digitalWrite(buzzer,0)
        //faire la messure avec le capteur de température après leffort
        apres = "temperature corporelle apres effort : str(tapres)"
        fichier = open("valeur.txt", "a")
        fichier.write(date + " ; " + nbe + "\n")
                time.sleep(.4)
                setText("Voulez-vous recommencez ?")
                time.sleep(2)
                setText("Si oui maintenez\nle bouton")
                while r != 4 :
                        r = r+1
                        time.sleep(1)
                        if grovepi.digitalRead(button)==1 :
                                recommencer()
                                r=4
                time.sleep(.1)
                setRGB(0,250,0)
                time.sleep(0.1)
                setText("Vous avez \n termine !")
                time.sleep(2)
                textCommand(0x01)
                time.sleep(.1)
                setRGB(0,0,0)
                time.sleep(.1)
                fin = fin-1


