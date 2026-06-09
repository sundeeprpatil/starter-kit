from openai import OpenAI
from pydantic import BaseModel
import os 


c = OpenAI(
    base_url= os.environ["OPENAI_API_URL_MODERN"],
    api_key=os.environ["GITHUB_KEY"]
)






## Image use case 
import base64
with open('./data/sample_img.png', "rb") as f :
    image_data = f.read()
img_data  = base64.b64encode(image_data).decode()
messages  = [{"role":"user", "content": [{"type": "text", "text": "describe the image"},
{"type": "image_url", "image_url": {"url":f"data:image/png;base64, {img_data}"}} ]
}]

# PDF use case
import fitz 
pdf_path = r'./data/download.pdf'

f = fitz.open(pdf_path) 
text_content = '\n --PAGE BREAK-- \n'.join([ff.get_text() for ff in f ])


r = c.chat.completions.create(
    model="gpt-4o-mini",
    messages= messages

)

print(f'{r}')

# Bring data into a structure + validate
question = " what is 8x 8 + 29 + 43. Return the number as JSON format "
messages = [{"role": "system", "content": "you are expert math "},
{"role": "user", "content": f"use the {question} and format reponse  in JSON"}] 

from pydantic import BaseModel
class JsonREsponse(BaseModel):
    contents: list[int]
    total: float 

r = c.chat.completions.parse(
    model = 'gpt-4o-mini',
    messages = messages,
    response_format = JsonREsponse
)

#Streaming example 
messages = [{"role": "system", "content": "you are a creative software engineer "},
{"role" : "user", "content": "explain streaming"} 
]

r = c.chat.completions.create(
    model = 'gpt-4o-mini',
    messages = messages,
    stream = True
)


text= ''
for chunk in r : 
    if len(chunk.choices) > 0 :
        if chunk.choices[0].delta.content is not None: 
            print(chunk.choices[0].delta.content)
            text +=chunk.choices[0].delta.content



