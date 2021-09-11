import gym
from gym import spaces

class GaussianBandit(gym.Env):
    
    def __init__(self, means, rng, std=1):
        self.np_random = rng
        self.action_space = spaces.Discrete(10) # 0 -> left, alpha 1-> right, beta
        self.state = 0 # start state
        self.means = means
        self.std = std


    def step(self, action):
        self.state = action + 1
        reward = self.np_random.normal(loc=self.means[action], scale=self.std)
        return self.state, reward, True, {}

    def reset(self):
        self.state = 0
        return self.state
