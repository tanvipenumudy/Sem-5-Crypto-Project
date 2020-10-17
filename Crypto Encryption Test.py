{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Crypto Encryption Test.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "ot1XfK675aDr",
        "outputId": "6e02ba1f-3725-4690-f984-851a100a9428",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 121
        }
      },
      "source": [
        "pip install pycryptodome"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Collecting pycryptodome\n",
            "\u001b[?25l  Downloading https://files.pythonhosted.org/packages/17/55/17fa0b55849dc135f7bc400993a9206bf06d1b5d9520b0bc8d47c57aaef5/pycryptodome-3.9.8-cp36-cp36m-manylinux1_x86_64.whl (13.7MB)\n",
            "\u001b[K     |████████████████████████████████| 13.7MB 303kB/s \n",
            "\u001b[?25hInstalling collected packages: pycryptodome\n",
            "Successfully installed pycryptodome-3.9.8\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DOAegTAJ5uP4"
      },
      "source": [
        "from Crypto.Cipher import AES\n",
        "\n",
        "key = b'0123456789abcdef'\n",
        "IV = b'0123456789abcdef'         # Initialization vector: discussed later\n",
        "mode = AES.MODE_CBC\n",
        "encryptor = AES.new(key, mode, IV=IV)\n",
        "text = b'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'\n",
        "ciphertext = encryptor.encrypt(text)"
      ],
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AFXlajlJ7HXQ",
        "outputId": "3a1a1ff2-ee75-48b2-e6dd-f3233776ab3c",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        }
      },
      "source": [
        "ciphertext"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "b'\\xca<w(\\x8c%\\xf6\\x05\\xe6\\x8e0\\tU\\xe1\\xa3\\xd8\\xacR\\x1a\\xbe\\xa7}\\x13\\xf9\\xe7\\x14\\xbd\\x86\\x13\\xdc\\xa3\\x99\\xd9\\xc8V6\\x9f\\xba\\x14L\\xad,z~\\xd8\\x93\\x0bt\\x03\\xe0\\xe2\\xc7\\x8e;R&\\x0f\\x04ZM\\xf0\"9\\x83\\xce4`\\x8av\\x03\\x0c3\\x1f\\xd0\\xea\\xe6X2&ci\\x86\\x8a\\x9b\\x05\\x83\\x7f~v\\x81\\xfb\\xed\\xc0_\\x93\\xff\\xac\\nO\\x85\\x99+\\xa0\\xc2K~\\x06k\\x19\\\\\\xef\\xa1\\xb2\\x9c\\xdc\\xc5t\\xe0\\xf3\\xa4\\x14\\xc3r\\xc7\\xc1\\x94!tY\\xe2\\x02\\xaf\\xba?\\x11\\xee$D\\x01EK\\xd1B\\x8dYx\\x9c\\xc8Z?lo\\xc867\\xdf\\xc1\\xec;\\x08\\xca\\xf1\\x88\\xba\\xa6W!i>\\xd3\\x0e\\x0f\\xf6\\xa0\\xa1]^Y2\\x9e\\\\\\xed\\x0c]c?\\xe6\\x0fxU\\xdec'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ThWknxiJ7HYu"
      },
      "source": [
        "import hashlib\n",
        "\n",
        "password = b'kitty'\n",
        "key = hashlib.sha256(password).digest()"
      ],
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gMxuoq1N7Hcf",
        "outputId": "bf0c561f-b725-47e6-9448-947f29f849ca",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        }
      },
      "source": [
        "key"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "b'gs\\x1f\\xf5\\x817\\xeb9q:\\xe3\\x0e\\xba3\\xc5L\\x8c\\x1dT\\x18\\xe0\\x81B\\x8c\\xa8\\x15\\xe4\\xe73\\xd6Om'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Gv_8659E69-Z"
      },
      "source": [
        "key = b'0123456789abcdef'\n",
        "IV = b'0123456789abcdef' \n",
        "decryptor = AES.new(key, mode, IV=IV)\n",
        "plain = decryptor.decrypt(ciphertext)"
      ],
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "p2p3cpl77TyN",
        "outputId": "cb6fe146-0034-40fc-9a63-1bd8222615cd",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        }
      },
      "source": [
        "plain"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "b'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "F3TyIiDj7T0E"
      },
      "source": [
        "import os, random, struct\n",
        "from Crypto.Cipher import AES\n",
        "\n",
        "def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):\n",
        "    \"\"\" Encrypts a file using AES (CBC mode) with the\n",
        "        given key.\n",
        "\n",
        "        key:\n",
        "            The encryption key - a string that must be\n",
        "            either 16, 24 or 32 bytes long. Longer keys\n",
        "            are more secure.\n",
        "\n",
        "        in_filename:\n",
        "            Name of the input file\n",
        "\n",
        "        out_filename:\n",
        "            If None, '<in_filename>.enc' will be used.\n",
        "\n",
        "        chunksize:\n",
        "            Sets the size of the chunk which the function\n",
        "            uses to read and encrypt the file. Larger chunk\n",
        "            sizes can be faster for some files and machines.\n",
        "            chunksize must be divisible by 16.\n",
        "    \"\"\"\n",
        "    if not out_filename:\n",
        "        out_filename = in_filename + '.enc'\n",
        "\n",
        "    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))\n",
        "    encryptor = AES.new(key, AES.MODE_CBC, iv)\n",
        "    filesize = os.path.getsize(in_filename)\n",
        "\n",
        "    with open(in_filename, 'rb') as infile:\n",
        "        with open(out_filename, 'wb') as outfile:\n",
        "            outfile.write(struct.pack('<Q', filesize))\n",
        "            outfile.write(iv)\n",
        "\n",
        "            while True:\n",
        "                chunk = infile.read(chunksize)\n",
        "                if len(chunk) == 0:\n",
        "                    break\n",
        "                elif len(chunk) % 16 != 0:\n",
        "                    chunk += ' ' * (16 - len(chunk) % 16)\n",
        "\n",
        "                outfile.write(encryptor.encrypt(chunk))"
      ],
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "iy25vgOS7T3C",
        "outputId": "510ac818-6c7c-4b20-a2a9-fec563ea14bc",
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCkgewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwogICAgICBwZXJjZW50LnRleHRDb250ZW50ID0KICAgICAgICAgIGAke01hdGgucm91bmQoKHBvc2l0aW9uIC8gZmlsZURhdGEuYnl0ZUxlbmd0aCkgKiAxMDApfSUgZG9uZWA7CiAgICB9CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 90
        }
      },
      "source": [
        "from google.colab import files\n",
        "files.upload()"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-7e505a81-b055-48c4-934b-89d808450202\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-7e505a81-b055-48c4-934b-89d808450202\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "Saving test.zip to test.zip\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'test.zip': b'PK\\x05\\x06\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00'}"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_dKwEbrm7T6S",
        "outputId": "b67ca38b-34de-42bc-ee86-0a9eafc1ae09",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 162
        }
      },
      "source": [
        "encrypt_file(key= b'0123456789abcdef',in_filename='test.txt')"
      ],
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-41-9c5f23db3738>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mencrypt_file\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[0;34m=\u001b[0m \u001b[0;34mb'0123456789abcdef'\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0min_filename\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'test.txt'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m: encrypt_file() got an unexpected keyword argument 'in_filename'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YeO8gLuB7T80"
      },
      "source": [
        "from Crypto import Random\n",
        "from Crypto.Cipher import AES\n",
        "\n",
        "def pad(s):\n",
        "    return s + b\"\\0\" * (AES.block_size - len(s) % AES.block_size)\n",
        "\n",
        "def encrypt(message, key, key_size=256):\n",
        "    message = pad(message)\n",
        "    iv = Random.new().read(AES.block_size)\n",
        "    cipher = AES.new(key, AES.MODE_CBC, iv)\n",
        "    return iv + cipher.encrypt(message)\n",
        "\n",
        "def decrypt(ciphertext, key):\n",
        "    iv = ciphertext[:AES.block_size]\n",
        "    cipher = AES.new(key, AES.MODE_CBC, iv)\n",
        "    plaintext = cipher.decrypt(ciphertext[AES.block_size:])\n",
        "    return plaintext.rstrip(b\"\\0\")\n",
        "\n",
        "def encrypt_file(file_name, key):\n",
        "    with open(file_name, 'rb') as fo:\n",
        "        plaintext = fo.read()\n",
        "    enc = encrypt(plaintext, key)\n",
        "    with open(file_name + \".enc\", 'wb') as fo:\n",
        "        fo.write(enc)\n",
        "\n",
        "def decrypt_file(file_name, key):\n",
        "    with open(file_name, 'rb') as fo:\n",
        "        ciphertext = fo.read()\n",
        "    dec = decrypt(ciphertext, key)\n",
        "    with open(file_name[:-4], 'wb') as fo:\n",
        "        fo.write(dec)\n",
        "\n",
        "\n",
        "key = b'\\xbf\\xc0\\x85)\\x10nc\\x94\\x02)j\\xdf\\xcb\\xc4\\x94\\x9d(\\x9e[EX\\xc8\\xd5\\xbfI{\\xa2$\\x05(\\xd5\\x18'\n",
        "\n",
        "encrypt_file('test.txt', key)"
      ],
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "TxJEhQfC9kbz"
      },
      "source": [
        "test.txt.enc"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FumjkAPe9kdm"
      },
      "source": [
        "decrypt_file('test.txt.enc', key)"
      ],
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vwuop_HZ9kjA"
      },
      "source": [
        "encrypt_file('test.zip', key)"
      ],
      "execution_count": 39,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "9LlSd5gU9klw"
      },
      "source": [
        "decrypt_file('test.zip.enc',key)"
      ],
      "execution_count": 40,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "NAcWc4bX9kqb"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xP1tm3n39khu"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}