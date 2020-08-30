import csv
import time
from abc import ABC
from twitchio.ext import commands

min_call_freq = 5
used = {}


def addComG(message):
    mensagem = message.content
    comando = mensagem.split(" ")[1]
    conteudoCom = message.content
    conteudoCom = conteudoCom.split(" ")[2:]
    conteudoCom = ' '.join(conteudoCom)
    with open('ArquivosCsv/commandsG.csv') as csvfileread:
        read = csv.reader(csvfileread)
        for row in read:
            if comando in row:
                return "Ja existe esse trem ;-;"
    with open('ArquivosCsv/commandsM.csv') as csvfileread:
        read = csv.reader(csvfileread)
        for row in read:
            if comando in row:
                return "Ja existe esse trem, só q ta pra Mods ;-;"
    with open('ArquivosCsv/commandsG.csv', 'a', newline='') as csvfilewrite:
        writer = csv.writer(csvfilewrite)
        writer.writerow([comando, conteudoCom])
        if '{count}' in mensagem:
            addCount(message)
    return "Deu certo viu? SeemsGood "


def addComM(message):
    mensagem = message.content
    comando = mensagem.split(" ")[1]
    conteudoCom = message.content
    conteudoCom = conteudoCom.split(" ")[2:]
    conteudoCom = ' '.join(conteudoCom)
    with open('ArquivosCsv/commandsM.csv') as csvfileread:
        read = csv.reader(csvfileread)
        for row in read:
            if comando in row:
                return "Ja existe esse trem ;-;"
    with open('ArquivosCsv/commandsG.csv') as csvfileread:
        read = csv.reader(csvfileread)
        for row in read:
            if comando in row:
                return "Ja existe esse trem, só q ta pra Geral ;-;"
    with open('ArquivosCsv/commandsM.csv', 'a', newline='') as csvfilewrite:
        writer = csv.writer(csvfilewrite)
        writer.writerow([comando, conteudoCom])
        if '{count}' in mensagem:
            addCount(message)
    return "Deu certo viu? SeemsGood "


def delCom(message):
    strRetorno = 'O fiw, não da pra excluir algo q nn existe...'
    mensagem = message.content
    comando = mensagem.split(" ")[1]
    with open('ArquivosCsv/commandsG.csv') as csvfileread:
        with open('ArquivosCsv/bkcommandsG.csv', 'w', newline='') as bkcsvfilewrite:
            read = csv.reader(csvfileread)
            bkwriter = csv.writer(bkcsvfilewrite)
            for row in read:
                if comando == row[0]:
                    strRetorno = "Mais um deletado igual minha autoestima LUL "
                    if '{count}' in row[1]:
                        delCount(message)
                else:
                    bkwriter.writerow([row[0], row[1]])
    with open('ArquivosCsv/bkcommandsG.csv') as bkcsvfileread:
        with open('ArquivosCsv/commandsG.csv', 'w', newline='') as csvfilewrite:
            readbk = csv.reader(bkcsvfileread)
            writer = csv.writer(csvfilewrite)
            for rowbk in readbk:
                writer.writerow([rowbk[0], rowbk[1]])

    with open('ArquivosCsv/commandsM.csv') as csvfileread:
        with open('ArquivosCsv/bkcommandsM.csv', 'w', newline='') as bkcsvfilewrite:
            read = csv.reader(csvfileread)
            bkwriter = csv.writer(bkcsvfilewrite)
            for row in read:
                if comando == row[0]:
                    strRetorno = "Mais um deletado igual minha autoestima LUL "
                    if '{count}' in row[1]:
                        delCount(message)
                else:
                    bkwriter.writerow([row[0], row[1]])
    with open('ArquivosCsv/bkcommandsM.csv') as bkcsvfileread:
        with open('ArquivosCsv/commandsM.csv', 'w', newline='') as csvfilewrite:
            readbk = csv.reader(bkcsvfileread)
            writer = csv.writer(csvfilewrite)
            for rowbk in readbk:
                writer.writerow([rowbk[0], rowbk[1]])
    return strRetorno


def searchCom(message):
    mensagem = message.content
    comando = mensagem.split(" ")[0]
    with open('ArquivosCsv/commandsG.csv') as csvfileread:
        read = csv.reader(csvfileread)
        for row in read:
            if comando == row[0]:
                return row[1]
    if message.author.is_mod:
        with open('ArquivosCsv/commandsM.csv') as csvfileread:
            read = csv.reader(csvfileread)
            for row in read:
                if comando == row[0]:
                    return row[1]
    return None


def addCount(message):
    mensagem = message.content
    comando = mensagem.split(" ")[1]
    with open('ArquivosCsv/countcommands.csv', 'a', newline='') as csvfilewrite:
        writer = csv.writer(csvfilewrite)
        writer.writerow([comando, 0])


def delCount(message):
    mensagem = message.content
    comando = mensagem.split(" ")[1]
    with open('ArquivosCsv/countcommands.csv') as csvfileread:
        with open('ArquivosCsv/bkcountcommands.csv', 'w', newline='') as bkcsvfilewrite:
            read = csv.reader(csvfileread)
            bkwriter = csv.writer(bkcsvfilewrite)
            for row in read:
                if comando != row[0]:
                    bkwriter.writerow([row[0], row[1]])
    with open('ArquivosCsv/bkcountcommands.csv') as bkcsvfileread:
        with open('ArquivosCsv/countcommands.csv', 'w', newline='') as csvfilewrite:
            readbk = csv.reader(bkcsvfileread)
            writer = csv.writer(csvfilewrite)
            for rowbk in readbk:
                writer.writerow([rowbk[0], rowbk[1]])


def seachCount(message):
    mensagem = message.content
    comando = mensagem.split(" ")[0]
    with open('ArquivosCsv/countcommands.csv') as csvfileread:
        read = csv.reader(csvfileread)
        for row in read:
            if comando == row[0]:
                countAddplusOne(message)
                return int(row[1]) + 1


def countAddplusOne(message):
    mensagem = message.content
    comando = mensagem.split(" ")[0]
    with open('ArquivosCsv/countcommands.csv') as csvfileread:
        with open('ArquivosCsv/bkcountcommands.csv', 'w', newline='') as bkcsvfilewrite:
            read = csv.reader(csvfileread)
            bkwriter = csv.writer(bkcsvfilewrite)
            for row in read:
                if comando != row[0]:
                    bkwriter.writerow([row[0], row[1]])
                else:
                    bkwriter.writerow([row[0], int(row[1]) + 1])
    with open('ArquivosCsv/bkcountcommands.csv') as bkcsvfileread:
        with open('ArquivosCsv/countcommands.csv', 'w', newline='') as csvfilewrite:
            readbk = csv.reader(bkcsvfileread)
            writer = csv.writer(csvfilewrite)
            for rowbk in readbk:
                writer.writerow([rowbk[0], rowbk[1]])


def is_spam(command):
    if (
            command not in used or
            time.time() - used[command] > min_call_freq
    ):
        used[command] = time.time()
        return 'command'
    else:
        return 'spam'


class Bot(commands.Bot, ABC):
    def __init__(self):
        super().__init__(irc_token='oauth:f5u0ogcf99o2lmr4pu36ghrxvdfn73',
                         client_id='7ri5xc6qmbljxoxom9vd51cdnaxmad',
                         nick='bioboterson',
                         prefix='!',
                         initial_channels=['biolocky', 'amandinhadequeijo'])

    async def event_ready(self):
        print(f'O {self.nick} ficou pronto!')

    async def event_message(self, message):
        mensagem = message.content
        comando = mensagem.split(" ")
        print(message.author.name + ": " + message.content)
        if message.author != self.nick:
            if not (is_spam(comando[0]) == 'spam'):
                if message.author.is_mod or (message.author.name == 'biolocky'):
                    if comando[0] == '!addcomG':
                        # print("Com")
                        # print("Entrou em add Geral")
                        await message.channel.send(addComG(message))
                    elif comando[0] == '?addcomG':
                        await message.channel.send("!addcomG {comando} {ação}")

                    elif comando[0] == '!addcomM':
                        # print("Com")
                        # print("Entrou em add Mod")
                        await message.channel.send(addComM(message))
                    elif comando[0] == '?addcomM':
                        await message.channel.send("!addcomM {comando} {ação}")

                    elif comando[0] == '!delcom':
                        print("Com")
                        # print("Entrou em del")
                        await message.channel.send(delCom(message))
                    elif comando[0] == '?delcom':
                        await message.channel.send("!delcom {comando}")
                    else:
                        resposta = searchCom(message)
                        if resposta is not None:
                            if '{count}' in resposta:
                                num = str(seachCount(message))
                                resposta = resposta.replace('{count}', num)
                            if '{marcado}' in resposta:
                                if len(comando) == 1:
                                    resposta = resposta.replace('{marcado}', message.author.name)
                                else:
                                    resposta = resposta.replace('{marcado}', comando[1])
                            if '{autor}' in resposta:
                                #
                                resposta = resposta.replace('{autor}', message.author.name)
                            await message.channel.send(resposta)
                else:
                    resposta = searchCom(message)
                    if resposta is not None:
                        if '{count}' in resposta:
                            num = str(seachCount(message))
                            resposta = resposta.replace('{count}', num)
                        if '{marcado}' in resposta:
                            if len(comando) == 1:
                                resposta = resposta.replace('{marcado}', message.author.name)
                            else:
                                resposta = resposta.replace('{marcado}', comando[1])
                        if '{autor}' in resposta:
                            #
                            resposta = resposta.replace('{autor}', message.author.name)
                        await message.channel.send(resposta)


bot = Bot()
bot.run()
