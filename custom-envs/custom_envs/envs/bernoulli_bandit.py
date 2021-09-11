import gym
from gym import spaces

class BernoulliBandit(gym.Env):
    
    def __init__(self, alpha, beta, rng):
        self.np_random = rng
        self.action_space = spaces.Discrete(2) # 0 -> left, alpha 1-> right, beta
        self.state = 0 # start state
        self.alpha = alpha
        self.beta = beta


    def step(self, action):
        if action == 0:
            if self.np_random.uniform() < self.alpha:
                self.state = 1
                reward = 1
            else:
                self.state = 2
                reward = 0
        else:
            if self.np_random.uniform() < self.beta:
                self.state = 2
                reward = 1
            else:
                self.state = 1
                reward = 0

        return self.state, reward, True, {}

    def reset(self):
        self.state = 0
        return self.state
