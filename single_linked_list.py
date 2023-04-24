class SingleLinkedList:
    class Node:
        def __init__(self,value):
            self.value = value 
            self.next = None
    '''Por fuera de la clase nodo'''
    def __init__(self):
        self.head = None
        self.tail = None
        self.length= 0
    def show_list(self):
        # 1. Declarar un array (lista) vacia que contendra los valores de los nodos de la lista simplemente enlazada
        # varray_with_nodes_value = list()  --> Otra forma de inicializar una lista
        array_with_nodes_value = list()
        current_node = self.head
        # Mientras que el nodo actual que estoy visitando sea diferente de None
        while(current_node != None):
            #Añandiendo al final de la lista el valor extraido del nodo
            array_with_nodes_value.append(current_node.value)
            #Incrementamos en 1 el valor del nodo visitado
            # current_node+1 --> Se usa solo para cuando usamos indices, trabajando con nodos no sirve

            #Pasamos del nodo actual al siguiente nodo -> Forma correcta para pasar de nodo
            current_node = current_node.next
        print(f'Los valores de los nodos de la SLL son : \n {array_with_nodes_value}')
        
    def crear_node_sll_ends(self,value):
        # Creamos una varaible que va a contener la estructura de un nodo
        new_node = self.Node(value)
        #Validar si la Single Linked List tiene nodos o no
        # Forma 1 una validar si hay nodos
        """if self.length ==0:
            print("La lista simplemente enlazada no tiene nodos")
        else:
            print("La lista simplemente enlazada si tiene nodos") """
        
        # Forma 2 una validar si hay nodos
        # self.tail es redundante ya que si la cola (head) es null, la cola (tail) tambien sera null y significa que no hay nodos
        if self.head == None and self.tail == None:
            #Al nuevo nodo se convierte en la cabeza y cola de la lista
            self.head = new_node
            self.tail = new_node
            print("La lista simplemente enlazada no tiene nodos")
        else:
            #Si ingresa en esta condicion, es porque ya existe almenos un nodo
            # 1. Debemos relacionar al nuevo nodo con la cola de la lista
            # 2. Convertir al nuevo nodo en la cola de la lista

            self.tail.next = new_node
            self.tail = new_node
            print("La lista simplemente enlazada si tiene nodos")
        #Incrementamos el tmamaño de la lista
        self.length+=1

    def create_node_sll_unshift(self,value):
        new_node = self.Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            #!. Debemos relacionar el nuevo nodo con la cabeza de la lista
            #2. Convertir al nuevo nodo en la cabeza de la lista
            new_node.next = self.head
            self.head = new_node
        # Incrementamos en 1 el tamaño de la lista
        self.length +=1

        
    def delete_node_sll_pop(self):
        #1.Validar si la lista esta vacia
        #2. Validar si la lista tiene un unico nodo
        #3. Si tiene mas de un nodo, eliminar la cola de la lista
        #4. Asignar al nodo anterior, como la nueva cola
        if self.length ==0:
            print(" >> No hay nodos para eliminar << ")
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length-=1
        else:
            #Recorrer la lista para identificar la cola
            current_node = self.head
            # Validar mediante el enlace del nodo actual que haya por visitar (Diferente a None)
            # Variables auxilliar donde se guarda la cola 
            new_tail = current_node
            while current_node.next != None:
                #3. Convertirmos en la coal de la lista el nodo que actualmente estamos visitando
                new_tail = current_node
                #4. Pasamos al siguiente nodo antes de salir del while
                current_node = current_node.next
            #Actualizamos la cola de la lista
            self.tail = new_tail
            self.tail.next = None
            #6. Restamos en 1 el tamaño de la lista
            self.length-=1


    def shift_node_sll(self):
        if self.length == 0:
            print('>> Lista vacía no hay nodos por eliminar <<')
        elif self.length == 1:

            self.head = None
            self.tail = None
            self.length -= 1
        else:
            remove_node = self.head
            print(f'Valor del nodo a eliminar es: {remove_node.value}')
            self.head = remove_node.next
            self.length -=1

    def get_node(self, index):
        if index < 1 or index > self.length:
            return None
        elif index == 1:
            return self.head
        elif index == self.length:
            return self.tail
        else:
            current_node = self.head
            node_counter=1
            while(index!=node_counter):
                current_node = current_node.next
                node_counter+=1
            return current_node
        
    def get_node_value(self, index):
        if index < 1 or index > self.length:
            return -1
        elif index == 1:
            return self.head.value
        elif index == self.length:
            return self.tail.value
        else:
            current_node = self.head
            node_counter=1
            while(index!=node_counter):
                current_node = current_node.next
                node_counter+=1
            return current_node.value
        
    def update_node_value(self,index,new_value):
        search_node = self.get_node(index)
        if search_node !=None:
            search_node.value = new_value
            print(f'Actualizando el valor del nodo ... \n {search_node.value} por {new_value}')
        else:
            print("No se encontro el nodo")

    def reverse(self):
        if self.length > 1:
            aux_head = self.tail
            aux_tail = self.head
            if self.length == 2:
                self.head = aux_head
                self.head.next = aux_tail
                self.tail = aux_tail
                self.tail.next = None
                return
            
            current_node = self.tail
            for i in range (1, self.length - 1):
                node = self.get_node(self.length - i)
                current_node.next = node
                current_node = node
            node.next = aux_tail
            self.head = aux_head
            self.tail = aux_tail
            self.tail.next = None

    def delete_list(self):
        if self.head != None:
            self.head.next = None
            self.head = None
            self.tail = None
            self.length = 0

    def remove_node(self,index):
        if index == 1:
            self.shift_node_sll()
        elif index == self.length:
            self.delete_node_sll_pop()
        else:
            remove_node_sll = self.get_node(index)
            if remove_node_sll != None:
                previous_node = self.get_node(index - 1)
                previous_node.next = remove_node_sll.next
                remove_node_sll.next = None
                self.length-=1

    def add_node(self, index, value):
        # Pedir valor del nodo
        if index == 1:
            self.create_node_sll_unshift(value)
        elif index == self.length:
            self.crear_node_sll_ends(value)
        else:
            new_node = self.Node(value)
            actual_node_sll = self.get_node(index)
            if actual_node_sll != None:
                previous_node = self.get_node(index - 1)
                previous_node.next = new_node
                new_node.next = actual_node_sll
                self.length+=1

    def update_node_value(self, index, new_value):
        search_node = self.get_node(index)
        if search_node != None:
            search_node.value = new_value