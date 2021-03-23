note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

#Question 4 a
def moyenne(liste):
    somme = []
    for note in liste:
      if note[0] == "eleve1":
        somme.append(note[2])
    return sum(somme)/len(somme)

print(moyenne(notes))



#Question 4 b
def moyennemath(liste):
    somme = []
    for note in liste:
      if note[0] == "eleve1" and note[1] == "math":
        somme.append(note[2])
    return sum(somme)/len(somme)

print(moyennemath(notes))


#Question 4 c
def moyenne_tuples(liste, eleve, matiere):
  somme = []
  for note in liste:
    if note[0] == eleve and note[1] == matiere:
      somme.append(note[2])
    return sum(somme)/len(somme)

print(moyenne_tuples(notes, "eleve1", "math"))

#Question 5
class Note:
  def __init__(self, eleve, matiere, valeur): 
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onotes = Note('eleve1', 'maths', 13)
print(onotes.eleve)
print(onotes.matiere)
print(onotes.valeur)
Note.afficher(onotes)


