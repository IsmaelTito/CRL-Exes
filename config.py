
config_data = {'epuck_error': 0.05, 'reward_error': 0.025, 'epuck_exp': 4.00, 'reward_exp': 2.20, 'l_reward_weight': 0.75, 'reward_area': 0.675, 'reward_c': 0.80}


def set_parameters(e_error, r_error, e_exp, r_exp, lr_weight, r_area, r_const,):
    config_data['epuck_error'] = e_error
    config_data['reward_error'] = r_error
    config_data['epuck_exp'] = e_exp
    config_data['reward_exp'] = r_exp
    config_data['l_reward_weight'] = lr_weight
    config_data['reward_area'] = r_area
    config_data['reward_c'] = r_const
