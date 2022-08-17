from src.jobs import read


def get_unique_job_types(path):
    unique_data = set()
    data = read(path)
    for jobs in data:
        unique_data.add(jobs["job_type"])
    return unique_data


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    unique_data = set()
    data = read(path)
    for industries in data:
        if industries["industry"] != "":
            unique_data.add(industries["industry"])
    return unique_data


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    salaries_data = []
    data = read(path)
    for salaries in data:
        if salaries["max_salary"] != "invalid" and \
           salaries["max_salary"] != "":
            salaries_data.append(int(salaries["max_salary"]))
    salaries_data.sort(reverse=True)
    return salaries_data[0]


def get_min_salary(path):
    salaries_data = []
    data = read(path)
    for salaries in data:
        if salaries["min_salary"] != "invalid" and \
           salaries["min_salary"] != "":
            salaries_data.append(int(salaries["min_salary"]))
    salaries_data.sort()
    return salaries_data[0]


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
