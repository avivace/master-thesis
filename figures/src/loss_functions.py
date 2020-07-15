import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "Adobe Caslon Pro"
plt.rcParams["axes.titlesize"] = "larger"
plt.rcParams["mathtext.fontset"] = "stix"

xaxis_label = 'Prediction Error ($y - \hat{y}$)'
fig, ax1 = plt.subplots(1,1, figsize = (7,5))

# array of same target value 10000 times
target = np.repeat(100, 10000) 
pred = np.arange(-10000,10000, 2)

x = np.arange(-1., 1.01, 0.01)

mae = np.abs(x)
mse = np.power(x, 2)

#loss_mse = [mse(target[i], pred[i]) for i in range(len(pred))]
#loss_mae = [mae(target[i], pred[i]) for i in range(len(pred))]

color = 'tab:red'
mseplot, = ax1.plot(x, mse, color=color, label='MSE (L1)')
maeplot, = ax1.plot(x, mae, color="tab:blue", label="MAE (L2)")
ax1.set_xlabel(xaxis_label)
ax1.set_ylabel('Loss')

#ax2 = ax1.twinx()

color = 'tab:blue'
#ax2.set_ylabel('L2', color=color)
#ax2.tick_params(axis='y', labelcolor=color)
#mse, = ax1.plot(pred, loss_mse, color=color, label='L2')

#ax1.set_title("MSE (L1) vs MAE (L2)")

#fig.tight_layout()
plt.legend(handles=[mseplot, maeplot])
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
ax1.set_xlabel(xaxis_label)
ax1.set_ylabel('Loss')
#ax1.set_title("Huber Loss/ Smooth MAE Loss")
ax1.legend(title="$\delta$ values")
ax1.set_ylim(bottom=-1, top = 15)

print("Exported loss_Huber.svg")
plt.savefig(fname="../loss_Huber.svg")
#plt.show()


###

def logcosh(true, pred):
    loss = np.log(np.cosh(pred - true))
    return np.sum(loss)

fig, ax1 = plt.subplots(1,1, figsize = (7,5))

target = np.repeat(0, 1000) 
pred = np.arange(-10,10, 0.02)

loss_logcosh = [logcosh(target[i], pred[i]) for i in range(len(pred))]

ax1.plot(pred, loss_logcosh)
ax1.set_xlabel(xaxis_label)
ax1.set_ylabel('Loss')
print("Exported loss_logcosh.svg")
plt.savefig(fname="../loss_logcosh.svg")

#plt.show()

def quan(true, pred, theta):
    loss = np.where(true >= pred, theta*(np.abs(true-pred)), (1-theta)*(np.abs(true-pred)))
    return np.sum(loss)


###


fig, ax1 = plt.subplots(1,1, figsize = (7,5))

target = np.repeat(0, 1000) 
pred = np.arange(-10,10, 0.02)

quantiles = [0.25, 0.5, 0.75, 0.90]

losses_quan = [[quan(target[i], pred[i], q) for i in range(len(pred))] for q in quantiles]

# plot 
for i in range(len(quantiles)):
    ax1.plot(pred, losses_quan[i], label = quantiles[i])
ax1.set_xlabel(xaxis_label)
ax1.set_ylabel('Loss')
ax1.legend(title="Quantiles ($\gamma$)")
print("Exported loss_quant.svg")
plt.savefig(fname="../loss_quant.svg")