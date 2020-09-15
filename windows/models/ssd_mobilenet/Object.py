class Object:
    def __init__(self, box, score, category) -> None:
        self._box = box
        self._score = score
        self._category = category
        
    @property
    def box(self):
        return self._box
        
    @property
    def score(self):
        return self._score
        
    @property
    def category(self):
        return self._category
        