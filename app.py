{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP8nMQ3fwbRfsQlFdzxllyg",
      "include_colab_link": True
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
        "<a href=\"https://colab.research.google.com/github/Tushar01yadav/Streamlit_app/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "\n",
        "# Title\n",
        "st.title(\"🎈 My First Streamlit App\")\n",
        "\n",
        "# Header\n",
        "st.header(\"👋 Hello there!\")\n",
        "\n",
        "# Text input\n",
        "name = st.text_input(\"Enter your name:\")\n",
        "\n",
        "# Slider\n",
        "age = st.slider(\"Select your age:\", 1, 100, 25)\n",
        "\n",
        "# Button\n",
        "if st.button(\"Submit\"):\n",
        "    if name:\n",
        "            st.success(f\"✅ Welcome, {name}! You are {age} years old.\")\n",
        "    else:\n",
        "                        st.warning(\"⚠️ Please enter your name above.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ENy4SdPucTQw",
        "outputId": "59f5230b-da9a-44f6-f2b9-7dc0e7520d38"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-07-04 08:37:25.795 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.797 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.799 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.800 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.801 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.802 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.803 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.803 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.807 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.808 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.809 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.810 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.810 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.811 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.812 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.815 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.816 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.817 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.817 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.818 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.819 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.819 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.820 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.820 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-07-04 08:37:25.824 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Qu2YZ1qClf-0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!git init"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EUtSsEWCdHy8",
        "outputId": "3ad9e13c-331c-4f2c-917d-49a1530df22e"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reinitialized existing Git repository in /content/.git/\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git add ."
      ],
      "metadata": {
        "id": "XBed6YB0ggJO"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!git status"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r4W9L6_bkd5t",
        "outputId": "12685a71-1c8c-4ed3-8578-9a31b4c95033"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "On branch main\n",
            "\n",
            "No commits yet\n",
            "\n",
            "Changes to be committed:\n",
            "  (use \"git rm --cached <file>...\" to unstage)\n",
            "\t\u001b[32mnew file:   .config/.last_opt_in_prompt.yaml\u001b[m\n",
            "\t\u001b[32mnew file:   .config/.last_survey_prompt.yaml\u001b[m\n",
            "\t\u001b[32mnew file:   .config/.last_update_check.json\u001b[m\n",
            "\t\u001b[32mnew file:   .config/active_config\u001b[m\n",
            "\t\u001b[32mnew file:   .config/config_sentinel\u001b[m\n",
            "\t\u001b[32mnew file:   .config/configurations/config_default\u001b[m\n",
            "\t\u001b[32mnew file:   .config/default_configs.db\u001b[m\n",
            "\t\u001b[32mnew file:   .config/gce\u001b[m\n",
            "\t\u001b[32mnew file:   .config/hidden_gcloud_config_universe_descriptor_data_cache_configs.db\u001b[m\n",
            "\t\u001b[32mnew file:   .config/logs/2025.07.01/21.03.20.550425.log\u001b[m\n",
            "\t\u001b[32mnew file:   .config/logs/2025.07.01/21.03.41.948871.log\u001b[m\n",
            "\t\u001b[32mnew file:   .config/logs/2025.07.01/21.03.53.252709.log\u001b[m\n",
            "\t\u001b[32mnew file:   .config/logs/2025.07.01/21.03.54.626322.log\u001b[m\n",
            "\t\u001b[32mnew file:   .config/logs/2025.07.01/21.04.06.597104.log\u001b[m\n",
            "\t\u001b[32mnew file:   .config/logs/2025.07.01/21.04.07.490711.log\u001b[m\n",
            "\t\u001b[32mnew file:   sample_data/README.md\u001b[m\n",
            "\t\u001b[32mnew file:   sample_data/anscombe.json\u001b[m\n",
            "\t\u001b[32mnew file:   sample_data/california_housing_test.csv\u001b[m\n",
            "\t\u001b[32mnew file:   sample_data/california_housing_train.csv\u001b[m\n",
            "\t\u001b[32mnew file:   sample_data/mnist_test.csv\u001b[m\n",
            "\t\u001b[32mnew file:   sample_data/mnist_train_small.csv\u001b[m\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "!git commit -m \"Add app.py from Colab\"\n",
        "!git push"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l2pog-9dliq8",
        "outputId": "e52866e8-4bd4-4db0-d08c-e2e86ca9acc1"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "On branch main\n",
            "nothing to commit, working tree clean\n",
            "fatal: The current branch main has no upstream branch.\n",
            "To push the current branch and set the remote as upstream, use\n",
            "\n",
            "    git push --set-upstream origin main\n",
            "\n"
          ]
        }
      ]
    }
  ]
}
