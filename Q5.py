import os

def create_dir(name,address):
    address = os.path.join(address,name)
    if os.path.exists(address) is False:
        os.mkdir(address)

def create_file(name,address):
    address = os.path.join(address,name)
    print(address)
    if os.path.exists(address) is False:
           with open(address,'a') as f:
               pass

def delete(name,address):
    address = os.path.join(address,name)
    print(address)
    if os.path.exists(address) is True:
        os.remove(address)

def find(name,address):
    list=[]
    for subdir , dirs , files in os.walk(address):
        for file in files:
            if file == name :
                list.append((os.path.join(subdir,file).split(address))[1])
    return list


Ctrl=''
print('For Quiting Program Press Tab and then Enter.')
while Ctrl is not '\t':
    Ctrl=input()
    if Ctrl.startswith('create_dir'):
        s1=Ctrl.split(',')
        name = s1[0][11:]
        address = s1[1][:-1]
        create_dir(name,address)
    if Ctrl.startswith('create_file'):
        s1=Ctrl.split(',')
        name = s1[0][12:]
        address = s1[1][:-1]
        create_file(name,address)
    if Ctrl.startswith('delete'):
        s1=Ctrl.split(',')
        name = s1[0][7:]
        address = s1[1][:-1]
        delete(name,address)
    if Ctrl.startswith('find'):
        s1=Ctrl.split(',')
        name = s1[0][5:]
        address = s1[1][:-1]
        print(find(name,address))
