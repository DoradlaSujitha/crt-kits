class Candidate:
    def __init__(self,name,age,email_id,skills):
        self.name=name
        self.age=age
        self.email_id=email_id
        self.skills=skills
class JobOpening:
    def __init__(self,title,required_skills):
        self.title=title
        self.required_skills=required_skills
class Interview:
    def __init__(self):
        self.score={}
    def add_score(self,candidate,round_score,score):
        self.candidate=candidate
        self.round_score=round_score
        self.score=score
        def get_total(self,candidate):
            return sum(self.scores.get(candidate.name, {}).values())
class RecruitmentManager:
    def __init__(self,candidate,jobs,interview):
        self.candidate=candidate
        self.jobs=jobs
        self.interview=interview
    def add_candidate(self, candidate):
        self.candidates.append(candidate)
    def add_job(self, job):
        self.jobs.append(job)
    def apply(self, candidate, job):
        candidate.applied_jobs.append(job)
    def shortlist(self, job):
        result = []
        for c in self.candidates:
            if job in c.applied_jobs:
                if job.required_skills.issubset(c.skills):
                    score = self.interview.get_total(c)
                    if score >= 10:
                        result.append((c.name, score))
        return result