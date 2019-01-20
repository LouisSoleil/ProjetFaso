import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
 
msg['From'] = 'pushup.coach@gmail.com'
msg['To'] = 'louis.soleilhavoup@gmail.com'
msg['Subject'] = 'Félicitation pour votre session'
 
body = "Ci-joint, vos résultats de votre session d'aujourd'hui ainsi que les précédentes \n Bonne continuation."
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "valeur.txt"
attachment = open("a modifier", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("pushup.coach@gmail.com", "pushupcoachIG3")
text = msg.as_string()
server.sendmail("pushup.coach@gmail.com", 'louis.soleilhavoup@gmail.com', text)
server.quit()