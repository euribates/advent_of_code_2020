import re


def is_valid_byr(value):
    return 1920 <= int(value) < 2003


def is_valid_iyr(value):
    return 2010 <= int(value) < 2021


def is_valid_eyr(value):
    return 2020 <= int(value) < 2031


def is_valid_hgt(value):
    pat_height = re.compile(r'(\d+)(in|cm)$')
    match = pat_height.match(value)
    if match:
        value = int(match.group(1))
        units = match.group(2)
        if units == 'cm':
            return 150 <= value < 194
        elif units == 'in':
            return 59 <= value < 77
    return False


def is_valid_hcl(value):
    pat_color = re.compile(r'#[0-9a-f]{6}$')
    match = pat_color.match(value)
    return bool(match)


def is_valid_ecl(value):
    return value in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])


def is_valid_pid(value):
    pat_pid = re.compile(r'\d{9}$')
    match = pat_pid.match(value)
    return bool(match)


def is_valid_passport(passport):
    validators = {
        'byr': is_valid_byr,
        'iyr': is_valid_iyr,
        'eyr': is_valid_eyr,
        'hgt': is_valid_hgt,
        'hcl': is_valid_hcl,
        'ecl': is_valid_ecl,
        'pid': is_valid_pid,
    }
    return all([
        is_valid(passport[name]) for name, is_valid in validators.items()
        ])


def is_full_passport(passport):
    return all([
        'byr' in passport,
        'iyr' in passport,
        'eyr' in passport,
        'hgt' in passport,
        'hcl' in passport,
        'ecl' in passport,
        'pid' in passport,
        # 'cid' in passport,
    ])

