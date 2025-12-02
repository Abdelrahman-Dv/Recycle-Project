from flask import render_template, request, redirect, url_for, flash, current_app, jsonify
from app import db
from app.models import User
from flask import current_app as app
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.urls import url_parse

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = request.form.get("remember", "").lower() == "on"
        
        user = User.query.filter_by(email=email).first()
        
        if not user or not user.check_password(password):
            flash("البريد الإلكتروني أو كلمة المرور غير صحيحة", "danger")
            return redirect(url_for("login"))
        
        login_user(user, remember=remember)
        next_page = request.args.get("next")
        
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
            
        flash("تم تسجيل الدخول بنجاح", "success")
        return redirect(next_page)
        
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
        
    if request.method == "POST":
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        organization = request.form.get("organization", "")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        
        # Check if passwords match
        if password != confirm_password:
            flash("كلمات المرور غير متطابقة", "danger")
            return redirect(url_for("register"))
            
        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("هذا البريد الإلكتروني مستخدم بالفعل", "danger")
            return redirect(url_for("register"))
            
        # Create new user
        user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            organization=organization,
            registration_type="web_account"
        )
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            flash("تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول", "success")
            return redirect(url_for("login"))
        except Exception as e:
            db.session.rollback()
            flash(f"حدث خطأ أثناء التسجيل: {str(e)}", "danger")
            return redirect(url_for("register"))
            
    return render_template("register.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("تم تسجيل الخروج بنجاح", "success")
    return redirect(url_for("index"))

@app.route("/who-are-we.html")
def who_are_we():
    return render_template("who-are-we.html")

@app.route("/services.html")
def services():
    return render_template("services.html")

@app.route("/Environmental.html")
def environmental():
    return render_template("Environmental.html")

@app.route("/get-our-services.html", methods=["GET", "POST"])
def get_our_services():
    if request.method == "POST":
        try:
            # Get form data
            full_name = request.form.get("full_name")
            email = request.form.get("email")
            phone = request.form.get("phone")
            services = request.form.getlist("services")  # Get all selected services
            
            # Create new user with services
            user = User(
                full_name=full_name,
                email=email,
                phone=phone,
                services=",".join(services)  # Join services with comma
            )
            
            # Save to database
            db.session.add(user)
            db.session.commit()
            
            flash("Your request has been submitted successfully!", "success")
            return redirect(url_for("get_our_services"))
            
        except Exception as e:
            print(f"Error: {e}")
            flash("An error occurred. Please try again.", "error")
            return redirect(url_for("get_our_services"))
            
    return render_template("get-our-services.html")

@app.route("/Registration.html")
def registration():
    return render_template("Registration.html")

@app.route("/api/register", methods=["POST"])
def register_membership():
    """API endpoint to handle membership registration"""
    try:
        # Extract form data
        membership_type = request.form.get('membership_type')
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        payment_method = request.form.get('payment_method', '')
        
        # Validate required fields
        if not all([membership_type, full_name, email, phone, address]):
            return jsonify({"success": False, "message": "جميع الحقول مطلوبة"}), 400
        
        # Create new user for membership
        user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            registration_type=membership_type,
            position=membership_type,
        )
        
        # Save to database
        db.session.add(user)
        db.session.commit()
        
        # Return success response
        return jsonify({
            "success": True, 
            "message": "تم التسجيل بنجاح! سيتم التواصل معك قريباً"
        }), 201
        
    except Exception as e:
        db.session.rollback()
        print(f"Registration error: {e}")
        return jsonify({
            "success": False, 
            "message": f"حدث خطأ أثناء التسجيل: {str(e)}"
        }), 500
    
@app.route("/contact-us.html", methods=["GET", "POST"])  # Add .html to match the URL
def contact_us():
    print(f"Method: {request.method}")  # Debug print
    
    if request.method == "POST":
        try:
            print("Form data:", request.form)  # Debug print
            
            # Get form data
            name = request.form.get("name")
            email = request.form.get("email")
            phone = request.form.get("phone")
            message = request.form.get("message")

            # Create new user
            user = User(
                full_name=name,
                email=email,
                phone=phone,
                message=message
            )

            # Save to database
            db.session.add(user)
            db.session.commit()

            flash("Message sent successfully!", "success")
            return redirect(url_for("contact_us"))

        except Exception as e:
            print(f"Error: {e}")  # Debug print
            db.session.rollback()
            flash("An error occurred. Please try again.", "error")
            return redirect(url_for("contact_us"))

    return render_template("contact-us.html")

@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin_panel():
    # Only allow admin users to access the panel
    if not current_user.is_admin:
        flash("You don't have permission to access this page", "danger")
        return redirect(url_for("index"))
        
    # Fetch all messages from the database
    messages = User.query.all()
    return render_template("admin.html", messages=messages)

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    if request.method == "POST":
        full_name = request.form.get("full_name")
        phone = request.form.get("phone")
        organization = request.form.get("organization", "")
        
        # Update user profile
        current_user.full_name = full_name
        current_user.phone = phone
        current_user.organization = organization
        
        # Update password if provided
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")
        
        if current_password and new_password:
            if not current_user.check_password(current_password):
                flash("كلمة المرور الحالية غير صحيحة", "danger")
                return redirect(url_for("profile"))
                
            if new_password != confirm_password:
                flash("كلمة المرور الجديدة وتأكيدها غير متطابقين", "danger")
                return redirect(url_for("profile"))
                
            current_user.set_password(new_password)
        
        try:
            db.session.commit()
            flash("تم تحديث الملف الشخصي بنجاح", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"حدث خطأ أثناء تحديث الملف الشخصي: {str(e)}", "danger")
            
        return redirect(url_for("profile"))
        
    return render_template("profile.html", user=current_user)

@app.route("/save_registration", methods=["POST"])
def save_registration():
    try:
        # Get form data
        full_name = request.form.get("full_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        
        # Get optional fields if they exist in your form
        organization = request.form.get("organization", "")
        position = request.form.get("position", "")
        
        # Validate required fields
        if not full_name or not email or not phone:
            return jsonify({"success": False, "message": "جميع الحقول المطلوبة يجب ملؤها"})
            
        # Create new user for registration
        user = User(
            full_name=full_name,
            email=email,
            phone=phone,
            organization=organization,
            position=position,
            registration_type="event"  # Add a type to distinguish registrations
        )
        
        # Save to database
        db.session.add(user)
        db.session.commit()
        
        return jsonify({"success": True})
        
    except Exception as e:
        db.session.rollback()
        print(f"Registration error: {e}")
        return jsonify({"success": False, "message": str(e)})
    
@app.route("/createDB")
def createDB():
    db.create_all()
    return "Database tables created!"

@app.route("/deleteDB")
def deleteDB():
    db.drop_all()
    return "Database tables deleted!"