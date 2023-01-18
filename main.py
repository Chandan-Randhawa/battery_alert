import openai
from docxtpl import DocxTemplate

api_key = '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'

openai.api_key = api_key

aa = input('which type of letter you want: ')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=aa,
  temperature=0.3,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

msg = response['choices'][0]['text']

doc = DocxTemplate('openaiword.docx')
context = {
  'message': msg
}
doc.render(context)
doc.save('new_doc.docx')