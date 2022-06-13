from database.db import get_connection
from .entities.Instrumento import Instrumento

class InstrumentoModel():
    
    @classmethod
    def get_instrumentos(self):
        try:
            connection=get_connection()
            instrumentos=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id,name,marca,categoria,sucursal FROM Instrumento ")
                resultset=cursor.fetchall()

                for row in resultset:
                    instrumento=Instrumento(row[0],row[1],row[2],row[3],row[4])
                    instrumentos.append(instrumento.to_JSON())
            
            connection.close()
            return instrumentos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_instrumentos_name(self,suc):
        try:
            connection=get_connection()
            instrumentos=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT name,Count(id) FROM instrumento Where sucursal=%s group by name;",(suc,))
                resultset=cursor.fetchall()
                dic={}
                for row in resultset:
                    dic[row[0]]=row[1]
            
            connection.close()
            return dic
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_instrumento(self,id):
        try:
            connection=get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT id,name,marca,categoria,sucursal FROM instrumento WHERE id= %s",(id,))
                row = cursor.fetchone()
                instrumento = None

                if row != None:
                    instrumento=Instrumento(row[0],row[1],row[2],row[3],row[4])
                    instrumento = instrumento.to_JSON()
            connection.close()
            return instrumento
        except Exception as ex:
            raise Exception(ex)


    
    @classmethod
    def get_sucursal(self,inst):
        try:
            connection=get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT sucursal, COUNT(id) FROM instrumento WHERE name=%s group by sucursal;",(inst,))
                row = cursor.fetchall()
                if row != None:
                    k=len(row)
                    s={}
                    for i in range(k):
                        s[str(i)]= str(row[i])
                    
                    
            connection.close()
            return s
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_inst(self,inst):
        try:
            connection=get_connection()
            
            with connection.cursor() as cursor:
                
                cursor.execute("SELECT name, categoria, marca FROM instrumento WHERE name=%s limit 1;",(inst,))
                row = cursor.fetchone()
                if row != None:
                    k=len(row)
                    s={}
                    for i in range(k):
                        s[str(i)]= str(row[i])
                    
                    
            connection.close()
            return s
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def get_inst_lim(self,inst,suc,lim):
        try:
            connection=get_connection()
            
            with connection.cursor() as cursor:
                
                cursor.execute("SELECT id FROM instrumento WHERE name=%s and sucursal=%s limit %s;",(inst,suc,lim))
                row = cursor.fetchall()
             
                    
            connection.close()
            return row
        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def add_instrumento(self,instrumento):
        try:
            connection=get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO instrumento (id,name,marca,categoria,sucursal) 
                VALUES (%s,%s,%s,%s,%s)""",(instrumento.id,instrumento.name,instrumento.marca,instrumento.categoria,instrumento.sucursal))
                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_instrumento(self,instrumento):
        try:
            connection=get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE  instrumento SET name=%s,categoria=%s,marca=%s,sucursal=%s 
                WHERE id = %s""",(instrumento.name,instrumento.marca,instrumento.categoria,instrumento.sucursal,instrumento.id))
                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_instrumento(self,instrumento):
        try:
            connection=get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM instrumento WHERE id=%s;",(instrumento.id,))
                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def venta_instrumento(self,sucursal,name):
        try:
            connection=get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute("DELETE from instrumento WHERE id = (SELECT id from instrumento WHERE sucursal=%s AND name =%s limit 1);",(sucursal,name,))
                #row = cursor.fetchone()
                affected_rows = cursor.rowcount
                connection.commit()
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)