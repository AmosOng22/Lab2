import Lab2 as temperature

def test_min_max():
    test_arr=[2,45,23,6,75,4,67]
    test_result=[2,75]
    result_arr=temperature.find_min_max(test_arr)
    assert (result_arr==test_result)

def test_average():
    test_arr=[2,45,23,6,75,4,67]
    test_result=(2+45+23+6+75+4+67)/7.0
    result_arr=temperature.calc_average(test_arr)
    assert (result_arr==test_result)

def test_median():
    test_arr=[2,45,23,6,75,4]
    test_result=14.5
    result_arr=temperature.calc_median_temperature(test_arr)
    assert (result_arr==test_result)
