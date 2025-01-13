from random import uniform as rd
import matplotlib.pyplot as plt

class Atom():
    """
    Esta clase guarda la pocision de los atomos\n
    Pero en un futuro pudiera guardar propiedades atomicas
    """
    def __init__(self,xcord:float,ycord:float,zcord:float,atomtp="None"):
        self.x=xcord
        self.y=ycord
        self.z=zcord
        self.atomtp=atomtp
    
    def __str__(self) -> str:
        return "Esto es un atomo\nPara obtener su posicion usar\".pos\""
   
    def pos(self):
        return([self.x,self.y,self.z])
    def atomtype(self):
        return(self.atomtp)



class Layer():
    """
    Esto lo agregue dentro
    Esta clase Genera Dominios de Atomos\n
    Esta clase recibe como valores iniciales:\n
     {"Rango: epsilon -> Ubica los atomos en pocisiones aleatorias entre [zlayer-epsilon,zlayer+epsilon "}\n
     {"Condicion de distancia minima: r_cond"}\n
     {"zlayer: pocision del eje z en el que se va ubicar la capa"}

    Cuenta con las siguientes funciones:\n
    --'create_layer(n)' -> Genera en la capa una configuracion de n-atomos aleatoriamente
    
    --'show_layer()' -> Muestra la posicion de los atomos de la capa

    --'outfile(args,file) -> Muestra en {file} las posiciones de atomos de {args}'

    --graph(args) -> Muestra en una grafica las posiciones de los atomos dentro de {args}

    --'entry_layer(Layer, str(PATH_datos) )' Lee la configuracion atomica desde un documento
    el documento debe tener el siguiente formato:\n
    x0 y0 z0
    x1 y1 z1
    x2 y2 z2
    ...
    xn yn zn
    
    --'help() -> Muestra las funcionalidades de eesta clase'
    """
    def __init__(self,epsilon=0 , r_cond=0,zlayer=0, xcond0=0,xcon1=1,ycond0=0,ycon1=1):
        self.x0=xcond0
        self.x1=xcon1
        self.y0=ycond0
        self.y1=ycon1
        
        self.z_min=zlayer-epsilon
        self.z_max=zlayer+epsilon
        self.rcond=r_cond
        self.zlayer=zlayer
        self.dominio=[]
        pass

    def create_layer(self,n,name:str):
        i=0
        while(i<n):
            x=rd(self.x0,self.x1)
            x=round(x,7)
            y=rd(self.y0,self.y1)
            y=round(y,7)
            z=rd(self.z_min,self.z_max) #Esto es debido a la logica de que el las capas tendran un zlayer que indica donde se encuentra la capa
            z=round(z,7)
            lugar=True
            
            
            for j in range(len(self.dominio)):
                pos_1=self.dominio[j].pos()#Esta posicion se refiere al j-esimo atomo de la capa
                r_p=((pos_1[0]-x)**2+(pos_1[1]-y)**2+(pos_1[2]-z)**2)**1/2
                if( z<self.z_min or z>self.z_max or r_p<self.rcond):
                    lugar=False
                    break
            if(lugar):
                self.dominio.append(Atom(x,y,z,name))
                self.dominio.append(Atom(x,y,-z,name))             #quitar esto si no lo quieres simetrico   
                i=i+1

    def show_layer(self):
        if(len(self.dominio)==0):
            print("Tu capa no tiene ningun atomo\nUse la funcion 'create_layer' o 'entry_layer'")
        else:
            for i in self.dominio:
                print(i.pos())
    def help():
        print(Layer.__doc__)

    

def entry_layer(wlayer:Layer,file:str):
    f=open(file,"r")
    a=f.read()
    a=a.splitlines()
    b=a
    zlayer=0
    cont=0
    for i in b:
        if(i[0]==''):
            cont+=1
        i=i.split(sep='\t')
        print(i)
        x=float(i[1])
        y=float(i[2])
        z=float(i[3])
        atomtp=i[4]
        temp=Atom(x,y,z,atomtp=atomtp)
        zlayer=zlayer+float(i[2+cont])
        wlayer.dominio.append(temp)
        cont=0
    wlayer.zlayer=zlayer/len(b)

def graph(args):

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for i in args:
        xset=[]
        yset=[]
        zset=[]
        for j in i.dominio:
            tem_pos=j.pos()
            xset.append(tem_pos[0])
            yset.append(tem_pos[1])
            zset.append(tem_pos[2])
        ax.scatter(xset, yset, zset, marker='o',)
    
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

def outfile(args,file):
    f=open(file,"w+")
    for i in args:
        for j in i.dominio:
            tem_pos=j.pos()
            tipo=j.atomtype()
            f.writelines("\n\t{}\t{}\t{}\t{}".format((tem_pos[0]),(tem_pos[1]),(tem_pos[2]),tipo))
    f.close()
    




class Solid():
    
    pass






if(__name__=="__main__"):
    print("Created by int-64 \nMailto carlosr301101@gmail.com")

