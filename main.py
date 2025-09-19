import pyttsx3
import PyPDF2
import os
from tqdm import tqdm

def gerar_audiobook(pdf_path, output_filename="audiobook.mp3"):
    """
    Gera um audiobook a partir de um arquivo PDF sem usar o pydub.
    Todo o texto é extraído e depois salvo de uma vez só.
    """
    try:
        
        pdf_file = open(pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        full_text = ""

        print(f"Iniciando a extração do texto do PDF...")

        
        for page_num in tqdm(range(num_pages), desc="Extraindo texto"):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if text:
                full_text += text

        pdf_file.close()

        
        if not full_text:
            print("Nenhum texto foi encontrado no arquivo PDF.")
            return

        print("\nTexto extraído com sucesso. Iniciando a conversão para áudio...")
        
        print('\nAguarde alguns instantes para o Download ser concluído, esse processo pode demorar um pouco...')

        
        speaker = pyttsx3.init()
        speaker.setProperty('rate' , 250)
        speaker.save_to_file(full_text, output_filename)
        speaker.runAndWait()

        print("\nProcesso de conversão concluído!")

        
        absolute_path = os.path.abspath(output_filename)
        print(f"LINK PARA O ARQUIVO: {absolute_path}")
        
        
        file_size_bytes = os.path.getsize(output_filename)
        file_size_mb = file_size_bytes / (1024 * 1024)
        print(f"TAMANHO DO ARQUIVO: {file_size_mb:.2f} MB")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{pdf_path}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


if __name__ == "__main__":
    print("="*27)
    print('CONVERSOR DE PDF PARA ÁUDIO')
    print("="*27)
    pdf_to_convert = str(input("Cole o seu arquivo .pdf:"))
    gerar_audiobook(pdf_to_convert)