a = 100
def fun():
    global a
    print(a)
    a = 500
    print(a)

def gen():
    print(a)

def function_summon():
    gen()
    fun()
    gen()

#function_summon()

global_variable = 100

def modify_global():
    global global_variable
    global_variable = 200
    print(f"Valor de global_variable dentro de la función: {global_variable}")
    return global_variable

def use_local():
    local_variable = 300
    print(f"Valor de local_variable dentro de la función: {local_variable}")


def use_global():
    print(f"Valor de global_variable dentro de la función: {global_variable}")


def main():
    print(f"Funcion use_local():")
    use_local()
    print(f"\nFuncion use_global():")
    use_global()
    print(f"\nFuncion modify_global():")
    modify_global()
    print(f"\nValor de global_variable después de modificarla: {global_variable}")

main()