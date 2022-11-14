# TTT3L -> TIC TAC TOE 3 LAYER
#### Video Demo:  <https://youtu.be/wUlBYTonRM4>
### Description: The tic-tac-toe even deeper. where a move can be overlapped and surprise your opponent
    
##### IN ENGLISH

##### Files
 #### engine.py
 ## import engine
 ## eng = engine.Engine(width, height, colorBG)

 this python file facilitates access to py Library features   that were used during the coding process.

 # functionalities:
 - access mouse clicks by eng.mouse click[ 0 to 2 incluse] where 0 is the state of the left button, 1 is the state of the central button (scroll pressed) and 2 is the state of the right button.

 - return mouse position via eng.get_mousePosition

 - execute a gameLoop that renders objects that have a method named draw(eng.display) passing the display of the eng object as a parameter.

 - draw new objects via the eng.addToDrawList(obj) function

 - add function to be executed inside the gameLoop through the eng.addFunction(external_function_name) method

 - draw a button on the window using the method drawButton(btn_color, x, y, x_length, y_length)

 - draw text in the window using the method eng.drawText(font_name, font_type, font_size)

 - change the window title and background color via the eng.display_config(title, color) method

 #### casa.py
 ## import casa
 ## home = casa.Casa(x, y ,a, l, cor, index, nivel)
file responsible for creating a square with position x(house.x), position y(house.y), height(house.a), width(house.l), color (house.color), index(house.index) , level(house.level). and return your initial and final x position, and final initial y through the casa.get_pos(dot) method where dot can take on the values of xi, xf, yi, yf


 #### tabuleiro.
 ## import tabuleiro
 ## board = tabuleiro.Tabuleio(x, y ,a, l, cor, index, nivel)
 file responsible for creating a list of objects of the type house and distributing them in an orderly way in the window. passing as parameters (dim, tam, color) where dim is the dimension of the board, tam is the size of the home object and color is the color of the home object.

 #### player.py
 ## from player import *
 ## bola = Bola(x, y, cor, casa)
 ## xis = Xis(x, y, cor, casa)
 file that has 3 classes, 1 parent class (Player) and 2 child class (Ball and Cheese). passing as vestment the x position, y position, color and a house object. either a circle (Ball) or an X (Xis) will be drawn on the designated casa.

 #### replays.py
 ## from replays import *
 this file is responsible for managing the save.txt file. which creates it if it doesn't exist and updates it on save game.

 #### project.py
 ## import project
 ## game = project.Project()
 ## game.main()
 the project class is responsible for creating an Engine object and a board where the game will take place. add your business rules inside gameLoop.

 #### requirements.txt
 has all the libraries that were used in the project and their pip

##### EM PORTUGUÊS

 ##### Arquivos
 #### engine.py
 ## import engine
 ## eng = engine.Engine(largura, altura, colorBG)

 este arquivo python facilita o acesso aos recursos da biblioteca py que foram usados ​​durante o processo de codificação.

 # funcionalidades:
 - acessar cliques do mouse por eng.mouse click[ 0 to 2 include] onde 0 é o estado do botão esquerdo, 1 é o estado do botão central (scroll pressionado) e 2 é o estado do botão direito.

 - retornar a posição do mouse via eng.get_mousePosition

 - executa um gameLoop que renderiza objetos que possuem um método chamado draw(eng.display) passando a exibição do objeto eng como parâmetro.

 - desenhe novos objetos através da função eng.addToDrawList(obj)

 - adicionar função a ser executada dentro do gameLoop através do método eng.addFunction(external_function_name)

 - desenhe um botão na janela usando o método drawButton(btn_color, x, y, x_length, y_length)

 - desenhe o texto na janela usando o método eng.drawText(font_name, font_type, font_size)

 - altere o título da janela e a cor de fundo através do método eng.display_config(title, color)

 #### casa.py
 ## import casa
 ## home = casa.Casa(x, y ,a, l, cor, index, nivel)
 arquivo responsável por criar um quadrado com posição x(casa.x), posição y(casa.y), altura(casa.a), largura(casa.l), cor (casa.cor), índice(casa.índice) , nível(casa.nível). e retorne sua posição x inicial e final, e y inicial final através do método casa.get_pos(dot) onde dot pode assumir os valores de xi, xf, yi, yf


 #### tabuleiro.
 ## import tabuleiro
 ## tabuleiro = tabuleiro.Tabuleio(x, y ,a, l, cor, índice, nível)
 arquivo responsável por criar uma lista de objetos do tipo casa e distribuí-los de forma ordenada na janela. passando como parâmetros (dim, tam, color) onde dim é a dimensão do tabuleiro, tam é o tamanho do objeto home e color é a cor do objeto home.

 #### jogador.py
 ## from player import *
 ## bola = Bola(x, y, cor, casa)
 ## xis = Xis(x, y, cor, casa)
 arquivo que possui 3 classes, 1 classe pai (Player) e 2 classes filhas (Bola e Queijo). passando como vestimenta a posição x, a posição y, a cor e um objeto casa. um círculo (Bola) ou um X (Xis) será desenhado na casa designada.

 #### replays.py
 ## da importação de replays *
 este arquivo é responsável por gerenciar o arquivo save.txt. que o cria se não existir e o atualiza ao salvar o jogo.

 #### project.py
 ## import project
 ## jogo = projeto.Projeto()
 ## jogo.main()
 a classe de projeto é responsável por criar um objeto Engine e um tabuleiro onde o jogo acontecerá. adicione suas regras de negócios dentro do gameLoop.

 #### requirements.txt
 tem todas as bibliotecas que foram usadas no projeto e seus pip
