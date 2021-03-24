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
print("4.a)")
def moyenne(liste):
    somme = []
    for note in liste:
      if note[0] == "eleve1":
        somme.append(note[2])
    return sum(somme)/len(somme)

print(moyenne(notes))



#Question 4 b
print("4.b)")
def moyennemath(liste):
    somme = []
    for note in liste:
      if note[0] == "eleve1" and note[1] == "math":
        somme.append(note[2])
    return sum(somme)/len(somme)

print(moyennemath(notes))


#Question 4 c
print("4.c)")
def moyenne_tuples(liste, eleve, matiere):
  somme = []
  for note in liste:
    if note[0] == eleve and note[1] == matiere:
      somme.append(note[2])
    return sum(somme)/len(somme)



#Question 5
print("5)")
class Note:
  instances = []
  def __init__(self, eleve, matiere, valeur): 
    self.eleve = eleve
    self.matiere = matiere 
    self.valeur = valeur
    self.instances.append(self)

  def __str__(self):
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')"

  @classmethod
  def vider(cls):
    cls.instances = []

  def afficher(self):
      print(self)

  @classmethod
  def moyenne(cls, eleve=None, matiere=None):
      note_eleve = [note for note in cls.instances if note.eleve == eleve] if eleve is not None else notes
      notes_matiere = [note for note in note_eleve if note.matiere == matiere] if matiere is not None else note_eleve
      return sum([note.valeur for note in notes_matiere])/len(notes_matiere)

onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)

onotes=[Note(a,b,c) for a,b,c in notes]
Note.moyenne('eleve1', 'math')

#Question 6 
print("6)")
print(onote)


#Question 8
print("8)")
def moyenne_notes(notes, eleve = None, matiere = None):
  note_eleve = [note for note in notes if note.eleve == eleve] if eleve is not None else notes
  notes_matiere = [note for note in note_eleve if note.matiere == matiere] if matiere is not None else note_eleve
  return sum([note.valeur for note in notes_matiere])/len(notes_matiere)

print(moyenne_notes(onotes))
print(moyenne_notes(onotes, 'eleve1', 'eco'))
