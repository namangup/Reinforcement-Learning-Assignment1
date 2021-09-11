from gym.envs.registration import register

register(
    id = 'bernoulli-bandit-v0',
    entry_point = 'custom_envs.envs:BernoulliBandit'
)
register(
    id = 'gaussian-bandit-v0',
    entry_point = 'custom_envs.envs:GaussianBandit'
)
register(
    id = 'random-walk-v0',
    entry_point = 'custom_envs.envs:RandomWalk'
)