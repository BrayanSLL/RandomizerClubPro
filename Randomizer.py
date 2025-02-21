import tkinter as tk
import random

# Liste des compositions et leurs postes
formations = {
    "4-4-2": ["GB", "DD", "DC", "DC", "DG", "MC", "MC", "MG", "MD", "BU", "BU"],
    "4-3-3": ["GB", "DD", "DC", "DC", "DG", "MC", "MC", "MC", "AD", "AG", "BU"],
    "3-5-2": ["GB", "DC", "DC", "DC", "MG", "MD", "MC", "MC", "MOC", "BU", "BU"],
    "5-3-2": ["GB", "DD", "DC", "DC", "DC", "DG", "MC", "MC", "MC", "BU", "BU"],
    "4-2-3-1": ["GB", "DD", "DC", "DC", "DG", "MC", "MC", "MOC", "AD", "AG", "BU"],
}

def randomize():
    players = entry_players.get("1.0", tk.END).strip().split("\n")
    players = [p.strip() for p in players if p.strip()]  # Nettoyer la liste
    
    if not players:
        result_label.config(text="Ajoutez au moins un joueur.")
        return
    
    formation = random.choice(list(formations.keys()))
    positions = random.sample(formations[formation], len(players))  # Tirage totalement aléatoire
    random.shuffle(players)
    
    result_text = f"Formation : {formation}\n" + "\n".join(f"{players[i]} -> {positions[i]}" for i in range(len(players)))
    result_label.config(text=result_text)

# Création de l'interface
tk_app = tk.Tk()
tk_app.title("Bevebance Randomizer")

tk.Label(tk_app, text="Entrez les joueurs (un par ligne) :").pack()
entry_players = tk.Text(tk_app, height=10, width=30)
entry_players.pack()

tk.Button(tk_app, text="Randomize !", command=randomize).pack()
result_label = tk.Label(tk_app, text="", justify="left")
result_label.pack()

tk_app.mainloop()