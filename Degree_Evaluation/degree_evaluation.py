class Course:
    def __init__(self, params):
        self.subject = params.get('subject')
        self.number = params.get('number')

class CompletedCourse:
    def __init__(self, params):
        self.course = params.get('course')
        self.semester_completed = params.get('semester_completed')
        self.unites = params.get('units')
        self.grade = params.get('grade')
        self.title = params.get('title')

class SubRequirement:
    def __init__(self, params):
        self.name = params.get('name')
        self.is_fulfilled = params.get('is_fulfilled')
        self.list_of_courses = params.get('list_of_courses')
        self.note = params.get('note')

class UserInformation:
    def __init__(self, params):
        self.name = params.get('name')
        self.major = params.get('major')
        self.prepared_on = params.get('prepared_on')
        self.program_code = params.get('program_code')
        self.catalog_year = params.get('catalog_year')
        self.student_id = params.get('student_id')
        self.graduation_date = params.get('graduation_date')

class CourseworkTotals:
    def __init__(self, params):
        self.units_earned = params.get('units_earned')
        self.units_attemped = params.get('units_attemped')
        self.points = params.get('points')
        self.gpa = params.get('gpa')

class AcademicCoursework:
    def __init__(self, params):
        self.courses = params.get('courses')
        self.current_courses = params.get('current_courses')
        self.sdsu_cumulative_totals = params.get('sdsu_cumulative_totals')
        self.transfer_cumulative_totals = params.get('transfer_cumulative_totals')
        self.total_units_earned = params.get('total_units_earned')

class DegreeEvaluation:
    def __init__(self, params):
        self.user_information = params.get('user_information')
        self.competency_requirements = params.get('competency_requirements')
        self.graduation_writing_assessment_requirement = params.get('graduation_writing_assessment_requirement')
        self.american_institutions_requirements = params.get('american_institutions_requirements')
        self.unit_residence_and_gpa_requirements = params.get('unit_residence_and_gpa_requirements')
        self.general_education_unit_requirements = params.get('general_education_unit_requirements')
        self.communication_and_critical_thinking = params.get('communication_and_critical_thinking')
        self.foundations_natural_sciences_and_quantitative_reasoning = params.get('foundations_natural_sciences_and_quantitative_reasoning')
        self.foundations_social_and_behavioral_sciences = params.get('foundations_social_and_behavioral_sciences')
        self.foundations_humanities = params.get('foundations_humanities')
        self.general_education_american_institutions = params.get('general_education_american_institutions')
        self.cultural_diversity = params.get('cultural_diversity')
        self.explorations_natural_sciences = params.get('explorations_natural_sciences')
        self.explorations_social_and_behavioral_sciences = params.get('explorations_social_and_behavioral_sciences')
        self.explorations_humanities = params.get('explorations_humanities')
        self.preparation_for_the_major = params.get('preparation_for_the_major')
        self.major_requirements = params.get('major_requirements')
        self.academic_coursework = params.get('academic_coursework')
