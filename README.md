# armario
O Armário é uma ferramenta criada para auxiliar na organização de hackerspaces. Ele permite catalogar e gerenciar todos os recursos presentes no espaço, desde equipamentos eletrônicos até ferramentas. Com o Armário, é possível adicionar novos objetos e atualizar informações existentes, tornando o processo de busca de recursos muito mais eficiente.

# Funcionalidades:
1. Visualizar todos os objetos do hackerspace, incluindo descrição e quantidade.
2. Verificar se o produto está em uso.
3. Adicionar um novo objeto com imagem, quantidade e descrição.
4. Atualizar um objeto existente no sistema.
5. Excluir um objeto no sistema.

# Instalação:
Para usar o Armário, é necessário ter Python 3 instalado. Além disso, é preciso ter as bibliotecas Flask Restful e Dataset lib instaladas. Para instalar as bibliotecas, siga as etapas abaixo:

Abra o terminal e digite `pip install Flask-RESTful` e pressione enter para instalar a biblioteca Flask Restful.

Em seguida, digite `pip install dataset` e pressione enter para instalar a biblioteca Dataset lib.

# Uso:
1. Abra o terminal e execute o seguinte comando para iniciar o servidor:
`python app.py`
2. Em seguida, você pode testar as funcionalidades do Armário utilizando os comandos curl abaixo:
* Visualizar todos os objetos:
``` bash 
$ curl -X GET http://localhost:5000/api/
```
* Adicionar um novo objeto:
``` bash 
curl -X POST -H "Content-Type: application/json" -d '{"nome":"nome","dec":"descrição", "quant":"Quantidade"}' http://localhost:5000/api/
```
* Atualizar um objeto existente:
``` bash 
curl -X PUT -H "Content-Type: application/json" -d '{"id":"1", "nome":"nome_atualizado","dec":"descrição_atualizado", "quant":"Quantidade_atualizada"}' http://localhost:5000/api/
```
* Excluir um objeto: 
``` bash 
curl -X DELETE -H "Content-Type: application/json" -d '{"id":"1"}' http://localhost:5000/api/
```

# arquitetura:
<p align="center">
<img src="/src/arquitetura.jpeg">
</p>


