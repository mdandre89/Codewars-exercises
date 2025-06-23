def byte_to_set(byte):
    return {index for index, item in enumerate(format(byte, '08b')) if item == '1' }