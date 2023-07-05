import os
from cover_letter import cover_letter
from cover_letter_txt import cover_letter_txt
from merge_pdf import merge_pdf
from datetime import date
import shutil

def main():
    # Take inputs
    choice = input("Choose option:\n1 for Data Analyst\n2 for Data Scientist\n3 for ML Engineer\n4 for MLOps Engineer\n5 for Data Engineer: ") or "2"
    if choice == "1":
        role = input("Enter role (Data Analyst): ") or "Data Analyst"
        company = input("Enter company (XYZ Analytics): ") or "XYZ Analytics"
        skill_1 = input("Enter skill 1: ") or "Data Analysis"
        skill_2 = input("Enter skill 2: ") or "Data Visualization"
    elif choice == "2":
        role = input("Enter role (Data Scientist): ") or "Data Scientist"
        company = input("Enter company (XYZ Analytics): ") or "XYZ Analytics"
        skill_1 = input("Enter skill 1: ") or "Machine Learning"
        skill_2 = input("Enter skill 2: ") or "Advanced Analytics"
    elif choice == "3":
        role = input("Enter role (ML Engineer): ") or "ML Engineer"
        company = input("Enter company (XYZ Analytics): ") or "XYZ Analytics"
        skill_1 = input("Enter skill 1: ") or "Machine Learning"
        skill_2 = input("Enter skill 2: ") or "Software Engineering"
    elif choice == "4":
        role = input("Enter role (MLOps Engineer): ") or "MLOps Engineer"
        company = input("Enter company (XYZ Analytics): ") or "XYZ Analytics"
        skill_1 = input("Enter skill 1: ") or "Infrastructure Technologies"
        skill_2 = input("Enter skill 2: ") or "DevOps"
    elif choice == "5":
        role = input("Enter role (Data Engineer): ") or "Data Engineer"
        company = input("Enter company (XYZ Analytics): ") or "XYZ Analytics"
        skill_1 = input("Enter skill 1: ") or "Data Warehousing & ETL"
        skill_2 = input("Enter skill 2: ") or "Database Systems"
    today = date.today()
    date_ll = today.strftime("%b-%d-%Y")
    
    # Declare paths
    root_dir = f"/home/himalaya/Desktop/FT/Jobs applied/{date_ll}-{company}"
    cover_letter_path = os.path.join(root_dir, f"Himalaya Sharma {company} Cover Letter.pdf")
    cover_letter_txt_path = os.path.join(root_dir, f"Himalaya Sharma {company} Cover Letter.txt")
    resume_path = os.path.join(root_dir, f"Himalaya Sharma {company} Resume.pdf")
    transcript_path = os.path.join(root_dir, f"Himalaya Sharma {company} UWaterloo Transcript.pdf")
    application_package_path = os.path.join(root_dir, f"Himalaya Sharma {company} Application Package.pdf")

    # Check if root directory exists or not
    if(os.path.exists(root_dir) == False):
        os.makedirs(root_dir)

    # Create cover letter
    cover_letter(choice, role, company, skill_1, skill_2, cover_letter_path)
    cover_letter_txt(choice, role, company, skill_1, skill_2, cover_letter_txt_path)
    if choice == "1":
        # Copy resume and change name
        shutil.copyfile('/home/himalaya/Desktop/coding/create-application-package/static/data-analyst-resume.pdf', resume_path)
    elif choice == "2":
        # Copy resume and change name
        shutil.copyfile('/home/himalaya/Desktop/coding/create-application-package/static/data-scientist-resume.pdf', resume_path)
    elif choice == "3":
        # Copy resume and change name
        shutil.copyfile('/home/himalaya/Desktop/coding/create-application-package/static/ml-engineer-resume.pdf', resume_path)
    elif choice == "4":
        # Copy resume and change name
        shutil.copyfile('/home/himalaya/Desktop/coding/create-application-package/static/mlops-engineer-resume.pdf', resume_path)
    elif choice == "5":
        # Copy resume and change name
        shutil.copyfile('/home/himalaya/Desktop/coding/create-application-package/static/data-engineer-resume.pdf', resume_path)
    shutil.copyfile('/home/himalaya/Desktop/coding/create-application-package/static/transcript.pdf', transcript_path)

    # Merge transcript, cover letter and transcript
    merge_pdf(resume_path, cover_letter_path, transcript_path, application_package_path)

if __name__ == "__main__":
    main()