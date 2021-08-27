from typing import List
from WeightedScalesPOM import ScalesPOM, Browsers, Bowls

def first_comparison(pom:ScalesPOM):
    left_side_values = [0,1,2]
    middle_values = [3,4,5]
    right_side_values = [6,7,8]

    pom.enter_values_for_bowl(side=Bowls.left, values=left_side_values)
    pom.enter_values_for_bowl(side=Bowls.right, values=middle_values)
    pom.press_weigh_button()
    result = pom.get_result_value()

    if result == ">":
        next_target = middle_values
    elif result == "<":
        next_target = left_side_values
    else:
        next_target = right_side_values
    return next_target

def second_comparison(options, pom:ScalesPOM) -> List[int]:
    pom.press_reset_button()
    left_elem = options[0]
    middle_elem = options[1]
    right_elem = options[2]

    pom.enter_values_for_bowl(side=Bowls.left, values=[left_elem])
    pom.enter_values_for_bowl(side=Bowls.right, values=[middle_elem])
    pom.press_weigh_button()
    result = pom.get_result_value()

    if result == ">":
        answer = middle_elem
    elif result == "<":
        answer = left_elem
    else:
        answer = right_elem
    return answer

def main(pom:ScalesPOM) -> None:
    first_weighing = first_comparison(pom)
    answer = second_comparison(first_weighing, pom)
    print(pom.select_coin(answer))
    print(*pom.show_what_was_weighed(), sep="\n")
    pom.driver.close()

if __name__ == '__main__':
    url = "http://ec2-54-208-152-154.compute-1.amazonaws.com/"
    pom = ScalesPOM(url, Browsers.Firefox())

    main(pom)


