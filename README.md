# Yatzi-api

## Installationsguide

Yatzi-api'et kræver installation af pakkerne fastapi og uvicorn, som skal installeres med pip:

> pip install fastapi[standard]
> pip install uvicorn

Hvis det ønskes, kan api'et køres i et virtuelt environment, som oprettes således:

> python -m venv .venv

Og aktiveres således (windows/mac):
> .venv\Scripts\activate 
eller
> source .venv/bin/activate


# Kørselsguide

API'et køres med kommandoen:
> fastapi dev app.py

og dernæst åbnes swagger-docs på linket i terminalen: http://127.0.0.1:8000/docs

API'et kører på denne måde i developer-mode, hvilket betyder at ændringer i koden med det samme opdateres  i UI'et (front-enden, swagger-docs).

Leg rundt med det og prøv de forskellige endpoints!

API'et stoppes ved at skrivt CTRL + C i terminalen. 