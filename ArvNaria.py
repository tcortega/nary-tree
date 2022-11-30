import copy


class ArvNaria:
    m = 0
    root = None

    def __init__(self, data=None, child_count=2):
        self.data = data
        self.children = [None] * child_count

    @staticmethod
    def inicArvnaria(child_count=2):
        return ArvNaria(None, child_count)

    def criaArvNaria(self, data):
        self.data = data

    def subArvNaria(self):
        if self.children:
            return self.children

    def raizArvoreNaria(self):
        return self.data

    def vazioArvNaria(self):
        return not self.children and self.data is None

    def insereArvNaria(self, child, father):
        if self.data == father:
            return self.handle_insertion_below_root(child, father)

        return self.handle_insertion(child, father)

    def handle_insertion_below_root(self, child, father):
        if not self.children.count(None):
            return False

        children_size = len(self.children)
        for _ in range(children_size):
            index = self.children.index(None)
            if index == 0:
                self.children[index] = copy.deepcopy(child)
            else:
                for i in reversed(range(children_size)):
                    self.children[i] = copy.deepcopy(self.children[i-1])

                self.children[0] = copy.deepcopy(child)

            return True

    def handle_insertion(self, child, father):
        for tree_child in self.children:
            if tree_child is None:
                continue

            if tree_child.insereArvNaria(child, father):
                return True

    def adicionaArvNaria(self, child, father):
        if self.data == father:
            return self.handle_addition_below_root(child, father)

        return self.handle_insertion(child, father)

    def handle_addition_below_root(self, child, father):
        if not self.children.count(None):
            return False

        children_size = len(self.children)
        for i in reversed(range(children_size)):
            if self.children[i] is None:
                self.children[i] = copy.deepcopy(child)
            else:
                for j in range(children_size-1):
                    self.children[j] = copy.deepcopy(self.children[j+1])

                self.children[children_size-1] = copy.deepcopy(child)

            return True

    def elimSubArvNaria(self, data):
        for i in range(len(self.children)):
            if self.children[i] is None:
                continue

            if self.children[i].data == data:
                return self.children.pop(i)

            child = self.children[i].elimSubArvNaria(data)
            if child is not None:
                return child

    def destruirArvNaria(self):
        self.children.clear()
        return True

    def estaArvNaria(self, data):
        if self.data == data:
            return True

        for child in self.children:
            if child is None:
                continue

            if child.data == data:
                return True

            found = child.estaArvNaria(data)
            if found:
                return True

    def imprime(self):
        print(f'{self.data} => ', end='')
        for child in self.children:
            if child is None:
                continue

            print(f'{child.data} , ', end='')

        print()

        for child in self.children:
            if child is None:
                continue

            child.imprime()
