{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNaCDrc0Ks1e2ZV95QQRgZ6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/hu-prog/Deep-Learning-course/blob/master/lr_utils.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "O0vQS53yj7en"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import h5py\n",
        "\n",
        "\n",
        "def load_dataset():\n",
        "    train_dataset = h5py.File('datasets/train_catvnoncat.h5', \"r\")\n",
        "    train_set_x_orig = np.array(train_dataset[\"train_set_x\"][:]) # your train set features\n",
        "    train_set_y_orig = np.array(train_dataset[\"train_set_y\"][:]) # your train set labels\n",
        "\n",
        "    test_dataset = h5py.File('datasets/test_catvnoncat.h5', \"r\")\n",
        "    test_set_x_orig = np.array(test_dataset[\"test_set_x\"][:]) # your test set features\n",
        "    test_set_y_orig = np.array(test_dataset[\"test_set_y\"][:]) # your test set labels\n",
        "\n",
        "    classes = np.array(test_dataset[\"list_classes\"][:]) # the list of classes\n",
        "\n",
        "    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))\n",
        "    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))\n",
        "\n",
        "    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes"
      ]
    }
  ]
}