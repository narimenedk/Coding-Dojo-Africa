from flask import redirect, render_template, request, session, flash
from flask_app import app
from flask_app.models.recipe import Recipe 
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/recipes/create')
def create():
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template('create.html', logged_user = logged_user)

@app.route('/recipes/new', methods=['POST'])
def new_recipe():
    # print(request.form)
    if 'user_id' not in session:
        flash('Please log in to view this page', 'register')
        return redirect('/login')
    
    if not Recipe.validate_create(request.form):
        return redirect('/recipes')
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instruction': request.form['instruction'],
        'under_cook': request.form.get('under_cook', 'no'),  # Assuming under_cook is optional with default value 'no'
        'user_id': session['user_id']
    }
    Recipe.create(data)
    return redirect('/recipes')


# @app.route('/recipes/<int:id>')
# def show_recipe(id):
#     data = {'id': id}
#     recipe = Recipe.get_by_id(data)
#     return render_template("recipe.html" , recipe=recipe)

@app.route('/recipes/<int:id>')
def show_recipe(id):
    data = {'id': id}
    recipe = Recipe.get_by_id(data)
    logged_user = User.get_by_id({'id': session['user_id']})  # Fetch logged in user
    return render_template("recipe.html", recipe=recipe, logged_user=logged_user)

@app.route('/recipes/edit/<int:id>')
def edit_recipes(id):
    data = {'id': id}
    recipe = Recipe.get_by_id(data)
    return render_template("edit_recipe.html" , recipe=recipe)


# @app.route('/recipes/update/<int:id>', methods=['POST'])
# def update_recipe():
#     data = request.form
#     Recipe.update(data)
#     return redirect('/recipes')

@app.route('/recipes/update/<int:id>', methods=['POST'])
def update_recipe(id):
    # print(request.form)
    if not Recipe.validate_update(request.form):
        return redirect('/recipes')
    data = request.form
    Recipe.update({'id': id}, data)
    return redirect('/recipes')





