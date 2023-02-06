import tkinter as tk

def calcul() :
    masse = float(entry1.get())
    taille = float(entry2.get())

    imc = masse / (taille**2)

    affichage1.config(text=f"Votre imc est de : {imc:.2f}")

    if imc < 18.5 :
        affichage2.config(text="Vous êtes trop maigre.")
    elif imc > 25 :
        affichage2.config(text="Vous êtes en surpoids.")
    else :
        affichage2.config(text="Vous avez une corpulance normal.")

root = tk.Tk()
root.geometry("300x200")
root.title("Calculateur d'IMC :")

label_p = tk.Label(root , text="Poid en kg :")
label_p.pack()

entry1 = tk.Entry(root)
entry1.pack()

label_t = tk.Label(root ,text="Taille en mètres :")
label_t.pack()

entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root, text="Calculer mon IMC", command=calcul)
button.pack()

affichage1 = tk.Label(root, text="Résultat ...")
affichage1.pack()

affichage2 = tk.Label(root, text="")
affichage2.pack()

root.mainloop()