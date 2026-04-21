# ETAPA 1 - Apresentação do Desafio Profissional.
#
# Você foi contratado como desenvolvedor iniciante em uma empresa de tecnologia educacional 
# chamada EduLogic Sistemas. A empresa está criando um módulo chamado “Assistente de Aprovação”, 
# que ajudará professores a calcular automaticamente a situação final de estudantes em uma disciplina, 
# com base nas notas e frequência.
#
# Atualmente, o processo é manual: cada professor usa planilhas diferentes, faz contas na calculadora e, 
# muitas vezes, comete erros na aplicação das regras. A direção decidiu padronizar a lógica em 
# um sistema que siga as seguintes regras:
#
# >> Cada estudante possui duas notas principais (N1 e N2).
# >> A média final (M) é calculada como: o M=(N1+N2)/2
# >> A situação final depende de média e frequência: 
#    > Aprovado: se M ≥ 7,0 E frequência ≥75%  
#    > Recuperação: se 5,0 ≤ M < 7,0 E frequência ≥ 75%
#    > Reprovado: se M < 5,0 OU frequência < 75% 
#
# Seu papel será projetar a lógica desse módulo, produzindo:
#
# - Um pseudocódigo (portugol) ou em Python bem estruturado.
# - Um fluxograma representando a sequência de decisões do programa.
# - Uma explicação de como os conectivos lógicos (E, OU, NÃO) aparecem nas condições de decisão.

from calculos import *

print("=================================================")
print("   EduLogic Sistemas - Assistente de aprovação   ")
print("=================================================")

print("Seja bem-vindo ao assistente de aprovação.")
print("O que deseja fazer ?")
print("1 - Cadastrar novo aluno")
print("2 - Consultar informações de aluno cadastrado")
print("3 - Cadastrar as notas de um aluno")
print("4 - Cadastrar a frequência de um aluno")

print("=================================================")


n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

print("A média do aluno é",media(n1,n2))
print("=================================================")
