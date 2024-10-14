# Caça ao Monstro

## Descrição

Caça ao Monstro é um jogo de adivinhação em que o jogador tenta capturar um monstro que se move aleatoriamente em uma grade de tamanho variável. O jogador tem um número limitado de tentativas para encontrar o monstro, e dicas sobre a proximidade do monstro são fornecidas após cada tentativa. O objetivo é capturar o monstro antes que ele escape ou as tentativas se esgotem.

## Como Instalar

1. **Clone o Repositório**:
   
   git clone https://github.com/SEU_USUARIO/caca_ao_monstro.git
   cd caca_ao_monstro
   

2. **Instale as Dependências**:
   Caso o projeto tenha dependências listadas no arquivo `requirements.txt`, instale-as com:
   
   pip install -r requirements.txt
   

## Como Jogar

1. **Inicie o Jogo**:
   Navegue até a pasta `src` e execute o jogo:
   
   cd src
   python game.py
   

2. **Escolha a Dificuldade**:
   Ao iniciar o jogo, você será solicitado a escolher a dificuldade:
   - **fácil**: Mais tentativas, o monstro demora mais para escapar.
   - **médio**: Configuração padrão.
   - **difícil**: Menos tentativas, o monstro escapa mais rápido.

3. **Escolha o Tamanho da Grade**:
   Depois de escolher a dificuldade, você poderá escolher o tamanho da grade. O tamanho mínimo é 3x3 e o máximo é 10x10.

4. **Jogue o Jogo**:
   - Digite as coordenadas da linha e coluna separadas por espaço (por exemplo, `2 3`) para tentar capturar o monstro.
   - O jogo fornecerá dicas sobre a proximidade do monstro, como "Você está muito perto!" ou "Você está longe!"
   - Continue jogando até capturar o monstro ou perder todas as suas tentativas.

## Exemplos de Jogabilidade

- **Iniciando o Jogo**:
   
   Jogo está iniciando...
   Escolha a dificuldade: fácil, médio ou difícil
   Digite a dificuldade desejada: médio
   Escolha o tamanho da grade (mínimo 3x3, máximo 10x10):
   Digite o tamanho da grade: 5
   Bem-vindo ao Caça ao Monstro! Tente capturar o monstro em até 10 tentativas.
   

- **Exemplo de Palpite**:
   
   Digite a linha e a coluna separadas por espaço: 2 3
   Você está perto!
   Tentativas restantes: 9
   

## Contribuição

Se você deseja contribuir com o projeto, siga os passos abaixo:

1. Faça um **fork** do projeto.
2. Crie uma nova **branch** para sua funcionalidade ou correção.
3. Envie um **pull request** quando sua contribuição estiver pronta.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).