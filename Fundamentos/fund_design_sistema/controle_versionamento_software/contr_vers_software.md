## Controle de Versionamento de Software

- Tópicos:
	- Git e Versionamento
	- Repositórios Git
	- Termos do Git
	- Comandos Git

## Configurando o Git

- git config:
	- Define o usuário que irá trabalhar com o Git.
	- Sintaxe:
		- git config --global user.name "Bruno S Silveira"
		- git config --global user.email "bruno.englishprog@gmail.com"
		- git config --global core.editor vscode
		- git config --list (lista todas as configurações)

- git init (inicia um repositório na pasta)

## Branchs (ramificações)

- Podemos ramificar nosso projeto para trabalharmos em funcionalidade separadas simultaneamente.
- O branch padrão é chamado de main. É criado quando você cria o repositório.

- Fluxo de trabalho:
	- git add -> git commit -> git push
		- git add: seleciona os arquivos a commitar, "add ." seleciona todos.
		- git commit: faz o commit localmente, salva localmente a alteração.
		- git push: não é obrigatório, ele envia para o repositório remoto tudo que foi commitado no repo. local.

	- git push:
		- git push origin main
		- git push origin funcionalidade_x (aqui seria uma outra branch)
	
	- git pull:
		- git pull origin main
		- git pull origin funcionalidade_x (aqui seria uma outra branch)
		- **OBS.: Em projetos com mais gente, é importante sempre no inicio do trabalho fazer um pull para garantir que está com o projeto mais atualizado.

## Outros comandos Git

- git log:
	- mostra os últimos commits, com um código, a branch, o autor, a data e o comentário do commit.

- git reset:
	- soft: retorna imediatamente ao estado antes do commit
	- mixed - retorna ao estado antes do commit e antes do add
	- hard - apaga tudo para antes do último commit

- git diff:
	- Mostra os detalhes das alterações nos arquivos. Sintaxe: git diff, git diff --name-Only, git diff <nomeArquivo>

## Trabalhando com Branchs

- git branch: Mostra as branchs e qual está agora. git branch nomeParaBranch: adiciona uma nova branch com o nome escolhido
- git checkout nomeDaBranch: muda para a branch escolhida

- Criar um repositório local, depois ligar ele com um repositório remoto: git remote add origin "endereço do repositório remoto"