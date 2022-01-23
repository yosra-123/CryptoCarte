######################################
import random

import datetime
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import hashlib
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import binascii

# Generate 1024-bit RSA key pair (private + public key)
keyPair = RSA.generate(bits=1024)
pubKey = keyPair.publickey()


image = Image.new('RGB', (1500, 1000), (255, 255, 255))
draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=45)


d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(reg_format_date)
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

# starting position of the message
(x, y) = (50, 50)
company = input('\nEnter Your Company Name: ')

color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=80)
draw.text((x, y), company, fill=color, font=font)

# adding an unique id number. You can manually take it from user
(x, y) = (600, 75)
idno = random.randint(10000000, 90000000)
message = str('ID: ' + str(idno))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)

# For the Name
(x, y) = (50, 250)
name = input('Enter Your Full Name: ')

fname = str('Name: ' + str(name))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), fname, fill=color, font=font)

# For the email
(x, y) = (50, 350)
email = input('Enter Your email: ')

femail = str('Email: ' + str(email))
color = 'rgb(0, 0, 0)'  # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), femail, fill=color, font=font)

# For the Age
(x, y) = (50, 450)
age = int(input('Enter Your Age: '))
fage = str('Age: ' + str(age))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), fage, fill=color, font=font)

# For the DOB
(x, y) = (50, 550)
dob = input('Enter Your Date Of Birth: ')
fdob = str('Date of Birth: ' + str(dob))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), fdob, fill=color, font=font)

# For the Blood Group
(x, y) = (50, 650)
blood_group= input('Enter Your Blood Group: ')
flood_group = str('Blood Group: ' + str(blood_group))
color = 'rgb(255, 0, 0)'  # black color
draw.text((x, y), flood_group, fill=color, font=font)

# For the Mob No
(x, y) = (50, 750)
No = int(input('Enter Your Mobile Number: '))

fNo = str('Mobile Number: ' + str(No))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), fNo, fill=color, font=font)

# For the Address
(x, y) = (50, 850)
address = input('Enter Your Address: ')
faddress = str('Address: ' + str(address))
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), faddress, fill=color, font=font)

# save the edited image

image.save(str(name) + '.png')

QR = qrcode.make(str(company) +'\n' + str(name)+'\n' + str(idno) )  # this info. is added in QR code, also add other things
QR.save(str(idno) + '.bmp')


ID = Image.open(name + '.png')
QR = Image.open(str(idno) + '.bmp')  # 25x25
ID.paste(QR, (650, 350))
ID.save(name + '.png')

print(('\n\n\nYour ID Card Successfully created in a PNG file ' + name + '.png'))

###############################################################################################################################################################

image1 = Image.new('RGB', (1500, 1000), (255, 255, 255))
draw1 = ImageDraw.Draw(image1)

font1 = ImageFont.truetype('arial.ttf', size=45)


d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t  %I:%M:%S %p")
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(reg_format_date)
print(
    '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

##################################################
#Signature RSA + SHA256
###########################################################
print("This is the signature part :")
name=name.encode()
hash = SHA256.new(name)
signer = PKCS115_SigScheme(keyPair)
signature = signer.sign(hash)
print("Signature:", binascii.hexlify(signature))

(x, y) = (25, 150)
fname1 = str('Name : \n' + str(signature) )
color = 'rgb(0, 0, 0)'  # black color
draw1.text((x, y), fname1, fill=color, font=font)
##########################################################

email=email.encode()
hash1 = SHA256.new(email)
signer1 = PKCS115_SigScheme(keyPair)
signature1 = signer.sign(hash1)
print("Signature1:", binascii.hexlify(signature1))

(x, y) = (25, 250)
femail1 = str('email : \n' + str(signature1))
color = 'rgb(0, 0, 0)'  # black color
draw1.text((x, y), femail1, fill=color, font=font)
################################################################
#Empreinte md5
################################################################
print("This is the empreint part :")
md5Hash = hashlib.md5(name)
hash = md5Hash.hexdigest()
print(hash)
(x, y) = (25, 350)
femail1 = str('name : \n' + str(hash))
color = 'rgb(0, 0, 0)'  # black color
draw1.text((x, y), femail1, fill=color, font=font)
################################################################

md5Hash = hashlib.md5(email)
hash = md5Hash.hexdigest()
print(hash)
(x, y) = (25, 450)
femail1 = str('email : \n' + str(hash))
color = 'rgb(0, 0, 0)'  # black color
draw1.text((x, y), femail1, fill=color, font=font)

#########################################################################################################
image1.save(str(name) + '.png')

print(('\n\n\nYour ID Card crypted Successfully created in a PNG file ' + str(name) + '.png'))
#########################################################################################################
#Save:
#########################################################################################################
md5hash = hashlib.md5(Image.open(str(name) +'.png').tobytes())
print(md5hash.hexdigest())
f= open("carte.md5","w")
f.write(md5hash.hexdigest())
f.close()
########################################################################################################












