from sorveteria import Sorveteria
class Main:
   def __init__(self) -> None:
      self.sorveteria = Sorveteria()

   def execute(self):
      self.sorveteria.opcoes_menu()


if __name__ == '__main__':
   main = Main()
   main.execute()
