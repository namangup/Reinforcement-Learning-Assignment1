import gym
from gym import spaces

class RandomWalk(gym.Env):
    
    def __init__(self, rng):
        self.np_random = rng
        self.action_space = spaces.Discrete(2) # 0 -> left, alpha 1-> right, beta
        self.observation_space = spaces.Discrete(5) # number of non terminal states = 5
        self.n_states = 5 # number of non terminal states
        self.state = self.n_states // 2  # Current state


    def step(self, action):
        # doesn't matter what action is taken since transition probabilites for both a_0 and a_1 are same
        if self.np_random.uniform() < 0.5:
            self.state -= 1
        else:
            self.state += 1

        if self.state == 5:
            reward = 1
            return self.state, reward, True, {}
        elif self.state == -1:
            reward = 0
            return self.state, reward, True, {}
        else:
            reward = 0
            return self.state, reward, False, {}

    def reset(self):
        self.state = self.n_states // 2
        return self.state
