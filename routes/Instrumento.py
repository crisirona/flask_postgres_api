from flask import Blueprint
from flask import jsonify,request
from models.entities.Instrumento import Instrumento
from flask_cors import CORS
import random
def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

#models
from models.InstrumentoModel import InstrumentoModel

main=Blueprint('instrumento_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        instrumentos = InstrumentoModel().get_instrumentos()
        return jsonify(instrumentos)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('names/<suc>')
def get_inst_name(suc):
    try:
        instrumentos = InstrumentoModel().get_instrumentos_name(suc)
        return jsonify(instrumentos)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/<id>')
def get_movie(id):
    try:
        instrumento = InstrumentoModel().get_sucursal(id)
        if instrumento != None:    
            return jsonify(instrumento)
        else:
            return jsonify({'message':'no se encuentra'}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('sucursal/<inst>')
def sucur(inst):
    try:
        instrumento = InstrumentoModel().get_sucursal(inst)
        if instrumento != None:    
            return jsonify(instrumento)
        else:
            return jsonify({'message':'no se encuentra'}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('au/<inst>')
def sdf(inst):
    try:
        instrumento = InstrumentoModel().get_inst(inst)
        if instrumento != None:    
            return jsonify(instrumento)
        else:
            return jsonify({'message':'no se encuentra'}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('di/<inst>/<suc>/<lim>')
def sdf2(inst,suc,lim):
    try:
        instrumento = InstrumentoModel().get_inst_lim(inst,suc, lim)
        if instrumento != None:    
            return jsonify(instrumento)
        else:
            return jsonify({'message':'no se encuentra'}),404
    except Exception as ex:
        return jsonify({'message':str(ex)}),500


@main.route('/add',methods=['POST'])
def add_movie():
    try:
        unique_sequence = uniqueid()
        id1 = round(next(unique_sequence)/100)
        name=request.json['name']
        categoria=request.json['categoria']
        marca=request.json['marca']
        sucursal=request.json['sucursal']
        instrumento = Instrumento(id1,name,categoria,marca,sucursal)

        
        affected_rows = InstrumentoModel.add_instrumento(instrumento)
        if affected_rows ==1:

            return jsonify(instrumento.id)
        else:
            return jsonify({'message':'no se inserta'}),500
    except Exception as ex:
        return jsonify({'message':str(ex)}),500

@main.route('/update/<id>',methods=['PUT'])
def update_movie(id):
    try:
        name=request.json['name']
        categoria=request.json['categoria']
        marca=request.json['marca']
        sucursal=request.json['sucursal']
        instrumento = Instrumento(id,name,categoria,marca,sucursal)

        
        affected_rows = InstrumentoModel.update_instrumento(instrumento)
        if affected_rows ==1:

            return jsonify(instrumento.id)
        else:
            return jsonify({'message':'no se actualiza'}),500
    except Exception as ex:
        return jsonify({'message':str(ex)}),500


@main.route('/delete/<id>',methods=['DELETE'])
def delete_movie(id):
    try:
        instrumento = Instrumento(id)

        
        affected_rows = InstrumentoModel().delete_instrumento(instrumento)
        if affected_rows ==1:

            return jsonify(instrumento.id)
        else:
            return jsonify({'message':'no se elimina'}),500
    except Exception as ex:
        return jsonify({'message':str(ex)}),500




@main.route('/venta/<sucursal>/<name>',methods=['DELETE'])
def delete_instrumento(sucursal,name):
    try:
    
        affected_rows = InstrumentoModel.venta_instrumento(sucursal,name )
        if affected_rows ==1:

            return jsonify({'message':'Vendido '+ str(affected_rows)})
        else:
            return jsonify({'message':'no se elimina'}),500
    except Exception as ex:
        return jsonify({'message':str(ex)}),50

@main.route('/aumentar/<sucursal>/<name>',methods=['POST'])
def aumentar_stock():
    try:
        unique_sequence = uniqueid()
        id1 = round(next(unique_sequence)/100)
        name=request.json['name']
        categoria=request.json['categoria']
        marca=request.json['marca']
        sucursal=request.json['sucursal']
        instrumento = Instrumento(id1,name,categoria,marca,sucursal)

        
        affected_rows = InstrumentoModel.add_instrumento(instrumento)
        if affected_rows ==1:

            return jsonify(instrumento.id)
        else:
            return jsonify({'message':'no se inserta'}),500
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
