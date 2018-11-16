from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Test')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Eu estou bem']
conversa2 = ['Qual seu nome?', 'Meu nome é bot']
conversa3 = ['Qual é a sua cor preferida?', 'preto', 'O que você gosta de fazer?', 'gosto de conversa']

bot.set_trainer(ListTrainer)
bot.train(conversa)
bot.train(conversa2)
bot.train(conversa3)

while True:
      quest = input("Você: ")
      resposta = bot.get_response(quest)
      if float(resposta.confidence) > 0.5:
            print ('Bot: ', resposta)
      else:
            print ('Bot: não sei')
