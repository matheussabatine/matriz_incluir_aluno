# import the canvas object
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import paragraph


# cria canvas e definir nome e tamanho
c = canvas.Canvas("teste.pdf", pagesize=A4)  # A4 pagesize
largura, altura = A4

#altura da primeira linha
y=795

# texto.uppercase()
prof_base="LAURA"
prof_artes="MARINA"
prof_ingles="VERA"
prof_edu_fisica="EVELIN"
aluno="alberto cortez da cruz limeira aparecida diniz vasconcelos"
num=17
data_inicio="10/03/2025"
ir_embora_sozinho="NÃO"

def pular_linha(valor):
    global y
    y-=valor

def paragrafo(aluno, num, data_inicio, ir_embora_sozinho, prof_base, prof_especial=""):
    
    x=15
    global y
    c.drawInlineImage("catavento.png", x, y, width=None,height=None)
    #titulo
    c.setFont('Times-Roman', 15)
    x=220
    c.drawString(x, y, "SECRETARIA CEMUS VIII")
    #titulo

    #linhas
    c.setFont('Times-Roman', 12)
    #pular linha
    pular_linha(30)

    x=20
    
    if prof_especial != "":
        c.drawString(x, y, f"Professor (a):{prof_especial} - {prof_base}")
    else:
        c.drawString(x, y, f"Professor (a): {prof_base}")
    #pular linha
    pular_linha(15)

    c.drawString(x, y, "Por favor, incluir no seu diário de classe o (a) aluno (a):")
    #pular linha
    pular_linha(15)

    c.drawString(x, y, aluno)
    #pular linha
    pular_linha(15)

    c.drawString(x, y, f"como nº {num} para lista de chamada.")
    #pular linha
    pular_linha(15)

    c.drawString(x, y, f"Data de Início: {data_inicio}")
    #pular linha
    pular_linha(15)

    c.drawString(x, y, f"Autorizado a ir embora sozinho?: {ir_embora_sozinho}")
    #pular linha
    pular_linha(15)

    c.line(0, y,600, y)

    pular_linha(45)

paragrafo(aluno, num, data_inicio, ir_embora_sozinho, prof_base)

paragrafo(aluno, num, data_inicio, ir_embora_sozinho, prof_base, prof_artes)

paragrafo(aluno, num, data_inicio, ir_embora_sozinho, prof_base, prof_ingles)

paragrafo(aluno, num, data_inicio, ir_embora_sozinho, prof_base, prof_edu_fisica)





# fim da pagina
c.showPage()
# construct and save file to .pdf
c.save()