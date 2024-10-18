from flask import render_template
from flask.views import MethodView
from flask import url_for
from models.models import Attendee
from app import db
from flask import redirect
from flask import request
from models.models import Level

def register_routes(app):

    class Main(MethodView):
        def get(self):
            data = Attendee.query.all()
            context = {"attendee":data}
            return render_template('index.html',**context)

        def post(self):

            self.summit_form()
            return redirect(url_for("main"))

        def summit_form(self):
            data = request.form.to_dict()
            data['member'] = request.form.get('member') == 'true'
            data['first_time'] = request.form.get('first_time') == 'true'

            # Extract other form fields (example)
            first_name = data.get('first_name','')
            last_name = data.get('last_name', '')
            department = data.get('department', '')
            address = data.get('address', '')
            unit = data.get('unit', '')
                    # Handle the Level enum conversion safely
            level_str = data.get('level', '')
            try:
                level = Level[level_str]  # Attempt to convert to enum
            except KeyError:
                print(f"Invalid level value: {level_str}")
                level = None  # Or set to a default value if needed

            if level is None:
                # Handle the case where level is invalid
                print("No valid level provided; attendee not added.")
                return

            new_attendee = Attendee(
                    first_name=first_name,
                    last_name=last_name,
                    department=department,
                    address=address,
                    unit_in_church=unit,
                    first_time=data['first_time'],
                    member=data['member'],
                    level=level  # Ensure 'level' matches your Enum values
                )

            # Add to the session and commit to the database

            try:
                db.session.add(new_attendee)
                db.session.commit()

            except Exception as e:
                print(f"Failed to person,\n Possible Reason: {e}")

    app.add_url_rule("/",view_func=Main.as_view("main"))


    @app.route('/download/')
    def download():
        data = Attendee.query.all()
        context = {"attendee":data}
        return render_template("print.html",**context)

    @app.route('/table')
    def table():
        data = Attendee.query.all()
        context = {"attendee":data}
        return render_template('table.html',**context)