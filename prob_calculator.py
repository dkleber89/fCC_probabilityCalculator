"""Probility calculator module"""
import copy
import random

class Hat:
    """Hat with balls to draw"""
    def __init__(self, **args: int) -> None:
        self.contents: list[str] = []

        for color, count in args.items():
            self.contents.extend([color]*count)

    def draw(self, amount: int) -> list[str]:
        """Draw balls from heat

        Args:
            amount (int): Amount of balls to draw

        Returns:
            list[str]: List of drawed balls
        """
        temp_list: list[str] = []

        if len(self.contents) <= amount:
            temp_list = copy.copy(self.contents)
            self.contents.clear()

            return temp_list

        index_list: list[int] = []
        max_index = len(self.contents) - 1

        while len(index_list) < amount:
            random_index = random.randint(0, max_index)

            if index_list.count(random_index) != 0:
                continue

            index_list.append(random_index)

        index_list.sort(reverse=True)

        for index in index_list:
            temp_list.append(self.contents.pop(index))

        return temp_list


def experiment(
    hat: Hat,
    expected_balls: dict[str, int],
    num_balls_drawn: int, num_experiments: int
    ) -> float:
    """Calculate the probability of drawing,
    at least the expected balls (Not a math calc -> Bases on trail)

    Args:
        hat (Hat): Hat with balls
        expected_balls (dict[str, int]): Expectation of drawed balls
        num_balls_drawn (int): Amount of balls to be drawn
        num_experiments (int): How many tryouts

    Returns:
        float: Calculated probability
    """
    match_count = 0

    i = num_experiments
    while i > 0:
        i -= 1

        temp_hat = copy.deepcopy(hat)

        drawn_balls = temp_hat.draw(num_balls_drawn)

        balls = {}

        for drawn_ball in drawn_balls:
            balls[drawn_ball] = balls.get(drawn_ball, 0) + 1

        match = True

        for expected_color, expected_count in expected_balls.items():
            if balls.get(expected_color, 0) >= expected_count:
                continue

            match = False

        if match:
            match_count += 1

    return match_count / num_experiments
