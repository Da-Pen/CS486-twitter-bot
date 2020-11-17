import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots()
ax1.plot(list(range(1, 11)), [5.76, 4.2, 3.26, 2.51, 1.93, 1.49, 1.18, 1.06, 0.98, 0.96])
ax1.set_title('LSTM: # Epochs vs Cross Entropy')
ax1.set_xlabel('# Epochs')
ax1.set_ylim([0, 6])
ax1.set_ylabel('Cross Entropy')
fig1.savefig('LSTM-epochs-vs-loss.png')