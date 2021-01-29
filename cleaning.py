import numpy as np

def is_outlier(data, level=1, continuous=False, log=False):
  """Flag outliers in data

  :return: A series of boolean flags indicating `True` if within acceptable range, and `False` if an outlier
  :rtype: series of booleans
  Source: https://becominghuman.ai/outlier-detection-in-real-estate-data-4e7375e2c8ba
  """
  if log is True:
      data = np.log(data + 1)
  pct_range = pct_method(data, level)
  iqr_range = iqr_method(data)
  std_range = std_method(data)

  high_limit = np.max([pct_range[1],
                       iqr_range[1],
                       std_range[1]]) 
  if continuous:
    low_limit = np.min(data)
  else:
    low_limit = np.min([pct_range[0],
                        iqr_range[0],
                        std_range[0]])
  # Restrict data between the minimum and maximum
  outlier = data.between(low_limit, high_limit)

  return outlier

def pct_method(data, level):
  """Percentile based method
  Cut perdefined percentage amount from the top and bottom of the distribution
  """
  percentile = level / 100
  upper = data.quantile(1 - percentile)
  lower = data.quantile(percentile)
  return [lower, upper]

def iqr_method(data):
  """Interquartile range method
  """
  # Calculating the IQR
  perc_75 = data.quantile(0.75)
  perc_25 = data.quantile(0.25)
  iqr_range = perc_75 - perc_25
  # Obtaining the lower and upper bound
  iqr_upper = perc_75 + 1.5 * iqr_range
  iqr_lower = perc_25 - 1.5 * iqr_range
  
  return [iqr_lower, iqr_upper]


def std_method(data):
  """Standard deviation method
  Derived from emperical rule https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule
  """
  std = np.std(data)
  upper_3std = np.mean(data) + 3 * std
  lower_3std = np.mean(data) - 3 * std

  return [lower_3std, upper_3std]