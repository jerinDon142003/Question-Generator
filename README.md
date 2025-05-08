create readme for this code
import PyPDF2

def generate\_questions(pdf\_path):

questions = \[]

# Extract text from PDF

with open(pdf\_path, 'rb') as pdf\_file:
pdf\_reader = PyPDF2.PdfReader(pdf\_file)
text = ""
for page in pdf\_reader.pages:
text += page.extract\_text()

# Identify keywords (replace with more sophisticated NLP techniques)

keywords = \["who", "what", "when", "where", "why", "how"]

# Generate questions based on keywords

for sentence in text.split("."):
for keyword in keywords:
if keyword in sentence.lower():
question = sentence.strip() + "?"
questions.append(question)

return questions

# Example usage

pdf\_file = "sample.pdf"
questions = generate\_questions(pdf\_file)

# Print generated questions

for question in questions:
print(question)
