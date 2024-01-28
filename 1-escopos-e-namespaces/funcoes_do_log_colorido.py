import colorama

colorama.init()

nome_de_usuario = 'Dori'

def imprimir_no_log(texto, nivel='info'):
  if nivel == 'info':
    print(colorama.Fore.LIGHTBLUE_EX + f'Info: ', end='')
    print(colorama.Style.RESET_ALL + texto)
  elif nivel == 'aviso':
    print(colorama.Fore.YELLOW + f'Aviso: ', end='')
    print(colorama.Style.RESET_ALL + texto)
  elif nivel == 'erro':
    print(colorama.Fore.RED + f'Erro: ', end='')
    print(colorama.Style.RESET_ALL + texto)
  else:
    print(colorama.Fore.RED + f'Erro interno - nível desconhecido de mensagem' + colorama.Style.RESET_ALL)