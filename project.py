from flask import Flask, render_template, request, redirect, jsonify
from flask import url_for, flash, Blueprint
from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from catalog_database import Base, Categories, Items, User, Comments
from sqlalchemy import and_, or_, not_
from flask import session as login_session

from authorization import simple_page
from authorization import createUser, getUserInfo, getUserID
from authorization import login_required, user_authed

app = Flask(__name__)
app.register_blueprint(simple_page)

# Connect to Database and create database session
engine = create_engine('sqlite:///catalogproject.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# JSON functions
@app.route('/categories/JSON')
def categoriesJSON():
    """renders JSON format of all the categories"""
    categories = session.query(Categories).all()
    return jsonify(categories=[c.serialize for c in categories])


@app.route('/categories/<int:category_id>/item/JSON')
def categoriesItemJSON(category_id):
    """renders JSON format of all the items in each category"""
    category = session.query(Categories).filter_by(id=category_id).one()
    items = session.query(Items).filter_by(category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])


@app.route('/categories/<int:category_id>/item/<item_id>/JSON')
def itemJSON(category_id, item_id):
    """renders JSON format of each particular item"""
    category_Items = session.query(Items).filter_by(id=item_id).one()
    return jsonify(Items=category_Items.serialize)


# Show all categories
@app.route('/')
@app.route('/categories/')
def showCategories():
    """Landing page. Shows all the categories and the latest items added"""
    categories = session.query(Categories).order_by(asc(Categories.name))
    items = session.query(Items).order_by(desc(Items.created_date)).limit(7)
    logged_in = 'username' in login_session
    if 'username' not in login_session:
        return render_template('publicCategories.html', categories=categories,
                               items=items, logged_in=logged_in)
    else:
        return render_template('categories.html', categories=categories,
                               items=items, logged_in=logged_in,
                               username=login_session['username'])


# Create new Category
@app.route('/categories/new/', methods=['GET', 'POST'])
@login_required
def newCategory():
    """Renders and creates new categories for the catalog"""
    if request.method == 'POST':
        if request.form['name']:
            newCategory = Categories(name=request.form['name'],
                                     user_id=login_session['user_id'])
            session.add(newCategory)
            flash('New Category %s successfully created' % newCategory.name)
            session.commit()
            return redirect(url_for('showCategories'))
        else:
            error = "Need name of category, please!!!"
            return render_template('newCategory.html', error=error)
    else:
        return render_template('newCategory.html')


# Edit a Category
@app.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
@login_required
def editCategory(category_id):
    """Renders and handles editing of each category"""
    editCategory = session.query(Categories).filter_by(id=category_id).one()

    def inner_fn():
        if request.method == 'POST':
            if request.form['name']:
                editCategory.name = request.form['name']
                session.add(editCategory)
                flash('Category Successfully Edited %s' % editCategory.name)
                session.commit()
                return redirect(url_for('showCategories'))
            else:
                error = "Need name of category, please!!!"
                return render_template('editCategory.html', category=editCategory, error=error)
        else:
            return render_template('editCategory.html', category=editCategory)
    return user_authed(editCategory.user_id, inner_fn)


# Delete a category
@app.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
@login_required
def deleteCategory(category_id):
    """Handles deleting of each category"""
    categoryToDelete = session.query(Categories).filter_by(id=category_id).one()
    itemsinCategory = session.query(Items).filter_by(category_id=category_id).count()

    def inner_fn():
        if itemsinCategory > 0:
            return "<script>function myFunction() {alert('Cannot delete a category that has items in it.');}</script><body onload='myFunction()''>"
        if request.method == 'POST':
            session.delete(categoryToDelete)
            flash('%s Successfully Deleted' % categoryToDelete.name)
            session.commit()
            return redirect(url_for('showCategories'))
        else:
            return render_template('deleteCategory.html', category=categoryToDelete)
    return user_authed(categoryToDelete.user_id, inner_fn)


# Show category
@app.route('/categories/<int:category_id>/')
@app.route('/categories/<int:category_id>/category/')
def showCategory(category_id):
    """Handles and renders specific category in the catalog"""
    categories = session.query(Categories).order_by(asc(Categories.name))
    category = session.query(Categories).filter_by(id=category_id).one()
    items = session.query(Items).filter_by(category_id=category_id).all()
    count_item = session.query(Items).filter_by(category_id=category_id).count()
    logged_in = 'username' in login_session
    if 'username' not in login_session:
        return render_template('publicSpecificCategory.html', categories=categories, items=items,
                               category=category, logged_in=logged_in, count=count_item)
    else:
        return render_template('specificCategory.html', categories=categories, items=items,
                               category=category, logged_in=logged_in, username=login_session['username'],
                               count=count_item)


# Show category items
@app.route('/categories/<int:category_id>/category/<int:item_id>/items/')
def showItem(category_id, item_id):
    """Renders and Handles all the items in each category"""
    category = session.query(Categories).filter_by(id=category_id).one()
    creator = getUserInfo(category.user_id)
    item = session.query(Items).filter_by(category_id=category_id, id=item_id).one()
    comments = session.query(Comments).filter_by(item_id=item_id).order_by(desc(Comments.created_date))
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('publicItem.html', category=category, item=item, comments=comments)
    else:
        return render_template('privateItem.html', category=category, item=item, comments=comments)


# Create new category items
@app.route('/categories/<int:category_id>/items/new', methods=['GET', 'POST'])
@login_required
def newCategoryItem(category_id):
    """Handles creating new category items"""
    category = session.query(Categories).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            newItem = Items(name=request.form['name'],
                            description=request.form['description'],
                            picture=request.form['picture'],
                            price=request.form['price'],
                            category_id=category_id)
            session.add(newItem)
            session.commit()
            return redirect(url_for('showItem', category_id=category_id, item_id=newItem.id))
        else:
            error = "Need at the minimum the name of the item"
            return render_template('newitem.html', category_id=category_id, error=error)
    else:
        return render_template('newitem.html', category_id=category_id)


# Edit category items
@app.route('/categories/<int:category_id>/items/<int:item_id>/edit', methods=['GET', 'POST'])
@login_required
def editItem(category_id, item_id):
    """Renders and handles editing of a particular item in each category"""
    editedItem = session.query(Items).filter_by(id=item_id).one()
    categories = session.query(Categories).order_by(asc(Categories.name))
    category = session.query(Categories).filter_by(id=category_id).one()

    def inner_fn():
        if request.method == 'POST':
            if not request.form['name']:
                error = "Ensure that there is a name for the item"
                return render_template('editItem.html', category_id=category_id, item_id=item_id,
                                       item=editedItem, categories=categories, error=error)
            else:
                if request.form['name']:
                    editedItem.name = request.form['name']
                if request.form['description']:
                    editedItem.description = request.form['description']
                if request.form['picture']:
                    editedItem.picture = request.form['picture']
                if request.form['price']:
                    editedItem.price = request.form['price']
                if request.form['category_id']:
                    editedItem.category_id = request.form['category_id']
                session.add(editedItem)
                flash('Item Successfully Edited')
                session.commit
                return redirect(url_for('showItem', category_id=editedItem.category_id, item_id=item_id))
        else:
            return render_template('editItem.html', category_id=category_id, item_id=item_id, item=editedItem,
                                   categories=categories)
    return user_authed(category.user_id, inner_fn)


# Delete an item
@app.route('/categories/<int:category_id>/items/<int:item_id>/delete', methods=['GET', 'POST'])
@login_required
def deleteItem(category_id, item_id):
    """Renders and handles deleting of items in each category"""
    category = session.query(Categories).filter_by(id=category_id).one()
    itemTodelete = session.query(Items).filter_by(id=item_id).one()

    def inner_fn():
        if request.method == 'POST':
            session.delete(itemTodelete)
            flash('Item Successfully Deleted')
            session.commit()
            return redirect(url_for('showCategory', category_id=category_id))
        else:
            return render_template('deleteItem.html', item=itemTodelete, category_id=category_id)
    return user_authed(category.user_id, inner_fn)


# Comment on a post
@app.route('/categories/<int:category_id>/items/<int:item_id>/comment', methods=['GET', 'POST'])
@login_required
def commentItem(category_id, item_id):
    """Renders and handles comments for each item"""
    if request.method == 'POST':
        if request.form['comment']:
            newComment = Comments(user_comments=request.form['comment'],
                                  user_id=login_session['user_id'],
                                  item_id=item_id)
            session.add(newComment)
            session.commit()
            return redirect(url_for('showItem', category_id=category_id, item_id=item_id))
        else:
            error = "Need comments please!!!"
            return render_template('comment.html', category_id=category_id, item_id=item_id, error=error)
    else:
        return render_template('comment.html', category_id=category_id, item_id=item_id)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = False
    app.run(host='0.0.0.0', port=5000)