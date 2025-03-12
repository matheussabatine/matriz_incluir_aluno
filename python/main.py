# import the canvas object
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import ParagraphStyle

# cria canvas e definir nome e tamanho
c = canvas.Canvas("teste.pdf", pagesize=A4)  # A4 pagesize
largura, altura = A4
#tamanho para pular uma linha y -=15
x=15
y=795

# texto.uppercase()
prof_base="carmenita"
prof_artes="MARINA"
prof_ingles="VERA"
prof_edu_fisica="EVELIN"
aluno="alberto cortez da cruz limeira aparecida diniz vasconcelos"
num=17
data_inicio="10/03/2025"
ir_embora_sozinho="NÃO"

def paragrafo(x, y, aluno, num, data_inicio, ir_embora_sozinho, prof_base, prof_especial=""):

    c.drawInlineImage("catavento.png", x,y, width=None,height=None)
    #titulo
    c.setFont('Times-Roman', 15)
    x=220
    c.drawString(x, y, "SECRETARIA CEMUS VIII")
    #titulo



    #linhas
    c.setFont('Times-Roman', 12)
    #pular linha
    y -= 30

    x=20
    
    if prof_especial != "":
        c.drawString(x, y, f"Professor (a):{prof_especial} - {prof_base}")
    else:
        c.drawString(x, y, f"Professor (a): {prof_base}")
    #pular linha
    y -= 15

    c.drawString(x, y, "Por favor, incluir no seu diário de classe o (a) aluno (a):")
    #pular linha
    y -= 15

    c.drawString(x, y, aluno)
    #pular linha
    y -= 15

    c.drawString(x, y, f"como nº {num} para lista de chamada.")
    #pular linha
    y -= 15

    c.drawString(x, y, f"Data de Início: {data_inicio}")
    #pular linha
    y -= 15

    c.drawString(x, y, f"Autorizado a ir embora sozinho?: {ir_embora_sozinho}")
    #pular linha
    y -= 15

    c.line(0, y,600, y)

paragrafo(x, y, aluno, num, data_inicio, ir_embora_sozinho, prof_base)
y -=170
paragrafo(x, y, aluno, num, data_inicio, ir_embora_sozinho, prof_base, prof_artes)
y -=170
paragrafo(x, y, aluno, num, data_inicio, ir_embora_sozinho, prof_base, prof_ingles)
y -=170
paragrafo(x, y, aluno, num, data_inicio, ir_embora_sozinho, prof_base, prof_edu_fisica)
y -=170




# fim da pagina
c.showPage()
# construct and save file to .pdf
c.save()

# Professor (a): EDA
# Por favor, incluir no seu diário de classe o (a) aluno (a): SILAS EDUARDO SANTOS BRITO como nº 29 para lista de chamada.
# Data de Início: 11/09/2024
# Autorizado (a) a ir embora sozinho: (    ) SIM    ( X ) NÃO
