from module import greet

x=42
z=12

def outer():
    print("")
    y = 12 #global это оч плохо
    print()
    def answer():
        asdas = 12 + y + z
        print(f'y in answer: {"y" in locals()}')
        print(locals)
        print(globals)
        return x
    return answer

if __name__ == '__name__':
    x = 42
    print(
        answer()
    )