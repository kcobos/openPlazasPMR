class plaza:
      def __init__ (self, direccion, numero, plazas, nota, latitud, longitud ):
            self.direccion = direccion
            self.numero = numero
            self.plazas = plazas
            self.nota = nota
            self.latitud = latitud
            self.longitud = longitud

      def csv_header():
            return "direccion,numero,plazas,nota,latitud,longitud"

      def csv( self ):
            return "{}, {}, {}, {}, {}, {}".format(self.direccion,self.numero,self.plazas,self.nota,self.latitud,self.longitud)
