import PyPDF2

def generate_questions(pdf_path):
  
  questions = []
  
  # Extract text from PDF
  with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
      text += page.extract_text()
  
  # Identify keywords (replace with more sophisticated NLP techniques)
  keywords = ["who", "what", "when", "where", "why", "how"]

  # Generate questions based on keywords
  for sentence in text.split("."):
    for keyword in keywords:
      if keyword in sentence.lower():
        question = sentence.strip() + "?"
        questions.append(question)
  
  return questions

# Example usage
pdf_file = "sample.pdf"
questions = generate_questions(pdf_file)

# Print generated questions
for question in questions:
  print(question)

