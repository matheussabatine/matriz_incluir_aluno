from fpdf import FPDF

turma="5 A"
prof="SAURA"
nome_prof_base=f"{turma}, {prof}"
nome_prof_artes="MARINA"
nome_prof_ed_fisica="EVELIN"
nome_prof_ingles="VERA"
nome_aluno="EDIMILSON COSTEIRA PINTO SALAFRÁRIO"
num_aluno=20
data_inicio="13/03/2025"
ir_embora_sozinho="NÃO"

pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()

def bilhete(nome_aluno, num_aluno, data_inicio, ir_embora_sozinho, nome_prof_base, nome_prof_especial=""):
    pdf.image("catavento.png", x = None, y = None, w = 30, h = 10, type = '', link = '')

    pdf.set_font('Arial', 'B', 10)
    pdf.cell(w = 0, h = 0, txt = 'SECRETARIA CEMUS VIII', border = 0, ln = 1, 
            align = 'C', fill = False, link = '')
    #pular linha
    pdf.set_font('Arial', '', 10)
    pdf.cell(w = 0, h = 4, txt = '', border = 0, ln = 2, 
            align = '', fill = False, link = '')
    pdf.cell(w = 0, h = 4, txt = '', border = 0, ln = 2, 
            align = '', fill = False, link = '')

    if (nome_prof_especial != ""):
        pdf.cell(w = 0, h = 4, txt = f'Professor (a): {nome_prof_especial} - {nome_prof_base}', border = 0, ln = 1, 
                align = '', fill = False, link = '')
    else:
        pdf.cell(w = 0, h = 4, txt = f'Professor (a): {nome_prof_base}', border = 0, ln = 1, 
                align = '', fill = False, link = '')
        


    pdf.cell(w = 0, h = 4, txt = 'Por favor, incluir no seu diário de classe o (a) aluno (a):', border = 0, ln = 2, 
            align = '', fill = False, link = '')
    pdf.cell(w = 0, h = 4, txt = nome_aluno, border = 0, ln = 2, 
            align = '', fill = False, link = '')
    pdf.cell(w = 0, h = 4, txt = f'como nº {num_aluno} para lista de chamada.', border = 0, ln = 2, 
            align = '', fill = False, link = '')
    pdf.cell(w = 0, h = 4, txt = f'Data de Início: {data_inicio}', border = 0, ln = 2, 
            align = '', fill = False, link = '')
    pdf.cell(w = 0, h = 4, txt = f'Autorizado a ir embora sozinho?: {ir_embora_sozinho}', border = 0, ln = 2, 
            align = '', fill = False, link = '')
    #pular linha
    pdf.cell(w = 0, h = 4, txt = '', border = "B", ln = 2, 
            align = '', fill = False, link = '')
    pdf.cell(w = 0, h = 4, txt = '', border = 0, ln = 2, 
            align = '', fill = False, link = '')
    
bilhete(nome_aluno, num_aluno, data_inicio, ir_embora_sozinho, nome_prof_base)
bilhete(nome_aluno, num_aluno, data_inicio, ir_embora_sozinho, nome_prof_base, nome_prof_artes)
bilhete(nome_aluno, num_aluno, data_inicio, ir_embora_sozinho, nome_prof_base, nome_prof_ed_fisica)
bilhete(nome_aluno, num_aluno, data_inicio, ir_embora_sozinho, nome_prof_base, nome_prof_ingles)

pdf.multi_cell(w = 40, h = 6, txt = nome_aluno, border = 1, align = 'C', fill = False)
pdf.output('tuto1.pdf', 'F')