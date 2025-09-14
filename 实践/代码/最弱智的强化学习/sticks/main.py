import gymnasium as gym
from random_policy import random_policy

p = [random_policy]

if __name__ == '__main__':
    while True:
        a = input('policy choice: \'random\'(0)')
        if a in ['0']:
            policy = p[0]()
            break
        else:
            print('输入有误')
    env = gym.make('CartPole-v1')
    epoch = 1
    total_reward = 0
    R = []
    counter = 0
    for e in range(epoch):
        obs = env.reset()
        total_reward = 0
        counter = 0
        while True:
            action_space = env.action_space
            print(action_space)
            action = policy.act(obs, action_space)
            obs, reward, done, tru, info = env.step(action)
            total_reward += reward
            print(obs)
            if done:
                R.append(reward)
                policy.update()
                break
            else:
                counter += 1
        print(f'training_{e + 1}, reward: {total_reward}')
