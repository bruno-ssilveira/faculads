## Estrutura de Diretórios do Linux

- **Diretório bin**
    - /bin
        - binaries. onde econtram-se os binários (executáveis) de diversos programas.

- **Shell scripts:**
    - Similares aos Arquivos de Programas do windows. A diferença é que aqui ficam somente executáveis.

- **Diretório boot**
    - /boot
        - Contém os arquivos necessários para seu SO inicializar.
        - Contém o GRUB, por exemplo.

- **Diretório dev**
    - /dev
        - Devices (dispositivos).
        - Estão os arquivos do seu hardware. Discos, som, câmera, etc.

- **Unidades de disco são chamadas de:**
    - /dev/sda1 ou /dev/sda2.
    - O número no final varia de acordo com a partição.

- **Diretório etc**
    - /etc
        - Et cetera
        - Mantém as configurações gerais do sistema para todos os usuários.

- **Diretório home**
    - /home
        - Mantém os arquivos e configurações dos usuários do sistema.
        - Similar ao Users/Usuários do Windows.

- **Diretório root**
    - /root
        - Mantém os arquivos e configurações do root do sistema (adm).

- **Diretório lib**
    - /lib
        - Library. Mantém bibliotecas usadas por softwares. Similar a DLL em abiente Windows.

- **Diretórios media e mnt**
    - /media
        - Local de montagem de discos removíveis automáticos.
    - /mnt
        - Mount. Local de montagem de discos manuais pelo usuário.

- **Diretório opt**
    - /opt
        - Optional. Diretório usado por alguns fabricantes para instalar seus softwares. O Google Chrome é um exemplo de software que fica por padrão nessa pasta.

- **Outros diretórios**
    - /proc
        - Mantém arquivos sobre o sistema e seus processos.
    - /run
        - Armazena info e logs de serviços que rodaram.
    - /sbin
        - Semelhante ao bin, mas são binários que só podem ser acessados pelo root.
    - /temp
        - Diretório de arquivos temporários de cada sessão.
    - /usr
        - Já foi a pasta de usuários. Hoje, mantém arquivos de programas para usuários.
    - /var
        - Arquivos como logs do sistema, backups, ou seja, arquivos de tamanhos variáveis e que tendem a crescer de tamanho.

## Comandos de Manipulação de Diretórios

- **Comando ls**
    - Lista o conteúdo de um diretório. Sintaxe: ls (opções) (arquivo...)
    - ls -A: inclui os arquivos com o nome iniciando com "." na listagem - arquivos ocultos.
    - ls -R: lista recursivamente os diretórios encontrados.
    - ls -d: lista nomes de diretórios como arquivo, preferencialmente no lugar de seus conteúdos.

- **Comando cd**
    - Muda o diretório corrente para "dir". Sintaxe: cd (-L / -P) (dir)... "cd Downloads" entra na pasta Downloads, "cd .." volta uma página, "cd ~" volta direto pra /home.

- **Comando mkdir**
    - Cria diretórios. Sintaxe: mkdir (opções) diretório.
    - "-p" cria os diretórios-pai de um caminho, caso eles não existam ainda.
    - "-m" indica o modo - permissões de um diretório no momento de sua criação.

- **Comando rmdir**
    - Remove diretórios vazios. Sintaxe: rmdir (opções) diretório.
    - "rm -r" remove tudo que tem dentro da pasta e depois a pasta.

- **Comando pwd**
    - Mostra o caminho do diretório em que você está.

## Comandos de Gerenciamento de Pacotes

- **Comando apt**
    - Instala e atualiza pacotes/programas.
    - "sudo apt update", localiza todos os pacotes a serem atualizados.
    - "sudo apt list nomePacote", descobre se o pacote está instalado ou não e sua versão.
    - "sudo apt install nomePacote", instala o pacote escolhido.
    - "sudo apt remove nomePacote", remove o pacote escolhido.

- **Comando dpkg**
    - Instala o pacote escolhido que está em uma pasta (fora do repositório).

## Comandos de Processos

- **Processos e jobs**
    - Todos os programas em execução podem ser chamados de processos e são identificados por um número chamado PID (process identification).
    - Os processos podem estar em três estados diferentes: em foreground(primeiro plano), background(segundo plano) ou suspensos.

- **Comando ps**
    - Retorna uma lista dos processos em execução. Sintaxe: ps (opções).
    - "ps -a", lista todos os processos no sistema.
    - "ps -x", lista todos os processos pertencentes ao usuário
    - "ps -u", mostra o nome de usuário que iniciou o processo e hora em que o processo foi iniciado.

- **Comando top**
    - Mostra os programas em execução ativos, parados, uso de CPU, memória RAM, Swap, etc.
    - Continua em execução mostrando continuamente os processos que estão rodando em seu computador e os recursos utilizados por eles.
    - Sintaxe: top (opções).
    - Apertando "Q" encerra o top.

- **Comando jobs**
    - Mostra os processos que estão parados ou rodando em segundo plano.
    - Processos em segundo plano são iniciados usando o símbolo "&" no final da linha de comando.
    - Sintaxe: jobs (opções).

- **Comandos "fg" e "bg"**
    - Coloca um processo em foreground(fg). Sintaxe: fg (número).
    - Coloca um processo em background(bg). Sintaxe: bg (número).
    - Pode por exemplo fazer um "top" para ver o PID do processo, depois "fg/bg + PID".

- **Comando kill**
    - Encerra um processo em execução. Sintaxe: kill (opções) (sinal) (número).

## Comandos de Acesso e Permissões

- **Permissões de acesso**
    - Protegem o sistema e arquivos de acessos indevidos de pessoas ou programas não autorizados.

- **Dono**
    - É quem criou o arquivo ou diretório. É o mesmo nome do usuário que estiver logado no sistema.
    - A identificação do dono também é chamada de user id (UID).

- **Grupo**
    - Permite que vários usuários diferentes tenham acesso a um mesmo arquivo.
    - A identificação do grupo é chamada de group id (GID).

- **Tipos de permissões de acesso**
    - "r -" permissão de leitura para arquivos. Para diretórios, permite listar seu conteúdo (com comando ls, por exemplo).
    - "w -" permissão de escrita para arquivos. Para diretórios, permite a gravação de arquivos ou outros diretórios dentro dele.
    - Um arquivo/diretório só pode ser apagado se tiver permissão de escrita.
    - "x -" permite executar um arquivo (caso seja um programa executável). Para diretórios, permite que seja acessado através do comando cd.
    - Exemplo: "-rwxr-xr-- bruno users nomeArquivo". 1º caractere: diz o tipo do arquivo. Um "d" é um diretório; um "l", um link a um arquivo no sistema; um "-" é um arquivo comum. 2-4º caractere: permissões do dono do arquivo (bruno). 5-7º caractere: permissões do grupo do arquivo (users). 8-10º caractere: permissões de outros usuários ao arquivo.

- **O root (superusuário)**
    - O usuário root não tem nenhuma restrição de acesso ao sistema.
    - A conta root somente deve ser usada para fazer a administração do sistema. Além disso, deve ser usada o menor tempo possível.
    - Utilize uma conta de usuário normal em vez da conta root para operar seu sistema.

## Comandos de manipulação de diretórios

- **Comando touch**
    - Muda a data e a hora que um arquivo foi criado.
    - Também pode ser usado para criar aquivos vazios. Caso o touch seja usado com arquivos que não existam, por padrão ele criará estes arquivos.
    - Sintaxe: touch (opções) (arquivos).
    - Parâmetros:
        - "-c": não cria arquivos que não existam; por padrão, apenas o uso do touch sem argumentos faz com que arquivos inexistentes sejam criados com tamanho zero - arquivos vazios.

- **Comando nano**
    - Editor de texto. Sintaxe: nano (arquivo).
    - Além de editar o texto de um arquivo existente, ele pode criar um novo arquivo escolhendo um nome que não exista.

- **Comando cat**
    - Lista o conteúdo do arquivo. Sintaxe: cat (arquivo).
    - Também serve para concatenar arquivos.

## Compactadores de arquivos

- **Tipos:**
    - .gz - compactado pelo gzip.
    - .bzip2 - compactado pelo bzip2.
    - .tar.gz - compactado pelo gzip no utilitário de arquivamento tar.

- **Comando tar:**
    - É um arquivador, ou seja, ele junta arquivos e não compacta.
    - Pode ser usado em conjunto com o gzip para compactar e arquivar.
    - Sintaxe: tar (opções) (arquivo-destino) (arquivos-origem).
    - Opções:
        - "-c", cria um novo arquivo.
        - "-x", extrai arquivos de um arquivo compactado.
        - "-j", filtra o arquivo compactado por meio do bzip2.
        - "-z", filtra o arquivo compactado através do gzip.
        - "-t", lista o conteúdo do arquivo compactado.
        - "-f", usa o arquivo especificado para gravação
        - Exemplo: tar -cf testes.tar teste* ("teste*" seleciona todos arquivos que começam com "teste" e zipa eles).
        - Exemplo: tar -tf testes.tar (lista os arquivos zipados).
        - Exemplo: tar -czf testesCompactado.tar teste* (zipa e compacta os arquivos). Obs.: diminuiu 10 mil bytes pra mais no tamanho.

- **Comando dpkg**

    - sudo dpkg -i (nomeArquivo)
        - Instala o pacote escolhido que está em uma pasta (fora do repositório).
        - Exemplo: baixar o chrome, vai cair o pacote na pasta Downloads, no terminal digitar "sudo dpkg -i google (depois de digitar google da para apertar TAB para autocompletar o nome do pacote, se tiver outro arquivo que começam com google teria que digitar até o ponto de diferencia-los)".