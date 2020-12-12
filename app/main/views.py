from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from ..models import Pitch,User,Comment
from . import main
from flask import render_template
from .. import db,photos
from .forms import PitchForm,CommentForm,UpdateProfile

@main.route('/')
def index():
    '''
    Index page
    return
    '''
    return render_template('index.html')

@main.route('/pitch', methods = ['POST','GET'])
@login_required
def pitch():
        return redirect(url_for('main.index'))
        
        return render_template('pitch.html')


@main.route('/category/<category>')
def category(category):
    '''
    function to return the pitches by category
    '''
    category = Pitch.get_pitch(category)
    title = f'{category}'
    return render_template('category.html',title = title, category = category)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.author))
    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(author = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)


