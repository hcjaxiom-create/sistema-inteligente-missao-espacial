# Sistema Inteligente de Monitoramento da Colônia Espacial Aurora

Aluno: Hugo Camisotti Junior  
RM: rm570978

## Resumo do problema

As missões espaciais modernas dependem de sistemas inteligentes capazes de monitorar dados operacionais em tempo real. Durante uma missão, falhas em módulos críticos, queda de energia, aumento da radiação ou perda de comunicação podem colocar em risco a segurança da tripulação e o sucesso da operação.

Este projeto simula um sistema inteligente de monitoramento da Colônia Espacial Aurora. O sistema analisa dados de telemetria, identifica situações de risco, gera alertas automáticos e recomenda ações para manter a missão em segurança.

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

## Estruturas de dados utilizadas

O sistema utiliza diferentes estruturas de dados estudadas nas fases iniciais do curso.

### Listas

As listas foram usadas para armazenar séries de dados ao longo do tempo, como geração de energia, consumo, reserva, temperatura, radiação e qualidade da comunicação.

Exemplo:

```python
reserva_energia = [76, 70, 62, 51, 38, 28]
