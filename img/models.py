from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    Workstatus = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    ProfileStatus = [
        ('pending', 'pending'),
        ('started', 'started'),
        ('underreview', 'underreview'),
        ('rejected', 'rejected')
    ]

    industry_choices = [
        ('Accounting ', 'Accounting '),
        ('Airlines/Aviation', 'Airlines/Aviation'),
        ('Alternative Dispute Resolution', 'Alternative Dispute Resolution'),
        ('Alternative Medicine', 'Alternative Medicine'),
        ('Animation', 'Animation'),
        ('Apparel/Fashion', 'Apparel/Fashion'),
        ('Architecture/Planning', 'Architecture/Planning'),
        ('Arts/Crafts', 'Arts/Crafts'),
        ('Automotive', 'Automotive'),
        ('Aviation/Aerospace', 'Aviation/Aerospace'),
        ('Banking/Mortgage', 'Banking/Mortgage'),
        ('Biotechnology/Greentech', 'Biotechnology/Greentech'),
        ('Broadcast Media', 'Broadcast Media'),
        ('Building Materials', 'Building Materials'),
        ('Business Supplies/Equipment', 'Business Supplies/Equipment'),
        ('Capital Markets/Hedge Fund/Private Equity', 'Capital Markets/Hedge Fund/Private Equity'),
        ('Chemicals', 'Chemicals'),
        ('Civic/Social Organization', 'Civic/Social Organization'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Commercial Real Estate', 'Commercial Real Estate'),
        ('Computer Games', 'Computer Games'),
        ('Computer Hardware', 'Computer Hardware'),
        ('Computer Networking', 'Computer Networking'),
        ('Computer Software/Engineering', 'Computer Software/Engineering'),
        ('Computer/Network Security', 'Computer/Network Security'),
        ('Construction', 'Construction'),
        ('Consumer Electronics', 'Consumer Electronics'),
        ('Consumer Goods', 'Consumer Goods'),
        ('Consumer Services', 'Consumer Services'),
        ('Cosmetics', 'Cosmetics'),
        ('Dairy', 'Dairy'),
        ('Defense/Space', 'Defense/Space'),
        ('Design', 'Design'),
        ('E-Learning', 'E-Learning'),
        ('Education Management', 'Education Management'),
        ('Electrical/Electronic Manufacturing', 'Electrical/Electronic Manufacturing'),
        ('Entertainment/Movie Production', 'Entertainment/Movie Production'),
        ('Environmental Services', 'Environmental Services'),
        ('Events Services', 'Events Services'),
        ('Executive Office', 'Executive Office'),
        ('Facilities Services', 'Facilities Services'),
        ('Farming', 'Farming'),
        ('Financial Services', 'Financial Services'),
        ('Fine Art', 'Fine Art'),
        ('Fishery', 'Fishery'),
        ('Food Production', 'Food Production'),
        ('Food/Beverages', 'Food/Beverages'),
        ('Fundraising', 'Fundraising'),
        ('Furniture', 'Furniture'),
        ('Gambling/Casinos', 'Gambling/Casinos'),
        ('Glass/Ceramics/Concrete', 'Glass/Ceramics/Concrete'),
        ('Government Administration', 'Government Administration'),
        ('Government Relations', 'Government Relations'),
        ('Graphic Design/Web Design', 'Graphic Design/Web Design'),
        ('Health/Fitness', 'Health/Fitness'),
        ('Higher Education/Acadamia', 'Higher Education/Acadamia'),
        ('Hospital/Health Care', 'Hospital/Health Care'),
        ('Hospitality', 'Hospitality'),
        ('Human Resources/HR', 'Human Resources/HR'),
        ('Import/Export', 'Import/Export'),
        ('Individual/Family Services', 'Individual/Family Services'),
        ('Industrial Automation', 'Industrial Automation'),
        ('Information Services', 'Information Services'),
        ('Information Technology/IT', 'Information Technology/IT'),
        ('Insurance', 'Insurance'),
        ('International Affairs', 'International Affairs'),
        ('International Trade/Development', 'International Trade/Development'),
        ('Internet', 'Internet'),
        ('Investment Banking/Venture', 'Investment Banking/Venture'),
        ('Investment Management/Hedge Fund/Private Equity', 'Investment Management/Hedge Fund/Private Equity'),
        ('Judiciary', 'Judiciary'),
        ('Law Enforcement', 'Law Enforcement'),
        ('Law Practice/Law Firms', 'Law Practice/Law Firms'),
        ('Legal Services', 'Legal Services'),
        ('Legislative Office', 'Legislative Office'),
        ('Leisure/Travel', 'Leisure/Travel'),
        ('Library', 'Library'),
        ('Logistics/Procurement', 'Logistics/Procurement'),
        ('Luxury Goods/Jewelry', 'Luxury Goods/Jewelry'),
        ('Machinery', 'Machinery'),
        ('Management Consulting', 'Management Consulting'),
        ('Maritime', 'Maritime'),
        ('Market Research', 'Market Research'),
        ('Marketing/Advertising/Sales', 'Marketing/Advertising/Sales'),
        ('Mechanical or Industrial Engineering', 'Mechanical or Industrial Engineering'),
        ('Media Production', 'Media Production'),
        ('Medical Equipment', 'Medical Equipment'),
        ('Medical Practice', 'Medical Practice'),
        ('Mental Health Care', 'Mental Health Care'),
        ('Military Industry', 'Military Industry'),
        ('Mining/Metals', 'Mining/Metals'),
        ('Motion Pictures/Film', 'Motion Pictures/Film'),
        ('Museums/Institutions', 'Museums/Institutions'),
        ('Music', 'Music'),
        ('Nanotechnology', 'Nanotechnology'),
        ('Newspapers/Journalism', 'Newspapers/Journalism'),
        ('Non-Profit/Volunteering', 'Non-Profit/Volunteering'),
        ('Oil/Energy/Solar/Greentech', 'Oil/Energy/Solar/Greentech'),
        ('Online Publishing', 'Online Publishing'),
        ('Other Industry', 'Other Industry'),
        ('Outsourcing/Offshoring', 'Outsourcing/Offshoring'),
        ('Package/Freight Delivery', 'Package/Freight Delivery'),
        ('Packaging/Containers', 'Packaging/Containers'),
        ('Paper/Forest Products', 'Paper/Forest Products'),
        ('Performing Arts', 'Performing Arts'),
        ('Pharmaceuticals', 'Pharmaceuticals'),
        ('Philanthropy', 'Philanthropy'),
        ('Photography', 'Photography'),
        ('Plastics', 'Plastics'),
        ('Political Organization', 'Political Organization'),
        ('Primary/Secondary Education', 'Primary/Secondary Education'),
        ('Printing', 'Printing'),
        ('Professional Training', 'Professional Training'),
        ('Program Development', 'Program Development'),
        ('Public Relations/PR', 'Public Relations/PR'),
        ('Public Safety', 'Public Safety'),
        ('Publishing Industry', 'Publishing Industry'),
        ('Railroad Manufacture', 'Railroad Manufacture'),
        ('Ranching', 'Ranching'),
        ('Real Estate/Mortgage', 'Real Estate/Mortgage'),
        ('Recreational Facilities/Services', 'Recreational Facilities/Services'),
        ('Religious Institutions', 'Religious Institutions'),
        ('Renewables/Environment', 'Renewables/Environment'),
        ('Research Industry', 'Research Industry'),
        ('Restaurants', 'Restaurants'),
        ('Retail Industry', 'Retail Industry'),
        ('Security/Investigations', 'Security/Investigations'),
        ('Semiconductors', 'Semiconductors'),
        ('Shipbuilding', 'Shipbuilding'),
        ('Sporting Goods', 'Sporting Goods'),
        ('Sports', 'Sports'),
        ('Staffing/Recruiting', 'Staffing/Recruiting'),
        ('Supermarkets', 'Supermarkets'),
        ('Telecommunications', 'Telecommunications'),
        ('Textiles', 'Textiles'),
        ('Think Tanks', 'Think Tanks'),
        ('Tobacco', 'Tobacco'),
        ('Translation/Localization', 'Translation/Localization'),
        ('Transportation', 'Transportation'),
        ('Utilities', 'Utilities'),
        ('Venture Capital/VC', 'Venture Capital/VC'),
        ('Veterinary', 'Veterinary'),
        ('Warehousing', 'Warehousing'),
        ('Wholesale', 'Wholesale'),
        ('Wine/Spirits', 'Wine/Spirits'),
        ('Wireless', 'Wireless'),
        ('Writing/Editing', 'Writing/Editing')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    phonenumber = models.PositiveIntegerField(default=234, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True, choices=Workstatus)
    bvn = models.PositiveIntegerField(default=0000, blank=True, max_length=600)
    residential_address = models.CharField(blank=True, max_length=600)
    rep_address_1 = models.CharField(blank=True, max_length=600)
    rep_city = models.CharField(blank=True, max_length=600)
    rep_state = models.CharField(blank=True, max_length=600)
    rep_zip = models.CharField(blank=True, max_length=600)
    work_sector = models.CharField(blank=True, max_length=600, choices=industry_choices)
    form_of_id = models.CharField(blank=True, max_length=600)
    id_number = models.PositiveIntegerField(default=0000, blank=True, max_length=600)
    job_title = models.CharField(blank=True, max_length=600)
    country = models.CharField(blank=True, max_length=600)
    city = models.CharField(blank=True, max_length=600)
    region = models.CharField(blank=True, max_length=600)
    profile_verified = models.BooleanField(default=False)
    rc_number = models.CharField(blank=True, max_length=600)
    company_name = models.CharField(blank=True, max_length=600)
    keyman_email = models.EmailField(blank=True, max_length=600)
    keyman_phonenumber = models.PositiveIntegerField(blank=True, max_length=600, default='234')
    tin = models.CharField(blank=True, max_length=600)
    profuuid = models.UUIDField(blank=True, max_length=600)
    profile_status = models.CharField(blank=True, max_length=600, default='pending', choices=ProfileStatus)

    def __str__(self):
        return self.user.username


class Phoneotp(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_token = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    data = models.CharField(max_length=500, blank=True, null=True)
    datever = models.DateTimeField(auto_now_add=True, editable=True)
    otplimit = models.PositiveIntegerField(default=5)
    optsent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username


class Status(models.Model):
    Accounttype = [
        ('individual', 'individual'),
        ('corporate', 'corporate'),
        ('none', 'none')
    ]
    requestuser = models.OneToOneField(User, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=100, default='individual', choices=Accounttype)
    application_status = models.CharField(max_length=100, default='pending')
    stage_1 = models.BooleanField(default=False)
    stage_2 = models.BooleanField(default=False)
    stage_3 = models.BooleanField(default=False)
    stage_4 = models.BooleanField(default=False)
    stage_5 = models.BooleanField(default=False)
    stage_6 = models.BooleanField(default=False)
    stage_7 = models.BooleanField(default=False)
    stage_8 = models.BooleanField(default=False)

    def __str__(self):
        return self.requestuser.username


class Security_question(models.Model):
    security_questionare = [
        ('What was the house number and street name you lived in as a child? ',
         'What was the house number and street name you lived in as a child? '),
        ('What were the last four digits of your childhood telephone number?',
         'What were the last four digits of your childhood telephone number?'),
        ('What primary school did you attend?', 'What primary school did you attend?'),
        ('What are the last five digits of your drivers license number?',
         'What are the last five digits of your drivers license number?'),
        ('How many languages do I speak?', 'How many languages do I speak?'),
        ('What’s one thing I really love about myself?', 'What’s one thing I really love about myself?'),
        ('Do I consider myself addicted to anything?', 'Do I consider myself addicted to anything?'),
        ('Do I have a favorite name? What is it?', 'Do I have a favorite name? What is it?'),
        ('What’s my exact street address?', 'What’s my exact street address?'),
        ('Without peeking, what color are my eyes?', 'Without peeking, what color are my eyes?'),
        ('How do you think I describe our relationship to my friends?',
         'How do you think I describe our relationship to my friends?'),
        ('What’s one thing about myself I’m trying to change?', 'What’s one thing about myself I’m trying to change?'),
        (
            'Do I play any video games? Do I have a favorite one?',
            'Do I play any video games? Do I have a favorite one?'),
        ('What’s my favorite book or author?', 'What’s my favorite book or author?'),
        ('Cats or dogs? Which do I like more?', 'Cats or dogs? Which do I like more?'),
        ('How are my parents named?', 'How are my parents named?'),
        (
            'What’s one talent I have that I chose not to pursue?',
            'What’s one talent I have that I chose not to pursue?'),
        ('Out of any country in the world, which one would I want to visit right now?',
         'Out of any country in the world, which one would I want to visit right now?'),
        ('What foods I don’t really like, but will eat them if I’m hungry?',
         'What foods I don’t really like, but will eat them if I’m hungry?'),
        ('What’s my favorite TV show or actor ?', 'What’s my favorite TV show or actor ?'),
        ('What won’t I eat under any circumstances?', 'What won’t I eat under any circumstances?'),
        ('What time of the day was your first child born? ', 'What time of the day was your first child born? '),
        ('What time of the day were you born? ', 'What time of the day were you born? '),
        ('In what town or city did your parents meet?', 'In what town or city did your parents meet?')
    ]
    requestuser = models.OneToOneField(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000, choices=security_questionare)
    answer = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.question


class Accountdetails(models.Model):
    requestuser = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_code = models.CharField(blank=True, max_length=500)
    bank_name = models.CharField(blank=True, max_length=500)
    account_number = models.CharField(default=234, blank=True, max_length=500)
    account_name = models.CharField(max_length=500)

    def __str__(self):
        return self.account_name


class Nextofkin(models.Model):
    gender = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]
    requestuser = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    phonenumber = models.PositiveIntegerField(default=234, blank=True)
    gender = models.CharField(max_length=100, blank=True, choices=gender)
    residential_address = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.first_name


class Myprofileimage(models.Model):
    requestuser = models.OneToOneField(User, on_delete=models.CASCADE)
    profilepic = models.ImageField(blank=True, upload_to='profile_photo',
                                   default='profile_photo/simon-lee-IEgvy4o3byM-unsplash_1_apju7s.jpg')
    utilitybill = models.ImageField(blank=True, upload_to='utility')
    cac_document = models.FileField(upload_to='files', blank=True)
    cac_document = models.FileField(upload_to='files', blank=True)


class PaymentDetails(models.Model):
    requestuser = models.OneToOneField(User, on_delete=models.CASCADE)
    authorization_code = models.CharField(max_length=100, blank=True)
    authorization_data = models.JSONField()
    authorization_reference = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.requestuser.username


class Directors(models.Model):
    requestuser = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    email_address = models.EmailField(max_length=100, blank=True)
    phone_number = models.PositiveIntegerField(default=234, blank=True)
    bvn = models.PositiveIntegerField(default=234, blank=True)
    residential_address = models.TextField(max_length=700, blank=True)

    def __str__(self):
        return self.first_name


class Adminreg(models.Model):
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE)
    code_status = models.BooleanField(default=False)
    code = models.UUIDField(max_length=100)
    user_validation = models.BooleanField(default=False)
    loan_collection = models.BooleanField(default=False)
    resolution = models.BooleanField(default=False)
    payment_validation = models.BooleanField(default=False)
    contact_us = models.BooleanField(default=False)
    profile_review = models.BooleanField(default=False)
    payment_dispute = models.BooleanField(default=False)

