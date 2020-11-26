class Film(object):
    # Initializer / Instance Attributes
    def __init__(self, titel,score,stars,genres,titleImage,runtime,year,description):
        self.titel=titel
        self.score=score
        self.stars=stars
        self.genres=genres
        self.titleImage=titleImage
        self.runtime=runtime
        self.year=year
        self.description=description
