# Sistema para reabrir mesa no G6 - Digisat

Escopo desse repo
-----------------
 
Esse repositorio foi criado com intuito de reabrir a mesa no sistema G6 da Digisat, pois quando fazia uma nota manual e 
por algum motivo fecha-se o sem o concluir, a mesa que foi importada era finalizada junto. Por esse motivo acabou sendo 
necessario a criação desse sistema.

Como instalar
-----------------
* Ele foi desenvolvido para o python 3.6, não quer dizer que não funcione com futuras versões do python ou até mesmo que 
funcione. Então esse fica sendo um dos primeiro requisitos.

* Depois de instalar o python fica sendo necessario criar um ambiente virtual para controle as bibliotecas utlizadas
dentro desse projeto. O mesmo pode ser criado usando o seguinte comando pelo CMD:


    python -m venv venv
    
> Lembrando que o python precisa esta nas variaveis ambientes do windows para que o comando acima seja reconhecido pelo CMD.

* Depois precisamos ativar o ambiente virtual que acabamos de criar usando o comando

    
    venv\Scripts\activate.bat
    
> É necessario que a pasta ativa do CMD seja a pasta que acabamos de criar o ambiente virtual, caso não seja use o 
> comando CD para se deslocar até a pasta correta


* Agora vamos instalar as bibliotecas utilizadas no projeto com o comando abaixo:


    pip install -r requeriments.txt
    
Quando todos os passos acima forem concluidos a instalação esta finalizada.

Como utilizar
-----------------

Depois de instalado você deverar abrir o arquivo **start.bat**, ele fornecerar um endereço para que você consiga 
acessar via navegador(browser).

Você deverar pega tal endereço e acessar pelo navegador(browser) e encontrar uma tela pedindo o **número da mesa**, 
**hora de abertura da mesa** e a **hora de fechamento da mesa**. Ao inserir tais informações o sistema irar buscar os produtos 
com as informações fornecedias fechada na data atual e mostrar na tela dando a opção de reabrir a mesa ou retornar a tela
anterior para correção das informações.

Uma vez que for clicado em reabrir a mesa, o sistema ira pega tais produtos e volta ao sistema como pendentes de 
faturamento.