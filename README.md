# Sistema Inteligente de Monitoramento da Colônia Espacial Aurora

## Axiom Hcj

Aluno: Hugo Camisotti Junior  
RM: rm570978

---

## Resumo do problema

As missões espaciais modernas dependem de sistemas inteligentes capazes de monitorar dados operacionais em tempo real. Durante uma missão, falhas em módulos críticos, queda de energia, aumento da radiação ou perda de comunicação podem colocar em risco a segurança da tripulação e o sucesso da operação.

Este projeto simula um sistema inteligente de monitoramento da Colônia Espacial Aurora. O sistema analisa dados de telemetria, identifica situações de risco, gera alertas automáticos e recomenda ações para manter a missão em segurança.

---

## Cenário analisado

A Colônia Espacial Aurora é uma missão experimental fora da Terra. Para manter a operação segura, foram monitorados módulos e variáveis essenciais, como:

- suporte à vida;
- energia;
- comunicação;
- habitat;
- laboratório;
- armazenamento;
- geração de energia;
- consumo de energia;
- reserva de energia;
- temperatura interna;
- radiação;
- qualidade de comunicação.

---

## Estruturas de dados utilizadas

O sistema utiliza diferentes estruturas de dados estudadas nas fases iniciais do curso.

### Listas

As listas foram usadas para armazenar séries de dados ao longo do tempo, como geração de energia, consumo de energia, reserva de energia, temperatura interna, radiação e qualidade da comunicação.

Exemplo:

    reserva_energia = [76, 70, 62, 51, 38, 28]

### Dicionários

Os dicionários foram utilizados para acessar rapidamente o status dos módulos críticos da missão.

Exemplo:

    modulos = {
        "suporte_vida": 1,
        "energia": 1,
        "comunicacao": 0,
        "habitat": 1,
        "laboratorio": 1,
        "armazenamento": 1
    }

### Fila

A fila foi utilizada para armazenar os alertas gerados pelo sistema. Cada alerta é inserido na fila conforme uma condição de risco é identificada.

Exemplo:

    fila_alertas = []

### Pilha

A pilha foi utilizada para registrar os eventos críticos da missão, como falhas, instabilidades ou baixa reserva de energia.

Exemplo:

    pilha_eventos_criticos = []

### Hierarquia

A hierarquia foi usada para representar sistemas e subsistemas da missão, como energia, habitat e comunicação.

Exemplo:

    hierarquia_missao = {
        "energia": {
            "solar": "painéis solares principais",
            "baterias": "banco de baterias de reserva",
            "distribuicao": "controle de distribuição de energia"
        },
        "habitat": {
            "oxigenio": "controle de oxigênio",
            "temperatura": "controle térmico interno",
            "pressurizacao": "controle de pressão interna"
        },
        "comunicacao": {
            "antena_principal": "comunicação com a base",
            "antena_emergencia": "canal reserva de comunicação"
        }
    }

### Matriz

A matriz foi usada para organizar as leituras por horário. Cada linha representa um horário da missão e cada coluna representa uma variável monitorada.

Exemplo:

    matriz_leituras = [
        ["08:00", 85, 70, 76, 22, 15, 95],
        ["10:00", 80, 75, 70, 23, 18, 90]
    ]

---

## Regras lógicas principais

O sistema utiliza regras com `if`, `elif`, `else` e operadores lógicos como `and`, `or` e `not`.

A expressão booleana principal do diagnóstico é:

    Situação crítica =
    (suporte_vida == 0) OR
    (reserva_energia < 30 AND consumo_energia > geracao_energia) OR
    (radiacao > 50 AND temperatura_interna > 28)

Em linguagem simples, a missão será considerada crítica se:

- o suporte à vida falhar;
- a reserva de energia estiver abaixo de 30% e o consumo for maior que a geração;
- a radiação estiver elevada e a temperatura interna também estiver alta.

Exemplo no código:

    if ultima_reserva < 30 and ultimo_consumo > ultima_geracao:
        status_missao = "CRÍTICA"

    if comunicacao == 0 or ultima_comunicacao < 50:
        status_missao = "ALERTA"

    if not suporte_vida:
        status_missao = "CRÍTICA"

---

## Técnica de previsão utilizada

A técnica de previsão utilizada foi a extrapolação de tendência.

O sistema analisa os dois últimos valores da reserva de energia, calcula a variação entre eles e projeta essa mesma variação para o próximo ciclo.

Exemplo:

    Penúltima reserva: 38%
    Última reserva: 28%
    Variação: -10 pontos percentuais
    Previsão para o próximo ciclo: 18%

Com isso, o sistema identifica que a reserva pode cair para um nível crítico e recomenda a redução imediata do consumo.

---

## Alertas e recomendações

O sistema gera alertas automáticos classificados em:

- NORMAL;
- ALERTA;
- CRÍTICO.

Exemplos de alertas gerados:

    CRÍTICO: Reserva de energia abaixo de 30% e consumo maior que a geração.
    Recomendação: Ativar modo de economia, desligar laboratório e priorizar suporte à vida e habitat.

    ALERTA: Sistema de comunicação comprometido.
    Recomendação: Ativar antena de emergência e reduzir transmissões não essenciais.

    CRÍTICO: Nível de radiação acima do limite seguro.
    Recomendação: Transferir tripulação para área protegida e suspender atividades externas.

---

## Inconsistência proposital nos dados

Foi incluída uma inconsistência proposital para testar a capacidade de diagnóstico do sistema.

O módulo de comunicação foi marcado como falha:

    "comunicacao": 0

Porém, ainda existe uma leitura de qualidade de comunicação:

    qualidade_comunicacao = 40%

Essa inconsistência gera um alerta para que os sensores sejam verificados manualmente.

---

## Como executar o projeto

Para executar o sistema, use o comando:

    python src/sistema.py

O programa exibirá no terminal:

- status final da missão;
- motivos do diagnóstico;
- módulos críticos;
- matriz de leituras;
- eventos críticos;
- alertas automáticos;
- previsão da reserva de energia;
- recomendação final.

---

## Exemplo de entrada

Os dados simulados estão no arquivo:

    data/dados.csv

Exemplo:

    horario,geracao_energia,consumo_energia,reserva_energia,temperatura_interna,radiacao,qualidade_comunicacao
    08:00,85,70,76,22,15,95
    10:00,80,75,70,23,18,90
    12:00,72,82,62,24,22,85
    14:00,60,88,51,25,35,70
    16:00,48,92,38,27,48,55
    18:00,35,96,28,29,65,40

---

## Exemplo de saída

    ============================================================
    SISTEMA INTELIGENTE DE MONITORAMENTO
    ============================================================

    Projeto:
    Sistema Inteligente de Monitoramento da Colônia Espacial Aurora

    Status final da missão:
    CRÍTICA

    Motivos do diagnóstico:
    - Reserva de energia abaixo de 30% e consumo maior que a geração.
    - Comunicação comprometida ou qualidade de comunicação abaixo de 50%.
    - Radiação elevada combinada com temperatura interna alta.
    - Reserva de energia baixa e radiação acima do nível seguro.

    Previsão de energia:
    Última reserva: 28 %
    Variação observada: -10 pontos percentuais
    Previsão para o próximo ciclo: 18 %

    Recomendação final:
    Ativar protocolo de emergência, reduzir consumo e priorizar suporte à vida, habitat e comunicação.

---

## Link do vídeo

Inserir aqui o link do vídeo no YouTube como "Não listado".

---

## Conclusões e aprendizados

O projeto demonstrou como conceitos básicos de programação podem ser aplicados em um cenário realista de monitoramento espacial.

Foram utilizados dados simulados, estruturas de dados, regras lógicas, alertas automáticos e previsão simples para apoiar decisões operacionais.

Com isso, o sistema mostra como a computação pode contribuir para segurança, análise de riscos e tomada de decisão em missões críticas.
