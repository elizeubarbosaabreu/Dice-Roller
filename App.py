import PySimpleGUI as sg
from random import choice

dados = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

def jogada():
    return choice(dados)
    
sg.theme('DarkAmber')

layout = [
    [sg.Text(jogada(), key='-dado1-', font=('Arial', 180)),
     sg.Text(jogada(), key='-dado2-', font=('Arial', 180))],
    [sg.Stretch(),
     sg.Button('Nova_Jogada'),
     sg.Button('Regras_do_Jogo'),
     sg.Button('Sair_do_Jogo'),
     sg.Stretch()]
    ]

window = sg.Window('Jogo de Dados', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair_do_Jogo':
        break
    elif event == 'Nova_Jogada':
        window['-dado1-'].update(jogada())
        window['-dado2-'].update(jogada())
    elif event == 'Regras_do_Jogo':
        sg.Popup('REGRAS DO JOGO',
                 '''
1 - Através de sorteio do tipo 'Cara ou Coroa' ou 'Par ou Ímpar' decide quem vai começar o jogo...
2 - O primeiro jogador abre o software e anota a pontuação contando e somando os pontos dos dois dados...
3 - O jogadores seguintes clicam em nova jogada e também anotam a pontuação...
4 - A quantidade de jogada pode ser decidida previamente...
5 - Ganha o jogador que fizer a melhor pontuação...
6 - Se houver empate, joga-se novas partidas até que decida o vencedor...

Este jogo foi criado inteiramente em Python por Elizeu Barbosa Abreu...
Linkedin -> https://www.linkedin.com/in/elizeu-barbosa-abreu-69965b218/
GitHub -> https://github.com/elizeubarbosaabreu
''')
        
window.close()
        