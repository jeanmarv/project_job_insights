from src.jobs import read


def get_unique_job_types(path):
    unique_data = set()
    data = read(path)
    for jobs in data:
        unique_data.add(jobs["job_type"])
    return unique_data


def filter_by_job_type(jobs, job_type):
    job_type_data = []
    for alljobs in jobs:
        if alljobs["job_type"] == job_type:
            job_type_data.append(alljobs)
    return job_type_data


def get_unique_industries(path):
    unique_data = set()
    data = read(path)
    for industries in data:
        if industries["industry"] != "":
            unique_data.add(industries["industry"])
    return unique_data


def filter_by_industry(jobs, industry):
    job_type_data = []
    for alljobs in jobs:
        if alljobs["industry"] == industry:
            job_type_data.append(alljobs)
    return job_type_data


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


def salary_error_tester(minsal, maxsal, sal):
    if minsal == "" or\
       minsal == "invalid" or\
       maxsal == "" or\
       maxsal == "invalid":
        raise ValueError
    elif (type(minsal) != int or
          type(maxsal) != int or
          type(sal) != int):
        raise ValueError
    elif minsal > maxsal:
        raise ValueError


def matches_salary_range(job, salary):
    try:
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]
        salary_error_tester(min_salary, max_salary, salary)
        return min_salary <= salary <= max_salary
    except KeyError:
        raise ValueError


def filter_by_salary_range(jobs, salary):
    jobs_list = []
    for alljobs in jobs:
        try:
            if matches_salary_range(alljobs, salary):
                jobs_list.append(alljobs)
        except ValueError:
            pass
    return jobs_list
