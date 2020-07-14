import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "Adobe Caslon Pro"
plt.rcParams["axes.titlesize"] = "larger"

def mse(true, pred):
    """
    true: array of true values    
    pred: array of predicted values
    
    returns: mean square error loss
    """
    
    return np.sum((true - pred)**2)

def mae(true, pred):
    """
    true: array of true values    
    pred: array of predicted values
    
    returns: mean absolute error loss
    """
    
    return np.sum(np.abs(true - pred))

fig, ax1 = plt.subplots(1,1, figsize = (7,5))

# array of same target value 10000 times
target = np.repeat(100, 10000) 
pred = np.arange(-10000,10000, 2)

loss_mse = [mse(target[i], pred[i]) for i in range(len(pred))]
loss_mae = [mae(target[i], pred[i]) for i in range(len(pred))]

color = 'tab:red'
mae, = ax1.plot(pred, loss_mae, color=color, label='L1')
ax1.set_xlabel('Predictions')
ax1.set_ylabel('L1', color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('L2', color=color)
ax2.tick_params(axis='y', labelcolor=color)
mse, = ax2.plot(pred, loss_mse, color=color, label='L2')

ax1.set_title("MSE (L1) vs MAE (L2)")

#fig.tight_layout()
plt.legend(handles=[mse, mae])
print("Exported loss_L1_L2.svg")
plt.savefig(fname="../loss_L1_L2.svg")

#plt.show()


def sm_mae(true, pred, delta):
    """
    true: array of true values    
    pred: array of predicted values
    
    returns: smoothed mean absolute error loss
    """
    loss = np.where(np.abs(true-pred) < delta , 0.5*((true-pred)**2), delta*np.abs(true - pred) - 0.5*(delta**2))
    return np.sum(loss)

fig, ax1 = plt.subplots(1,1, figsize = (7,5))

target = np.repeat(0, 1000) 
pred = np.arange(-10,10, 0.02)

delta = [0.1, 0.5, 1, 2, 10]

losses_huber = [[sm_mae(target[i], pred[i], q) for i in range(len(pred))] for q in delta]

# plot 
for i in range(len(delta)):
    ax1.plot(pred, losses_huber[i], label = delta[i])
ax1.set_xlabel('Predictions')
ax1.set_ylabel('Loss')
ax1.set_title("Huber Loss/ Smooth MAE Loss")
ax1.legend(title="$\delta$ values")
ax1.set_ylim(bottom=-1, top = 15)

print("Exported loss_Huber.svg")
plt.savefig(fname="../loss_Huber.svg")
#plt.show()