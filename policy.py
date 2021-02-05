import random


class RandomPolicy:
    def decide(self, observation, actions):
        return random.choice(actions)


def run_tests():
    policy = RandomPolicy()
    result1 = policy.decide([1, 2, 3], ["a", "b"])
    assert result1 in ["a", "b"]
    result2 = policy.decide([1, 2, 3], ["a", "b"])
    assert result2 in ["a", "b"]
    result3 = policy.decide([1, 2, 3], ["a", "b"])
    assert result3 in ["a", "b"]
    print("Tests passed!")


if __name__ == "__main__":
    run_tests()
