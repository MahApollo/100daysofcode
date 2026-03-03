from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# ── Margens ──────────────────────────────────────────────────────────────
for section in doc.sections:
    section.top_margin    = Cm(3)
    section.bottom_margin = Cm(2)
    section.left_margin   = Cm(3)
    section.right_margin  = Cm(2)

# ── Estilos base ─────────────────────────────────────────────────────────
styles = doc.styles

# Corpo do texto
normal = styles['Normal']
normal.font.name = 'Times New Roman'
normal.font.size = Pt(12)
normal.paragraph_format.space_after  = Pt(6)
normal.paragraph_format.line_spacing = Pt(24)  # 2x
normal.paragraph_format.alignment    = WD_ALIGN_PARAGRAPH.JUSTIFY

def set_font(style, name='Times New Roman', size=12, bold=False, color=None):
    style.font.name = name
    style.font.size = Pt(size)
    style.font.bold = bold
    if color:
        style.font.color.rgb = RGBColor(*color)

# Heading 1
h1 = styles['Heading 1']
set_font(h1, size=14, bold=True, color=(0,0,0))
h1.paragraph_format.space_before = Pt(18)
h1.paragraph_format.space_after  = Pt(6)
h1.paragraph_format.alignment    = WD_ALIGN_PARAGRAPH.CENTER

# Heading 2
h2 = styles['Heading 2']
set_font(h2, size=13, bold=True, color=(0,0,0))
h2.paragraph_format.space_before = Pt(14)
h2.paragraph_format.space_after  = Pt(4)

# Heading 3
h3 = styles['Heading 3']
set_font(h3, size=12, bold=True, color=(0,0,0))
h3.paragraph_format.space_before = Pt(10)
h3.paragraph_format.space_after  = Pt(2)

# ── Helpers ───────────────────────────────────────────────────────────────
def h(level, text):
    p = doc.add_heading(text, level=level)
    # garantir fonte correta nos runs
    for run in p.runs:
        run.font.name = 'Times New Roman'
        run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def body(text, first_indent=False):
    p = doc.add_paragraph(text)
    p.style = doc.styles['Normal']
    if first_indent:
        p.paragraph_format.first_line_indent = Cm(1.25)
    return p

def bold_body(label, rest):
    p = doc.add_paragraph()
    p.style = doc.styles['Normal']
    run = p.add_run(label)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    r2 = p.add_run(rest)
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(12)
    return p

def bullet(text, level=0):
    p = doc.add_paragraph(text, style='List Bullet')
    p.paragraph_format.left_indent = Cm(1.25 + level * 0.63)
    for run in p.runs:
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)
    return p

def ref(text):
    p = doc.add_paragraph()
    p.style = doc.styles['Normal']
    p.paragraph_format.first_line_indent = Cm(-1.25)
    p.paragraph_format.left_indent       = Cm(1.25)
    p.paragraph_format.space_after       = Pt(4)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    return p

def separator():
    doc.add_paragraph()

# ═══════════════════════════════════════════════════════════════════════════
# CAPA / TÍTULO
# ═══════════════════════════════════════════════════════════════════════════
h(1, 'Revisão da Literatura sobre o Jesus Histórico:\nEstado da Arte na Pesquisa Contemporânea')

p = doc.add_paragraph('Revisão Bibliográfica Sistemática — 2015–2026')
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.runs[0].font.name = 'Times New Roman'
p.runs[0].font.size = Pt(11)
p.runs[0].italic = True

doc.add_page_break()

# ═══════════════════════════════════════════════════════════════════════════
# 1. INTRODUÇÃO
# ═══════════════════════════════════════════════════════════════════════════
h(1, '1. Introdução')

body(
    'A pesquisa sobre o Jesus Histórico constitui um dos campos mais fecundos, '
    'metodologicamente disputados e interdisciplinarmente ricos das ciências humanas e '
    'religiosas. Situada na confluência da teologia, história, sociologia, antropologia e '
    'filosofia, essa área mobiliza, desde os séculos XVIII e XIX, gerações de estudiosos '
    'que buscam reconstituir, com rigor crítico, a figura do pregador galileu que deu '
    'origem ao movimento cristão. O debate não é meramente erudito: as conclusões sobre '
    'quem foi Jesus de Nazaré possuem implicações profundas para a teologia cristã, para '
    'o diálogo inter-religioso, para a compreensão da história do Mediterrâneo antigo e, '
    'cada vez mais, para questões de classe, gênero e etnia que perpassam o presente.',
    first_indent=True)

body(
    'Nas últimas duas décadas, o campo passou por transformações substanciais. O '
    'esgotamento relativo das ferramentas metodológicas herdadas do século XX — '
    'especialmente os chamados "critérios de autenticidade" — abriu espaço para '
    'abordagens inovadoras: a teoria da memória social, a leitura materialista histórica, '
    'a arqueologia galiliana integrada, as hermenêuticas feministas e pós-coloniais, e um '
    'chamado à renovação denominado por alguns estudiosos de "Próxima Busca" (Next Quest). '
    'O presente trabalho oferece uma revisão sistemática da literatura especializada '
    'produzida predominantemente entre 2015 e 2026, articulando os principais debates, '
    'metodologias, descobertas e lacunas que definem o estado da arte da pesquisa sobre '
    'o Jesus Histórico.',
    first_indent=True)

# ═══════════════════════════════════════════════════════════════════════════
# 2. PANORAMA HISTÓRICO DAS "QUESTS"
# ═══════════════════════════════════════════════════════════════════════════
h(1, '2. Panorama Histórico das "Quests"')

h(2, '2.1 A Primeira Busca (séc. XVIII – início do séc. XX)')
body(
    'O ponto inaugural convencional da pesquisa histórico-crítica sobre Jesus é Herman '
    'Samuel Reimarus (1694–1768), cujos fragmentos póstumos, publicados por Gotthold '
    'Ephraim Lessing entre 1774 e 1778, propuseram uma separação radical entre o Jesus '
    'da história e o Cristo da fé. Para Reimarus, Jesus era um reformador judeu '
    'apocalíptico cujo projeto fracassou na cruz, e a ressurreição era uma invenção de '
    'seus discípulos. A crítica de Albert Schweitzer em Von Reimarus zu Wrede (1906) — '
    'traduzida ao inglês como The Quest of the Historical Jesus — encerrou a Primeira '
    'Busca ao demonstrar que cada estudioso havia, inadvertidamente, projetado seu próprio '
    'ideal cultural sobre a figura de Jesus. Para Schweitzer, o Jesus autêntico era um '
    'profeta apocalíptico judeu inteiramente estranho à sensibilidade moderna.',
    first_indent=True)

h(2, '2.2 O Período de "Nenhuma Busca" (1906–1953)')
body(
    'A crítica de Schweitzer, combinada com o advento da crítica das formas '
    '(Formgeschichte) promovida por Martin Dibelius e Rudolf Bultmann nas décadas de '
    '1920 e 1930, levou a um período de desconfiança profunda em relação à possibilidade '
    'de conhecer o Jesus da história. Para Bultmann, os evangelhos eram documentos de fé '
    'comunitária, não registros biográficos, e o kerygma (a proclamação teológica) era a '
    'única coisa historicamente acessível. O Jesus histórico tornava-se metodologicamente '
    'inacessível — e, para Bultmann, teologicamente irrelevante.',
    first_indent=True)

h(2, '2.3 A Segunda Busca (1953–c. 1980)')
body(
    'Em 1953, Ernst Käsemann, discípulo de Bultmann, inaugura a Segunda Busca em sua '
    'famosa palestra "O Problema do Jesus Histórico", defendendo que alguma continuidade '
    'histórica entre Jesus e o Cristo pregado era teologicamente necessária. Günther '
    'Bornkamm, com Jesus von Nazareth (1956), e outros estudiosos retomaram a pesquisa, '
    'mas ainda muito dependentes do critério da dissimilaridade — segundo o qual seria '
    'autêntico apenas o que fosse distinto tanto do judaísmo contemporâneo quanto da '
    'Igreja primitiva.',
    first_indent=True)

h(2, '2.4 A Terceira Busca (c. 1980 – início dos anos 2010)')
body(
    'O rótulo "Terceira Busca" (Third Quest) é atribuído ao teólogo escocês Stephen '
    'Neill, popularizado por N.T. Wright. A Terceira Busca distingue-se das anteriores '
    'por sua ênfase no judaísmo do Segundo Templo como contexto incontornável para '
    'compreender Jesus. Seus protagonistas incluem E.P. Sanders (Jesus and Judaism, '
    '1985), Gerd Theissen, Paula Fredriksen, John P. Meier (com sua monumental série A '
    'Marginal Jew, 5 vols., 1991–2016), N.T. Wright, James D.G. Dunn, Richard Bauckham '
    'e Bart Ehrman. Pela primeira vez, estudiosos judeus, mulheres, latinos e africanos '
    'integram-se de forma significativa ao debate.',
    first_indent=True)
body(
    'Dentro da Terceira Busca, subsistem tensões profundas. O Jesus Seminar de Robert '
    'Funk e John Dominic Crossan — com seu método de votação por esferas coloridas — foi '
    'amplamente criticado por desnudar Jesus de seu caráter apocalíptico judaico. A '
    'principal tensão interna permanece: Jesus era um profeta apocalíptico (Ehrman, '
    'Sanders, Allison, Fredriksen) ou um mestre da sabedoria não-apocalíptico (Crossan, '
    'Borg)?',
    first_indent=True)

h(2, '2.5 A "Próxima Busca" (Next Quest): O Debate Atual')
body(
    'Em 2021, James Crossley publicou no Journal for the Study of the Historical Jesus '
    'o artigo programático "The Next Quest for the Historical Jesus". Em 2024, Crossley '
    'e Chris Keith editaram o volume coletivo The Next Quest for the Historical Jesus '
    '(Eerdmans, 2024), reunindo dezenas de especialistas internacionais. O ponto de '
    'ruptura é metodológico e ideológico: o Next Quest abandona a obsessão com os '
    'critérios de autenticidade, a ênfase excessiva na unicidade de Jesus em relação ao '
    'judaísmo (que frequentemente reproduzia supersessionismo implícito) e o eurocentrismo '
    'da pesquisa anterior. Em seu lugar, propõe abordagens baseadas em memória social, '
    'história das classes, comparação intercultural, arqueologia material e perspectivas '
    'de gênero, raça e deficiência. O volume foi descrito na Review of Biblical Literature '
    'como um "momento pivô na erudição sobre o Jesus histórico."',
    first_indent=True)

# ═══════════════════════════════════════════════════════════════════════════
# 3. ABORDAGENS TEOLÓGICAS CONTEMPORÂNEAS
# ═══════════════════════════════════════════════════════════════════════════
h(1, '3. Abordagens Teológicas Contemporâneas')

h(2, '3.1 N.T. Wright e a Theologia Crucis Historicamente Fundamentada')
body(
    'Nicholas Thomas Wright é um dos mais prolíficos e influentes estudiosos do Jesus '
    'Histórico nas décadas recentes. Em Jesus and the Victory of God (1996), Wright '
    'argumenta que Jesus compreendeu sua missão à luz das narrativas proféticas de '
    'Israel: o exílio não havia terminado, e Jesus se via como o agente da nova criação '
    'e do retorno de YHWH a Sião. Wright rejeita a leitura apocalíptica no sentido de um '
    'fim literal do cosmos, propondo que a linguagem do fim-dos-tempos é metáfora '
    'profética para eventos históricos de magnitude universal.',
    first_indent=True)
body(
    'Em The Resurrection of the Son of God (2003), Wright sustenta que a ressurreição '
    'corporal de Jesus é a melhor explicação histórica para o surgimento do movimento '
    'cristão primitivo. Seu argumento é duplo: (a) anastasis no judaísmo do Segundo '
    'Templo significava vida corporal renovada, não imortalidade da alma; (b) nem o '
    'túmulo vazio nem as aparições, isoladamente, seriam suficientes para gerar as '
    'afirmações cristológicas primitivas — apenas a combinação de ambos explica os dados.',
    first_indent=True)

h(2, '3.2 John P. Meier e o Método da "Comissão de Experts Fictícios"')
body(
    'John P. Meier (1942–2022), em A Marginal Jew: Rethinking the Historical Jesus '
    '(Yale University Press, 5 vols., 1991–2016), parte de um experimento mental: o '
    'que concluiria uma "comissão de experts fictícios" — um exegeta católico, um '
    'protestante, um judeu e um agnóstico — forçados a chegar a um consenso sobre o que '
    'é historicamente verificável sobre Jesus? Os critérios que Meier articula — embaraço, '
    'atestação múltipla, coerência, descontinuidade relativa e rejeição-execução — '
    'tornaram-se referência padrão, embora também alvo das críticas mais severas da '
    'geração seguinte.',
    first_indent=True)
body(
    'O Volume 5 (2016), dedicado à autenticidade das parábolas, é o mais polêmico: '
    'Meier questiona a presunção quase universal de que as parábolas sinóticas são ipso '
    'facto palavras do Jesus histórico, concluindo que apenas quatro — Semente de '
    'Mostarda, Arrendatários Violentos, Talentos e Grande Banquete — passam nos seus '
    'critérios de autenticidade.',
    first_indent=True)

h(2, '3.3 Paula Fredriksen e o Jesus Judeu de Nazaré')
body(
    'Paula Fredriksen (Boston University / Hebrew University de Jerusalém), em Jesus of '
    'Nazareth, King of the Jews (1999, Prêmio Nacional do Livro Judaico), argumenta que '
    'a chave para compreender a crucificação de Jesus reside no paradoxo: seus seguidores '
    'não foram crucificados com ele. Isso indica que Pilatos não o via como um verdadeiro '
    'líder político de uma revolta, mas como um profeta cujo seguimento era '
    'temporariamente perigoso. Em When Christians Were Jews (2018), Fredriksen situa o '
    'movimento de Jesus dentro do mosaico de messianismos judeus do período, reforçando '
    'que a identidade judaica de Jesus é constitutiva, não periférica.',
    first_indent=True)

h(2, '3.4 Bart Ehrman e o Jesus como Profeta Apocalíptico Fracassado')
body(
    'Bart Ehrman (University of North Carolina), em Jesus: Apocalyptic Prophet of the '
    'New Millennium (1999), Did Jesus Exist? (2012) e Jesus Before the Gospels (2016), '
    'sustenta que Jesus era um profeta apocalíptico judeu cujas predições sobre o fim '
    'iminente do sistema presente falharam — o "Filho do Homem" não veio. Ehrman também '
    'argumenta que o historiador, enquanto tal, não pode afirmar que um milagre ocorreu, '
    'dado que o método histórico opera com probabilidades e os milagres são, por '
    'definição, eventos de probabilidade mínima.',
    first_indent=True)

h(2, '3.5 Richard Bauckham e o Jesus das Testemunhas Oculares')
body(
    'Richard Bauckham, em Jesus and the Eyewitnesses: The Gospels as Eyewitness '
    'Testimony (2006; 2ª ed. expandida, 2017, Eerdmans), oferece uma alternativa ao '
    'modelo formcrítico de transmissão anônima. Bauckham argumenta que os evangelhos '
    'estão solidamente fundamentados em testemunho ocular: Pedro seria a fonte principal '
    'de Marcos; e o Evangelho de João seria obra de uma testemunha ocular identificada '
    'como "o discípulo amado". O argumento é reforçado por análise onomástica — os nomes '
    'próprios dos evangelhos correspondem ao padrão estatístico dos nomes judaicos '
    'palestinos do período —, por paralelos com a prática historiográfica antiga e por '
    'dados da psicologia cognitiva sobre a memória de testemunhas oculares.',
    first_indent=True)

# ═══════════════════════════════════════════════════════════════════════════
# 4. ABORDAGENS SOCIOLÓGICAS E ANTROPOLÓGICAS
# ═══════════════════════════════════════════════════════════════════════════
h(1, '4. Abordagens Sociológicas e Antropológicas')

h(2, '4.1 A Cultura de Honra e Vergonha')
body(
    'O modelo da cultura mediterrânea de honra e vergonha (honor-shame culture), '
    'desenvolvido por antropólogos como David Gilmore e Bruce Malina, tornou-se uma '
    'ferramenta hermenêutica amplamente utilizada nos estudos do Jesus Histórico. A '
    'honra é entendida como a mercadoria escassa central das sociedades mediterrâneas '
    'antigas, estruturando relações sociais, políticas e religiosas. Os conflitos de '
    'Jesus com os fariseus, seus comentários sobre riqueza e pobreza, e a dinâmica da '
    'crucificação — morte maximamente desonrosa — tornam-se legíveis nesse quadro. '
    'Embora criticado por essencializar o "Mediterrâneo" como unidade cultural '
    'homogênea, o modelo permanece relevante com nuances contextuais.',
    first_indent=True)

h(2, '4.2 A Economia Camponesa e a Galileia do Século I')
body(
    'John Dominic Crossan (The Historical Jesus, 1991) retratou Jesus como um camponês '
    'galileu que operava um programa de cura e comensalidade radicalmente igualitário, '
    'subversivo das hierarquias de pureza e de status. A arqueologia galileana recente '
    'confirmou e refinado o quadro: Nazaré era uma aldeia de menos de 400 habitantes, a '
    'menos de 8 km de Séforis em plena reconstrução herodiana — contexto de intensas '
    'transformações que deslocaram famílias camponesas e acentuaram tensões de classe.',
    first_indent=True)

h(2, '4.3 Jesus: A Life in Class Conflict — A Leitura Materialista')
body(
    'James Crossley e Robert J. Myles, em Jesus: A Life in Class Conflict (Zer0 Books, '
    '2023), propõem a primeira análise plenamente articulada do Jesus Histórico a partir '
    'de uma perspectiva marxista. Os autores situam Jesus e seu movimento dentro das '
    'contradições de classe da Palestina do século I, marcada pela extração fiscal '
    'romana, pela concentração fundiária, pelo endividamento e expropriação dos '
    'camponeses galileus e pela ideologia legitimadora do templo de Jerusalém. A '
    '"limpeza do templo" é reinterpretada como um protesto contra a exploração '
    'econômica. O Journal for the Study of the Historical Jesus (2024) descreveu o '
    'livro como "uma obra que define o campo" e que "não será facilmente descartada em '
    'trabalhos futuros sobre o Jesus Histórico."',
    first_indent=True)

h(2, '4.4 Sociologia da Religião e o Movimento de Jesus')
body(
    'Gerd Theissen (The Sociology of Early Palestinian Christianity, 1978) foi pioneiro '
    'na aplicação da sociologia à reconstituição histórica do movimento jesuânico. Mais '
    'recentemente, Sarah Rollens (Framing Social Inquiry in the Jesus Tradition, 2021) '
    'examina como o discurso igualitário do movimento jesuânico operou como tecnologia '
    'social de recrutamento e coesão de grupo em ambiente de crescente diferenciação '
    'social. Alan Kirk (Jesus Tradition, Early Christian Memory, and Gospel Writing, '
    'Eerdmans, 2023) integra teoria da memória, oralidade e crítica das fontes, '
    'argumentando que a escrita dos evangelhos era um ato de mnemônica social — não a '
    'substituição da memória viva, mas sua monumentalização.',
    first_indent=True)

# ═══════════════════════════════════════════════════════════════════════════
# 5. ABORDAGENS FILOSÓFICAS E METODOLÓGICAS
# ═══════════════════════════════════════════════════════════════════════════
h(1, '5. Abordagens Filosóficas e Metodológicas')

h(2, '5.1 A Crise dos Critérios de Autenticidade')
body(
    'O desenvolvimento e o declínio dos critérios de autenticidade constituem o drama '
    'metodológico central da pesquisa sobre o Jesus Histórico no século XX e início do '
    'XXI. As críticas mais articuladas foram sistematizadas no volume editado por Chris '
    'Keith e Anthony Le Donne, Jesus, Criteria, and the Demise of Authenticity (T&T '
    'Clark, 2012). Keith demonstra que os critérios são herdeiros não reconhecidos da '
    'crítica das formas bultmanniana. Le Donne qualifica a abordagem como "historiografia '
    'positivista": a crença de que é possível separar cirurgicamente o "autêntico" do '
    '"inautêntico" pressupõe uma concepção de memória que a psicologia cognitiva e a '
    'sociologia da memória contemporâneas simplesmente não sustentam.',
    first_indent=True)
body(
    'Dale Allison (2009) sentenciou: "Usamos nossos critérios para obter o que já '
    'queremos." Jonathan Bernier (2016) concluiu que os critérios são "instrumentos '
    'historiográficos falidos que necessitam de revisão séria ou abandono." O consenso '
    'emergente é que o juízo histórico é sempre um juízo de plausibilidade contextual, '
    'e não de autenticidade atomística.',
    first_indent=True)

h(2, '5.2 A Plausibilidade como Substituto dos Critérios')
body(
    'Gerd Theissen e Dagmar Winter, em The Quest for the Plausible Jesus (2002), '
    'sistematizaram o modelo dominante: o juízo histórico sobre Jesus é um juízo de '
    'plausibilidade contextual dupla — plausibilidade em relação ao contexto judaico do '
    'século I e plausibilidade em relação ao efeito histórico. Jonathan Bernier '
    '(Rethinking the Dates of the New Testament, 2022) desenvolve essa abordagem no '
    'quadro de uma epistemologia bayesiana aplicada ao estudo do Novo Testamento.',
    first_indent=True)

h(2, '5.3 A Questão dos Milagres e a Epistemologia Histórica')
body(
    'A questão dos milagres é o ponto de máxima tensão filosófica. Ehrman argumenta que '
    'o historiador, por ofício, não pode afirmar que milagres provavelmente ocorreram, '
    'pois o método histórico opera com analogia e probabilidade comparativa. Wright '
    'replica que Ehrman confunde epistemologia histórica com metafísica naturalista: o '
    'historiador pode afirmar que algo inesperado e sem paralelo aconteceu, mesmo que '
    'não possa nomear sua causa definitiva.',
    first_indent=True)
body(
    'Dale Allison, em Resurrecting Jesus (2005), oferece uma posição metodologicamente '
    'sofisticada: as aparições pós-morte de Jesus têm paralelos em toda a literatura de '
    'luto e visão do mundo antigo (e moderno), o que não as explica, mas as situa num '
    'horizonte humano reconhecível. A probabilidade da ressurreição, conclui Allison, '
    'depende da Weltanschauung (cosmovisão) que o investigador traz à análise — nenhum '
    'argumento histórico pode sozinho fundamentar ou refutar uma cosmovisão.',
    first_indent=True)

h(2, '5.4 A Epistemologia Crítico-Realista')
body(
    'Ben F. Meyer (The Aims of Jesus, 1979), inspirado em Bernard Lonergan, propôs '
    'situar a pesquisa histórica dentro de uma epistemologia crítico-realista: o '
    'historiador não tem acesso direto ao passado, mas pode alcançar compreensão real '
    'por inferência a partir dos vestígios disponíveis, se operar com horizonte '
    'hermenêutico aberto e autoconhecimento de seus pressupostos. N.T. Wright desenvolveu '
    'esse quadro em The New Testament and the People of God (1992), propondo uma '
    '"epistemologia crítico-realista" que rejeita tanto o positivismo ingênuo quanto o '
    'relativismo pós-moderno.',
    first_indent=True)

# ═══════════════════════════════════════════════════════════════════════════
# 6. ABORDAGENS HISTÓRICAS E ARQUEOLÓGICAS
# ═══════════════════════════════════════════════════════════════════════════
h(1, '6. Abordagens Históricas e Arqueológicas')

h(2, '6.1 As Fontes Textuais')
body(
    'As fontes primárias para o estudo do Jesus Histórico incluem: (a) fontes cristãs '
    '— as cartas de Paulo (c. 50–60 d.C.), os evangelhos sinóticos (Marcos c. 70 d.C.; '
    'Mateus e Lucas c. 80–90 d.C.) e João (c. 90–100 d.C.), a hipotética fonte Q e o '
    'problemático Evangelho de Tomé; (b) fontes não-cristãs — Tácito (Anais XV.44, '
    'c. 116 d.C.), Plínio, o Jovem (Epístola X.96), Josefo (Antiguidades Judaicas '
    'XVIII.63-64, o Testimonium Flavianum, e XX.200) e referências rabínicas posteriores.',
    first_indent=True)
body(
    'O Testimonium Flavianum de Josefo permanece objeto de debate: a maioria dos '
    'especialistas hoje admite um núcleo josefénico autêntico submetido a interpolações '
    'cristãs (Meier, 1991; Ehrman, 2012). Os elementos que chegam ao consenso '
    'historiográfico são: a existência histórica de Jesus, seu batismo por João Batista, '
    'seu ministério na Galileia, sua crucificação sob Pôncio Pilatos (c. 30–33 d.C.) e '
    'o surgimento de uma comunidade de seguidores após sua morte.',
    first_indent=True)

h(2, '6.2 Descobertas Arqueológicas Recentes')
body(
    'A arqueologia do século I na Galileia transformou profundamente a compreensão do '
    'contexto social e cultural de Jesus. Entre as descobertas mais significativas:')
bullet('Sinagoga de Magdala (escavada desde os anos 2000): uma das poucas sinagogas do '
       'século I identificadas. A Pedra de Magdala, esculpida com uma menorá e outros '
       'símbolos do Templo de Jerusalém, é datada para o período do ministério de Jesus.')
bullet('Escavações de el-Araj / Betsaida (desde 2016): concorrente ao título de '
       'Betsaida, cidade natal de Pedro, André e Filipe. Uma basílica bizantina com '
       'inscrições dedicatórias a São Pedro foi identificada no sítio.')
bullet('Sinagoga de Capernaum: a arqueologia confirmou a existência de sinagoga do '
       'século I, contrapondo-se às teorias de que referências sinóticas seriam '
       'anacronismos pós-70 d.C.')
bullet('Igreja do Santo Sepulcro (escavações de 2025): estratos do século I '
       'identificados correspondem à descrição joanina de um jardim próximo ao local '
       'da crucificação; achados arqueobotânicos são consistentes com o texto de João.')
bullet('Evidências de observância judaica: jarras de pedra que não transmitem impureza, '
       'ausência de ossos de porco, moedas sem efígies — confirmando a profunda '
       'identidade judaica do contexto de Jesus.')

h(2, '6.3 A Questão da Galileia Urbana vs. Rural')
body(
    'Jonathan Reed e Mark Chancey demonstraram que a Galileia do século I era um '
    'espaço de intensas transformações sociais e econômicas induzidas pelo processo de '
    'urbanização romano-herodiana. Nazaré, a menos de 8 km de Séforis em plena '
    'expansão sob Herodes Antipas, estava imersa num processo que deslocou famílias '
    'camponesas e criou as tensões estruturantes do ministério de Jesus.',
    first_indent=True)

# ═══════════════════════════════════════════════════════════════════════════
# 7. DEBATES CENTRAIS ATUAIS
# ═══════════════════════════════════════════════════════════════════════════
h(1, '7. Debates Centrais Atuais')

h(2, '7.1 O Apocalipsismo de Jesus')
body(
    'A posição de Schweitzer — Jesus como profeta apocalíptico cujas expectativas de '
    'fim iminente não se realizaram — é sustentada pela maioria dos acadêmicos não-'
    'confessionais: Ehrman, Sanders, Allison, Fredriksen, Vermes. As fontes mais antigas '
    '(Paulo, Marcos, Q) atestam de forma consistente uma mensagem de iminência do Reino '
    'de Deus com conotações cósmicas.',
    first_indent=True)
body(
    'Wright, por sua vez, rejeita o "fim literal do universo" como chave interpretativa, '
    'propondo que a linguagem profética do fim-dos-tempos é metáfora para eventos '
    'histórico-políticos. Esta posição é contestada por Allison e Ehrman, que consideram '
    'a reinterpretação "metaforista" de Wright apologeticamente motivada.',
    first_indent=True)

h(2, '7.2 A Morte de Jesus')
body(
    'A crucificação é o dado mais firmemente estabelecido sobre Jesus — atestado por '
    'Tácito, Josefo e todas as fontes cristãs primitivas. O debate incide sobre as '
    'razões: para Fredriksen, Jesus foi vítima de uma dinâmica que ele próprio não '
    'controlava; para Wright, Jesus buscou deliberadamente a morte como parte de sua '
    'vocação messiânica; para Ehrman, a crucificação resulta da perturbação da paz '
    'pública no templo — suficiente para a execução sumária de um agitador provincial.',
    first_indent=True)

h(2, '7.3 A Ressurreição')
body(
    'Os dados históricos com relativo consenso são: (a) o túmulo foi encontrado vazio '
    'por discípulas — o critério do embaraço favorece a historicidade, pois mulheres '
    'eram testemunhas juridicamente desqualificadas; (b) houve aparições pós-morte '
    'experimentadas por Pedro, Paulo e grupos de seguidores; (c) o anúncio da '
    'ressurreição está no coração das mais antigas camadas do kerigma cristão (1 Cor 15, '
    'datável a c. 35–36 d.C.).',
    first_indent=True)
body(
    'A interpretação é radicalmente divergente: Wright afirma a ressurreição corporal '
    'como o único dado histórico adequado; Allison propõe suspensão agnóstica; Ehrman '
    'e outros explicam as aparições como visões de luto (grief visions), fenômeno '
    'psicológico bem documentado.',
    first_indent=True)

h(2, '7.4 A Memória e a Tradição Oral')
body(
    'James D.G. Dunn, em Jesus Remembered (Eerdmans, 2003), argumenta que a tradição '
    'oral constitui o meio primário de transmissão da herança de Jesus, com combinação '
    'de fixidez (do núcleo essencial) e fluidez (da formulação variável) como '
    'característica da oralidade.',
    first_indent=True)
body(
    'Keith e Le Donne, a partir de Maurice Halbwachs, Jan Assmann e Barry Schwartz, '
    'propõem a "memória social" como quadro interpretativo alternativo: toda memória é '
    'socialmente mediada, e o que os evangelhos transmitem é o Jesus-como-lembrado pelas '
    'comunidades que o sucederam. A distinção autêntico/inautêntico é epistemicamente '
    'infundada; o que se pode investigar é como e por que Jesus foi lembrado de '
    'determinadas maneiras.',
    first_indent=True)

h(2, '7.5 Identidade Étnica, Gênero e Pós-colonialismo')
body(
    'O Next Quest trouxe ao centro debates antes marginalizados. Adele Reinhartz examina '
    'a persistência de leituras supersessionistas. Elisabeth Schüssler Fiorenza e Mary '
    'Ann Tolbert contribuíram décadas de hermenêutica feminista que recolocam as mulheres '
    'do movimento — Maria Madalena, as discípulas, as financiadoras galileias — como '
    'sujeitos históricos plenos. O Next Quest inclui capítulos sobre sexualidade, '
    'deficiência (disability studies) e raça aplicados ao Jesus histórico — territórios '
    'praticamente inexplorados na Terceira Busca.',
    first_indent=True)

# ═══════════════════════════════════════════════════════════════════════════
# 8. LACUNAS E PERSPECTIVAS FUTURAS
# ═══════════════════════════════════════════════════════════════════════════
h(1, '8. Lacunas de Pesquisa e Perspectivas Futuras')

h(2, '8.1 Lacunas Identificadas')
body('A revisão da literatura permite identificar as seguintes lacunas de pesquisa:')
bullet('Perspectivas do Sul Global: Cristologias africanas (Jesus como ancestral, como '
       'curandeiro sagrado) e hermenêuticas da libertação latino-americana carecem de '
       'maior integração metodológica com os debates histórico-críticos centrais.')
bullet('Humanidades Digitais: análise computacional de corpus, mapeamento de redes '
       'sociais antigas e ferramentas de análise linguística computacional permanecem '
       'raramente mobilizados.')
bullet('Psicobiografia e Cognição Religiosa: a aplicação de ciências cognitivas da '
       'religião ao estudo do Jesus Histórico — suas visões, experiências místicas e '
       'estados alterados de consciência — está em estágio incipiente.')
bullet('Jesus e o Corpo: estudos sobre deficiência, corporalidade e saúde no contexto '
       'do ministério terapêutico de Jesus são ainda limitados, mas crescentes.')
bullet('Recepção Histórica (Wirkungsgeschichte): o estudo de como Jesus foi recebido, '
       'representado e instrumentalizado em diferentes contextos históricos está se '
       'tornando subcampo próprio.')
bullet('O Papel das Mulheres: a reconstituição histórica do papel das discípulas '
       'galileias — Maria Madalena, Joana, Suzana — ainda enfrenta lacunas documentais '
       'e resistências hermenêuticas.')

h(2, '8.2 Perspectivas Futuras')
body(
    'O campo está claramente em transição. A Next Quest representa não uma simples '
    'adição a uma sequência numerada, mas uma reorientação paradigmática que: (a) '
    'abandona a hegemonia dos critérios de autenticidade em favor de abordagens baseadas '
    'em memória, plausibilidade e comparação cultural; (b) amplia o objeto de pesquisa '
    'para incluir a recepção, a política, a economia e o corpo; (c) diversifica os '
    'sujeitos da pesquisa, superando o monopólio europeu-protestante; (d) integra '
    'sistemicamente a arqueologia, a numismática, a papirologia e outros campos materiais '
    'à análise textual.',
    first_indent=True)
body(
    'A questão metodológica mais urgente permanece: como fazer história de um personagem '
    'cujas tradições são inseparáveis de interpretações teológicas, sem capitular ao '
    'confessionalismo ou praticar uma laicidade ingênua que também é, ela própria, uma '
    'posição ideológica? A diversidade metodológica do campo — longe de ser um sinal de '
    'crise — é a evidência de sua vitalidade. O Jesus Histórico continuará sendo, nas '
    'próximas décadas, um espelho no qual os estudiosos encontram não apenas a Galileia '
    'do século I, mas também a si mesmos.',
    first_indent=True)

# ═══════════════════════════════════════════════════════════════════════════
# 9. REFERÊNCIAS
# ═══════════════════════════════════════════════════════════════════════════
doc.add_page_break()
h(1, 'Referências Bibliográficas')

refs = [
    'Allison, D. C. (1998). Jesus of Nazareth: Millenarian prophet. Fortress Press.',
    'Allison, D. C. (2005). Resurrecting Jesus: The earliest Christian tradition and its interpreters. T&T Clark.',
    'Bauckham, R. (2017). Jesus and the eyewitnesses: The gospels as eyewitness testimony (2nd ed.). Eerdmans. (Original: 2006)',
    'Bernier, J. (2016). Rethinking the dates of the New Testament: The evidence for early composition. Baker Academic.',
    'Crossan, J. D. (1991). The historical Jesus: The life of a Mediterranean Jewish peasant. HarperSanFrancisco.',
    'Crossley, J. (2021). The next quest for the historical Jesus. Journal for the Study of the Historical Jesus, 19(3), 261–264.',
    'Crossley, J., & Keith, C. (Eds.). (2024). The next quest for the historical Jesus. Eerdmans.',
    'Crossley, J., & Myles, R. J. (2023). Jesus: A life in class conflict. Zer0 Books.',
    'Dunn, J. D. G. (2003). Jesus remembered (Christianity in the Making, Vol. 1). Eerdmans.',
    'Ehrman, B. D. (1999). Jesus: Apocalyptic prophet of the new millennium. Oxford University Press.',
    'Ehrman, B. D. (2012). Did Jesus exist? The historical argument for Jesus of Nazareth. HarperOne.',
    'Ehrman, B. D. (2016). Jesus before the Gospels. HarperOne.',
    'Fredriksen, P. (1999). Jesus of Nazareth, king of the Jews: A Jewish life and the emergence of Christianity. Knopf.',
    'Fredriksen, P. (2018). When Christians were Jews: The first generation. Yale University Press.',
    'Fredriksen, P. (2024). Ancient Christianities: The first five centuries. Princeton University Press.',
    'Keith, C., & Le Donne, A. (Eds.). (2012). Jesus, criteria, and the demise of authenticity. T&T Clark.',
    'Kirk, A. (2023). Jesus tradition, early Christian memory, and Gospel writing. Eerdmans.',
    'Kloppenborg, J. S. (2000). Excavating Q: The history and setting of the Sayings Gospel. Fortress Press.',
    'Malina, B. J., & Rohrbaugh, R. L. (1992). Social-science commentary on the Synoptic Gospels. Fortress Press.',
    'Meier, J. P. (1991–2016). A marginal Jew: Rethinking the historical Jesus (Vols. 1–5). Yale University Press / Doubleday.',
    'Rollens, S. E. (2014). Framing social inquiry in the Jesus tradition. Mohr Siebeck.',
    'Sanders, E. P. (1985). Jesus and Judaism. Fortress Press.',
    'Sanders, E. P. (1993). The historical figure of Jesus. Penguin Books.',
    'Schüssler Fiorenza, E. (1983). In memory of her: A feminist theological reconstruction of Christian origins. Crossroad.',
    'Schweitzer, A. (2001). The quest of the historical Jesus (W. Montgomery, Trans.). Fortress Press. (Original: 1906)',
    'Theissen, G., & Winter, D. (2002). The quest for the plausible Jesus: The question of criteria. Westminster John Knox Press.',
    'Wright, N. T. (1992). The New Testament and the people of God (Christian Origins and the Question of God, Vol. 1). Fortress Press.',
    'Wright, N. T. (1996). Jesus and the victory of God (Christian Origins and the Question of God, Vol. 2). Fortress Press.',
    'Wright, N. T. (2003). The resurrection of the Son of God (Christian Origins and the Question of God, Vol. 3). Fortress Press.',
]

for r in refs:
    ref(r)

# ── Salvar ────────────────────────────────────────────────────────────────
output = '/home/user/100daysofcode/revisao_jesus_historico.docx'
doc.save(output)
print(f'Arquivo salvo: {output}')
