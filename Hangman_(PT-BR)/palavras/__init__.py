palavras = [
    "tempo", "dia", "pessoa", "ano", "vez", "vida", "forma", "hora", "homem", "mulher",
    "trabalho", "mao", "caso", "parte", "problema", "fim", "olho", "casa", "governo", "pais",
    "grupo", "empresa", "familia", "mundo", "ponto", "cidade", "escola", "crianca", "senhor", "senhora",
    "amigo", "amiga", "jogo", "situacao", "sistema", "cabeca", "grupo", "corpo", "carro", "cidade",
    "mesa", "porta", "sala", "pe", "sistema", "coracao", "amor", "vida", "arte", "cabeca",
    "mundo", "dia", "momento", "ideia", "caminho", "razao", "proposito", "voz", "pergunta", "resposta",
    "mente", "sonho", "numero", "fato", "razao", "coisa", "amor", "vida", "pessoa", "historia",
    "mes", "senso", "motivo", "lugar", "amor", "poder", "prazer", "energia", "felicidade", "esperanca",
    "paz", "amizade", "trabalho", "sonho", "riqueza", "sabedoria", "saude", "conhecimento", "beleza", "verdade",
    "coragem", "alegria", "liberdade", "justica", "igualdade", "fe", "forca", "coragem", "amor", "caridade",
    "gratidao", "humildade", "honestidade", "lealdade", "paciencia", "perseveranca", "respeito", "solidariedade", "tolerancia", "virtude",
    "paz", "amor", "esperanca", "alegria", "coragem", "fe", "beleza", "sabedoria", "verdade", "bondade",
    "generosidade", "paciencia", "perseveranca", "respeito", "honestidade", "integridade", "humildade", "tolerancia", "solidariedade", "gratidao",
    "vida", "amor", "felicidade", "alegria", "paz", "beleza", "saude", "sucesso", "realizacao", "harmonia",
    "prosperidade", "inspiracao", "crescimento", "sabedoria", "conhecimento", "espiritualidade", "liberdade", "poder", "criatividade", "transformacao",
    "renovacao", "esperanca", "fe", "gratidao", "humildade", "generosidade", "paciencia", "respeito", "solidariedade", "gratidao",
    "conhecimento", "sabedoria", "inteligencia", "educacao", "cultura", "aprendizado", "desenvolvimento", "criatividade", "inovacao", "pensamento",
    "raciocinio", "analise", "reflexao", "curiosidade", "experimentacao", "descoberta", "exploracao", "imaginacao", "expressao", "arte",
    "musica", "literatura", "teatro", "danca", "cinema", "pintura", "escultura", "arquitetura", "design", "moda",
    "culinaria", "tecnologia", "ciencia", "natureza", "meio ambiente", "sustentabilidade", "ecologia", "cosmos", "universo", "terra",
    "agua", "ar", "fogo", "energia", "clima", "vegetacao", "animais", "minerais", "biologia", "ecossistema",
    "evolucao", "genetica", "celula", "organismo", "saude", "medicina", "doenca", "tratamento", "prevencao", "cura",
    "alimentacao", "nutricao", "exercicio", "sono", "relaxamento", "equilibrio", "bem-estar", "mente", "corpo", "espirito",
    "emocao", "sentimento", "pensamento", "consciencia", "autoconhecimento", "autoestima", "autoconfianca", "autocontrole", "autodomínio", "autocuidado",
    "autossuficiencia", "autenticidade", "autodesenvolvimento", "autorealizacao", "autoaperfeicoamento", "autotransformacao", "autolibertacao", "autogratidao", "autocompaixao", "autocompreensao",
    "autotranscendencia", "autossuperacao", "autodisciplina", "autodeterminacao", "autoexpressao", "autoafirmacao", "autovalorizacao", "autonomia", "autoresponsabilidade", "autocoaching",
    "autoinspiracao", "autocrenca", "autoreflecao", "autoaceitacao", "autoperdao", "autotolerancia", "autogenerosidade", "autossolidariedade", "autocompreensao", "autoconsciencia",
    "cultura", "heranca", "patrimonio", "tradicao", "folclore", "ritual", "cerimonia", "ritmo", "melodia", "harmonia",
    "instrumento", "pintor", "escultor", "escritor", "poeta", "autor", "obra", "capitulo", "pagina", "verso",
    "ensaio", "conceito", "teoria", "hipotese", "experimento", "resultado", "conclusao", "descobridor", "inventor", "criador",
    "inovacao", "descoberta", "exploracao", "curiosidade", "viagem", "aventura", "descanso", "lazer", "diversao", "brincadeira",
    "passatempo", "entretenimento", "esporte", "competicao", "vitoria", "derrota", "campeao", "torneio", "evento", "espetaculo",
    "apresentacao", "performance", "ato", "cena", "papel", "personagem", "protagonista", "antagonista", "figura", "imagem",
    "foto", "quadro", "retrato", "paisagem", "paisagem", "ambiente", "atmosfera", "clima", "temperatura", "pressao",
    "vento", "chuva", "sol", "lua", "estrela", "galaxia", "planeta", "satelite", "orbita", "gravidade",
    "materia", "energia", "atomo", "molecula", "substancia", "composto", "reagente", "produto", "elemento", "ligacao",
    "reacao", "equacao", "processo", "experiencia", "procedimento", "operacao", "calculo", "formula", "numero", "quantidade",
    "unidade", "medida", "escala", "grandeza", "magnitude", "dimensao", "extensao", "tamanho", "volume", "massa",
    "densidade", "forma", "estrutura", "organizacao", "sistema", "modelo", "teoria", "lei", "principio", "conceito",
    "definicao", "interpretacao", "analise", "sintese", "abstracao", "generalizacao", "especificacao", "classificacao", "categorizacao",
    "padrao", "norma", "criterio", "valor", "etica", "moral", "etica", "filosofia", "religiao", "crenca",
    "ritual", "deidade", "divindade", "culto", "adoracao", "oracao", "prece", "fe", "espiritualidade", "iluminacao",
    "conhecimento", "sabedoria", "inteligencia", "educacao", "aprendizado", "desenvolvimento", "inovacao", "descoberta", "exploracao", "conquista",
    "aventura", "jornada", "missao", "proposito", "objetivo", "meta", "destino", "rota", "trajetoria", "caminho",
    "passo", "movimento", "acao", "iniciativa", "projeto", "plano", "estrategia", "tatica", "manobra", "operacao",
    "execucao", "realizacao", "conclusao", "resultado", "exito", "sucesso", "fracasso", "derrota", "obstaculo", "desafio",
    "dificuldade", "problema", "solucao", "estrategia", "tatica", "acao", "reacao", "iniciativa", "resposta", "resultado",
    "consequencia", "efeito", "impacto", "influencia", "transformacao", "mudanca", "evolucao", "progresso", "crescimento", "desenvolvimento",
    "aprimoramento", "melhoria", "aperfeicoamento", "inovacao", "descoberta", "exploracao", "curiosidade", "viagem", "aventura", "descanso",
    "lazer", "diversao", "brincadeira", "passatempo", "entretenimento", "esporte", "competicao", "vitoria", "derrota", "campeao",
    "torneio", "evento", "espetaculo", "apresentacao", "performance", "ato", "cena", "papel", "personagem", "protagonista",
    "antagonista", "figura", "imagem", "foto", "quadro", "retrato", "paisagem", "ambiente", "atmosfera", "clima",
    "temperatura", "pressao", "vento", "chuva", "sol", "lua", "estrela", "galaxia", "planeta", "satelite",
    "orbita", "gravidade", "materia", "energia", "atomo", "molecula", "substancia", "composto", "reagente", "produto",
    "elemento", "ligacao", "reacao", "equacao", "processo", "experiencia", "procedimento", "operacao", "calculo", "formula",
    "numero", "quantidade", "unidade", "medida", "escala", "grandeza", "magnitude", "dimensao", "extensao", "tamanho",
    "volume", "massa", "densidade", "forma", "estrutura", "organizacao", "sistema", "modelo", "teoria", "lei",
    "principio", "conceito", "definicao", "interpretacao", "analise", "sintese", "abstracao", "generalizacao", "especificacao", "classificacao",
    "categorizacao", "padrao", "norma", "criterio", "valor", "etica", "moral", "etica", "filosofia", "religiao",
    "crenca", "ritual", "deidade", "divindade", "culto", "adoracao", "oracao", "prece", "fe", "espiritualidade",
    "iluminacao"
]
