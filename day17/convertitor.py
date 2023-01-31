INCHES_TO_METER = 0.0254
FEET_TO_METER = 0.3048


def convert(feet_local, inches_local):
    convert_result = (FEET_TO_METER*feet_local) + (INCHES_TO_METER*inches_local)
    return convert_result


if __name__ == "__main__":
    result_lo = convert(3,4)
    print(f"{result_lo} m")

