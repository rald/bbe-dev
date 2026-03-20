class Cite:
    def __init__(self,bname,scnum,ecnum,svnum,evnum):
        self.bname=bname
        self.scnum=scnum
        self.ecnum=ecnum
        self.svnum=svnum
        self.evnum=evnum
    def __repr__(self):
        return f"Cite {{ bname: \"{self.bname}\", scnum: {self.scnum}, ecnum: {self.ecnum}, svnum: {self.svnum}, evnum: {self.evnum} }}"
