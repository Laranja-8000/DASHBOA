# Autor: Lucas Cavalcante
# Atualizado em: 04/02/2023
import PyPDF2
import io

# Importando o arquivo pdf
pdf_file_object = open("boa.pdf",'rb')

# Criando variável leitora
pdf_reader = PyPDF2.PdfReader( pdf_file_object )

# Pegando o número de páginas
num_pages = len(pdf_reader.pages)

# Extraindo texto
text = '' # A variável 'text' armazenada todo o texto do arquivo extraído pelo PyPDF em uma única String

for i in range(num_pages):
    text += pdf_reader.pages[i].extract_text()

# salvando o texto extraído em arquivo para teste
test_file = open('boa_pdf_text.txt','w')
test_file.write(text)
test_file.close()

text = io.StringIO(text)

# Processamento primário do texto (Como pede o funcionamento do PDF)
text_lines = text.readlines() # Guardando todas as linhas de texto em uma lista de Strings
text_lines.append("EOF")

# Créditos das Disciplinas

## int credits_data = [[ 'falta cumprir', 'total a ser cumprido'], ... ]
credits_data = [[0,0], # Obrigatórias
                [0,0], # Optativas
                [0,0], # Optativas (Escolha Restrita)
                [0,0]] # Livre Escolha

num_linha = 0 # numero da linha
j = 0 # índice

while( text_lines[num_linha] != 'EOF' ): # Percorrendo as linhas de texto
    num_linha += 1

    # Retirando as informações das linhas que as contém
    # Otimização evidentemente faz-se necessária neste trecho:
    if( 'Falta Cumprir' in text_lines[num_linha] and j == 0 ): # Obrigatórias
        credits_data[j][0] = int(text_lines[num_linha + 2].split('.')[0])
        credits_data[j][1] = int(text_lines[num_linha + 1].split('.')[0])
        j += 1
        
    elif( 'Falta Cumprir' in text_lines[num_linha] and j == 1 ): # Optativas
        '''
        print(text_lines[num_linha],end='')
        print(text_lines[num_linha + 2],end='')
        print(text_lines[num_linha + 1],end='')
        '''
        credits_data[j][0] = int( text_lines[num_linha + 2].split('.')[0] )
        credits_data[j][1] = int( text_lines[num_linha + 1].split(' ')[0] )
        j+=1
  

    elif( 'Falta Cumprir' in text_lines[num_linha] and j == 2): # Optativas (Escolha Restrita)
        '''print(text_lines[num_linha],end='')
        print(text_lines[num_linha + 2],end='')
        print(text_lines[num_linha + 1],end='')'''

        credits_data[j][0] = int( text_lines[num_linha + 1].split('.')[0] )
        credits_data[j][1] = int( text_lines[num_linha + 2].split(' ')[0] )

        '''print( "Falta cumprir: "+ str(credits_data[j][0]) )
        print( "Total a cumprir: "+ str(credits_data[j][1]) )'''
        j+=1


    elif( 'Falta Cumprir' in text_lines[num_linha] and j == 3): # Esta parte de Livre Escolha requer mais testes
        '''
        print(text_lines[num_linha],end='')
        print(text_lines[num_linha + 2],end='')
        print(text_lines[num_linha + 1],end='') '''
        
        credits_data[j][0] = int( text_lines[num_linha +1].split('.')[0] )
        credits_data[j][1] = int( text_lines[num_linha +2].split('.')[0] )

        '''print( "Falta cumprir: "+ str(credits_data[j][0]) )
        print( "Total a cumprir: "+ str(credits_data[j][1]) )'''
        j+=1
  

# Exibição

'''
for i in text_lines: 
    print(i)
'''

'''
for i in range(len(credits_data)):

    if(i==0): print("\n=== ATIVIDADES ACADÊMICAS OBRIGATÓRIAS ===\n")
    if(i==1): print("\n=== ATIVIDADES OPTATIVAS ===\n")
    if(i==2): print("\n=== ATIVIDADES OPTATIVAS (ESCOLHA RESTRITA) ===\n")
    if(i==3): print("\n=== LIVRE ESCOLHA ===\n")

    print("Total a cumprir: "+str(credits_data[i][1]))
    print("Falta cumprir: "+str(credits_data[i][0]))
    print("Já cumpridos: "+str(abs(credits_data[i][1] - credits_data[i][0])))
'''

# Fim
pdf_file_object.close()