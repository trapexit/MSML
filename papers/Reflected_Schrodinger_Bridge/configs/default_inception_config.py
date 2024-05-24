import ml_collections

def get_inception_default_configs():
  config = ml_collections.ConfigDict()
  # training
  config.training = training = ml_collections.ConfigDict()
  config.seed=42 #The utlimate answer of UNIVERSE!
  config.T = 1.0
  config.interval = 100
  config.train_method = 'alternate'
  config.t0 = 0.001  # doesn't work for sde_type - 'vp', 've'
  config.problem_name = 'inception'
  config.num_itr = 250
  config.eval_itr = 200
  config.forward_net = 'toy_inception'
  config.backward_net = 'toy_inception'
  config.use_arange_t = False  # True
  config.num_epoch = 1
  config.num_stage = 8
  config.train_bs_x = 48
  config.train_bs_t = 48
  config.sde_type = 'simple'
  # sampling
  config.samp_bs = 5000
  config.sigma_min = 0.1
  config.sigma_max = 2
  config.snapshot_freq = 2
  # optimization
#   config.optim = optim = ml_collections.ConfigDict()
  config.weight_decay = 0
  config.optimizer = 'AdamW'
  config.lr = 1e-3
  config.lr_gamma = 0.9

  model_configs={}
  return config, model_configs

