import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText


msg = MIMEMultipart()
 
msg['From'] = 'pushup.coach@gmail.com'
msg['To'] = 'louis.soleilhavoup@gmail.com'
msg['Subject'] = 'Felicitation pour votre session'
 
message = "Ci-joint, vos resultats de votre session d'aujourd'hui ainsi que les precedentes \n \nBonne continuation."
 
msg.attach(MIMEText(message))
 
filename = "valeur.txt"
attachment = open("/home/pi/Desktop/ProjetFaso/CodePrincipal/valeur.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())

part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("pushup.coach@gmail.com", "pushupcoachIG3")
text = msg.as_string()
server.sendmail("pushup.coach@gmail.com", 'louis.soleilhavoup@gmail.com', msg.as_string())
server.quit()
