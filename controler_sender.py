from sender import send_email

def deliver_email(subject, emailBody, to):
 
  at_sign = "@" in to 
  email_leng = len(to) >= 6

  if(at_sign != False 
     and email_leng == True):
   send_email(subject, emailBody, to)

  else:
    return False

 


        
   
        
