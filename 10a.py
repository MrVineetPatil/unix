class city:
    def __init__(self,name,places=[]):
        self.cn=name
        self.pl=places

    def add_place(self,l):
        self.pl.append(l)
    def remove_place(self,l):
        self.pl.remove(l)
    def places(self):
        print("Places to visit in",self.cn,':',end='')
        for i in self.pl:
            print(i,'\t\t',sep='',end='')
        print()
b=city('Bengaluru',['Yeshwantpur','lalbagh'])
print("A city 'b' is initialized named bengaluru")
b.places()
b.add_place('Wonderla')
b.places()
b.remove_place('Yeshwantpur')
b.places()