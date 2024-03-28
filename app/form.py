from django import forms

class applicant_form(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Last Name'}), required=True)
    cv = forms.FileField(widget=forms.FileInput(attrs={'class': "form-control", 'type' : 'file', 'placeholder' : 'Select CV', 'accept' : '.pdf'}), required=True)

from .models import Job

profession_skills = {
    'Data Science': 'data_science',
    'HR': 'hr',
    'Advocate': 'advocate',
    'Arts': 'arts',
    'Web Designing': 'web_designing',
    'Mechanical Engineer': 'mechanical_engineer',
    'Sales': 'sales',
    'Health and Fitness': 'health_fitness',
    'Civil Engineer': 'civil_engineer',
    'Java Developer': 'java_developer',
    'Business Analyst': 'business_analyst',
    'SAP Developer': 'sap_developer',
    'Automation Testing': 'automation_testing',
    'Electrical Engineering': 'electrical_engineering',
    'Operations Manager': 'operations_manager',
    'Python Developer': 'python_developer',
    'DevOps Engineer': 'devops_engineer',
    'Network Security Engineer': 'network_security_engineer',
    'PMO': 'pmo',
    'Database': 'database',
    'Hadoop': 'hadoop',
    'ETL Developer': 'etl_developer',
    'DotNet Developer': 'dotnet_developer',
    'Blockchain': 'blockchain',
    'Testing': 'testing'
}

skills_dict = {
        'data_science': [
            'TensorFlow', 'Keras', 'PyTorch', 'Machine Learning', 'Deep Learning', 
            'Flask', 'Streamlit', 'Natural Language Processing', 'Data Visualization', 
            'Data Cleaning', 'Statistical Analysis', 'Regression Analysis', 
            'Classification Algorithms', 'Time Series Analysis', 'Dimensionality Reduction', 
            'Data Mining', 'Feature Engineering', 'Model Evaluation', 'Cross-Validation', 
            'Ensemble Learning', 'Data Wrangling', 'Exploratory Data Analysis', 
            'Big Data Analytics', 'Sentiment Analysis', 'Anomaly Detection', 
            'Recommender Systems', 'Image Processing', 'Transfer Learning', 
            'Model Deployment', 'Model Interpretability', 'A/B Testing', 
            'Deep Reinforcement Learning'
        ],
        'hr': [
            'Recruitment and Selection', 'Employee Relations', 'Performance Management', 
            'Compensation and Benefits', 'HRIS', 'Employment Law and Compliance', 
            'Talent Acquisition', 'Onboarding', 'Training and Development', 
            'Succession Planning', 'Diversity and Inclusion', 'Compensation Strategy', 
            'HR Metrics', 'Employee Engagement', 'Conflict Resolution', 
            'Organizational Development', 'Labor Relations', 'Workforce Planning', 
            'Change Management', 'HR Technology', 'Workforce Analytics', 
            'HR Strategy', 'Employer Branding', 'HR Outsourcing', 
            'Global HR Management'
        ],
        'advocate': [
            'Legal Research', 'Case Management', 'Oral and Written Communication', 
            'Negotiation', 'Analytical Skills', 'Advocacy and Persuasion', 
            'Legal Writing', 'Litigation', 'Legal Advice', 
            'Client Counseling', 'Legal Compliance', 'Mediation', 
            'Arbitration', 'Legal Documentation', 'Courtroom Experience', 
            'Legal Ethics', 'Trial Preparation', 'Legal Interpretation', 
            'Legal Drafting', 'Legal Representation', 'Legal Strategy', 
            'Legal Review', 'Legal Procedures', 'Legal Advocacy'
        ],
        'arts': [
            'Creativity and Imagination', 'Technical Skills', 'Art History and Theory', 
            'Digital Tools', 'Portfolio Development', 'Marketing and Self-Promotion', 
            'Painting', 'Drawing', 'Sculpture', 'Photography', 'Printmaking', 
            'Ceramics', 'Graphic Design', 'Illustration', 'Digital Art', 
            'Mixed Media', 'Art Criticism', 'Art Education', 'Art Therapy', 
            'Art Restoration', 'Curatorial Work', 'Exhibition Design', 
            'Art Sales', 'Art Licensing'
        ],
        'web_designing': [
            'React', 'Django', 'Node.js', 'React.js', 'PHP', 'Laravel', 
            'Magento', 'WordPress', 'JavaScript', 'Angular.js', 'C#', 
            'Flask', 'HTML', 'CSS', 'UI/UX Design', 'Responsive Design', 
            'Bootstrap', 'jQuery', 'Web Accessibility', 'Mobile Design', 
            'Cross-Browser Compatibility', 'Web Performance Optimization', 
            'Version Control Systems', 'Web Standards'
        ],
        'mechanical_engineer': [
            'Engineering Mechanics', 'CAD/CAM Software Proficiency', 
            'Thermodynamics', 'Material Science', 'Manufacturing Processes', 
            'Project Management', 'Mechanical Design', 'Finite Element Analysis', 
            'Fluid Mechanics', 'Heat Transfer', 'Mechatronics', 
            'Product Development', 'Automotive Engineering', 'Aerospace Engineering', 
            'Robotics', 'Structural Analysis', 'Engineering Mathematics', 
            'Technical Drawing', 'Industrial Engineering', 'Quality Control', 
            'Lean Manufacturing', 'Six Sigma', 'Rapid Prototyping'
        ],
        'sales': [
            'Communication Skills', 'Persuasion and Negotiation', 'Product Knowledge', 
            'Relationship Building', 'CRM', 'Closing Techniques', 
            'Prospecting', 'Sales Presentations', 'Customer Service', 
            'Market Research', 'Account Management', 'Sales Management', 
            'Cold Calling', 'Lead Generation', 'Sales Process', 
            'Consultative Selling', 'Strategic Selling', 'B2B Sales', 
            'B2C Sales', 'Retail Sales', 'Sales Training', 
            'Sales Forecasting', 'Sales Analytics', 'Key Account Management'
        ],
        'health_fitness': [
            'Anatomy and Physiology', 'Exercise Physiology', 'Nutrition Science', 
            'Personal Training Techniques', 'Wellness Coaching', 'First Aid and CPR Certification', 
            'Strength Training', 'Cardiovascular Training', 'Flexibility Training', 
            'Functional Training', 'Sports Nutrition', 'Weight Management', 
            'Injury Prevention', 'Rehabilitation', 'Mind-Body Connection', 
            'Group Fitness Instruction', 'Yoga Instruction', 'Pilates Instruction', 
            'Health Promotion', 'Behavior Change', 'Stress Management', 
            'Holistic Health', 'Health Education', 'Physical Therapy'
        ],
        'civil_engineer': [
            'Structural Engineering', 'Geotechnical Engineering', 'Construction Management', 
            'Transportation Engineering', 'Environmental Engineering', 'AutoCAD and Civil Engineering Software', 
            'Concrete Design', 'Steel Design', 'Wood Design', 
            'Earthquake Engineering', 'Foundation Engineering', 'Surveying', 
            'Construction Materials', 'Highway Design', 'Traffic Engineering', 
            'Water Resources Engineering', 'Hydrology', 'Hydraulics', 
            'Sustainable Design', 'Green Building', 'Urban Planning', 
            'Land Development', 'Project Estimation', 'Cost Engineering'
        ],
        'java_developer': [
            'Java Programming', 'Object-Oriented Programming', 'Data Structures and Algorithms', 
            'Spring Framework', 'Hibernate', 'RESTful Web Services', 
            'Microservices Architecture', 'JavaFX', 'Swing', 
            'Java EE', 'JDBC', 'Servlets', 'JSP', 
            'JavaServer Faces (JSF)', 'Enterprise Integration Patterns', 
            'Java Concurrency', 'Java Collections Framework', 'Java Streams', 
            'Java Networking', 'Java Security', 'Java GUI Development', 
            'Java Performance Tuning', 'Java Memory Management', 'Java Best Practices'
        ],
        'business_analyst': [
            'Business Analysis', 'Requirements Gathering', 'Data Analysis', 
            'Process Improvement', 'Documentation', 'Stakeholder Management', 
            'SWOT Analysis', 'Gap Analysis', 'Business Process Modeling', 
            'Use Case Modeling', 'User Story Mapping', 'Requirements Prioritization', 
            'Agile Methodologies', 'Scrum', 'Kanban', 'Lean Six Sigma', 
            'Business Intelligence', 'Data Visualization Tools', 'Predictive Analytics', 
            'Decision Modeling', 'Root Cause Analysis', 'Critical Thinking', 
            'Problem-Solving', 'Change Management', 'Project Management'
        ],
        'sap_developer': [
            'SAP ERP', 'ABAP', 'SAP HANA', 'SAP Fiori', 
            'SAP UI5', 'Integration Technologies', 'SAP BW/4HANA', 
            'SAP S/4HANA', 'SAP CRM', 'SAP SCM', 
            'SAP SRM', 'SAP BusinessObjects', 'SAP NetWeaver', 
            'SAP Solution Manager', 'SAP Cloud Platform', 'SAP Leonardo', 
            'SAP Analytics Cloud', 'SAP Mobile Platform', 'SAP Cloud Integration', 
            'SAP Hybris', 'SAP SuccessFactors', 'SAP Ariba', 
            'SAP Concur', 'SAP Lumira', 'SAP Crystal Reports'
        ],
        'automation_testing': [
            'Test Automation', 'Selenium', 'JUnit', 
            'TestNG', 'Cucumber', 'Continuous Integration', 
            'Test Management Tools', 'Load Testing', 'Performance Testing', 
            'Security Testing', 'API Testing', 'Mobile Testing', 
            'Web Services Testing', 'Test Driven Development (TDD)', 'Behavior Driven Development (BDD)', 
            'End-to-End Testing', 'Regression Testing', 'User Acceptance Testing', 
            'Smoke Testing', 'Integration Testing', 'Black Box Testing', 
            'White Box Testing', 'Exploratory Testing', 'Usability Testing'
        ],
        'electrical_engineering': [
            'Circuit Design', 'Electromagnetics', 'Power Systems', 
            'Control Systems', 'Renewable Energy', 'Electrical Safety', 
            'Electrical Machines', 'Analog Electronics', 'Digital Electronics', 
            'Microcontrollers', 'Signal Processing', 'Embedded Systems', 
            'Power Electronics', 'Instrumentation', 'Electric Drives', 
            'Electrical Distribution', 'High Voltage Engineering', 'Electric Power Transmission', 
            'Electrical Standards', 'Electrical Code Compliance', 'Electrical Testing', 
            'Electric Circuit Analysis', 'Electrical Troubleshooting', 'Electrical Maintenance'
        ],
        'operations_manager': [
            'Operations Management', 'Supply Chain Management', 'Quality Management', 
            'Process Optimization', 'Budgeting', 'Leadership', 
            'Strategic Planning', 'Inventory Management', 'Logistics', 
            'Lean Manufacturing', 'Six Sigma', 'Project Management', 
            'Continuous Improvement', 'Performance Metrics', 'Root Cause Analysis', 
            'Risk Management', 'Change Management', 'Vendor Management', 
            'Resource Allocation', 'Capacity Planning', 'Forecasting', 
            'Quality Assurance', 'Facilities Management', 'Health and Safety'
        ],
        'python_developer': [
            'Python Programming', 'Web Development', 'Data Analysis', 
            'Django', 'Flask', 'RESTful APIs', 
            'Data Visualization', 'Web Scraping', 'Data Science Libraries', 
            'Web Frameworks', 'Backend Development', 'Frontend Development', 
            'Scripting', 'Concurrency', 'Asyncio', 
            'Database Integration', 'ORMs', 'Deployment', 
            'Debugging', 'Unit Testing', 'Code Optimization', 
            'Machine Learning Libraries', 'Natural Language Processing Libraries', 'Image Processing Libraries'
        ],
        'devops_engineer': [
            'Continuous Integration/Continuous Deployment (CI/CD)', 'Configuration Management', 
            'Containerization', 'Monitoring and Logging', 'Scripting', 'Cloud Computing', 
            'Infrastructure as Code (IaC)', 'Orchestration Tools', 'Version Control Systems', 
            'Automated Testing', 'Security Best Practices', 'Site Reliability Engineering (SRE)', 
            'Microservices Architecture', 'Scalability Planning', 'High Availability Architecture', 
            'Disaster Recovery Planning', 'Network Security', 'Identity and Access Management (IAM)', 
            'Log Management', 'Performance Optimization', 'Cost Management', 
            'Incident Response', 'Compliance Management', 'Continuous Learning and Improvement'
        ],
        'network_security_engineer': [
            'Network Security', 'Firewalls', 'Intrusion Detection and Prevention Systems (IDPS)', 
            'Encryption', 'Vulnerability Assessment', 'Penetration Testing', 
            'Network Protocols', 'Security Policies', 'Access Control', 
            'Security Auditing', 'Security Standards', 'Wireless Security', 
            'Network Monitoring', 'Incident Response', 'Forensics', 
            'Cyber Threat Intelligence', 'Security Architecture', 'Security Risk Assessment', 
            'Security Awareness Training', 'Identity Management', 'Cloud Security', 
            'Endpoint Security', 'Data Loss Prevention (DLP)', 'Security Compliance'
        ],
        'pmo': [
            'Project Management', 'Program Management', 'Portfolio Management', 
            'Stakeholder Management', 'Risk Management', 'Change Management', 
            'Resource Management', 'Schedule Management', 'Budget Management', 
            'Quality Management', 'Scope Management', 'Communication Management', 
            'Issue Management', 'Dependency Management', 'Vendor Management', 
            'Contract Management', 'Governance Frameworks', 'Performance Measurement', 
            'Project Management Methodologies', 'Agile Frameworks', 'Waterfall Methodology', 
            'Critical Path Method (CPM)', 'Earned Value Management (EVM)', 'Project Management Tools'
        ],
        'database': [
            'Database Management', 'SQL', 'NoSQL', 
            'Database Design', 'Data Modeling', 'Query Optimization', 
            'Database Administration', 'Database Security', 'Database Performance Tuning', 
            'Relational Databases', 'Distributed Databases', 'Data Warehousing', 
            'ETL Processes', 'Database Backup and Recovery', 'Database Migration', 
            'Database Replication', 'Database Sharding', 'Data Consistency', 
            'ACID Properties', 'CAP Theorem', 'Database Normalization', 
            'Data Integrity', 'Database Triggers', 'Database Indexing'
        ],
        'hadoop': [
            'Hadoop', 'MapReduce', 'Hive', 
            'Pig', 'HBase', 'Spark', 
            'Apache Kafka', 'Apache Flume', 'Apache Sqoop', 
            'Apache Storm', 'Apache NiFi', 'Apache Oozie', 
            'Apache ZooKeeper', 'YARN', 'Hadoop Distributed File System (HDFS)', 
            'Hadoop Administration', 'Hadoop Security', 'Hadoop Ecosystem', 
            'Big Data Processing', 'Real-Time Data Processing', 'Data Ingestion', 
            'Data Storage', 'Data Analysis', 'Data Governance'
        ],
        'etl_developer': [
            'Extract, Transform, Load (ETL)', 'Data Warehousing', 'Data Integration', 
            'ETL Tools', 'SQL', 'Scripting', 
            'Data Extraction', 'Data Transformation', 'Data Loading', 
            'Data Cleansing', 'Data Quality', 'Data Profiling', 
            'Data Migration', 'Change Data Capture (CDC)', 'Incremental Loading', 
            'Full Load', 'Delta Load', 'Slowly Changing Dimensions (SCD)', 
            'Surrogate Keys', 'Data Mart', 'Data Lake', 
            'ETL Architecture', 'ETL Performance Tuning', 'ETL Automation'
        ],
        'dotnet_developer': [
            '.NET Framework', 'C#', 'ASP.NET', 
            'MVC', 'Entity Framework', 'Web API', 
            'Windows Forms', 'WPF', 'LINQ', 
            'ADO.NET', 'Windows Communication Foundation (WCF)', 'Windows Presentation Foundation (WPF)', 
            'ASP.NET Core', 'ASP.NET MVC', 'ASP.NET Web Forms', 
            'ASP.NET Web API', 'ASP.NET Identity', 'Entity Framework Core', 
            'NuGet', 'Visual Studio', 'Unit Testing in .NET', 
            'Integration Testing in .NET', 'Performance Testing in .NET', 'Debugging in .NET'
        ],
        'blockchain': [
            'Blockchain Technology', 'Smart Contracts', 'Cryptocurrency', 
            'Decentralized Applications (DApps)', 'Distributed Ledger Technology (DLT)', 'Consensus Mechanisms', 
            'Blockchain Security', 'Public Key Infrastructure (PKI)', 'Digital Signatures', 
            'Permissioned Blockchains', 'Permissionless Blockchains', 'Hyperledger Fabric', 
            'Ethereum', 'Solidity', 'Ripple', 
            'Stellar', 'Hash Functions', 'Digital Wallets', 
            'Tokenization', 'Blockchain Interoperability', 'Blockchain Scalability', 
            'Blockchain Governance', 'Blockchain Regulation', 'Blockchain Use Cases'
        ],
        'testing': [
            'Software Testing', 'Test Planning', 'Test Execution', 
            'Defect Tracking', 'Regression Testing', 'Automation Testing', 
            'Manual Testing', 'Functional Testing', 'Non-Functional Testing', 
            'Integration Testing', 'System Testing', 'Acceptance Testing', 
            'Usability Testing', 'Performance Testing', 'Load Testing', 
            'Stress Testing', 'Security Testing', 'Compatibility Testing', 
            'Exploratory Testing', 'Ad Hoc Testing', 'Smoke Testing', 
            'Sanity Testing', 'Black Box Testing', 'White Box Testing'
        ],
    }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_position', 'job_description', 'years_of_experience', 'salary', 'location', 'required_skills']

    
    job_description = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Job Description'}), required=True)
    years_of_experience = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control", 'type' : 'number', 'placeholder' : 'Years of Experience'}), required=True, min_value=0)
    salary = forms.DecimalField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'number', 'placeholder' : 'Salary'}), required=True, min_value=0, max_digits=10, decimal_places=2)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Location'}), required=True, max_length=100)
    required_skills = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'type' : 'text', 'placeholder' : 'Skills Required'}), required=True, max_length=255)
    job_position = forms.ChoiceField(choices=[(key, key) for key in profession_skills.keys()], widget=forms.Select(attrs={'class': "form-select"}))

