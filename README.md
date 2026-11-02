# Yatzy-api

## Installationsguide
Hvis du starter i teknologi_data_integration-mappen i terminalen:
> cd ..
> git clone https://github.com/atal-eaaa/my_first_api
> cd my_first_api





Hvis det ønskes, kan api'et køres i et virtuelt environment, som oprettes således:

> python -m venv .venv

Og aktiveres således (windows/mac):
> .venv\Scripts\activate 
eller
> source .venv/bin/activate

Yatzy-api'et kræver installation af pakkerne fastapi og uvicorn, som skal installeres med pip:

> pip install fastapi[standard]

> pip install uvicorn

# Kørselsguide

API'et køres med kommandoen:
> uvicorn main:app --reload

og dernæst åbnes swagger-docs på linket i terminalen: http://127.0.0.1:8000/docs

API'et kører på i reload-mode, hvilket betyder at ændringer i koden opdateres i UI'et (front-enden, swagger-docs) uden at skulle stoppe og tænde API'et igen.

Leg rundt med det og prøv de forskellige endpoints!

API'et stoppes ved at skrivt CTRL + C i terminalen. 

God fornøjelse!!!!