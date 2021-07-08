mapping = {
    "from_school": "Transfer College",
    "from_course_department": 'Transfer Subject',
    "from_course_code": 'Transfer Course Number',
    "from_course_name": 'Transfer Title',
    "from_course_credit_hours": None,
    "from_extra_department": None,
    "from_extra_code": None,
    "from_extra_name": None,
    "from_extra_credit_hours": None,
    "to_school": "University of Wyoming",
    "to_course_department": 'UW Subject',
    "to_course_code": 'UW Course Number',
    "to_course_name": 'UW Title',
    "to_course_credit_hours": None,
    "to_extra_department": None,
    "to_extra_code": None,
    "to_extra_name": None,
    "to_extra_credit_hours": None,
    "transfer_group": "Transfer Group **(means multiple courses must be taken)",
    'effective_term': 'Effective Term',
    'usp_attribute': 'USP Attribute',
}


def map_dict(main_dictionary):
    mapped_dict = dict((k, main_dictionary.get(v, v)) for (k, v) in mapping.items())
    return mapped_dict


def map_data(data):
    return [map_dict(item) for item in data]
