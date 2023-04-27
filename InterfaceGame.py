from pygame import *
import sys
from combo_box import ComboBox
from single_linked_list import SingleLinkedList
class Interface:

        #Colores
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    GREY= (200,200,200)
    RED = (255,0,0)
    BLUE = (0,0,255)
    size = (800,580)

    def __init__(self):
        init()
        self.myFont = font.SysFont("Comic Sans Ms",20)
        self.myFontTextCombo= font.SysFont("Comic Sans Ms", 16)
        self.myFontSmall = font.SysFont("Comic Sans Ms",13)
        self.myFontSuperSmall = font.SysFont("Comic Sans Ms",10)
        self.valor=5
        self.control=True

        self.flagEmpy=False

        self.widthPokemon= 60
        self.heigthPokemon=60
        #Posiciones solo para los pokemones
        self.balbausur= Rect(300,180,self.widthPokemon,self.heigthPokemon)
        self.charmander= Rect(370,180,self.widthPokemon,self.heigthPokemon)
        self.squirtle= Rect(440,180,self.widthPokemon,self.heigthPokemon)

        self.otherBalbausur=Rect(315, 240, self.widthPokemon,self.heigthPokemon)
        self.otherCharmander=Rect(380,240, self.widthPokemon, self.heigthPokemon)
        self.otherSquirtle=Rect(455, 240, self.widthPokemon, self.heigthPokemon)
        self.deleteFlag=False
        self.rectFooter=Rect(0,520, 800, 60)
        self.roserade = Rect(195,170,self.widthPokemon,self.heigthPokemon)
        self.charjabug= Rect(265,170,self.widthPokemon,self.heigthPokemon)
        self.cloyster = Rect(335,170,self.widthPokemon,self.heigthPokemon)
        self.furfrou = Rect(405,170,self.widthPokemon,self.heigthPokemon)
        self.quilladin = Rect(475,170,self.widthPokemon,self.heigthPokemon)
        self.bombirdier= Rect(545,170,self.widthPokemon,self.heigthPokemon)
        self.combo_rect= Rect(220,110,200,50)
        self.comboIndice_rect = Rect(530,110,100,50)
        self.screen = display.set_mode(self.size)
        self.instSll = SingleLinkedList()
        self.controlNoPress= True
        self.rectGithub=Rect(420,535,40,40)

        self.alert = Rect(200,160,400, 100)
        self.btnAlert = Rect(370,220,70,25)
        self.rectUAM = Rect(670,520,40,40)
        #Tamaño de lista de pokemones
        self.listPokemons= Rect(60,400,700,90)
        self.pokeName=''
        #Cargando imagenes pokemones iniciales
        self.charmanderImg= image.load('img/charmander.png')
        self.charmanderImg = transform.scale(self.charmanderImg,(self.charmander.width,self.charmander.height))
        self.balbausurImg= image.load('img/balbasaur.png')
        self.balbausurImg = transform.scale(self.balbausurImg,(self.balbausur.width,self.balbausur.height))
        self.squirtleImg = image.load('img/squirtle.png')
        self.squirtleImg= transform.scale(self.squirtleImg,(self.squirtle.width,self.squirtle.height))
        self.roseradeImg= image.load('img/roserade.png')
        self.roseradeImg= transform.scale(self.roseradeImg,(self.roserade.width,self.roserade.height))
        self.charjabugImg= image.load('img/charjabug.png')
        self.charjabugImg= transform.scale(self.charjabugImg,(self.charjabug.width,self.charjabug.height))
        self.cloysterImg = image.load('img/cloyster.png')
        self.cloysterImg = transform.scale(self.cloysterImg,(self.cloyster.width,self.cloyster.height))
        self.quilladinImg = image.load('img/quilladin.png')
        self.quilladinImg = transform.scale(self.quilladinImg,(self.quilladin.width,self.quilladin.height))
        self.bombirdierImg= image.load('img/bombirdier.png')
        self.bombirdierImg = transform.scale(self.bombirdierImg,(self.bombirdier.width,self.bombirdier.height))
        self.furfrouImg= image.load('img/furfrou.png')
        self.furfrouImg = transform.scale(self.furfrouImg,(self.furfrou.width,self.furfrou.height))
        self.background = image.load('img/pokemon3.jpg')
        self.background = transform.scale(self.background,(200,200))
        self.github = image.load('img/github.jpg')
        self.github= transform.scale(self.github,(40,40))
        self.UAMImg = image.load('img/UAM.jpg')
        self.UAMImg = transform.scale(self.UAMImg,(120,60))



        self.pokedex= [
            ("Balbausur",self.balbausurImg),
            ("Charmander",self.charmanderImg),
            ("Squirtle",self.squirtleImg),
            ("Bombardier", self.bombirdierImg),
            ("Charjabug", self.charjabugImg),
            ("Cloyster", self.cloysterImg),
            ("Furfrou", self.furfrouImg),
            ("Quilladin", self.quilladinImg),
            ("Roserade", self.roseradeImg)]
        self.listPokemon=[]

        self.operaciones={
            1:self.instSll.create_node_sll_unshift,
            2:self.instSll.crear_node_sll_ends,
            3:self.instSll.shift_node_sll,
            4:self.instSll.delete_node_sll_pop,
            5:self.instSll.reverse,
            6:self.instSll.delete_list,
            7:self.instSll.remove_node,
            8:self.instSll.add_node,
            9:self.instSll.update_node_value,
            10:""" Comprobar si la lista simplemente esta vacio si el usuario desea eliminar """
        }


        #botones
        self.btnAceptar= Rect(350,330,70,25)
        self.opcion=0
        self.touchUser = False
        self.indices =[]
        #Combobox
        self.screen.fill(self.GREY)
        self.combo = ComboBox(self.screen,["Agregar al principio","Agregar al final","Eliminar primero", "Eliminar ultimo","Invertir","Eliminar todos","Eliminar por posicion","Agregar en una posicion", "Actualizar pokemon"],self.combo_rect,self.WHITE,"Arial",16,5,self.BLACK,self.BLACK,30,"Seleccione")
        self.comboIndice = ComboBox(self.screen,self.indices,self.comboIndice_rect,self.WHITE,"Arial",16,5,self.BLACK,self.BLACK,30,"Seleccione")
        self.indice=0
        #Hover
        self.hoverPositionX=0
        self.hovePositionY=0
        self.hoverWidth=0
        self.hoverHeigth=0


    def init_screen(self):
        #self.draw_other_pokemons()()
        #self.draw_buttons()
        while True:
            for e in event.get():
                if e.type == QUIT:
                    sys.exit()
            draw.rect(self.screen,(255,255,255),(0,0,800,520))
                    #Fondo
            self.draw_list_pokemons()
            self.imprimir_pokemones()
            if(not self.touchUser):
                self.screen.blit(self.background,(320,-10))
                self.draw_begin_pokemons()
                self.draw_string()
                self.add_begin_pokemon_end()
                
            else:
                self.screen.blit(self.background,(285,-10))
                if not self.combo.combo_open:
                    self.press_aceptar() 
                    self.draw_buttons() 
                self.draw_string()
                self.draw_other_pokemons()
                self.add_other_pokemons() 
                self.combo.draw()
                self.comboIndice.draw()
                self.opcion= self.combo.getIndex()  
                self.indice = self.comboIndice.getIndex() 
            self.draw_footer()            
            display.flip()

        
    #Dibujar las imagenes de los pokemones iniciales
    def render_begin_pokemons(self):
        #RDibujando imagenes, pasando la imagen, y la posicion en la que se colocara
        self.screen.blit(self.charmanderImg,(self.charmander.x,self.charmander.y))
        self.screen.blit(self.balbausurImg,(self.balbausur.x,self.balbausur.y))
        self.screen.blit(self.squirtleImg,(self.squirtle.x, self.squirtle.y))

    #Dibujar las posiciones en las que estaran los pokemones iniciales
    def draw_begin_pokemons(self):
        draw.rect(self.screen,self.WHITE,self.balbausur)
        draw.rect(self.screen,self.WHITE,self.charmander)
        draw.rect(self.screen,self.WHITE, self.squirtle)
        self.render_begin_pokemons()
    
    #Dibujar las posiciones en las que estaran los otros pokemones a elegir
    def draw_other_pokemons(self):
        draw.rect(self.screen,self.WHITE,self.roserade)
        draw.rect(self.screen,self.WHITE,self.charjabug)
        draw.rect(self.screen,self.WHITE,self.bombirdier)
        draw.rect(self.screen,self.WHITE,self.cloyster)
        draw.rect(self.screen,self.WHITE,self.quilladin)
        draw.rect(self.screen,self.WHITE,self.furfrou)
        draw.rect(self.screen,self.WHITE,self.otherBalbausur)
        draw.rect(self.screen,self.WHITE,self.otherCharmander)
        draw.rect(self.screen,self.WHITE,self.otherSquirtle)

        self.render_other_pokemons()


    def render_other_pokemons(self):
        self.screen.blit(self.roseradeImg,(self.roserade.x,self.roserade.y))
        self.screen.blit(self.charjabugImg,(self.charjabug.x,self.charjabug.y))
        self.screen.blit(self.cloysterImg,(self.cloyster.x,self.cloyster.y))
        self.screen.blit(self.bombirdierImg,(self.bombirdier.x,self.bombirdier.y))
        self.screen.blit(self.quilladinImg,(self.quilladin.x,self.quilladin.y))
        self.screen.blit(self.furfrouImg,(self.furfrou.x,self.furfrou.y))
        self.screen.blit(self.charmanderImg,(self.otherCharmander.x,self.otherCharmander.y))
        self.screen.blit(self.squirtleImg,(self.otherSquirtle.x,self.otherSquirtle.y))
        self.screen.blit(self.balbausurImg,(self.otherBalbausur.x,self.otherBalbausur.y))


    #Dibujar texto para el menu
    def draw_string(self): 
        if(not self.touchUser):
            textoPrimeraSeleccion= self.myFont.render(" ----  Seleccione uno para iniciar   ---- ", True,(0,0,0))
            self.screen.blit(textoPrimeraSeleccion,(250,120))
        else:
                textCombo = self.myFontTextCombo.render(" Metodos", True,(0,0,0) )
                self.screen.blit(textCombo,(140,123))
                textComboIndice = self.myFontTextCombo.render(" Indice", True,(0,0,0) )
                self.screen.blit(textComboIndice,(450,123))
        textoLista= self.myFont.render(" ----  Lista actual   ---- ", True,(0,0,0))
        self.screen.blit(textoLista,(70, 370))

    def draw_list_pokemons(self):  
        draw.rect(self.screen,self.GREY,self.listPokemons)



    def draw_buttons(self):
        #Boton aceptar
        if not self.combo.combo_open:
            draw.rect(self.screen,(70,189,34),self.btnAceptar,0)
            texto= self.myFontSmall.render("Aceptar", True,(0,0,0))
            self.screen.blit(texto,(350+(self.btnAceptar.width-texto.get_width())/2,330+(self.btnAceptar.height-texto.get_height())/2))

    def add_begin_pokemon_end(self):
        if(self.balbausur.collidepoint(mouse.get_pos())) and mouse.get_pressed()[0]:
                    self.touchUser=True
                    self.instSll.create_node_sll_unshift(self.pokedex[0][0])
                    self.indices.append("1")
        elif self.charmander.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
                self.touchUser=True
                self.indices.append("1")
                self.instSll.create_node_sll_unshift(self.pokedex[1][0])
        elif self.squirtle.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
                self.instSll.create_node_sll_unshift(self.pokedex[2][0])
                self.touchUser=True
                self.indices.append("1")

    def add_other_pokemons(self):
        if (self.opcion>0 and self.opcion<=2) or self.opcion==8 or self.opcion==9:
            if not self.combo.combo_open:
                if(self.otherBalbausur.collidepoint(mouse.get_pos())) and mouse.get_pressed()[0]:
                    self.pokeName= self.pokedex[0][0]
                    self.give_valors_hover(self.otherBalbausur.x,self.otherBalbausur.y,self.widthPokemon,self.heigthPokemon)
                    self.deleteFlag=True
                elif self.otherCharmander.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
                    self.pokeName= self.pokedex[1][0]
                    self.give_valors_hover(self.otherCharmander.x,self.otherCharmander.y,self.widthPokemon,self.heigthPokemon)
                    self.deleteFlag=True

                elif self.otherSquirtle.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
                    self.pokeName= self.pokedex[2][0]
                    self.give_valors_hover(self.otherSquirtle.x,self.otherSquirtle.y,self.widthPokemon,self.heigthPokemon)
                    self.deleteFlag=True

                elif self.bombirdier.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
                    self.pokeName= self.pokedex[3][0]
                    self.give_valors_hover(self.bombirdier.x,self.bombirdier.y,self.widthPokemon,self.heigthPokemon)
                    self.deleteFlag=True

                elif self.charjabug.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
                    self.pokeName= self.pokedex[4][0]
                    self.give_valors_hover(self.charjabug.x,self.charjabug.y,self.widthPokemon,self.heigthPokemon)
                    self.deleteFlag=True

                elif self.cloyster.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
                    self.pokeName= self.pokedex[5][0]
                    self.give_valors_hover(self.cloyster.x,self.cloyster.y,self.widthPokemon,self.heigthPokemon)
                    self.deleteFlag=True

                elif self.furfrou.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
                    self.pokeName= self.pokedex[6][0]
                    self.give_valors_hover(self.furfrou.x,self.furfrou.y,self.widthPokemon,self.heigthPokemon)
                    self.deleteFlag=True

                elif self.quilladin.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
                    self.pokeName= self.pokedex[7][0]
                    self.give_valors_hover(self.quilladin.x,self.quilladin.y,self.widthPokemon,self.heigthPokemon)
                    self.deleteFlag=True

                elif self.roserade.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
                    self.pokeName= self.pokedex[8][0]
                    self.give_valors_hover(self.roserade.x,self.roserade.y,self.widthPokemon,self.heigthPokemon)
                    self.deleteFlag=True
                self.draw_hover(self.hoverPositionX,self.hovePositionY,self.hoverWidth,self.hoverHeigth)

        if self.opcion == 5 and self.deleteFlag:
            self.operaciones[self.opcion]()
            self.deleteFlag=False

        if (self.opcion>=3 and self.opcion<5) or self.opcion==6:
            
            #Eliminar
            if self.deleteFlag:
                if self.instSll.length != 0:
                    self.operaciones[self.opcion]()
                    if self.opcion == 6:
                        self.indices.clear()
                    else:
                        self.indices.pop()
                    self.deleteFlag=False
                    self.flagEmpy=True
                    self.comboIndice = ComboBox(self.screen,self.indices,self.comboIndice_rect,self.WHITE,"Arial",16,5,self.BLACK,self.BLACK,30,"Seleccione")
                else :
                    self.flagEmpy=True
                    self.is_empy_nodes()

    def seleccionar_pokemon(self):
        #Eliminar en una posicion especifica
        if self.indice>0 and self.opcion == 7:
            self.operaciones[self.opcion](self.indice)
            self.indices.pop()
        
        #Agregar en una posicion especifica
        if self.indice >0 and self.opcion==8:
            self.operaciones[self.opcion](self.indice,self.pokeName)
            self.indices.append(str(self.instSll.length))

        #Actualizar pokemon
        if self.indice >0 and self.opcion==9:
            self.operaciones[self.opcion](self.indice,self.pokeName)

        #Agregar pokemones
        if self.opcion> 0 and self.opcion<3:
            for name in self.pokedex:
                if self.pokeName == name[0] and self.deleteFlag:
                    self.operaciones[self.opcion](name[0])
                    self.indices.append(str(self.instSll.length))
        
        #Refresacando el combo de los indices
        self.comboIndice = ComboBox(self.screen,self.indices,self.comboIndice_rect,self.WHITE,"Arial",16,5,self.BLACK,self.BLACK,30,"Seleccione")
    
    def imprimir_pokemones(self):
            self.valor=5
            for poke in range(1,self.instSll.length+1):
                if self.instSll.get_node_value(poke) == 'Balbausur':
                    self.screen.blit(self.pokedex[0][1],(self.listPokemons.x+self.valor,245+(self.listPokemons.y- self.heigthPokemon)/2))
                    self.valor+=90
                if self.instSll.get_node_value(poke) == 'Charmander':
                    self.screen.blit(self.pokedex[1][1],(self.listPokemons.x+self.valor,245+(self.listPokemons.y- self.heigthPokemon)/2))
                    self.valor+=90
                if self.instSll.get_node_value(poke) == 'Squirtle':
                    self.screen.blit(self.pokedex[2][1],(self.listPokemons.x+self.valor,245+(self.listPokemons.y- self.heigthPokemon)/2))
                    self.valor+=90
                if self.instSll.get_node_value(poke) == 'Bombardier':
                    self.screen.blit(self.pokedex[3][1],(self.listPokemons.x+self.valor,245+(self.listPokemons.y - self.heigthPokemon)/2))
                    self.valor+=90
                if self.instSll.get_node_value(poke)=='Charjabug':
                    self.screen.blit(self.pokedex[4][1],(self.listPokemons.x + self.valor, 245+(self.listPokemons.y-self.heigthPokemon)/2))
                    self.valor+=90
                if self.instSll.get_node_value(poke) == 'Cloyster':
                    self.screen.blit(self.pokedex[5][1], (self.listPokemons.x+self.valor, 245+(self.listPokemons.y-self.heigthPokemon)/2))
                    self.valor+=90
                if self.instSll.get_node_value(poke)== 'Furfrou':
                    self.screen.blit(self.pokedex[6][1], (self.listPokemons.x+ self.valor, 245+(self.listPokemons.y- self.heigthPokemon)/2))
                    self.valor+=90
                if self.instSll.get_node_value(poke) == 'Quilladin':
                    self.screen.blit(self.pokedex[7][1], (self.listPokemons.x + self.valor, 245+(self.listPokemons.y - self.heigthPokemon)/2))
                    self.valor+=90
                if self.instSll.get_node_value(poke) == 'Roserade':
                    self.screen.blit(self.pokedex[8][1],(self.listPokemons.x+self.valor,245+(self.listPokemons.y-self.heigthPokemon)/2))
                    self.valor+=90
                
    def press_aceptar(self):
        event.wait()
        if(self.btnAceptar.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]):
            if((self.opcion>0 and self.opcion<3) or self.opcion>=7 and self.opcion <=9):
                self.seleccionar_pokemon()
                self.deleteFlag=False
            else: self.deleteFlag=True
            self.give_valors_hover(0,0,0,0)
            self.instSll.show_list()

    def draw_hover(self, positionX, positionY, width, heigth):
        if not self.combo.combo_open:
            self.rect_hover= Rect(positionX,positionY, width, heigth)
            draw.rect(self.screen,self.RED,self.rect_hover,2)
    
    def give_valors_hover(self,x,y,width,heigth):
        self.hoverPositionX=x-5
        self.hovePositionY=y-5
        self.hoverWidth=width+10
        self.hoverHeigth=heigth+10
        
    def is_empy_nodes(self):
        if self.flagEmpy:
            draw.rect(self.screen,self.BLACK,self.alert,0,8)
            draw.rect(self.screen,self.GREEN,self.btnAlert,0)
            textoAlert= self.myFont.render(" ----  No hay pokemones para eliminar   ---- ", True,self.WHITE)
            textoBtnAlert= self.myFont.render(" Ok", True,self.BLACK)
            self.screen.blit(textoBtnAlert,(370+(self.btnAlert.width-textoBtnAlert.get_width())/2,220+(self.btnAlert.height-textoBtnAlert.get_height())/2))
            self.screen.blit(textoAlert,(200+(self.alert.width-textoAlert.get_width())/2,140+(self.alert.height-textoAlert.get_height())/2))
            if self.btnAlert.collidepoint(mouse.get_pos()) and mouse.get_pressed()[0]:
                self.flagEmpy=False

    def draw_footer(self):
        draw.rect(self.screen, self.BLACK,self.rectFooter,0)
        draw.rect(self.screen,self.BLACK,self.rectGithub)
        draw.rect(self.screen,self.BLACK,self.rectUAM)
        self.screen.blit(self.UAMImg,(self.rectUAM.x, self.rectUAM.y))
        self.screen.blit(self.github,(self.rectGithub.x,self.rectGithub.y-5))
        textoGithub= self.myFontSmall.render("Desarrollado por Andres Perez", True, self.WHITE)
        textoClass= self.myFontSuperSmall.render("Estructura de datos", True, self.WHITE)
        self.screen.blit(textoGithub,(self.rectFooter.x+210, self.rectFooter.y+16))
        self.screen.blit(textoClass,(self.rectFooter.x+260, self.rectFooter.y+31))
