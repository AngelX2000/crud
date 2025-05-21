from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

usuarios=[]
id_contador=1



@app.route("/", methods=["GET", "POST"])
def crud():
    global id_contador


    if request.method=="POST":  #si accedemos a la ruta con datos en el formulario
        nombre=request.form.get("nombre") #guarda en una variable de python lo que el usuario entrega en el form
        email=request.form.get("email")
        usuarios.append({"id":id_contador, "nombre_usuario": nombre, "correo_usuario": email}) #insertando usuario
        id_contador+=1
        return redirect(url_for("crud"))
    

    id_eliminar=request.args.get("borrar") #siempre queda como texto
    if id_eliminar:  #si me entregan un id a eliminar
        #TODO: Eliminar el usuario con el id del parametro de la lista
        for item in usuarios:
            if str(item['id'])==id_eliminar:
                usuarios.remove(item)
                break
        return redirect(url_for("crud"))  #llamar al nombre de la funcion



    return render_template("registro.html", usuarios=usuarios) #lista que entregamos al html



#ruta de actualizacion de datos del usuario
@app.route("/update/<int:id>", methods=["GET","POST"]) #<int:id> significa que toma una variable de tipo numero entero que sera el numero asociado al usuario 
def update(id):
    print(usuarios) #esta es la lista global
    estudiante_a_editar=''
    #TODO: identificar el diccionario del usuario con id integer 
    for diccionario in usuarios:
        if diccionario['id']==id:
            estudiante_a_editar=diccionario
            print("El estudiante a editar es: ", estudiante_a_editar)
            break


#si despues de recorrer la lista, no encontramos el id entregado
    if estudiante_a_editar=='':
        return f"no existe el usuario con el id: {id}" #salgo de la funcion


    if request.method=='POST':
        estudiante_a_editar['nombre_usuario']=request.form.get('nombre')
        estudiante_a_editar['correo_usuario']=request.form.get('email')

        return redirect(url_for("crud"))


    return render_template("editar.html", estudiante_a_editar=estudiante_a_editar)



if __name__=="__main__":
    app.run(debug=True)

    



