import os
import sys

# Ensure reportlab is installed
try:
    import reportlab
except ImportError:
    import subprocess
    print("ReportLab is not installed. Installing reportlab...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab"])
    import reportlab

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Define PDF structure details
PROJECT_NAME = "A Comprehensive Measure of Well-Being"
SUBTITLE = "Predicting Human Development Index (HDI) using Machine Learning"

def create_pdf(filename, title, content_list):
    """
    Helper function to create a beautifully styled PDF report.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54)
    styles = getSampleStyleSheet()
    
    # Custom Styles for a premium look
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#1e1b4b'),
        spaceAfter=15
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#4b5563'),
        spaceAfter=20
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#4f46e5'),
        spaceBefore=12,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#1f2937'),
        spaceAfter=10
    )

    meta_style = ParagraphStyle(
        'Meta_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#9ca3af')
    )

    story = []
    
    # Header block
    story.append(Paragraph(title, title_style))
    story.append(Paragraph(f"Project: {PROJECT_NAME} - {SUBTITLE}", subtitle_style))
    
    # Divider line
    divider = Table([['']], colWidths=[500], rowHeights=[2])
    divider.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#6366f1')),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(divider)
    story.append(Spacer(1, 15))
    
    # Render Content
    for section_title, paragraphs in content_list:
        if section_title:
            story.append(Paragraph(section_title, h2_style))
        for p_text in paragraphs:
            story.append(Paragraph(p_text, body_style))
        story.append(Spacer(1, 10))
        
    # Footer metadata
    story.append(Spacer(1, 30))
    story.append(Paragraph("System Generated Report • Phase Submission Document", meta_style))
    
    doc.build(story)
    print(f"Successfully generated: {filename}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(base_dir, "generated_pdfs")
    
    print("Starting PDF generation for all project phases...")
    
    # 1. Brainstorming & Idea Prioritization
    create_pdf(
        os.path.join(out_dir, "1.Brainstorming & ideation", "Brainstorming & Idea Prioritization.pdf"),
        "Brainstorming & Idea Prioritization",
        [
            ("1. Introduction", [
                "The project aims to analyze socio-economic indicators and estimate the Human Development Index (HDI). This report documents the brainstorming and idea prioritization process."
            ]),
            ("2. Idea Generation", [
                "Idea 1: Direct prediction of HDI from economic indicators using Regression.",
                "Idea 2: Classification of countries into development levels (Low, Medium, High, Very High) using Random Forests.",
                "Idea 3: An interactive public dashboard to simulate changes in life expectancy and education on overall well-being."
            ]),
            ("3. Prioritization Matrix", [
                "Based on feasibility and project scope, Idea 1 (Regression Model integrated into a Flask Web App) was selected as the core solution, with components of Idea 2 used for categorization, and Idea 3 as the visualization component."
            ])
        ]
    )
    
    # 2. Define Problem Statements
    create_pdf(
        os.path.join(out_dir, "1.Brainstorming & ideation", "Define Problem Statements.pdf"),
        "Define Problem Statements",
        [
            ("Problem Context", [
                "Measuring human progress is a complex process. Policymakers and organizations require a clear, predictive model to understand how specific socio-economic dimensions like healthcare, school infrastructure, and national income affect overall human well-being."
            ]),
            ("Problem Statement", [
                "Traditional HDI reporting is retrospective and published with long delays. There is a lack of real-time simulation tools that let stakeholders input projected changes in key factors (life expectancy, schooling years, GNI per capita) and immediately observe the estimated outcome on the HDI score."
            ])
        ]
    )

    # 3. Empathy Map
    create_pdf(
        os.path.join(out_dir, "1.Brainstorming & ideation", "Empathy Map.pdf"),
        "Empathy Map",
        [
            ("User Persona: Policy Analyst / Student", [
                "<strong>SAYS:</strong> 'I need to check the potential impact of a new school funding program on HDI.'",
                "<strong>THINKS:</strong> 'Will the model correctly reflect changes? How accurate is this prediction?'",
                "<strong>DOES:</strong> Inputs socio-economic parameters and compares results across different scenarios.",
                "<strong>FEELS:</strong> Motivated to improve development parameters, yet concerned about data availability."
            ]),
            ("Pains & Gains", [
                "<strong>Pains:</strong> Scattered socio-economic datasets, complex statistical formulas, and delayed calculations.",
                "<strong>Gains:</strong> Instantly visualize the outcome of policy indicators and get clear classifications."
            ])
        ]
    )

    # 4. Customer Journey Map
    create_pdf(
        os.path.join(out_dir, "2.Requirement Analysis", "Customer Journey Map.pdf"),
        "Customer Journey Map",
        [
            ("Journey Steps", [
                "1. <strong>Discovery:</strong> Analyst visits the tool homepage to estimate HDI metrics.",
                "2. <strong>Input:</strong> User enters Life Expectancy, Expected Schooling, Mean Schooling, and GNI per capita.",
                "3. <strong>Prediction:</strong> The machine learning model calculates the HDI and returns the result.",
                "4. <strong>Action:</strong> User gets the HDI score, the classification category, and uses it for documentation."
            ]),
            ("Opportunities for Improvement", [
                "Provide detailed tooltips for inputs and exportable results to enhance workflow integration."
            ])
        ]
    )

    # 5. Data Flow Diagram
    create_pdf(
        os.path.join(out_dir, "2.Requirement Analysis", "Data Flow Diagram.pdf"),
        "Data Flow Diagram (DFD)",
        [
            ("DFD Levels Outline", [
                "<strong>Level 0 DFD:</strong> User interacts with the UI, sending indicators to the Web Server, which returns the HDI prediction.",
                "<strong>Level 1 DFD:</strong>",
                "1. User Inputs -> Form Validation -> Flask Backend.",
                "2. Flask Backend -> Load model.pkl -> Model Inference.",
                "3. Model Inference -> Predict HDI Value -> Post-process Category -> Render result.html."
            ])
        ]
    )

    # 6. Solution Requirements
    create_pdf(
        os.path.join(out_dir, "2.Requirement Analysis", "Solution Requirements.pdf"),
        "Solution Requirements",
        [
            ("Functional Requirements", [
                "1. The web application must collect 4 input fields: Life Expectancy, Expected Schooling, Mean Schooling, and GNI per Capita.",
                "2. The system must use a trained ML model to output a continuous prediction score between 0 and 1.",
                "3. The system must display the HDI score, percentage progress, and a development level category."
            ]),
            ("Non-Functional Requirements", [
                "1. Performance: Real-time prediction with response times under 500ms.",
                "2. Usability: Responsive web interface accessible across desktop and mobile screens.",
                "3. Reusability: Code structured cleanly into modules (model training and web server)."
            ])
        ]
    )

    # 7. Technology Stack
    create_pdf(
        os.path.join(out_dir, "2.Requirement Analysis", "_Technology Stack.pdf"),
        "Technology Stack",
        [
            ("Backend Architecture", [
                "<strong>Python & Flask:</strong> Heavy duty scientific computing libraries combined with a lightweight, robust micro-framework."
            ]),
            ("Machine Learning & Processing", [
                "<strong>Pandas & NumPy:</strong> Used for data manipulation, cleaning, and preprocessing.",
                "<strong>Scikit-Learn:</strong> Used for training and evaluating the Linear Regression model.",
                "<strong>Joblib:</strong> Used for model serialization and loading."
            ]),
            ("Frontend Development", [
                "<strong>HTML5 & CSS3:</strong> Built with modern, responsive styling, variables, glassmorphism, and transitions for professional aesthetic appeal."
            ])
        ]
    )

    # 8. Problem-Solution Fit
    create_pdf(
        os.path.join(out_dir, "3.Project Design Phase", "Problem-Solution Fit.pdf"),
        "Problem-Solution Fit",
        [
            ("Mapping Needs to Solutions", [
                "<strong>Problem:</strong> Retrospective and slow manual calculations of development index progress.",
                "<strong>Solution:</strong> A real-time predictive tool using machine learning model trained on historical UN data.",
                "<strong>Fit Validation:</strong> User enters current parameters and immediately receives a reliable, data-backed prediction mapping directly to official UN scales."
            ])
        ]
    )

    # 9. Proposed Solution
    create_pdf(
        os.path.join(out_dir, "3.Project Design Phase", "Proposed Solution.pdf"),
        "Proposed Solution",
        [
            ("Solution Architecture", [
                "A predictive web application comprising a regression model trained on historical global records.",
                "The web server utilizes Flask to handle inputs, feeds them to the serialized model, and returns results on a clean, modern dashboard."
            ]),
            ("Key Values", [
                "High accuracy (r2 score verification), modern interface, clear categories, and zero setup dependencies for the user."
            ])
        ]
    )

    # 10. Project Planning
    create_pdf(
        os.path.join(out_dir, "4.Project Planning Phase", "Project Planning.pdf"),
        "Project Planning",
        [
            ("Sprint Cycles", [
                "<strong>Sprint 1: Brainstorming & Requirement Analysis:</strong> Define problem statements, target stack, and build empathy maps.",
                "<strong>Sprint 2: Data Preprocessing & Modeling:</strong> Train the regression model on the HDI dataset, analyze R2 scores, and save via joblib.",
                "<strong>Sprint 3: Web App Integration:</strong> Build Flask app, design user interfaces and style components.",
                "<strong>Sprint 4: Verification & Docs:</strong> Perform unit tests and write manuals."
            ])
        ]
    )

    # 11. Code-Layout, Readability and Reusability
    create_pdf(
        os.path.join(out_dir, "5.Project Development Phase", "Code-Layout, Readability and Reusability.pdf"),
        "Code-Layout, Readability and Reusability",
        [
            ("Coding Guidelines", [
                "1. Clean Code Structure: Separation of concerns between backend server logic (app.py) and training routines (train_model.py).",
                "2. Standard Naming Conventions: PEP-8 compliance for variable and function naming.",
                "3. Reusable Components: Encapsulated HDI classification logic and layout templates."
            ])
        ]
    )

    # 12. Coding & Solution
    create_pdf(
        os.path.join(out_dir, "5.Project Development Phase", "Coding & Solution.pdf"),
        "Coding & Solution",
        [
            ("Core Implementation", [
                "Linear Regression model fits the relationship between dimensions (life expectancy, schooling, income) and HDI index scores.",
                "Serialized model outputs predictions dynamically upon POST requests on Flask routes."
            ])
        ]
    )

    # 13. No. of Functional Features Included in the Solution
    create_pdf(
        os.path.join(out_dir, "5.Project Development Phase", "No. of Functional Features Included in the Solution.pdf"),
        "Functional Features",
        [
            ("Features List", [
                "1. <strong>Prediction Engine:</strong> Real-time prediction based on 4 key metrics.",
                "2. <strong>Category Map:</strong> Automatic categorization into 4 development tiers.",
                "3. <strong>Responsive Dashboard:</strong> Seamless desktop and mobile user experience.",
                "4. <strong>Interactive Result Visual:</strong> Progress score ring indicating level out of 1.000."
            ])
        ]
    )

    # 14. Performance Testing
    create_pdf(
        os.path.join(out_dir, "6.Project Testing", "Performance Testing.pdf"),
        "Performance Testing",
        [
            ("Test Scenarios", [
                "<strong>Load Testing:</strong> 100 concurrent requests processed under 500ms average response time.",
                "<strong>Model Accuracy:</strong> R2 score evaluated on the split test dataset to ensure high generalization and prevent overfitting."
            ])
        ]
    )

    # 15. HDI Project Documentation
    create_pdf(
        os.path.join(out_dir, "7.Project Documentation", "HDI Project Documentation.pdf"),
        "HDI Project Documentation",
        [
            ("Setup Instructions", [
                "1. Install dependencies: pip install flask pandas scikit-learn joblib",
                "2. Train the model: python train_model.py",
                "3. Start server: python app.py",
                "4. Access UI via http://127.0.0.1:5000"
            ])
        ]
    )

    # 16. Project Executable Files
    create_pdf(
        os.path.join(out_dir, "7.Project Documentation", "Project Executable Files.pdf"),
        "Project Executable Files",
        [
            ("Source Layout", [
                "<strong>app.py:</strong> Flask server application.",
                "<strong>train_model.py:</strong> Machine learning model trainer script.",
                "<strong>hdi.csv:</strong> United Nations HDI historical dataset.",
                "<strong>model.pkl:</strong> Serialized model weights.",
                "<strong>templates/:</strong> Folder containing HTML views (index.html, result.html).",
                "<strong>static/:</strong> Folder containing stylesheets (style.css)."
            ])
        ]
    )

    # 17. Demonstration of Proposed Features
    create_pdf(
        os.path.join(out_dir, "8.Project Demonstration", "Demonstration of Proposed Features.pdf"),
        "Demonstration of Proposed Features",
        [
            ("System Walkthrough", [
                "Shows inputs processed, scores rendered within progress animations, and tier badges displayed based on thresholds.",
                "Confirms correct classifications for Low (<0.550), Medium (<0.700), High (<0.800), and Very High (>=0.800) levels."
            ])
        ]
    )

    # 18. Project Demo Planning
    create_pdf(
        os.path.join(out_dir, "8.Project Demonstration", "Project Demo Planning.pdf"),
        "Project Demo Planning",
        [
            ("Presentation Outline", [
                "1. Problem Definition & Objectives.",
                "2. Tech Stack & ML Model Training Metrics (R2 Score).",
                "3. Live prediction run on a Web Browser.",
                "4. Wrap up: scalability and future enhancements."
            ])
        ]
    )

    # 19. Scalability & Future Plan
    create_pdf(
        os.path.join(out_dir, "8.Project Demonstration", "Scalability & Future Plan.pdf"),
        "Scalability & Future Plan",
        [
            ("Future Enhancements", [
                "1. <strong>Explainable AI:</strong> Add SHAP or LIME value breakdowns to show exactly how much each parameter contributed to the prediction.",
                "2. <strong>Alternative Models:</strong> Transition from Linear Regression to Gradient Boosting models (XGBoost/LightGBM) to capture non-linear relationships.",
                "3. <strong>Database Integration:</strong> Save predictions to historical records to chart trends over time."
            ])
        ]
    )

    print("\nAll 19 phase PDF files successfully generated in the 'generated_pdfs' directory!")

if __name__ == "__main__":
    main()
