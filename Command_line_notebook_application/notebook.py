import datetime
#use a variable to store the note_id, initialize to zero
note_id = 0

class Note:
   """Represent a note in the notebook. Match against a string in ssearches and store tags for each one"""
   def __init__(self, memo, tags=""):
      """initialize a note with memo and optional space-separated tags.
      Automatically set the note's creation date and a unique id"""

      self.memo = memo
      self.tags = tags
      self.creation_date = datetime.date.today()
      global note_id
      note_id += 1
      self.id = note_id

   def match(self, filter):
      """Determine if this note matches the filter text. Return True if it matches, False otherwise."""
      return filter in self.memo or filter in self.tags

class Books:
   """Represent a collection of notes that can be tagged, modified and searched."""

   def __init__(self):
      """initialize a notebook with an empty list."""
      self.notes = []

   def new_note(self, memo, tags=""):
      """create a few mnotes and add it to the list."""
      self.notes.append(Note(memo, tags))
#   
#   def modify_tags(self, note_id, tags):
#      """find the note with the given id and change its tags to the given value."""
#      for note in self.notes:
#         if note.id == note_id:
#            note.tags = tags
#           break

#   def modify_memo(self, note_id, memo):
#      """find a note with a given id and change its memo to a value"""
#      for note in self.notes:
#         if note.id == note_id:
#            note.memo = memo
#            break
#      """
   """since modify_tags and modify_memo aearches for a note with its id to make a change to it, we can refactor this way"""
   def _find_note(self, note_id):
      """locate the note using its id"""
      for note in self.notes:
         if str(note.id) == str(note_id):
            return note
      return None

   def modify_memo(self, note_id, memo):
      """find a note with the given id and change its memo"""
      note = self._find_note(note_id)
      if note:
         note.memo = memo
         return True 
      return False

   def modify_tags(self, note_id, tags):
      """find the note with the given id and change its tags"""
      self._find_note(note_id).tags = tags
       
   def search(self, filter):
      """Find all notes that maatch the given filter"""
      return [note for note in self.notes if note.match(filter)]