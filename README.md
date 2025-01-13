###
This project use python as a tool for SIESTA .fdf files, aiming to create, modify and graph atomic structures.
###
##
Uses a python package "AtomClass" wichone allow create some kind of atomic structure like , Solid and Layers, with few paramaters like interatomic distance and randomize those positions (x,y,z)
##
Different classes
  ---------
      class Atom():
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
  
  ---------
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
        def __init__(self,epsilon=0 , r_cond=0,zlayer=0.0):
            self.z_min=zlayer-epsilon
            self.z_max=zlayer+epsilon
            self.rcond=r_cond
            self.zlayer=zlayer
            self.dominio=[]
            pass
    
        def create_layer(self,n,name:str):
            i=0
            while(i<n):
                x=rd(0,1)
                y=rd(0,1)
                z=rd(self.z_min,self.z_max) #Esto es debido a la logica de que el las capas tendran un zlayer que indica donde se encuentra la capa
                lugar=True
                
                
                for j in range(len(self.dominio)):
                    pos_1=self.dominio[j].pos()#Esta posicion se refiere al j-esimo atomo de la capa
                    r_p=((pos_1[0]-x)**2+(pos_1[1]-y)**2+(pos_1[2]-z)**2)**1/2
                    if( z<self.z_min or z>self.z_max or r_p<self.rcond):
                        lugar=False
                        break
                if(lugar):
                    self.dominio.append(Atom(x,y,z,name))
                    i=i+1
    
        def show_layer(self):
            if(len(self.dominio)==0):
                print("Tu capa no tiene ningun atomo\nUse la funcion 'create_layer' o 'entry_layer'")
            else:
                for i in self.dominio:
                    print(i.pos())
        def help():
            print(Layer.__doc__)
  -------
