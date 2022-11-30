import time

from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator, EmptyInputValidator
from InquirerPy.base.control import Choice

from ArvNaria import ArvNaria
from util import cls


def handle_remove(main_tree):
    data = inquirer.text(message="Insira o valor da sub-árvore a ser removido:",
                         validate=EmptyInputValidator()).execute()

    if main_tree.data == data:
        main_tree = None
        removed = True
    else:
        removed = main_tree.elimSubArvNaria(data)

    if removed:
        print('\nNó removido com sucesso!')
        if main_tree is None:
            print('Árvore destruída por completo! Finalizando execução...')
            return True


def main_menu(main_tree, insert_order, child_size):
    while main_tree is not None:
        cls()
        action = inquirer.select(message='Selecione a ação que deseja realizar:',
                                 choices=['Inserir Nó', 'Remover Nó', 'Apagar Árvore', 'Imprimir', 'Buscar Elemento',
                                          Choice(value=None, name="Sair")], default='Inserir Nó').execute()

        if action is None:
            break

        cls()
        if 'Inserir' in action:
            handle_insert(child_size, insert_order, main_tree)

        elif 'Remover' in action:
            should_break = handle_remove(main_tree)
            if should_break:
                break

        elif 'Apagar' in action:
            handle_delete(main_tree)
            break

        elif action == 'Imprimir':
            main_tree.imprime()

        elif 'Buscar' in action:
            handle_search(main_tree)

        time.sleep(2)


def handle_search(main_tree):
    data = inquirer.text(message="Insira o valor do nó a ser buscado:",
                         validate=EmptyInputValidator()).execute()
    result = main_tree.estaArvNaria(data)
    if result:
        print(f'\nO elemento {data} está contido na árvore!')
    else:
        print(f'\nNão foi possível encontrar o nó {data}!')


def handle_delete(main_tree):
    print('\nÁrvore destruída por completo! Finalizando execução...')
    main_tree.destruirArvNaria()
    del main_tree


def handle_insert(child_size, insert_order, main_tree):
    data = inquirer.text(message="Insira o valor a ser inserido:", validate=EmptyInputValidator()).execute()
    child = ArvNaria(data, child_size)
    father = inquirer.text(message="Insira o nó pai que será associado:",
                           validate=EmptyInputValidator()).execute()
    child.root = father
    if insert_order == 'Inicio':
        success = main_tree.insereArvNaria(child, father)
    else:
        success = main_tree.adicionaArvNaria(child, father)
    if success:
        print(f'\nO nó {data} foi inserido com sucesso!')
    else:
        print('\nErro ao inserir nó, sub-árvore já está cheia ou o nó pai é inválido!')


if __name__ == '__main__':
    cls()
    child_count = int(inquirer.number(message="Insira o máximo de filhos por nó:", min_allowed=0,
                                      validate=NumberValidator()).execute())

    root = inquirer.text(message="Insira o valor da raíz:").execute()
    insertion_order = inquirer.select(message='Selecione a ordem de inserções:', choices=['Inicio', 'Fim']).execute()

    tree = ArvNaria.inicArvnaria(child_count)
    tree.data = root
    tree.m = child_count

    main_menu(tree, insertion_order, child_count)
