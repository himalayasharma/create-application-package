import os
from cover_letter import cover_letter
from merge_pdf import merge_pdf
from datetime import date
import shutil

def main():
    # Take inputs
    role = input("Enter role (Data Scientist): ") or "Data Scientist"
    company = input("Enter company (XYZ Analytics): ") or "XYZ Analytics"
    domain = input("Enter domain (Data Science): ") or "Data Science"
    greeting = input("Enter greeting (Dear Hiring Manager): ") or "Dear Hiring Manager"

    today = date.today()
    date_ll = today.strftime("%b-%d-%Y")
    
    # Declare paths
    root_dir = f"/home/himalaya/Desktop/application/Full-time jobs/{date_ll}-{company}"
    cover_letter_path = os.path.join(root_dir, f"Himalaya Sharma {company} Cover Letter.pdf")
    resume_path = os.path.join(root_dir, f"Himalaya Sharma {company} Resume.pdf")
    transcript_path = os.path.join(root_dir, f"Himalaya Sharma {company} UWaterloo Transcript.pdf")
    application_package_path = os.path.join(root_dir, f"Himalaya Sharma {company} Application Package.pdf")

    # Check if root directory exists or not
    if(os.path.exists(root_dir) == False):
        os.makedirs(root_dir)

    # Create cover letter
    cover_letter(role, company, domain, greeting, cover_letter_path)
    # Copy resume and change name
    shutil.copyfile('/home/himalaya/Desktop/coding/create-application-package/static/resume.pdf', resume_path)
    # Copy transcript and change name
    shutil.copyfile('/home/himalaya/Desktop/coding/create-application-package/static/transcript.pdf', transcript_path)
    # Merge transcript, cover letter and transcript
    merge_pdf(resume_path, cover_letter_path, transcript_path, application_package_path)

if __name__ == "__main__":
    main()