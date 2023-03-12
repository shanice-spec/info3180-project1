"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from app import app,db
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app.forms import PropertyForm
from app.models import Property


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['GET','POST'])
def properties_create():
    form = PropertyForm()
    if form.validate_on_submit():
        photo = form.photo.data
        photo_file = photo.filename
        property = Property(title=form.title.data, type=form.property_type.data, num_bedrooms=form.rooms.data,
        num_bathrooms=form.bathrooms.data, location=form.location.data,
        price=form.price.data, description=form.description.data,
          photo_filename=photo_file)
        db.session.add(property)
        db.session.commit()
        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo_file))
        flash('Property added successfully', 'success')
        return redirect(url_for("list_properties"))
    return render_template('propertyform.html', form=form)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/properties')
def list_properties():
    properties = Property.query.all()
    return render_template('propertylist.html', properties=properties)

@app.route('/properties/<int:propertyid>')
def view_property(propertyid):
    property = Property.query.get(propertyid)
    return render_template('view_property.html', property=property)

@app.route('/upload/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
