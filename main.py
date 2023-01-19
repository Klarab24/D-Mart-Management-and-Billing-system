import logo, os
#create a class to setup the billing system
class bill:
    def __init__(self, Parent_Company,Company_Name, CIN, GSTIN, FSSAI, Location, Address, Phone_No):
        self.Parent_Company = Parent_Company
        self.CIN = CIN
        self.GSTIN = GSTIN
        self.FSSAI = FSSAI
        self.Location = Location
        self.Company_Name = Company_Name
        self.Store_Name = Company_Name+" "+Location
        self.Address = Address
        self.Phone_No = Phone_No
        self.Date = os.popen("date").read()
        self.Time = os.popen("date +%T").read()

    def print_bill(self):
        print("-"*50)
        print(logo.logo().center(50))
        print("-"*50)
        print(self.Parent_Company.center(50))
        print("-"*50)
        print("CIN: ", self.CIN)
        print("GSTIN: ", self.GSTIN)
        print("FSSAI: ", self.FSSAI)
        print("-"*50)
        print(self.Store_Name.center(50))
        print("-"*50)
        #print the address of the store and wrap it to 50 characters
        print(self.Address[:48].center(50))
        print(self.Address[48:].center(50))
        print("Phone"+self.Phone_No.center(45))
        print("-"*50)
        


#call the class
bill1 = bill("IMV INNOVATIONS PRIVATE LIMITED", "D-MART", "U74999MH2017PTC301","27AABCI0001A1Z5", "10018001000009", "MUMBAI", "D-MART, 1st Floor, 7th Road, Khar West, Mumbai, Maharashtra 400052", "022 26000000")
bill1.print_bill()
