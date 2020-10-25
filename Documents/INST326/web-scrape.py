import imaplib
import csv
mail = imaplib.IMAP4_SSL('imap.gmail.com') #incoming
mail.login("your-email-address", 'your-password') #login, input your own information
mail.list() # Out: list of "folders" aka labels in gmail.
mail.select("INBOX") # connect to inbox.

result, data = mail.search(None, "ALL") #search all emails 

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
with open ("your-csv-name.csv", "w+", newline='') as csv_file: #creates new csv, can customize name 
    csv_writer=csv.writer(csv_file)  
    for id in id_list:
        result, data = mail.fetch(id, "(BODY[HEADER.FIELDS (FROM)])") #fetches address 
        raw_email = (data[0][1]).decode() #decodes to readable format
        # (raw_email.decode())
        if '<' in raw_email: #puts only the email address with no added characters 
            sender_parts = raw_email.split('<')
            sender = sender_parts[-1].split('>')[0]
        else:
            sender_parts = raw_email.split(': ') 
            sender = (sender_parts[-1])[:-4]
        csv_writer.writerow([sender]) 
        #print("{} - {}".format(id.decode(), sender))
        

        
    # here's the body, which is raw text of the whole email
    # including headers and alternate payloads
    #latest_email_id = id_list[-1] # get the latest

