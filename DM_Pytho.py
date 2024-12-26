import tkinter as tk
from tkinter import messagebox
import csv
import os

CLIENTS_CSV = "Clients.csv"
DEVIS_CSV = "Devis.csv"

# ------------------------- PARTIE CLIENT ------------------------- #

def creer_csv_clients():
    try:
        if not os.path.isfile(CLIENTS_CSV):
            with open(CLIENTS_CSV, 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(["ID Client", "Nom client", "Contact", "Tel", "Adresse", "Code Postal", "Ville", "Mail"])
    except IOError as e:
        messagebox.showerror("Erreur", f"Impossible de créer le fichier Clients.csv : {e}")

def creer_csv_devis():
    try:
        if not os.path.isfile(DEVIS_CSV):
            with open(DEVIS_CSV, 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(["Client", "Description", "Quantité", "Prix Unitaire", "Remise (%)", "Total"])
    except IOError as e:
        messagebox.showerror("Erreur", f"Impossible de créer le fichier Devis.csv : {e}")

def ajouter_client(data):
    try:
        with open(CLIENTS_CSV, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(data)
    except IOError as e:
        messagebox.showerror("Erreur", f"Impossible d'ajouter le client : {e}")

def rechercher_client(nom):
    try:
        if not os.path.isfile(CLIENTS_CSV):
            messagebox.showinfo("Information", "Aucun client n'a été enregistré.")
            return
        with open(CLIENTS_CSV, 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                if row["Nom client"].strip().upper() == nom.upper():
                    result = (f"Client trouvé:\n"
                              f"ID: {row['ID Client']}\n"
                              f"Nom: {row['Nom client']}\n"
                              f"Contact: {row['Contact']}\n"
                              f"Téléphone: {row['Tel']}\n"
                              f"Adresse: {row['Adresse']}\n"
                              f"Code Postal: {row['Code Postal']}\n"
                              f"Ville: {row['Ville']}\n"
                              f"Mail: {row['Mail']}")
                    messagebox.showinfo("Résultat", result)
                    return
            messagebox.showinfo("Résultat", "Client non trouvé.")
    except IOError as e:
        messagebox.showerror("Erreur", f"Impossible de lire le fichier Clients.csv : {e}")

def supprimer_client(nom):
    try:
        if not os.path.isfile(CLIENTS_CSV):
            messagebox.showinfo("Information", "Aucun client n'a été enregistré.")
            return
        with open(CLIENTS_CSV, 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            rows = list(reader)
        with open(CLIENTS_CSV, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=reader.fieldnames, delimiter=';')
            writer.writeheader()
            found = False
            for row in rows:
                if row["Nom client"].strip().upper() != nom.upper():
                    writer.writerow(row)
                else:
                    found = True
            if found:
                messagebox.showinfo("Succès", f"Le client '{nom}' a été supprimé avec succès.")
            else:
                messagebox.showinfo("Résultat", "Client non trouvé.")
    except IOError as e:
        messagebox.showerror("Erreur", f"Impossible de modifier le fichier Clients.csv : {e}")

def interface_creation_client():
    def enregistrer():
        data = [
            entry_id_client.get(),
            entry_nom_client.get().upper(),
            entry_contact.get(),
            entry_tel.get().replace(" ", ""),
            entry_adresse.get().upper(),
            entry_code_postal.get(),
            entry_ville.get().upper(),
            entry_mail.get()
        ]
        ajouter_client(data)
        messagebox.showinfo("Succès", "Client enregistré avec succès")
        window.destroy()

    window = tk.Toplevel()
    window.title("Créer un Client")
    window.configure(bg="lightblue")
    window.geometry("400x500")

    tk.Label(window, text="Créer un Client", bg="lightblue", font=("Arial", 14, "bold")).pack(pady=10)

    frame = tk.Frame(window, bg="lightblue")
    frame.pack(pady=10)

    tk.Label(frame, text="ID Client", bg="lightblue").grid(row=0, column=0, pady=5)
    entry_id_client = tk.Entry(frame)
    entry_id_client.grid(row=0, column=1)

    tk.Label(frame, text="Nom client", bg="lightblue").grid(row=1, column=0, pady=5)
    entry_nom_client = tk.Entry(frame)
    entry_nom_client.grid(row=1, column=1)

    tk.Label(frame, text="Contact", bg="lightblue").grid(row=2, column=0, pady=5)
    entry_contact = tk.Entry(frame)
    entry_contact.grid(row=2, column=1)

    tk.Label(frame, text="Tel", bg="lightblue").grid(row=3, column=0, pady=5)
    entry_tel = tk.Entry(frame)
    entry_tel.grid(row=3, column=1)

    tk.Label(frame, text="Adresse", bg="lightblue").grid(row=4, column=0, pady=5)
    entry_adresse = tk.Entry(frame)
    entry_adresse.grid(row=4, column=1)

    tk.Label(frame, text="Code Postal", bg="lightblue").grid(row=5, column=0, pady=5)
    entry_code_postal = tk.Entry(frame)
    entry_code_postal.grid(row=5, column=1)

    tk.Label(frame, text="Ville", bg="lightblue").grid(row=6, column=0, pady=5)
    entry_ville = tk.Entry(frame)
    entry_ville.grid(row=6, column=1)

    tk.Label(frame, text="Mail", bg="lightblue").grid(row=7, column=0, pady=5)
    entry_mail = tk.Entry(frame)
    entry_mail.grid(row=7, column=1)

    tk.Button(frame, text="Enregistrer", command=enregistrer, bg="green", fg="white").grid(row=8, column=0, columnspan=2, pady=10)

def interface_recherche_client():
    def rechercher():
        nom = entry_nom.get().strip()
        if not nom:
            messagebox.showwarning("Attention", "Veuillez entrer un nom pour la recherche.")
            return
        rechercher_client(nom)

    window = tk.Toplevel()
    window.title("Rechercher un Client")
    window.configure(bg="lightblue")
    window.geometry("400x200")

    tk.Label(window, text="Rechercher un Client", bg="lightblue", font=("Arial", 14, "bold")).pack(pady=10)

    frame = tk.Frame(window, bg="lightblue")
    frame.pack(pady=10)

    tk.Label(frame, text="Nom du Client", bg="lightblue").grid(row=0, column=0, pady=5)
    entry_nom = tk.Entry(frame)
    entry_nom.grid(row=0, column=1)

    tk.Button(frame, text="Rechercher", command=rechercher, bg="blue", fg="white").grid(row=1, column=0, columnspan=2, pady=10)

def lister_clients():
    try:
        if not os.path.isfile(CLIENTS_CSV):
            messagebox.showinfo("Information", "Aucun client n'a été enregistré.")
            return
        with open(CLIENTS_CSV, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            clients = list(reader)
        if len(clients) <= 1:
            messagebox.showinfo("Information", "Aucun client n'est présent dans la base de données.")
            return
        list_window = tk.Toplevel()
        list_window.title("Liste des Clients")
        list_window.geometry("600x400")

        tk.Label(list_window, text="Liste des Clients", font=("Arial", 14, "bold")).pack(pady=10)

        listbox = tk.Listbox(list_window, width=80, height=20)
        listbox.pack(pady=10)

        for client in clients[1:]:
            listbox.insert(tk.END, f"ID: {client[0]} | Nom: {client[1]} | Contact: {client[2]} | Tel: {client[3]} | Adresse: {client[4]} | Code Postal: {client[5]} | Ville: {client[6]} | Mail: {client[7]}")

        tk.Button(list_window, text="Fermer", command=list_window.destroy).pack(pady=10)

    except IOError as e:
        messagebox.showerror("Erreur", f"Impossible de lire le fichier Clients.csv : {e}")

def interface_suppression_client():
    def supprimer():
        nom = entry_nom.get().strip()
        if not nom:
            messagebox.showwarning("Attention", "Veuillez entrer un nom pour la suppression.")
            return
        supprimer_client(nom)
        window.destroy()

    window = tk.Toplevel()
    window.title("Supprimer un Client")
    window.configure(bg="lightblue")
    window.geometry("400x200")

    tk.Label(window, text="Supprimer un Client", bg="lightblue", font=("Arial", 14, "bold")).pack(pady=10)

    frame = tk.Frame(window, bg="lightblue")
    frame.pack(pady=10)

    tk.Label(frame, text="Nom du Client", bg="lightblue").grid(row=0, column=0, pady=5)
    entry_nom = tk.Entry(frame)
    entry_nom.grid(row=0, column=1)

    tk.Button(frame, text="Supprimer", command=supprimer, bg="red", fg="white").grid(row=1, column=0, columnspan=2, pady=10)

def menu_gestion_clients():
    def ouvrir_creation_client():
        interface_creation_client()

    def ouvrir_recherche_client():
        interface_recherche_client()

    def ouvrir_suppression_client():
        interface_suppression_client()

    def ouvrir_liste_clients():
        lister_clients()

    gestion_window = tk.Toplevel()
    gestion_window.title("Menu Gestion des Clients")
    gestion_window.configure(bg="lightblue")
    gestion_window.geometry("400x350")

    tk.Label(gestion_window, text="Menu Gestion des Clients", bg="lightblue", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(gestion_window, text="Créer un Client", command=ouvrir_creation_client, width=25, height=2, bg="lightgreen").pack(pady=5)
    tk.Button(gestion_window, text="Rechercher un Client", command=ouvrir_recherche_client, width=25, height=2, bg="lightblue").pack(pady=5)
    tk.Button(gestion_window, text="Supprimer un Client", command=ouvrir_suppression_client, width=25, height=2, bg="red").pack(pady=5)
    tk.Button(gestion_window, text="Lister les Clients", command=ouvrir_liste_clients, width=25, height=2, bg="purple", fg="white").pack(pady=5)

# ------------------------- PARTIE DEVIS ------------------------- #

def calcul_total(quantite, prix_unitaire, remise):
    try:
        quantite = float(quantite)
        prix_unitaire = float(prix_unitaire)
        remise = float(remise)
        total = quantite * prix_unitaire * (1 - remise / 100)
        return round(total, 2)
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")
        return None

def saisie_devis():
    def calculer_total():
        total = calcul_total(entry_quantite.get(), entry_prix_unitaire.get(), entry_remise.get())
        if total is not None:
            label_total.config(text=f"Total: {total:.2f} €")

    def nettoyer_champs():
        entry_client.delete(0, tk.END)
        entry_description.delete(0, tk.END)
        entry_quantite.delete(0, tk.END)
        entry_prix_unitaire.delete(0, tk.END)
        entry_remise.delete(0, tk.END)
        label_total.config(text="Total: ")

    def enregistrer():
        total = calcul_total(entry_quantite.get(), entry_prix_unitaire.get(), entry_remise.get())
        if total is not None:
            try:
                with open(DEVIS_CSV, 'a', newline='') as file:
                    writer = csv.writer(file, delimiter=';')
                    writer.writerow([
                        entry_client.get().strip(),
                        entry_description.get().strip(),
                        entry_quantite.get(),
                        entry_prix_unitaire.get(),
                        entry_remise.get(),
                        total
                    ])
                messagebox.showinfo("Succès", "Devis enregistré avec succès.")
                nettoyer_champs()
            except IOError as e:
                messagebox.showerror("Erreur", f"Impossible d'enregistrer le devis : {e}")

    window = tk.Toplevel()
    window.title("Saisie des Devis")
    window.configure(bg="lightyellow")
    window.geometry("500x400")

    tk.Label(window, text="Saisie des Devis", bg="lightyellow", font=("Arial", 14, "bold")).pack(pady=10)

    frame = tk.Frame(window, bg="lightyellow")
    frame.pack(pady=10)

    tk.Label(frame, text="Client", bg="lightyellow").grid(row=0, column=0, pady=5)
    entry_client = tk.Entry(frame)
    entry_client.grid(row=0, column=1)

    tk.Label(frame, text="Description", bg="lightyellow").grid(row=1, column=0, pady=5)
    entry_description = tk.Entry(frame)
    entry_description.grid(row=1, column=1)

    tk.Label(frame, text="Quantité", bg="lightyellow").grid(row=2, column=0, pady=5)
    entry_quantite = tk.Entry(frame)
    entry_quantite.grid(row=2, column=1)

    tk.Label(frame, text="Prix Unitaire", bg="lightyellow").grid(row=3, column=0, pady=5)
    entry_prix_unitaire = tk.Entry(frame)
    entry_prix_unitaire.grid(row=3, column=1)

    tk.Label(frame, text="Remise (%)", bg="lightyellow").grid(row=4, column=0, pady=5)
    entry_remise = tk.Entry(frame)
    entry_remise.grid(row=4, column=1)

    label_total = tk.Label(frame, text="Total: ", bg="lightyellow", font=("Arial", 12, "bold"))
    label_total.grid(row=5, column=0, columnspan=2, pady=10)

    tk.Button(frame, text="Calculer Total", command=calculer_total, bg="green", fg="white").grid(row=6, column=0, pady=10)
    tk.Button(frame, text="Nettoyer", command=nettoyer_champs, bg="blue", fg="white").grid(row=6, column=1, pady=10)
    tk.Button(frame, text="Enregistrer", command=enregistrer, bg="orange", fg="white").grid(row=7, column=0, columnspan=2, pady=10)

def liste_devis():
    try:
        if not os.path.isfile(DEVIS_CSV):
            messagebox.showinfo("Information", "Aucun devis enregistré.")
            return  
        with open(DEVIS_CSV, 'r') as file:
            reader = csv.reader(file, delimiter=';')
            devis = list(reader)
        if len(devis) <= 1:
            messagebox.showinfo("Information", "Aucun devis présent dans la base de données.")
            return
        list_window = tk.Toplevel()
        list_window.title("Liste des Devis")
        list_window.geometry("600x400")

        tk.Label(list_window, text="Liste des Devis", font=("Arial", 14, "bold")).pack(pady=10)

        listbox = tk.Listbox(list_window, width=80, height=20)
        listbox.pack(pady=10)

        for d in devis[1:]:
            listbox.insert(tk.END, f"Client: {d[0]} | Description: {d[1]} | Total: {d[5]} €")

        tk.Button(list_window, text="Fermer", command=list_window.destroy).pack(pady=10)

    except IOError as e:
        messagebox.showerror("Erreur", f"Impossible de lire le fichier Devis.csv : {e}")

def interface_devis():
    devis_window = tk.Toplevel()
    devis_window.title("Gestion des Devis")
    devis_window.configure(bg="lightyellow")
    devis_window.geometry("400x200")

    tk.Label(devis_window, text="Gestion des Devis", bg="lightyellow", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(devis_window, text="Saisie des Devis", command=saisie_devis, bg="lightblue", width=20, height=2).pack(pady=5)
    tk.Button(devis_window, text="Liste des Devis", command=liste_devis, bg="lightblue", width=20, height=2).pack(pady=5)

# ------------------------- MENU PRINCIPAL ------------------------- #

def main():
    creer_csv_clients()
    creer_csv_devis()

    root = tk.Tk()
    root.title("Menu Principal")
    root.geometry("500x300")
    root.configure(bg="blue")

    tk.Label(root, text="DM D’ALGORITHMIE ET DE PYTHON 2024", bg="blue", fg="white", font=("Arial", 10, "bold")).pack(pady=10)
    tk.Label(root, text="Menu Principal", bg="blue", fg="white", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(root, text="Gestion des Clients", command=menu_gestion_clients, width=30, height=2, bg="lightgreen").pack(pady=5)
    tk.Button(root, text="Gestion des Devis", command=interface_devis, width=30, height=2, bg="lightyellow").pack(pady=5)
    tk.Button(root, text="Quitter", command=root.destroy, width=30, height=2, bg="lightcoral").pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
