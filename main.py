#Alunos: Adriana Maciel Quintana Hortiz, Alexandre Adryan Fernandes Rodrigues, Beatriz Júlia Cavalcantes dos Santos e William de Mendonça Ribeiro
#2° ano técnico em informática vespertino

#Bibliotecas
import os
from datetime import date

#Globais
global novosUsuarios
novosUsuarios = []

global alguem

global tarefas
tarefas = []


#Classe usuário
class Usuario:
  def _init__(self, nome, email, senha):
    self.__nome = nome
    self.__email = email
    self.__senha = senha
    self.__tele = tele

  def cadastro(self):
    self.__nome = input('Digite o seu nome: ') 
    self.__email = input('Digite o seu email: ')
    self.__senha = input('Digite sua senha: ')
    self.__tele = input('Digite sua tele: ')
    
  def getCadastro(self):
    return self.__nome
    return self.__email
    return self.__senha
    return self.__tele
  def getNome(self):
    return self.__nome
  def getEmail(self):
    return self.__email
  def getTele(self):
    return self.__tele

  def exibir(self):
    if len(novosUsuarios) == 0:
      print("i")
    else:
      for a in novosUsuarios:
        print("Nome: {} \nEmail: {} \nSenha: {} \nTelefone: {}".format(a.nome, a.email, a.senha, a.tele))
    
          
#Iniciar class tarefa
class Tarefa:
  def _init__(self, nomeTarefa, dataTarefa, horarioTarefa, exibirT):
    self.__nomeTarefa = nomeTarefa
    self.__dataTarefa = dataTarefa
    self.__horarioTarefa = horarioTarefa
    self.__exibirT = exibirT

  def atividadesSet(self, nomeTarefa):
    self.__nomeTarefa = nomeTarefa

  def dataSet(self, dataTarefa):
    self.__dataTarefa = dataTarefa

  def horarioSet(self, horarioTarefa):
    self.__horarioTarefa = horarioTarefa

  def getTarefa(self):
    return self.__nomeTarefa
    return self.__dataTarefa
    return self.__horarioTarefa
  
  def definirTarefa(self):
    print('\033[1;49;36m -AGENDANDO ATIVIDADE- \033[m')
    self.nomeTarefa = input("Defina sua atividade: ")
    self.horarioTarefa = input("Insira o horário de sua atividade: ")
    self.dataTarefa = input("Digite a data da sua atividade: ")
    tarefas.append(tarefa)
    
  def exibirT(self):
     for x in range(len(tarefas)):
      print(tarefa.nomeTarefa, "\n", tarefa.dataTarefa, "\n", tarefa.horarioTarefa)
#Fim class

#Funções
def iniciar():
  global novosUsuarios
  print('\033[1;49;31m BEM VINDO AO SEU PLANNER \033[m')
  
  quest = int(input("\n1 - CADASTRO \n2 - Definir TAREFA \n3 - EXIBIR TAREFA \n4 - INFORMAÇÕES DE USUÁRIO \n--> "))
  if quest == 1:
    print('\033[1;49;36m \n-INICIANDO SEU CADASTRO- \033[m')
    alguem = Usuario()
    alguem.cadastro()
    novosUsuarios.append(alguem)
    os.system("clear")
    iniciar()
  elif quest == 2:
    definirTarefa()
    os.system("clear")
    iniciar()
  elif quest == 3:
    exibirTarefa()
    
  elif quest == 4:
    os.system("clear")
    if len(novosUsuarios) == 0:
      print("i")
    else:
      for a in novosUsuarios:
        print("Nome: {} \nEmail: {}\n Telefone: {}".format(a.getNome(), a.getEmail()))
    retornar()
  elif quest < 0:
    raise Exception("Não aceitamos número abaixo de zero")
  else:
    print("encerrando ")


def definirTarefa():
  os.system("clear")
  tarefa.definirTarefa()

def exibirTarefa():
  tarefa.exibirT()
  retornar()


#Retornar ao inciar
def retornar():
  op = int(input("DIGITE 0 SE DESEJA VOLTAR PARA O MENU: "))
  try:
    op != 0
  except: 
    print("numero não identificado")
  finally:
    print("O tratamento de exceção terminou") 
    if op == 0:
      os.system()
      clear()
    
    
#Objeto
alguem = Usuario()
tarefa = Tarefa()

#fim da class  

#Start
iniciar()