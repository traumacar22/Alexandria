


class Entry:
    def __init__(self, site: str, pword: str, email: str = None, uname: str = None):
        self.site = site
        self.pword = pword
        self.email = email
        self.uname = uname
        
    def to_dict(self):
        data: dict = {'Website': self.site, 'Password': self.pword, 'Email': self.email, 'Username': self.uname}
        return data
    
    def from_dict(result: dict):
        #print commands are for troubleshooting later and should be removed when satisfied
        print(f"Website: {result['Website']}")
        print(f"Password: {result['Password']}")
        print(f"Email: {result['Email']}")
        print(f"Username: {result['Username']}")
        
        return Entry(site=result['Website'], pword=result['Password'], email=result['Email'], uname=result['Username'])