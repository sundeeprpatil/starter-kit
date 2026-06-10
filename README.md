# Getting started with using LLMs as endpoints

Different modalities covered
- *"Unstructured to structured + validate"*
- *"Review image and talk about it"*
- *"Streaming example"*
- *"Extract text and feed into prompt"*



```python

starter_kit.py  # text, image, and multimodality usecase 
model_list.py # shows all models available


``` 

# Set up

```
export GITHUB_TOKEN=<your token>
```

# check git user is authenticated  
```
curl -H "Authorization: Bearer $GITHUB_TOKEN" https://api.github.com/user

```

# github model list 
```
curl -L   -H "Accept: application/vnd.github+json"   -H "Authorization: Bearer $GITHUB_TOKEN"   -H "X-GitHub-Api-Version: 2026-03-10"   https://models.github.ai/catalog/models

```


```
# TEXT only 
{"role": "user" , "content" : "...my text ..."}

# LLM likes string : binary -> ascii byte -> ascii

img_data = base64.b64encode(f.read()).decode("utf-8") 

# content will be list of typed blocks
{"role" : "user", "content": [
   {"type":"text", "text" : "<instruction for the task>"}, 
   {"type":"image_url","image_url":{"url":"data:<image_type>;base64,<img_data>"} } 
]}
```

# Summary 


|Key| Exactly| Why |
|------|-------|----|
|"role"|"system","user", "assistant"| API rejects anything else|
|"content"| string or list of content blocks/ typed blocks | only these 2 shape |
|"type"| "text" or "image_url"| discriminator for block type|
|"text"| inside text block :) |  do not call it  "prompt" or "message"|
|"image_url"|  both as type and nested key | Required | 
|"url"| within image_url object| actual data URL or HTTP URL : "data:/image/png;base,{img_data}"|

