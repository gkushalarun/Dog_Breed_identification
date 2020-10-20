{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Turn prediction probabilities into their respective label (easier to understand)\n",
    "def get_pred_label(prediction_probabilities):\n",
    "  \"\"\"\n",
    "  Turns an array of prediction probabilities into a label.\n",
    "  \"\"\"\n",
    "  return unique_breeds[np.argmax(prediction_probabilities)]\n",
    "\n",
    "# Get a predicted label based on an array of prediction probabilities\n",
    "pred_label = get_pred_label(predictions[0])\n",
    "pred_label"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
