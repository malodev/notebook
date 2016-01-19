import datetime
# Store the next available id for all new notes

class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''
    last_id = 0

    def __init__(self, memo, tags=''):
        '''initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        Note.last_id += 1
        self.id = Note.last_id

    def match(self, filtro, case_sensitive = True):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.'''
        if not case_sensitive:
            memo = self.memo.lower()
            tags = self.tags.lower()
            filtro = filtro.lower()
        else:
            memo = self.memo
            tags = self.tags

        return filtro in memo or filtro in tags

class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''
    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []
    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))
    def search(self, filter, case_sensitive = True):
        '''Find all notes that match the given filter
        string.'''
        return [note for note in self.notes if
        note.match(filter, case_sensitive)]

    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if note.id == note_id:
                return note
            return None

    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
        memo to the given value.'''
        note = self._find_note(note_id)
        if note is None:
            return None
        else:
            note.memo = memo
            return note

    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its
        memo to the given value.'''
        note = self._find_note(note_id)
        if note is None:
            return None
        else:
            note.tags = tags
            return note