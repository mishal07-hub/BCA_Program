raw_data = """          naveen KUMAR
naveen.kumar@COMPANY.com
+91-98765-43210
"""
lines=raw_data.split("\n")
name,email,phone=lines[0],lines[1],lines[2]
name=name.strip().title()
first,last=name.split()[0],name.split()[1]
initials=first[0].upper()+last[0].upper()
email=email.strip().lower()
domain=email.split("@")[1]
phone="*********"+phone.strip()[-4:]
valid="@" in email and email.endswith(".com")
print("Name :",name)
print("Initials :",initials)
print("Email :",email)
print("Domain :",domain)
print("Phone :",phone)
print("Valid :",valid)



