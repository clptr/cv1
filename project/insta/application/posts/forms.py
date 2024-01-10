from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CreatePostForm(FlaskForm):
    caption = TextAreaField('Caption')
    post_pic = FileField('Upload Image', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Add Post')


class EditPostForm(FlaskForm):
    caption = TextAreaField('Caption')
    image = FileField('Edit Image')
    submit = SubmitField('Save Changes')

