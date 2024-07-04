from fastapi import FastAPI


app = FastAPI()
@app.get("/")
async def root():
 return {"greeting":"Hello world"}

poid_du_corps = 78
poid_de_tete = 12

def calcul_mon_poid(poid_du_corps: int, poid_de_tete: int) -> int :
    total_poid: int = poid_du_corps + poid_de_tete
    return total_poid

total_poid = calcul_mon_poid(poid_du_corps, poid_de_tete)
print("mon poid total est de", total_poid, "kg")