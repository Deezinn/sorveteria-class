from utils.delay_texto import digitar
from sorvete_comum import SorveteComum
from sorvete_premium import SorvetePremium


class Sorveteria:
   def __init__(self) -> None:
      self.estoque = None
      self.sorveteComum = SorveteComum()
      self.sorvetePremium = SorvetePremium()

   def opcoes_menu(self):
      digitar('Bem vindo a sorveteria, o que deseja?')
      digitar('Temos sorvete **comum** e o **premium**...')
      opcao_sorvete = input("\nDigite o sorvete que deseja: ").strip().lower()

      if opcao_sorvete == 'comum':
         self.estoque = self.sorveteComum
      elif opcao_sorvete == 'premium':
         self.estoque = self.sorvetePremium
      else:
         digitar("Opção invalida, tente novamente.")
         return self.opcoes_menu()

      digitar(f"{opcao_sorvete} selecionado...")
      self.mostrar_opcoes_suporte()

   def mostrar_opcoes_suporte(self):
      digitar('Temos 2 opções de suporte: casquinha ou copinho. Qual deseja?')
      digitar(f'\n{self.estoque.sorvete_casquinha}')
      digitar(f'{self.estoque.sorvete_copinho}')

      opcao_suporte = input("\nDigite **casquinha** ou **copinho**: ").strip().lower()

      if opcao_suporte == 'casquinha':
         self.estoque.sorvete_casquinha = 2
      elif opcao_suporte == 'copinho':
         self.estoque.sorvete_casquinha = 1
      else:
         digitar("Opção invalida, tente novamente.")
         return self.mostrar_opcoes_suporte()
      self.mostrar_opcoes_cobertura()

   def mostrar_opcoes_cobertura(self):
      digitar("Temos dois tipos de coberturas: **simples** e **especial**.")

      opcao_cobertura = input("\nDigite a opção da cobertura: ").strip().lower()

      if opcao_cobertura not in ['simples', 'especial']:
         digitar("Opção inválida. Tente novamente.")
         return self.mostrar_opcoes_cobertura()

      self.estoque.sorvete_cobertura = opcao_cobertura

      digitar("Pedido finalizado!")
      digitar(f"Preço total: R${self.estoque._preco:.2f}")
