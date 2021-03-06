# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
from math import log
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    # Step I: Read Data
    data_dir = os.path.join(os.path.dirname(__file__), 'sample_data', '806初賽訓練數據')
    train_filename_list = os.listdir(data_dir)
    
    n_timesteps = 7500
    n_features = 4
    
    X = []
    y = []
    for train_filename in train_filename_list:
        
        data_path = os.path.join(data_dir, train_filename)
        data = pd.read_excel(data_path, header=None)
        
        # Get Features
        feature = np.array(data.iloc[:n_timesteps, :n_features].values, dtype=float)
        # Get Target Value
        target = float(data.iloc[n_timesteps, 0].replace('加工品質量測結果:', ''))
        
        X.append(feature)
        y.append(target)
    
    X = np.array(X)
    y = np.array(y)
    
#    # Step II: Plot 40 Samples
#    
#    fig_dir = os.path.join(os.path.dirname(__file__), 'fig')
#    if not os.path.exists(fig_dir):
#        os.makedirs(fig_dir)
#    
#    for i in range(len(X)):
#        print('\rProgress: {:.2f}%'.format((i+1)/len(X)*100), end='\r')
#        
#        sample_fig_dir = os.path.join(fig_dir, 'sample_{}'.format(i+1))
#        if not os.path.exists(sample_fig_dir):
#            os.makedirs(sample_fig_dir)
#        
#        for j in range(X[i].shape[1]):
#            plt.figure(figsize=(10, 8))
#            plt.title('Sample #{}, feature #{}'.format(i+1, j+1))
#            plt.plot(X[i][:, j], label='feature {}'.format(j+1))
#            plt.savefig(os.path.join(sample_fig_dir, 'sample{}_feature{}.jpg'.format(i+1, j+1)))
#            plt.close()
    
    feature_num = 0
    feature_0 = np.array([])
    y_series = np.array([])
    for i in range(len(X)):
        Xf0 = X[i][:, feature_num]
        yf0 = y[i]* np.ones(n_timesteps)
        
        # -Log
#        Xf0 = [-log(Xf0_) for Xf0_ in Xf0]
        
        if len(feature_0) == 0:
            feature_0 = Xf0
            y_series = yf0
        else:
            feature_0 = np.append(feature_0, Xf0)
            y_series = np.append(y_series, yf0)
         
    fig, ax1 = plt.subplots(figsize=(100,5))
    t = np.arange(0.01, 10.0, 0.01)
    s1 = np.exp(t)
    ax1.plot(feature_0, 'blue')
    
    ax2 = ax1.twinx()
    ax2.plot(y_series, 'r.')
    
        
    