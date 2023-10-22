# InstaReporter

Este é um bot simples que ajuda os usuários a denunciar em massa contas com iscas de clique ou conteúdo objetável no Instagram.

## Requisitos

Antes de usar este bot, você precisa ter o Python instalado em seu sistema. Além disso, é necessário instalar algumas bibliotecas Python. Você pode fazer isso usando o seguinte comando:

pip install webbot
Como Usar
Para usar o bot, siga estas etapas:

Clone ou faça o download deste repositório em seu computador.

Crie um arquivo chamado contas.txt no mesmo diretório do script. Este arquivo deve conter as credenciais de conta no seguinte formato:


nome_de_usuário:senha
nome_de_usuário2:senha2
Cada linha deve conter o nome de usuário e a senha de uma conta que você deseja usar para denunciar.

Execute o bot usando o seguinte comando:

python report_bot.py -u <nome_de_usuário_a_ser_denunciado>
Substitua <nome_de_usuário_a_ser_denunciado> pelo nome de usuário da conta que você deseja denunciar.

O bot irá automaticamente fazer login nas contas listadas em contas.txt e denunciar o usuário especificado.

Certifique-se de monitorar o progresso do bot e assegurar que ele está funcionando como esperado.

Quando o bot terminar, ele terá denunciado o usuário alvo usando todas as contas listadas em contas.txt.

Opções
O script oferece algumas opções:

-u, --usuario: Especifica o nome de usuário a ser denunciado (obrigatório).
-f, --arquivo: Especifica o nome do arquivo de contas (padrão é 'contas.txt' no diretório do programa).
Ajuda
Se você precisar de ajuda, execute o script com a opção -h para obter informações sobre como usá-lo:


python report_bot.py -h
Isso exibirá informações de ajuda sobre as opções disponíveis.
