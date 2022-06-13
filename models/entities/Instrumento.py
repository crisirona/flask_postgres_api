class Instrumento():
    def __init__(self, id, name=None,marca=None,categoria=None,sucursal=None) -> None:
        self.id=id
        self.name=name
        self.marca=marca
        self.categoria=categoria
        self.sucursal=sucursal

    def to_JSON(self):
        return{
            'id':self.id,
            'name':self.name,
            'marca':self.marca,
            'categoria':self.categoria,
            'sucursal':self.sucursal
        }
