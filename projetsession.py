import streamlit as st

class Calculateur_Van():
    st.title("Calculateur de VAN")
    st.write("""Cette application vous permettra de faire le choix entre deux projets mutuellement exclusifs.""")



    def __init__(self, nombre_d_années, investissement_initial, flux_monétaires, taux_de_rendement ):
        self.nombre_d_années = nombre_d_années
        self.investissement_initial = investissement_initial
        self.flux_monétaires = flux_monétaires
        self.taux_de_rendement = taux_de_rendement

    def calcul_VA(self):
         VA = []
         for i in range (self.nombre_d_années):
             n=i+1
             va = (self.flux_monétaires[i])/(1+self.taux_de_rendement)**(n)
             VA.append(va)
             VAN = sum(VA) - (self.investissement_initial)
         
             
         return VAN
 


#partie pour le calcul du projet 1
st.sidebar.title("Données du projet 1")
flux = []
nombre_d_années = st.sidebar.number_input("Quelle est la durée du projet en années ?", step = 1, value = 3)
st.sidebar.write("Quels sont les flux monétaires attendus du projet en $ ?")
for i in range (nombre_d_années):
    n=i+1
    st.sidebar.write("Entrez le flux monétaire de l'année",n)
    flux_monétaire = st.sidebar.number_input('',key=n,step=1)
    flux.append(flux_monétaire)

investissement_initial = st.sidebar.number_input("Quel est l'investissement initial du projet en $ ?", step =1, value = 60000)
taux_de_rendement = st.sidebar.number_input("Quel est le taux de rendement du projet? Exemple écrivez 0.1 pour dire 10%", value = 0.1)
st.title("Calcul de la VAN du Projet 1")
projet1 =  Calculateur_Van(nombre_d_années,investissement_initial,flux,taux_de_rendement)
projet1.calcul_VA()

resultat_projet1 = projet1.calcul_VA()
st.write(f"Voici le resultat de la VAN du projet 1 : ", round(resultat_projet1,2), "$")  



#partie pour le  calcul du projet2
st.sidebar.title("Données du projet 2")
flux2 = []
nombre_d_années2 = st.sidebar.number_input("Quelle est la durée du projet en années ?", step = 1, value = 2)
st.sidebar.write("Quels sont les flux monétaires attendus du projet en $ ?")
for k in range (nombre_d_années2):
    y=k+1
    x=k*10
    st.sidebar.write("Entrez le flux monétaire de l'année",y)
    flux_monétaire2 = st.sidebar.number_input('',key=x,step=1)
    flux2.append(flux_monétaire2)
investissement_initial2 = st.sidebar.number_input("Quel est l'investissement initial du projet en $?", step =1, value = 60000)
taux_de_rendement2 = st.sidebar.number_input("Quel est le taux de rendement du projet? Exemple écrivez 0.2 pour dire 20%", value = 0.2)
st.title("Calcul de la VAN du Projet 2")
projet2 = Calculateur_Van(nombre_d_années2,investissement_initial2,flux2,taux_de_rendement2)
projet2.calcul_VA()
resultat_projet2 = projet2.calcul_VA()
st.write(f"Voici le resultat de la VAN du projet 2 :" ,round(resultat_projet2, 2), "$")
  


if st.button('Afficher le projet le plus rentable'):
    if resultat_projet1 < 0 and resultat_projet2 < 0 :
        st.write("Malheureusement, aucun des deux projets n'est rentable.")
        
    elif resultat_projet2 > resultat_projet1:
        st.write('Le projet le plus rentable est le projet 2.')
    elif resultat_projet1 > resultat_projet2:
        st.write('Le projet le plus rentable est le projet 1.')
   
    


             

        


        


        


 