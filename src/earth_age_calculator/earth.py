def calculate_earth_age(year: int) -> int:
    """지구의 나이를 계산합니다.
    - 지구의 나이는 오래 전부터 과학자들이 추측해왔지만,
    - 정확하게 계산된 것은 1862년입니다. 1862년 프랑스의 천문학자 루이 드 라 히레는 지구의 나이를 약 45억 년으로 추정했습니다.
    - 이 추정을 기반으로 지구의 나이를 1864년에 4500000000 살로 두고 입력된 연도에는 몇살인지 계산합니다.

    :param year:
    :return:
    지구의 나이 (단위: 년)
    """
    # 지구의 탄생 시기를 45억 년으로 가정합니다.
    base_earth_age = 4550000000
    standard_age_year = 1956

    # 지구의 나이를 계산 합니다.
    age = base_earth_age + (year - standard_age_year)

    return age
