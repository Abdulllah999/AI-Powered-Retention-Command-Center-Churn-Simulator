"""Deterministic evidence matching; deliberately not candidate scoring."""
import re
SKILLS = ("python", "sql", "flask", "react", "docker", "pandas", "tensorflow", "excel")
def extract_skills(text):
    return {skill for skill in SKILLS if re.search(r"(?<!\w)" + re.escape(skill) + r"(?!\w)", text, re.I)}
def compare(resume, job):
    if not resume.strip() or not job.strip():
        raise ValueError("Provide both a fictional resume and job requirements.")
    if max(len(resume), len(job)) > 20000:
        raise ValueError("Each document must be at most 20,000 characters.")
    required = extract_skills(job)
    if not required:
        raise ValueError("No supported skills found in the job text.")
    found = extract_skills(resume)
    matched = sorted(required & found)
    missing = sorted(required - found)
    return {"evidence_terms": matched, "terms_to_review": missing,
            "interview_prompts": [f"Describe a project using {s} and a tradeoff you made." for s in sorted(required)],
            "note": "Keyword evidence only. Missing terms do not mean missing ability. Human review required."}
