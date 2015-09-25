#-*- coding: utf-8 -*-
#Linguagem Português, contém as strings que serão lidas para aparecerem no jogo

#Emojis
from emojis import *

#palavras
palavras = [
                ['Coisas', 'Vassoura', 'Panela', 'Cadeira', 'Chão'],
                ['Jogos', 'League of Legends', 'Defence of the Ancient', 'Tree of savior', 'Spore']
            ]

#Botões dos Keyboards
novojogo = 'Novo Jogo'
ajuda = 'Ajuda'
rank = 'Rank'
ligar = 'Ligar'
desligar = 'Desligar'
config = 'Configurações'
voltar = 'Voltar'
cancelar = 'Cancelar'
comandos = 'Comandos'
entrar = 'Entrar'
sair = 'Sair'
fechar_jogo = 'Fechar jogo'
cancelar_jogo = 'Cancelar jogo'
arriscar = 'Arriscar'
esta_fora = 'Você está fora desse jogo'

#Respostas iniciais
linguas = 'Escolha sua linguagem:'
iniciar_msg = 'Iniciando'
mudar_lingua = 'Mudança feita com sucesso'
start_msg = 'Olá, eu sou o Forca Bot e fui criado para organizar jogos da forca!\nAperte no botão "novo jogo" para começar!'
is_enabled = 'Forca Bot já está ligado'
stop_msg = 'Forca Bot desligado'
start_help_msg = 'Não há jogo em andamento, clique no botão "novo jogo" para começar um jogo'
config_help_msg = 'Escolha a linguagem do Bot.\nObs.: Palavra escolhida para o jogo depende da língua atual'
voltar_msg = 'Menu inicial'
cantdo_msg = 'Você não pode fazer isso'
comandos_msg = 'Comandos'
ocupado_msg = 'Bot ocupado'
teclado_msg = 'Teclado'

#respostas PreGame
def inicialMsg(u_name):
    return 'Começando um novo jogo!\n'+u_name+' será o administrador dessa rodada.'

inicial_msg = 'Vamos começar definindo os jogadores desta rodada, quem quiser participar escolha Entrar'+emoji_sorriso
close_game_msg = 'O jogo vai começar! Na sua vez, clique nas letras para chutar ou clique em arriscar e me mande a palavra para arriscar\nVocês jogarão nessa ordem:'
palavra_msg = 'A palavra é: '
categoria_msg = 'Categoria: '
esta_dentro_msg = 'Você já participa desta partida'
sem_jogador_msg = 'Todos os jogadores sairam, o jogo será cancelado'
cancelar_jogo_msg = 'Jogo cancelado pelo administrador'
is_out_msg = 'Você não participa desse jogo'
vidas_msg = 'Vidas: '
pre_game_help_msg = 'Jogo em modo de entrada, para entrar utilize Entrar\nADM: utilize Fechar Jogo para começar o jogo ou Cancelar Jogo para cancelar esse jogo'

def novoAdmMsg(u_name):
    return 'Um novo administrador foi definido! '+u_name+' é o novo administrador.'

def playerQuitMsg(u_name):
    return 'O jogador '+u_name+' saiu da partida.'

def entrarMsg(u_name):
    return 'Ok '+u_name+', você vai participar dessa rodada\nSe quiser sair é só usar o Sair'

#repostas InGame
in_game_help_msg = 'Clique nas letras para chuta-las, se quiser mais opções vá em Comandos'
arriscar_msg = 'Muito bem, agora me diga qual é a palavra? Pense bem, se você errar será eliminado!'
round_errado_msg = 'Não é a sua vez de jogar, espere a sua vez!'
fora_msg = 'Você não participa desse jogo, espere ele acabar para participar de um novo'
prox_round_msg = 'Agora é sua vez, '
venceu_msg = 'Acertou! Parabéns, você ganhou!'
perdeu_msg = 'Errou! E foi eliminado do jogo!'
