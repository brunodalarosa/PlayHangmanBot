#-*- coding: utf-8 -*-
#Linguagem Português, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#palavras
palavras = [
                ['Palavras com acento','Cristão','País','Médico','Solução']
            ]

#Botões dos Keyboards
novojogo = 'Novo Jogo' + emoji_joystick
ajuda = 'Ajuda' + emoji_light
rank = 'Rank' + emoji_trofeu
ligar = 'Ligar' + emoji_foguete
desligar = 'Desligar' + emoji_x
config = 'Configurações' + emoji_ferramenta
voltar = 'Voltar' + emoji_back
cancelar = 'Cancelar' + emoji_x
comandos = 'Comandos' + emoji_light
entrar = 'Entrar' + emoji_foguete
sair = 'Sair' + emoji_x
fechar_jogo = 'Fechar jogo' + emoji_foguete
cancelar_jogo = 'Cancelar jogo' + emoji_x
arriscar = 'Arriscar' + emoji_gritar
esta_fora = 'Você está fora desse jogo' + emoji_proibido

#Respostas iniciais
linguas = emoji_planeta + 'Escolha a linguagem:'
iniciar_msg = 'Carregando...'
mudar_lingua = 'Mudança feita com sucesso' + emoji_thumbsUp
start_msg = 'Olá, eu sou o Forca Bot e fui criado para organizar jogos da forca!\nAperte no botão "novo jogo" para começar!'
is_enabled = 'O Bot já está ligado'
stop_msg = 'Bot desligado'
start_help_msg = 'Não há nenhum jogo em andamento, clique no botão "novo jogo" para começar um jogo ou veja o ranking no botão "Rank".\n Você também pode alterar as configurações se desejar' + emoji_sorriso
config_help_msg = 'Escolha a lingua do Bot.\nObs.: As palavras do jogo dependem da língua escolhida'
voltar_msg = 'Menu inicial'
cantdo_msg = 'Você não pode fazer isso'
comandos_msg = 'Comandos'
ocupado_msg = 'Bot ocupado'
teclado_msg = 'Teclado'
ranking_msg = emoji_coroa + ' RANKING ' + emoji_coroa

#respostas PreGame
def inicialMsg(u_name):
    return 'Começando um novo jogo!\n'+u_name+' será o administrador dessa rodada.' + emoji_oculos

inicial_msg = 'Vamos começar definindo os jogadores, quem quiser participar clique em Entrar'+emoji_sorriso
close_game_msg = 'O jogo vai começar! Na sua vez, clique nas letras para chutar ou clique em arriscar e me mande a palavra completa se você acha que já a descobriu, mas cuidado, não tem volta!'+emoji_zoando+'\nVocês jogarão nesta ordem:'
palavra_msg = 'A palavra é: '
categoria_msg = 'Categoria: '
esta_dentro_msg = 'Você já participa desta partida'
sem_jogador_msg = 'Todos os jogadores sairam, o jogo será cancelado' + emoji_surpreso
cancelar_jogo_msg = 'Jogo cancelado pelo administrador'
is_out_msg = 'Você não participa desse jogo' + emoji_lua
vidas_msg = 'Vidas: '
pre_game_help_msg = 'Jogo em modo de entrada, clique em Entrar para participar\nADM: Clique em Fechar Jogo para começar o jogo com os participantes atuais'

def novoAdmMsg(u_name):
    return 'Um novo administrador foi definido! '+u_name+' é o novo administrador.' + emoji_oculos

def playerQuitMsg(u_name):
    return 'O jogador '+u_name+' saiu da partida.' + emoji_triste

def entrarMsg(u_name):
    return 'Ok '+u_name+', você vai participar dessa rodada' + emoji_blink

#repostas InGame
in_game_help_msg = 'Clique nas letras para chuta-las ou em Arriscar se você acha que já descobriu a palavra secreta! se quiser mais opções clique em Comandos'
arriscar_msg = 'Então você acha que já descobriu qual é a palavra? ' + emoji_zoando + ' Me mande a palavra, mas pense bem, se você errar será eliminado!' + emoji_lua
round_errado_msg = 'Não é a sua vez de jogar, espere a sua vez!' + emoji_lua
acertou_letra_msg = 'Você acertou!' + emoji_claps
errou_letra_msg = 'Errou' + emoji_triste
jachutada_msg = 'Essa letra já foi chutada' + emoji_surpreso
umavida_msg = 'Somente uma vida restante! Descubra a palavra ou aceite sua DERROTA!' + emoji_lua
gameover_msg = emoji_poop + ' PERDERAM, FIM DE JOGO ' + emoji_poop
fora_msg = 'Você não participa dessa rodada, espere ela acabar para participar de um novo'

def perdeu(u_name):
    return u_name + ' arriscou e errou! O jogador foi eliminado!' + emoji_lua

def nextPlayer(u_name):
    return 'Vez de ' + u_name + ' ' + emoji_point

def venceu(u_name):
    return emoji_confetti + ' Parabéns ' + u_name + ' você descobriu a palavra secreta e ganhou o jogo! ' + emoji_confetti + '\n Pontos calculados e ranking atualizado! ' + emoji_sorriso
