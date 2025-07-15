JOB_KEYWORDS = [
    "job", "career", "vacancy", "opportunity", "opening", "position", "hiring", "recruitment"
]

def is_job_enquiry(email):
    content = f"{email['subject']} {email['snippet']} {email['body']}".lower()
    return any(keyword in content for keyword in JOB_KEYWORDS) 