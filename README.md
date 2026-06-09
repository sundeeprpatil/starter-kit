# Getting started with using LLMs as endpoints

Different modalities 
*"Unstructured to structured + validate"*
*"Review image and talk about it"*
*"Streaming example"*
*"Extract text and feed into prompt"*



Starter kit to showscase how to use free tier github models
```
starter_kit.py # text, image, and multimodality usecase 
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