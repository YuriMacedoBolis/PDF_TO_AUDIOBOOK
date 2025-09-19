# PDF Audiobook (Versão Simples) # 
Um script em Python simples e leve que converte o texto de um arquivo PDF inteiro em um arquivo de áudio no formato MP3. Perfeito para transformar seus documentos em audiobooks sem a necessidade de dependências externas complexas.

## Funcionalidades 
* Converte o texto de todas as páginas de um PDF em áudio.

* Salva o áudio gerado em um único arquivo MP3.

* Exibe uma barra de progresso durante a extração do texto.

* Após a conclusão, informa o caminho e o tamanho do arquivo de áudio final.

* Não requer a instalação do ffmpeg.

## Requisitos
Para usar este script, você só precisa ter o Python instalado em seu sistema. As bibliotecas necessárias são:

#### PyPDF2 (para ler o PDF)

#### pyttsx3 (para gerar o áudio)

#### tqdm (para a barra de progresso)

#### Você pode instalar todas as dependências com o seguinte comando:

Bash

pip install -r requirements.txt

## Como Usar
Clone o repositório:

Bash

git clone https://github.com/seu-usuario/pdf-audiobook.git
cd pdf-audiobook

Coloque seu arquivo PDF na pasta do projeto:
O script precisa que o arquivo PDF que você quer ler esteja na mesma pasta que o arquivo pdf_reader.py.

📄 Licença
Este projeto está sob a licença MIT. Para mais detalhes, consulte o arquivo LICENSE.
