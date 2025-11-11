import pyttsx3
import PyPDF2

# Open the PDF file
pdf_file = open("Python+Handbook.pdf", "rb")
reader = PyPDF2.PdfReader(pdf_file)

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Extract and read text from each page
text = ""
for page in reader.pages:
    text += page.extract_text()

# Convert text to audio and save as MP3
speaker.save_to_file(text, "Python_Handbook_Audio.wav")
voices=speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)
speaker.runAndWait()

pdf_file.close()
print("✅ Audio file created successfully: Python_Handbook_Audio.wav")