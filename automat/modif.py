
if(__name__=="__main__"):

    f=open('tungsten.bcc.fdf1',"+r")
    data=open('salida.out',"+r")
   #print (f.read())
    a=f.read()
    xxx=a.index("XXX")
    f.close()
   #a[xxx]=data.read()
    mod=open('tungsten.bcc.fdf',"+w")
  #mod.writelines()
   #mod.writelines()
   #print (a)
    a=a.replace("XXX",data.read())
    data.close()
   #print(a)
    mod.write(a)
    mod.close()
