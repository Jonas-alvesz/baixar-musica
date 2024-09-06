Descrição:

Este projeto é uma aplicação web que permite aos usuários baixarem músicas do YouTube em formato MP3. A aplicação, criada com Flask e Pytube, extrai o áudio de vídeos do YouTube, converte-o para MP3, e permite ao usuário baixar o arquivo diretamente para sua máquina.


Funcionalidades:

Entrada de URL do YouTube: O usuário pode colar a URL de um vídeo do YouTube para fazer o download do áudio.

Conversão para MP3: A aplicação baixa o vídeo e converte automaticamente o áudio para o formato MP3.

Baixar Arquivo MP3: O arquivo MP3 resultante é movido para a pasta de downloads do usuário ou pode ser baixado diretamente através da interface da aplicação.

Limpar Campo: O formulário contém um botão para limpar a URL inserida.


Requisitos:

Python 3.x

Flask: Framework web em Python para construir a interface do servidor.

Pytube: Biblioteca Python para download de vídeos do YouTube.

MoviePy: Biblioteca para manipulação de arquivos multimídia, usada para converter vídeos em arquivos MP3.

Instalação de Dependências:

Antes de rodar o projeto, instale as dependências necessárias:

pip install flask 

pytube moviepy
