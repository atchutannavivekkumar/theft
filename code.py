# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L1L08vqqywGoXJyrpvCVYxygV_p_gMoT
"""

pip install twilio

import os
from twilio.rest import Client
import random
class PaymentProcess:    
  def NewRegister(self,MobileNum,DebitCardNum,Cvv) :
    self.Cardcvv = Cvv
    self.mn = MobileNum
    self.dcn = DebitCardNum
  def MakePayment(self) :
    cvv = int(input("ENTER THE CVV NUMBER "))
    if self.Cardcvv == cvv :
      account_sid = os.environ['TWILIO_ACCOUNT_SID']
      auth_token = os.environ['TWILIO_AUTH_TOKEN']
      client = Client(account_sid, auth_token)
      otp = random.randint(1111,9999)
      message = client.messages \
                .create(
                     body= otp ,
                     from_='+12316851234',
                     to= self.mn
                 )
      print(message.sid)
      sentotp = int(input("enter the OTP got on your mobile number"))
      if sentotp == otp :
        print("Your payment sucessfull !! Continue shopping")
      else :
        print("Error in payment")
    else :
      print("Error in payment")

newnumber = PaymentProcess()
newnumber.NewRegister('',  , )
newnumber.MakePayment()