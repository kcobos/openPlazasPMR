from plaza import plaza

class ciudad:
    def __init__ ( self, file ):
        self.pmrs = []
        pass

    def add( self, pmr ):
        self.pmrs.append( pmr )

    def csv( self ):
        """ Devuelve el array en CSV """
        csv = ""
        csv = csv + plaza.csv_header()
        for pmr in self.pmrs:
            csv = csv + pmr.csv() 

        return csv

    
    def json( self):
        """ Devuelve el array de PMRs en JSON """
        pass
