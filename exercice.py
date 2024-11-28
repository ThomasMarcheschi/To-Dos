# Fonction pour lister les todos - à réaliser 
def lister_todos():
  i = 0
  if list_of_todo == []:
    print("Votre To-Do liste est vide.")
  else :
    print("Vos tâches :")
    while i < len(list_of_todo):
      print("- Tache", i+1,":",list_of_todo[i],",",status[i])
      i = i + 1

list_of_todo = []
status = []
 
# Fonction pour créer un todo - à réaliser 
def creer_todo():
  todo = input("Entrez le nom de votre tâche :")
  list_of_todo.append(todo)
  status.append("A faire")

# Fonction pour modifier le statut d'un todo - à réaliser 
def modifier_statut_todo(): 
  choice_todo = int(input("indiquer le numéro de la tache que vous souhaitez modifier :"))
  if status[choice_todo - 1] == "A faire":
    status[choice_todo - 1] = "Fait"
    print("La tâche ",choice_todo,"à été modifiée en Fait")
  elif status[choice_todo - 1] == "Fait" :
    status[choice_todo - 1] = "A faire"
    print("La tâche ",choice_todo,"à été modifiéé en A faire")
 
# Fonction pour supprimer un todo - à réaliser 
def supprimer_todo(): 
  print('Fonctionnalité "supprimer un todo" à venir') 

# Menu principal 
choix = ' ' 
while choix !=  'q' : 
  # Affichage des choix 
  print('\n==== Menu principal ====') 
  print('1: Lister les todos') 
  print('2: Créer un todo') 
  print('3: Changer le statut d\'un todo') 
  print('4: Supprimer un todo')
  print('q: quitter') 
  print('========================') 
  # Actions suivant le choix 
  choix = input('=> Choix : ') 
  match choix: 
    case '1': lister_todos() 
    case '2': creer_todo() 
    case '3': modifier_statut_todo() 
    case '4': supprimer_todo() 
    case 'q': print('Au revoir') 
    case _: print('Choix invalide')
