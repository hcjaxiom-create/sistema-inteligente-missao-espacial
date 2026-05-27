# ==========================================================
# SISTEMA INTELIGENTE DE MONITORAMENTO DA COLÔNIA ESPACIAL AURORA
# ==========================================================

# Nome do projeto
nome_projeto = "Sistema Inteligente de Monitoramento da Colônia Espacial Aurora"


# ==========================================================
# 1. DADOS SIMULADOS DA MISSÃO
# ==========================================================

# Módulos críticos da missão
# 1 = funcionando
# 0 = falha
modulos = {
    "suporte_vida": 1,
    "energia": 1,
    "comunicacao": 0,
    "habitat": 1,
    "laboratorio": 1,
    "armazenamento": 1
}

# Listas com dados de telemetria
horarios = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00"]

geracao_energia = [85, 80, 72, 60, 48, 35]
consumo_energia = [70, 75, 82, 88, 92, 96]
reserva_energia = [76, 70, 62, 51, 38, 28]
temperatura_interna = [22, 23, 24, 25, 27, 29]
radiacao = [15, 18, 22, 35, 48, 65]
qualidade_comunicacao = [95, 90, 85, 70, 55, 40]

# Log com eventos da missão
log_eventos = [
    "08:00 - Sistemas iniciados normalmente",
    "10:00 - Pequena queda na geração de energia",
    "12:00 - Consumo ultrapassou a geração de energia",
    "14:00 - Radiação começou a aumentar",
    "16:00 - Reserva de energia abaixo de 40%",
    "17:00 - Comunicação apresentou instabilidade",
    "18:00 - Módulo de comunicação marcado como falha",
    "18:10 - Sistema entrou em modo de economia de energia"
]


# ==========================================================
# 2. ORGANIZAÇÃO DOS DADOS
# ==========================================================

# Dicionário para acesso rápido aos módulos
status_modulos = modulos

# Fila de alertas pendentes
fila_alertas = []

# Pilha de eventos críticos
pilha_eventos_criticos = []

# Hierarquia da missão
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

# Matriz de leituras
matriz_leituras = []

for i in range(len(horarios)):
    linha = [
        horarios[i],
        geracao_energia[i],
        consumo_energia[i],
        reserva_energia[i],
        temperatura_interna[i],
        radiacao[i],
        qualidade_comunicacao[i]
    ]
    matriz_leituras.append(linha)

# Registrando eventos críticos em uma pilha
for evento in log_eventos:
    if "falha" in evento.lower() or "abaixo" in evento.lower() or "instabilidade" in evento.lower():
        pilha_eventos_criticos.append(evento)


# ==========================================================
# 3. FUNÇÕES DO SISTEMA
# ==========================================================

def adicionar_alerta(severidade, mensagem, recomendacao):
    """
    Adiciona um alerta na fila de alertas.
    """
    alerta = {
        "severidade": severidade,
        "mensagem": mensagem,
        "recomendacao": recomendacao
    }
    fila_alertas.append(alerta)


def prever_reserva_energia(reservas):
    """
    Realiza uma previsão simples por extrapolação de tendência.
    Usa os dois últimos valores da reserva de energia.
    """
    reserva_penultima = reservas[-2]
    reserva_ultima = reservas[-1]

    variacao = reserva_ultima - reserva_penultima
    previsao = reserva_ultima + variacao

    if previsao < 0:
        previsao = 0

    return previsao, variacao


def diagnosticar_missao():
    """
    Analisa os dados mais recentes e classifica a missão.
    """
    ultima_geracao = geracao_energia[-1]
    ultimo_consumo = consumo_energia[-1]
    ultima_reserva = reserva_energia[-1]
    ultima_temperatura = temperatura_interna[-1]
    ultima_radiacao = radiacao[-1]
    ultima_comunicacao = qualidade_comunicacao[-1]

    suporte_vida = modulos["suporte_vida"]
    energia = modulos["energia"]
    comunicacao = modulos["comunicacao"]
    habitat = modulos["habitat"]

    status_missao = "NORMAL"
    motivos = []

    # Regra 1 - Suporte à vida
    if not suporte_vida:
        status_missao = "CRÍTICA"
        motivos.append("Falha no suporte à vida.")

    # Regra 2 - Energia crítica
    if ultima_reserva < 30 and ultimo_consumo > ultima_geracao:
        status_missao = "CRÍTICA"
        motivos.append("Reserva de energia abaixo de 30% e consumo maior que a geração.")

    # Regra 3 - Comunicação comprometida
    if comunicacao == 0 or ultima_comunicacao < 50:
        if status_missao != "CRÍTICA":
            status_missao = "ALERTA"
        motivos.append("Comunicação comprometida ou qualidade de comunicação abaixo de 50%.")

    # Regra 4 - Risco ambiental
    if ultima_radiacao > 50 and ultima_temperatura > 28:
        status_missao = "CRÍTICA"
        motivos.append("Radiação elevada combinada com temperatura interna alta.")

    # Regra 5 - Falha em sistemas essenciais
    if energia == 0 or habitat == 0:
        status_missao = "CRÍTICA"
        motivos.append("Falha em módulo essencial de energia ou habitat.")

    # Regra 6 - Alerta preventivo
    if ultima_reserva < 40 and ultima_radiacao > 40:
        if status_missao != "CRÍTICA":
            status_missao = "ALERTA"
        motivos.append("Reserva de energia baixa e radiação acima do nível seguro.")

    return status_missao, motivos


def gerar_alertas():
    """
    Gera alertas automáticos e recomendações.
    """
    ultima_geracao = geracao_energia[-1]
    ultimo_consumo = consumo_energia[-1]
    ultima_reserva = reserva_energia[-1]
    ultima_temperatura = temperatura_interna[-1]
    ultima_radiacao = radiacao[-1]
    ultima_comunicacao = qualidade_comunicacao[-1]
    comunicacao = modulos["comunicacao"]
    suporte_vida = modulos["suporte_vida"]

    if ultima_reserva < 30 and ultimo_consumo > ultima_geracao:
        adicionar_alerta(
            "CRÍTICO",
            "Reserva de energia abaixo de 30% e consumo maior que a geração.",
            "Ativar modo de economia, desligar laboratório e priorizar suporte à vida e habitat."
        )

    if comunicacao == 0 or ultima_comunicacao < 50:
        adicionar_alerta(
            "ALERTA",
            "Sistema de comunicação comprometido.",
            "Ativar antena de emergência e reduzir transmissões não essenciais."
        )

    if ultima_radiacao > 50:
        adicionar_alerta(
            "CRÍTICO",
            "Nível de radiação acima do limite seguro.",
            "Transferir tripulação para área protegida e suspender atividades externas."
        )

    if ultima_temperatura > 28:
        adicionar_alerta(
            "ALERTA",
            "Temperatura interna acima do nível ideal.",
            "Ajustar controle térmico do habitat e verificar sistema de refrigeração."
        )

    if not suporte_vida:
        adicionar_alerta(
            "CRÍTICO",
            "Falha no suporte à vida.",
            "Acionar sistema reserva de oxigênio e iniciar protocolo de emergência."
        )

    # Inconsistência proposital nos dados
    if comunicacao == 0 and ultima_comunicacao > 0:
        adicionar_alerta(
            "ALERTA",
            "Inconsistência detectada: módulo de comunicação indica falha, mas ainda há leitura de qualidade de comunicação.",
            "Verificar sensores de comunicação e validar os dados manualmente."
        )


def exibir_resumo():
    """
    Exibe o resumo final do sistema.
    """
    status_missao, motivos = diagnosticar_missao()
    gerar_alertas()

    previsao_reserva, variacao_reserva = prever_reserva_energia(reserva_energia)

    alertas_criticos = []
    alertas_atencao = []

    for alerta in fila_alertas:
        if alerta["severidade"] == "CRÍTICO":
            alertas_criticos.append(alerta)
        elif alerta["severidade"] == "ALERTA":
            alertas_atencao.append(alerta)

    print("=" * 60)
    print("SISTEMA INTELIGENTE DE MONITORAMENTO")
    print("=" * 60)

    print("\nProjeto:")
    print(nome_projeto)

    print("\nStatus final da missão:")
    print(status_missao)

    print("\nMotivos do diagnóstico:")
    if len(motivos) > 0:
        for motivo in motivos:
            print("-", motivo)
    else:
        print("- Nenhum risco identificado.")

    print("\nMódulos críticos:")
    for modulo, status in modulos.items():
        if status == 1:
            print("-", modulo, ": Funcionando")
        else:
            print("-", modulo, ": Falha")

    print("\nMatriz de leituras:")
    print("Horário | Geração | Consumo | Reserva | Temperatura | Radiação | Comunicação")
    for linha in matriz_leituras:
        print(linha)

    print("\nPilha de eventos críticos:")
    for evento in pilha_eventos_criticos:
        print("-", evento)

    print("\nAlertas críticos:")
    if len(alertas_criticos) > 0:
        for alerta in alertas_criticos:
            print("\nSeveridade:", alerta["severidade"])
            print("Mensagem:", alerta["mensagem"])
            print("Recomendação:", alerta["recomendacao"])
    else:
        print("Nenhum alerta crítico.")

    print("\nAlertas de atenção:")
    if len(alertas_atencao) > 0:
        for alerta in alertas_atencao:
            print("\nSeveridade:", alerta["severidade"])
            print("Mensagem:", alerta["mensagem"])
            print("Recomendação:", alerta["recomendacao"])
    else:
        print("Nenhum alerta de atenção.")

    print("\nPrevisão de energia:")
    print("Última reserva:", reserva_energia[-1], "%")
    print("Variação observada:", variacao_reserva, "pontos percentuais")
    print("Previsão para o próximo ciclo:", previsao_reserva, "%")

    print("\nRecomendação final:")
    if status_missao == "CRÍTICA":
        print("Ativar protocolo de emergência, reduzir consumo e priorizar suporte à vida, habitat e comunicação.")
    elif status_missao == "ALERTA":
        print("Manter monitoramento contínuo e corrigir pontos de risco.")
    else:
        print("Manter operação normal.")

    print("\nConclusão:")
    print("O sistema organizou dados simulados, aplicou regras lógicas, gerou alertas, identificou inconsistências e realizou uma previsão simples da reserva de energia.")


# ==========================================================
# 4. EXECUÇÃO DO SISTEMA
# ==========================================================

exibir_resumo()
