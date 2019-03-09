from plaza import plaza
import json

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
            print(pmr)
            csv = csv + pmr.csv()

        return csv


    def json( self):
        """ Devuelve el array de PMRs en JSON """
        js = []
        for pmr in self.pmrs:
            js.append(pmr)
        return json.dumps([ob.__dict__ for ob in js])
