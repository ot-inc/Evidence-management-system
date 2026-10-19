class Evidence:
    def __init__(
        self,
        evidence_number,
        case_number,
        description,
        location,
        officer
    ):
        self.evidence_number = evidence_number
        self.case_number = case_number
        self.description = description
        self.location = location
        self.officer = officer