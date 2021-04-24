import os

class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None
        
    def insertar(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insertar(a.left, dato)
            else:
                a.right = self.insertar(a.right, dato)
        return a

    def orden(self, a):
        if a == None:
            return None
        else:
            self.orden(a.left)
            print(a.dato)
            self.orden(a.right)

    def preorden(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorden(a.left)
            self.preorden(a.right)

    def postorden(self, a):
        if a == None:
            return None
        else:
            self.postorden(a.left)
            self.postorden(a.right)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)

tree = arbol()

while True:
    os.system("cls")
    print("Insertando Nodo a Arbol")
    opcion = input("\n1.-Insertar nodo \n2.-Orden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Salir \n\nEscoja opción a accionar ")

    if opcion == '1':
        nodo = input("\nIngresa el nodo a insertar")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.insertar(tree.root, nodo)
        else:      
            print("\nIngresar unicamente número")
    elif opcion == '2':
        if tree.root == None:
            print("Arbol Vacio")
        else:
            tree.orden(tree.root)
    elif opcion == '3':
        if tree.root == None:
            print("Arbol Vacio")
        else:
            tree.preorden(tree.root)
    elif opcion == '4':
        if tree.root == None:
            print("Arbol Vacio")
        else:
            tree.postorden(tree.root)
    elif opcion == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no encontrado...")
            else:
                print("\nNodo encontrado ",tree.buscar(nodo, tree.root), " si existe")
        else:
            print("\nIngresar unicamente número")        
    elif opcion == '6':
        print("\nSaliste del programa\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion dentro del rango (1-6)")
    print()
    os.system("pause")

print()