import gtts
import PyPDF2
# Читаем pdf и конвертируем в аудио
file_name = 'test_ru.pdf'
lang = 'ru'

with open(file_name, 'rb') as file:
    pdf_file = PyPDF2.PdfReader(file)
    text = pdf_file.pages[0].extract_text()

print('[+] Processing...')
t1 = gtts.gTTS(text, lang='ru')
t1.save('audio.mp3')
print('[+] Audio file saved')



