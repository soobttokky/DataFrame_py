{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO+UUEc8GOjrhTTo8uqBMmR",
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
        "<a href=\"https://colab.research.google.com/github/soobttokky/DataFrame_py/blob/main/jogo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "VZ4MMrfoYNgz"
      },
      "outputs": [],
      "source": [
        "'''\n",
        "Atividade Avaliativa A1 - 5,0pts\n",
        "\n",
        " - Nome: William Cavalcante da Silva\n",
        "\n",
        " - RGM: 1434383212\n",
        "\n",
        " - Tema: 10 jogos mais importantes da Historia do Basquete\n",
        "\n",
        " FONTES E LINKS:\n",
        "\n",
        " - https://www.nba.com/stats\n",
        "\n",
        " - https://www.nba.com/stats/alltime?SeasonType=Regular+Season\n",
        "\n",
        " - Curso Intensivo de Python: Uma introdução prática e baseada em projetos à programação, Eric Matthes:\n",
        "Disponívem em Português: https://edisciplinas.usp.br/pluginfile.php/6585696/mod_resource/content/1/Eric%20Matthes%20-%20Curso%20Intensivo%20de%20Python-Novatec%20%282016%29.pdf\n",
        "\n",
        " - https://pandas.pydata.org/docs/\n",
        "'''"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd #--> importando a biblioteca pandas\n",
        "\n",
        "#Criação de listas com os dados informados\n",
        "GameDate = ['14/06/1998', '19/06/2016', '14/05/1980', '08/06/1986', '05/05/1969', '04/06/1976', '31/05/2002', '20/06/2013', '18/04/1962', '11/06/1997']\n",
        "#--> Data do Jogo\n",
        "AwayTeam = ['Chicago Bulls', 'Cavaliers', 'Los Angeles Lakers', 'Houston Rockets', 'Los Angeles Lakers', 'Phoenix Sun', 'Sacramento Kings', 'San Antonio Spurs', 'Los Angeles Lakers', 'Utah Jazz']\n",
        "#--> Time Visitante\n",
        "HomeTeam = ['Utah Jazz', 'Golden State Warriors', 'Philadelphia 76ers', 'Boston Celtics', 'Boston Celtics', 'Boston Celtics', 'Los Angeles Lakers', 'Miami Heats', 'Boston Celtics', 'Chicago Bulls']\n",
        "#--> Time da Casa\n",
        "AwayPts = ['87', '93', '108', '97', '105', '126', '102', '88', '107', '88']\n",
        "#--> Quantidade de Pontos do Time Visitante\n",
        "HomePts = ['86', '89', '103', '114', '99', '128', '106', '95', '110', '90']\n",
        "#--> Quantidade de Pontos do Time da Casa\n",
        "Referees = ['Dick Bavetta', 'Mike Callahan', 'Joe Forte', ' Joe Forte', 'Joe Forte', 'Richie Powers', 'Dick Bavetta', 'Dan Crawford', 'Richie Powers', 'Bill Oakes']\n",
        "#--> Árbritos, podem ser até tres, mas so estou colocando um.\n",
        "TimesTied = ['18', '11', '0', '0', '0', '0', '11', '11', '0', '7']\n",
        "#--> Quantidade de vezes em que os times estavam empatados durante o jogo\n",
        "LeadChanges = ['8', '20', '0', '0', '0', '0', '22', '7', '0', '7']\n",
        "#--> Quantidade de vezes em que o lider de placar mudou\n",
        "LastMeetingWinner = ['Chicago Bulls', 'Cavaliers', 'Los Angeles Lakers', 'Boston Celtics', 'Los Angeles Lakers', 'Boston Celtics', 'Sacramento Kings', 'Miami Heats', 'Los Angeles Lakers', 'Chicago Bulls']\n",
        "#--> Vencedor do ultimo jogo entre os dois\n",
        "Winner = ['Chicago Bulls', 'Cavaliers', 'Los Angeles Lakers', 'Boston Celtics', 'Los Angeles Lakers', 'Boston Celtics', 'Los Angeles Lakers', 'Miami Heats', 'Boston Celtics', 'Chicago Bulls']\n",
        "#--> Vencedor da Partida em questão\n",
        "\n",
        "\n",
        "#Criação de um dicionário com as listas informadas\n",
        "dados_jogos= {\n",
        "    'Data do jogo': GameDate,\n",
        "    'Vencedor': Winner,\n",
        "    'Time de Fora': AwayTeam,\n",
        "    'Time da Casa': HomeTeam,\n",
        "    'Pontos de Fora': AwayPts,\n",
        "    'Pontos da Casa': HomePts,\n",
        "    'árbitro Principal': Referees,\n",
        "    'Pontos Iguais': TimesTied,\n",
        "    'Mudançã de Liderança': LeadChanges,\n",
        "    'Ultimo Vencedor': LastMeetingWinner,\n",
        "\n",
        "}\n",
        "\n",
        "#Criação de um DataFrame com o dicionário\n",
        "jogos_df = pd.DataFrame(dados_jogos)"
      ],
      "metadata": {
        "id": "CNJR_GcSUsTN",
        "collapsed": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "*   Usando a biblioteca Pandas foi-se criado um DataFrame sobre os jogos mais importantes na história do Basquete.\n",
        "*   Usei listas para armazenar os dados coletados e, com as listas informadas, foi feito um dicionário, que foi utilizado para a criação do DataFrame e sua variável.\n",
        "*   Todos os dados coletados foram tirados do site oficial da NBA e as informações sobre a criação do DataFrame foram tiradas do conteúdo mestrado em sala de aula e do livro \"Curso Intensivo de Python: Uma introdução prática e baseada em projetos à programação\" do autor Eric Matthes"
      ],
      "metadata": {
        "id": "T9m9fvRMEJUs"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 1 - Apresente em tela (output) toda a base de dados."
      ],
      "metadata": {
        "id": "ykfpZEDOwDwE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"1) Apresente em tela (output) toda a base de dados.\")\n",
        "#Utilizo o comando display para apresentar todos os dados do DataFrame.\n",
        "display(jogos_df)\n",
        "print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 398
        },
        "id": "cJT14aHQwDUs",
        "outputId": "dea3963d-178c-412f-8eb7-1ef5176189e5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1) Apresente em tela (output) toda a base de dados.\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  Data do jogo            Vencedor        Time de Fora           Time da Casa  \\\n",
              "0   14/06/1998       Chicago Bulls       Chicago Bulls              Utah Jazz   \n",
              "1   19/06/2016           Cavaliers           Cavaliers  Golden State Warriors   \n",
              "2   14/05/1980  Los Angeles Lakers  Los Angeles Lakers     Philadelphia 76ers   \n",
              "3   08/06/1986      Boston Celtics     Houston Rockets         Boston Celtics   \n",
              "4   05/05/1969  Los Angeles Lakers  Los Angeles Lakers         Boston Celtics   \n",
              "5   04/06/1976      Boston Celtics         Phoenix Sun         Boston Celtics   \n",
              "6   31/05/2002  Los Angeles Lakers    Sacramento Kings     Los Angeles Lakers   \n",
              "7   20/06/2013         Miami Heats   San Antonio Spurs            Miami Heats   \n",
              "8   18/04/1962      Boston Celtics  Los Angeles Lakers         Boston Celtics   \n",
              "9   11/06/1997       Chicago Bulls           Utah Jazz          Chicago Bulls   \n",
              "\n",
              "  Pontos de Fora Pontos da Casa árbitro Principal Pontos Iguais  \\\n",
              "0             87             86      Dick Bavetta            18   \n",
              "1             93             89     Mike Callahan            11   \n",
              "2            108            103         Joe Forte             0   \n",
              "3             97            114         Joe Forte             0   \n",
              "4            105             99         Joe Forte             0   \n",
              "5            126            128     Richie Powers             0   \n",
              "6            102            106      Dick Bavetta            11   \n",
              "7             88             95      Dan Crawford            11   \n",
              "8            107            110     Richie Powers             0   \n",
              "9             88             90        Bill Oakes             7   \n",
              "\n",
              "  Mudançã de Liderança     Ultimo Vencedor  \n",
              "0                    8       Chicago Bulls  \n",
              "1                   20           Cavaliers  \n",
              "2                    0  Los Angeles Lakers  \n",
              "3                    0      Boston Celtics  \n",
              "4                    0  Los Angeles Lakers  \n",
              "5                    0      Boston Celtics  \n",
              "6                   22    Sacramento Kings  \n",
              "7                    7         Miami Heats  \n",
              "8                    0  Los Angeles Lakers  \n",
              "9                    7       Chicago Bulls  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-9a6ed063-15f3-487f-9087-ec6b61fc22e6\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Data do jogo</th>\n",
              "      <th>Vencedor</th>\n",
              "      <th>Time de Fora</th>\n",
              "      <th>Time da Casa</th>\n",
              "      <th>Pontos de Fora</th>\n",
              "      <th>Pontos da Casa</th>\n",
              "      <th>árbitro Principal</th>\n",
              "      <th>Pontos Iguais</th>\n",
              "      <th>Mudançã de Liderança</th>\n",
              "      <th>Ultimo Vencedor</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>14/06/1998</td>\n",
              "      <td>Chicago Bulls</td>\n",
              "      <td>Chicago Bulls</td>\n",
              "      <td>Utah Jazz</td>\n",
              "      <td>87</td>\n",
              "      <td>86</td>\n",
              "      <td>Dick Bavetta</td>\n",
              "      <td>18</td>\n",
              "      <td>8</td>\n",
              "      <td>Chicago Bulls</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>19/06/2016</td>\n",
              "      <td>Cavaliers</td>\n",
              "      <td>Cavaliers</td>\n",
              "      <td>Golden State Warriors</td>\n",
              "      <td>93</td>\n",
              "      <td>89</td>\n",
              "      <td>Mike Callahan</td>\n",
              "      <td>11</td>\n",
              "      <td>20</td>\n",
              "      <td>Cavaliers</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>14/05/1980</td>\n",
              "      <td>Los Angeles Lakers</td>\n",
              "      <td>Los Angeles Lakers</td>\n",
              "      <td>Philadelphia 76ers</td>\n",
              "      <td>108</td>\n",
              "      <td>103</td>\n",
              "      <td>Joe Forte</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Los Angeles Lakers</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>08/06/1986</td>\n",
              "      <td>Boston Celtics</td>\n",
              "      <td>Houston Rockets</td>\n",
              "      <td>Boston Celtics</td>\n",
              "      <td>97</td>\n",
              "      <td>114</td>\n",
              "      <td>Joe Forte</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Boston Celtics</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>05/05/1969</td>\n",
              "      <td>Los Angeles Lakers</td>\n",
              "      <td>Los Angeles Lakers</td>\n",
              "      <td>Boston Celtics</td>\n",
              "      <td>105</td>\n",
              "      <td>99</td>\n",
              "      <td>Joe Forte</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Los Angeles Lakers</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>04/06/1976</td>\n",
              "      <td>Boston Celtics</td>\n",
              "      <td>Phoenix Sun</td>\n",
              "      <td>Boston Celtics</td>\n",
              "      <td>126</td>\n",
              "      <td>128</td>\n",
              "      <td>Richie Powers</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Boston Celtics</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>31/05/2002</td>\n",
              "      <td>Los Angeles Lakers</td>\n",
              "      <td>Sacramento Kings</td>\n",
              "      <td>Los Angeles Lakers</td>\n",
              "      <td>102</td>\n",
              "      <td>106</td>\n",
              "      <td>Dick Bavetta</td>\n",
              "      <td>11</td>\n",
              "      <td>22</td>\n",
              "      <td>Sacramento Kings</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>20/06/2013</td>\n",
              "      <td>Miami Heats</td>\n",
              "      <td>San Antonio Spurs</td>\n",
              "      <td>Miami Heats</td>\n",
              "      <td>88</td>\n",
              "      <td>95</td>\n",
              "      <td>Dan Crawford</td>\n",
              "      <td>11</td>\n",
              "      <td>7</td>\n",
              "      <td>Miami Heats</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>18/04/1962</td>\n",
              "      <td>Boston Celtics</td>\n",
              "      <td>Los Angeles Lakers</td>\n",
              "      <td>Boston Celtics</td>\n",
              "      <td>107</td>\n",
              "      <td>110</td>\n",
              "      <td>Richie Powers</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>Los Angeles Lakers</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>11/06/1997</td>\n",
              "      <td>Chicago Bulls</td>\n",
              "      <td>Utah Jazz</td>\n",
              "      <td>Chicago Bulls</td>\n",
              "      <td>88</td>\n",
              "      <td>90</td>\n",
              "      <td>Bill Oakes</td>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>Chicago Bulls</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-9a6ed063-15f3-487f-9087-ec6b61fc22e6')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-9a6ed063-15f3-487f-9087-ec6b61fc22e6 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-9a6ed063-15f3-487f-9087-ec6b61fc22e6');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-c26a31e4-5a33-468e-bef3-143933c3aa52\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-c26a31e4-5a33-468e-bef3-143933c3aa52')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-c26a31e4-5a33-468e-bef3-143933c3aa52 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_cd8140e7-d9c2-4d3f-9943-e8fde4702986\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('jogos_df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_cd8140e7-d9c2-4d3f-9943-e8fde4702986 button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('jogos_df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "jogos_df",
              "summary": "{\n  \"name\": \"jogos_df\",\n  \"rows\": 10,\n  \"fields\": [\n    {\n      \"column\": \"Data do jogo\",\n      \"properties\": {\n        \"dtype\": \"object\",\n        \"num_unique_values\": 10,\n        \"samples\": [\n          \"18/04/1962\",\n          \"19/06/2016\",\n          \"04/06/1976\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Vencedor\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"Cavaliers\",\n          \"Miami Heats\",\n          \"Los Angeles Lakers\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Time de Fora\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 8,\n        \"samples\": [\n          \"Cavaliers\",\n          \"Sacramento Kings\",\n          \"Chicago Bulls\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Time da Casa\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Utah Jazz\",\n          \"Golden State Warriors\",\n          \"Miami Heats\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Pontos de Fora\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 9,\n        \"samples\": [\n          \"88\",\n          \"93\",\n          \"126\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Pontos da Casa\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 10,\n        \"samples\": [\n          \"110\",\n          \"89\",\n          \"128\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"\\u00e1rbitro Principal\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 7,\n        \"samples\": [\n          \"Dick Bavetta\",\n          \"Mike Callahan\",\n          \"Dan Crawford\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Pontos Iguais\",\n      \"properties\": {\n        \"dtype\": \"category\",\n        \"num_unique_values\": 4,\n        \"samples\": [\n          \"11\",\n          \"7\",\n          \"18\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Mudan\\u00e7\\u00e3 de Lideran\\u00e7a\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 5,\n        \"samples\": [\n          \"20\",\n          \"7\",\n          \"0\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Ultimo Vencedor\",\n      \"properties\": {\n        \"dtype\": \"string\",\n        \"num_unique_values\": 6,\n        \"samples\": [\n          \"Chicago Bulls\",\n          \"Cavaliers\",\n          \"Miami Heats\"\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "*   Para apresentar uma tela de display usamos o comando '**df.display**', que tem como principal função criar uma tabela com os dados apresentados no DataFrame.\n",
        "*   Além da tabela, o comando '**df.display**' também permite a criação de gráficos a partir dos dados apresentados e a pesquisa de items dentro da tabela.\n",
        "*   O código apresenta todos os dados contidos no DataFrame jogos_df de forma organizada e legível na saída da tela. sendo útil para visualizar rapidamente os registros da base de dados."
      ],
      "metadata": {
        "id": "-fASi5dIBt8e"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 2 - Apresente o tamanho do seu dataframe (quantas linhas x colunas)."
      ],
      "metadata": {
        "id": "RJKyZQCaxPcp"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"2) Apresente o tamanho do seu dataframe (quantas linhas x colunas).\")\n",
        "#O comando shape mostrará as dimenções do DataFrame (Linhas e Colunas).\n",
        "print(jogos_df.shape)\n",
        "print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d6UgBIkjxQDL",
        "outputId": "1e39bd84-109c-4625-9abd-da3776a1b4bb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2) Apresente o tamanho do seu dataframe (quantas linhas x colunas).\n",
            "(10, 10)\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*   O comando '**df.shape**' retorna uma tupla com a dimensão do DataFrame (o número de linhas e colunas).\n",
        "*   É usado para saber quantas linhas e colunas existem no DataFrame e para o controle do tamanho do mesmo.\n"
      ],
      "metadata": {
        "id": "otr0ZCfkG9bW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 3 - Acesse a linha (x) e apresente em tela todas as características do item."
      ],
      "metadata": {
        "id": "CmNky-_PxviE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"3) Acesse a linha (x) e apresente em tela todas as características do item.\")\n",
        "#O comando iloc irá alocar apenas a linha e coluna especificada, neste caso, a primeira linha.\n",
        "print(jogos_df.iloc[1])\n",
        "print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "D4PxxNDOxv2j",
        "outputId": "7594347a-2a19-4923-bc8e-49f766cb1e2d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3) Acesse a linha (x) e apresente em tela todas as características do item.\n",
            "Data do jogo                       19/06/2016\n",
            "Vencedor                            Cavaliers\n",
            "Time de Fora                        Cavaliers\n",
            "Time da Casa            Golden State Warriors\n",
            "Pontos de Fora                             93\n",
            "Pontos da Casa                             89\n",
            "árbitro Principal               Mike Callahan\n",
            "Pontos Iguais                              11\n",
            "Mudançã de Liderança                       20\n",
            "Ultimo Vencedor                     Cavaliers\n",
            "Name: 1, dtype: object\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "*   O indexador '**iloc**' seleciona os números inteiros das linhas, arrays ou por slice.\n",
        "*   Podemos concluir que sua função principal é selecionar linhas e colunas por números, permitindo visualizar os detalhes específicos desse item no DataFrame .\n",
        "*   Uma observação importante é que a linha ou coluna deve estar entre cochetes [] para que o indexador funcione de forma correta.\n",
        "\n"
      ],
      "metadata": {
        "id": "LCHEMlseLMtT"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 4 - Verifique se o DataFrame está vazio.\n"
      ],
      "metadata": {
        "id": "PoON_mp6x_Vc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"4) Verifique se o dataframe está vazio.\")\n",
        "#Utilizando Do-While: imprimir na tela \"o DataFrame está vazio\" ou \"O DataFrame não está vazio\"\n",
        "while jogos_df.empty:\n",
        "  print(\"O DataFrame está vazio!\")\n",
        "  break\n",
        "else:\n",
        "  print(\"O DataFrame não está vazio!!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2agLnNCwx_pO",
        "outputId": "1b96d3b8-3bdd-4f2d-89c9-8212b34e686d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4) Verifique se o dataframe está vazio.\n",
            "O DataFrame não está vazio!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Usando df.empty: O comando empty irá retornar na tela se o DataFrame está vazio ou não utilizando true ou false\n",
        "print(\"4) Verifique se o dataframe está vazio.\")\n",
        "print(jogos_df.empty)\n",
        "print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SaFF5kpU-CxO",
        "outputId": "8860336b-1729-49c9-9db2-fa208c779e68"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "4) Verifique se o dataframe está vazio.\n",
            "False\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*   Através do modo '**Do-While**' é utilizado um loop while com a condição '**jogos_df.empty**', que verifica se o DataFrame está vazio e, com um retorno positivo, executa o loop\n",
        "*   A inclusão do '**break**'foi feita para que o loop seja interrompido imediatamente após a primeira vez em que o código for rodado, não importando se o DataFrame está vazio ou não. Logo, o loop será rodado apenas uma vez.\n",
        "*   Atravéz do método '**df.empty**', ele retornará na tela se o DataFrame está vazio ou não (usando *True* ou *False* para determinar sua resposta)"
      ],
      "metadata": {
        "id": "HVPWl4UBL0lY"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 5 - Apresente em tela os 5 primeiros registros da base de dados."
      ],
      "metadata": {
        "id": "O19unUubyLSt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"5) Apresente em tela os 5 primeiros registros da base de dados.\")\n",
        "#O comando head irá retonar a quantidade de linhas pedidas com o uso de (), neste caso, as 5 primeiras linahs serão retornadas.\n",
        "print(jogos_df.head(5))\n",
        "print()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V2MEAp55yLm1",
        "outputId": "9cf0f2c1-6845-49a3-9585-717187e85f24"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5) Apresente em tela os 5 primeiros registros da base de dados.\n",
            "  Data do jogo            Vencedor        Time de Fora           Time da Casa  \\\n",
            "0   14/06/1998       Chicago Bulls       Chicago Bulls              Utah Jazz   \n",
            "1   19/06/2016           Cavaliers           Cavaliers  Golden State Warriors   \n",
            "2   14/05/1980  Los Angeles Lakers  Los Angeles Lakers     Philadelphia 76ers   \n",
            "3   08/06/1986      Boston Celtics     Houston Rockets         Boston Celtics   \n",
            "4   05/05/1969  Los Angeles Lakers  Los Angeles Lakers         Boston Celtics   \n",
            "\n",
            "  Pontos de Fora Pontos da Casa árbitro Principal Pontos Iguais  \\\n",
            "0             87             86      Dick Bavetta            18   \n",
            "1             93             89     Mike Callahan            11   \n",
            "2            108            103         Joe Forte             0   \n",
            "3             97            114         Joe Forte             0   \n",
            "4            105             99         Joe Forte             0   \n",
            "\n",
            "  Mudançã de Liderança     Ultimo Vencedor  \n",
            "0                    8       Chicago Bulls  \n",
            "1                   20           Cavaliers  \n",
            "2                    0  Los Angeles Lakers  \n",
            "3                    0      Boston Celtics  \n",
            "4                    0  Los Angeles Lakers  \n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*   A Função '**head**' retorna as primeiras 'x' linhas do objeto com base na posição. É útil para testar rapidamente se o seu objeto contém o tipo certo de dados.\n",
        "*   se 'x' for um numero especifico de linhas (como foi feito acima) ela retorna-rá todas as linhas especificadas, e se for um numero maior será retornado todas as linhas presentes no DataFrame.\n"
      ],
      "metadata": {
        "id": "YvuY5PnKObFi"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 6 - Exclua um item (linha) de sua base de dados."
      ],
      "metadata": {
        "id": "0gMFvfcCyl63"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"6) Exclua um item (linha) de sua base de dados.\")\n",
        "#O comando drop irá excluir uma linha (especificada entre ()) do DataFrame.\n",
        "jogos_df = jogos_df.drop(9)\n",
        "print(jogos_df)\n",
        "print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NNKkI2z0ymOR",
        "outputId": "a3e2408d-48a7-4afb-c3e5-890be665ea6b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6) Exclua um item (linha) de sua base de dados.\n",
            "  Data do jogo            Vencedor        Time de Fora           Time da Casa  \\\n",
            "0   14/06/1998       Chicago Bulls       Chicago Bulls              Utah Jazz   \n",
            "1   19/06/2016           Cavaliers           Cavaliers  Golden State Warriors   \n",
            "2   14/05/1980  Los Angeles Lakers  Los Angeles Lakers     Philadelphia 76ers   \n",
            "3   08/06/1986      Boston Celtics     Houston Rockets         Boston Celtics   \n",
            "4   05/05/1969  Los Angeles Lakers  Los Angeles Lakers         Boston Celtics   \n",
            "5   04/06/1976      Boston Celtics         Phoenix Sun         Boston Celtics   \n",
            "6   31/05/2002  Los Angeles Lakers    Sacramento Kings     Los Angeles Lakers   \n",
            "7   20/06/2013         Miami Heats   San Antonio Spurs            Miami Heats   \n",
            "8   18/04/1962      Boston Celtics  Los Angeles Lakers         Boston Celtics   \n",
            "\n",
            "  Pontos de Fora Pontos da Casa árbitro Principal Pontos Iguais  \\\n",
            "0             87             86      Dick Bavetta            18   \n",
            "1             93             89     Mike Callahan            11   \n",
            "2            108            103         Joe Forte             0   \n",
            "3             97            114         Joe Forte             0   \n",
            "4            105             99         Joe Forte             0   \n",
            "5            126            128     Richie Powers             0   \n",
            "6            102            106      Dick Bavetta            11   \n",
            "7             88             95      Dan Crawford            11   \n",
            "8            107            110     Richie Powers             0   \n",
            "\n",
            "  Mudançã de Liderança     Ultimo Vencedor  \n",
            "0                    8       Chicago Bulls  \n",
            "1                   20           Cavaliers  \n",
            "2                    0  Los Angeles Lakers  \n",
            "3                    0      Boston Celtics  \n",
            "4                    0  Los Angeles Lakers  \n",
            "5                    0      Boston Celtics  \n",
            "6                   22    Sacramento Kings  \n",
            "7                    7         Miami Heats  \n",
            "8                    0  Los Angeles Lakers  \n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "*  A Função '**Drop**' remove linhas ou colunas quando se especifica os nomes das linhas ou eixos correspondentes, atualizando o DataFrame sem a mesma. Ao usar um índice múltiplo, os rótulos em níveis diferentes podem ser removidos especificando o nível.\n",
        "*  A especificação da linha pode ser feita usando () logo após a função\n",
        "\n"
      ],
      "metadata": {
        "id": "lNocP9jSQvSZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 7 - Adicione um item (linha) na sua base de dados."
      ],
      "metadata": {
        "id": "4khYUivezGuB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"7) Adicione um item (linha) na sua base de dados.\")\n",
        "#adicionei uma nova linha no nosso DataFrame com a ajuda do dicionario.\n",
        "novo_jogo = {\n",
        "    'Data do jogo': '11/06/1997',\n",
        "    'Time de Fora': 'Utah Jazz',\n",
        "    'Time da Casa': 'Chicago Bulls',\n",
        "    'Pontos de Fora': '88',\n",
        "    'Pontos da Casa': '90',\n",
        "    'árbitro Principal': 'Bill Oakes',\n",
        "    'Pontos Iguais': '7',\n",
        "    'Mudançã de Liderança': '7',\n",
        "    'Ultimo Vencedor': 'Chicago Bulls',\n",
        "    'Vencedor': 'Chicago Bulls',\n",
        "    }\n",
        "jogos_df = pd.concat([jogos_df, pd.DataFrame(novo_jogo, index=[5])],ignore_index=True)\n",
        "print(jogos_df)\n",
        "print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "r7LUQEw_zN44",
        "outputId": "96d3181b-7943-4fae-ba91-68f76a537b62"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7) Adicione um item (linha) na sua base de dados.\n",
            "  Data do jogo            Vencedor        Time de Fora           Time da Casa  \\\n",
            "0   14/06/1998       Chicago Bulls       Chicago Bulls              Utah Jazz   \n",
            "1   19/06/2016           Cavaliers           Cavaliers  Golden State Warriors   \n",
            "2   14/05/1980  Los Angeles Lakers  Los Angeles Lakers     Philadelphia 76ers   \n",
            "3   08/06/1986      Boston Celtics     Houston Rockets         Boston Celtics   \n",
            "4   05/05/1969  Los Angeles Lakers  Los Angeles Lakers         Boston Celtics   \n",
            "5   04/06/1976      Boston Celtics         Phoenix Sun         Boston Celtics   \n",
            "6   31/05/2002  Los Angeles Lakers    Sacramento Kings     Los Angeles Lakers   \n",
            "7   20/06/2013         Miami Heats   San Antonio Spurs            Miami Heats   \n",
            "8   18/04/1962      Boston Celtics  Los Angeles Lakers         Boston Celtics   \n",
            "9   11/06/1997       Chicago Bulls           Utah Jazz          Chicago Bulls   \n",
            "\n",
            "  Pontos de Fora Pontos da Casa árbitro Principal Pontos Iguais  \\\n",
            "0             87             86      Dick Bavetta            18   \n",
            "1             93             89     Mike Callahan            11   \n",
            "2            108            103         Joe Forte             0   \n",
            "3             97            114         Joe Forte             0   \n",
            "4            105             99         Joe Forte             0   \n",
            "5            126            128     Richie Powers             0   \n",
            "6            102            106      Dick Bavetta            11   \n",
            "7             88             95      Dan Crawford            11   \n",
            "8            107            110     Richie Powers             0   \n",
            "9             88             90        Bill Oakes             7   \n",
            "\n",
            "  Mudançã de Liderança     Ultimo Vencedor  \n",
            "0                    8       Chicago Bulls  \n",
            "1                   20           Cavaliers  \n",
            "2                    0  Los Angeles Lakers  \n",
            "3                    0      Boston Celtics  \n",
            "4                    0  Los Angeles Lakers  \n",
            "5                    0      Boston Celtics  \n",
            "6                   22    Sacramento Kings  \n",
            "7                    7         Miami Heats  \n",
            "8                    0  Los Angeles Lakers  \n",
            "9                    7       Chicago Bulls  \n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "*   novo_jogo está sendo criado apartir de um dicionário com chaves que representam atributos de um dos jogos de basquete que foi transformado em um DataFrame temporario e depois adicionado e concatenado com o DataFrame principal.\n",
        "*   O comando '**index=[5]**' define o indice como 5 e o comando '**ignore_index=True**' reindexa as linhas do DataFrame resultante.\n",
        "\n"
      ],
      "metadata": {
        "id": "F7CFzIogRyid"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 8 - Transponha a coluna para a linha em sua base de dados."
      ],
      "metadata": {
        "id": "hbXb6JYp0cCX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"8) Transponha a coluna para a linha em sua base de dados.\")\n",
        "#criei uma variável e aloquei ela ao comando T que irá transpor as colunas em linhas.\n",
        "jogos_df = pd.DataFrame(dados_jogos)\n",
        "df_transposto = jogos_df.T\n",
        "print(df_transposto)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IXxYBY600iA6",
        "outputId": "057fb6be-2c3f-4dee-de09-00377a91fc04"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "8) Transponha a coluna para a linha em sua base de dados.\n",
            "                                  0                      1  \\\n",
            "Data do jogo             14/06/1998             19/06/2016   \n",
            "Vencedor              Chicago Bulls              Cavaliers   \n",
            "Time de Fora          Chicago Bulls              Cavaliers   \n",
            "Time da Casa              Utah Jazz  Golden State Warriors   \n",
            "Pontos de Fora                   87                     93   \n",
            "Pontos da Casa                   86                     89   \n",
            "árbitro Principal      Dick Bavetta          Mike Callahan   \n",
            "Pontos Iguais                    18                     11   \n",
            "Mudançã de Liderança              8                     20   \n",
            "Ultimo Vencedor       Chicago Bulls              Cavaliers   \n",
            "\n",
            "                                       2                3                   4  \\\n",
            "Data do jogo                  14/05/1980       08/06/1986          05/05/1969   \n",
            "Vencedor              Los Angeles Lakers   Boston Celtics  Los Angeles Lakers   \n",
            "Time de Fora          Los Angeles Lakers  Houston Rockets  Los Angeles Lakers   \n",
            "Time da Casa          Philadelphia 76ers   Boston Celtics      Boston Celtics   \n",
            "Pontos de Fora                       108               97                 105   \n",
            "Pontos da Casa                       103              114                  99   \n",
            "árbitro Principal              Joe Forte        Joe Forte           Joe Forte   \n",
            "Pontos Iguais                          0                0                   0   \n",
            "Mudançã de Liderança                   0                0                   0   \n",
            "Ultimo Vencedor       Los Angeles Lakers   Boston Celtics  Los Angeles Lakers   \n",
            "\n",
            "                                   5                   6                  7  \\\n",
            "Data do jogo              04/06/1976          31/05/2002         20/06/2013   \n",
            "Vencedor              Boston Celtics  Los Angeles Lakers        Miami Heats   \n",
            "Time de Fora             Phoenix Sun    Sacramento Kings  San Antonio Spurs   \n",
            "Time da Casa          Boston Celtics  Los Angeles Lakers        Miami Heats   \n",
            "Pontos de Fora                   126                 102                 88   \n",
            "Pontos da Casa                   128                 106                 95   \n",
            "árbitro Principal      Richie Powers        Dick Bavetta       Dan Crawford   \n",
            "Pontos Iguais                      0                  11                 11   \n",
            "Mudançã de Liderança               0                  22                  7   \n",
            "Ultimo Vencedor       Boston Celtics    Sacramento Kings        Miami Heats   \n",
            "\n",
            "                                       8              9  \n",
            "Data do jogo                  18/04/1962     11/06/1997  \n",
            "Vencedor                  Boston Celtics  Chicago Bulls  \n",
            "Time de Fora          Los Angeles Lakers      Utah Jazz  \n",
            "Time da Casa              Boston Celtics  Chicago Bulls  \n",
            "Pontos de Fora                       107             88  \n",
            "Pontos da Casa                       110             90  \n",
            "árbitro Principal          Richie Powers     Bill Oakes  \n",
            "Pontos Iguais                          0              7  \n",
            "Mudançã de Liderança                   0              7  \n",
            "Ultimo Vencedor       Los Angeles Lakers  Chicago Bulls  \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*   A função '**df.t**' tem como objetivo espelhar as diagonais do DataFrame, tornando assim as Colunas em Linhas e vice-versa.\n",
        "*   O 'T' é um assessor da função transposto, sendo usado para facilitar o uso da função."
      ],
      "metadata": {
        "id": "LZ6a2rrJVMrL"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 9 - Apresente em tela somente a 1ª e a 2ª coluna (rótulo) da base de dados.\n"
      ],
      "metadata": {
        "id": "rvVg8XBR1ejO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"9) Apresente em tela somente a 1ª e a 2ª coluna (rótulo) da base de dados.\")\n",
        "#Utilizo uma variável do comando iloc, definindo as colunas que queremos alocar e apresentando-as em tela.\n",
        "print(jogos_df.loc[:, ['Data do jogo', 'Vencedor']])\n",
        "print()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x7a9OqaP1i6r",
        "outputId": "14eeb126-2cb2-4292-835b-ba5c6af607c1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "9) Apresente em tela somente a 1ª e a 2ª coluna (rótulo) da base de dados.\n",
            "  Data do jogo            Vencedor\n",
            "0   14/06/1998       Chicago Bulls\n",
            "1   19/06/2016           Cavaliers\n",
            "2   14/05/1980  Los Angeles Lakers\n",
            "3   08/06/1986      Boston Celtics\n",
            "4   05/05/1969  Los Angeles Lakers\n",
            "5   04/06/1976      Boston Celtics\n",
            "6   31/05/2002  Los Angeles Lakers\n",
            "7   20/06/2013         Miami Heats\n",
            "8   18/04/1962      Boston Celtics\n",
            "9   11/06/1997       Chicago Bulls\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "*   A função '**df.loc**' é primariamente baseada nas labels da colunas, ela é uma variação da função '**Iloc**'e está sendo usada para chamar duas colunas especificas no DataFrame, nesse caso, está sendo usada para chamar as colunas 'Data do jogo' e 'Vencedor'\n",
        "\n"
      ],
      "metadata": {
        "id": "KB3lJx5gW-9y"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### 10 - Informe como foi desenvolvido o Projeto"
      ],
      "metadata": {
        "id": "GkAet_MtYmgM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "O foco deste projeto foi criar e manipular um DataFrame usando a biblioteca Pandas em Python. Com o Tema escolhido sendo 10 melhores jogos de basquete na historia da NBA, foram coletados dados relevantes incluindo informações como data de jogo, vencedores, o nome dos times e suas devidas pontuaçoes e outras informações importantes como o nome do arbitro principal do jogo e numero de vezes em que o jogo estava empatado e a quantidade de vezes em que houve diferença de liderança.\n",
        "\n",
        "Primeiro, criei listas com esses dados e as agrupei em um dicionário. Cada chave do dicionário representa uma característica de uma partida. Em seguida, utilizamos esse dicionário para criar um DataFrame, que é uma estrutura de dados bidimensional com rótulos para linhas e colunas, fornecida pela biblioteca Pandas.\n",
        "\n",
        "Durante o projeto, apliquei várias operações ao DataFrame para responder às perguntas propostas. Utilizamos comandos específicos do Pandas, como shape para obter o tamanho do DataFrame, iloc para acessar linhas específicas, empty para verificar se o DataFrame estava vazio, head para mostrar os primeiros registros e drop para excluir uma linha.\n",
        "\n",
        "Além disso, realizei a transposição do DataFrame usando o método T, que troca linhas por colunas, e acessei colunas específicas com loc. Cada comando foi escolhido para demonstrar diferentes manipulações possíveis em um DataFrame, facilitando a compreensão e análise dos dados.\n",
        "\n",
        "O desenvolvimento do projeto também envolveu a explicação do que foi feito, usando o conhecimento que adquiri para explicar como aplicar corretamente os comandos e representar os dados de forma clara e precisa. Pesquisas adicionais e testes práticos foram necessários. No final, o projeto proporcionou uma boa compreensão da manipulação de dados com Pandas e mostrou como trabalhar eficientemente com dados de jogos de basquete."
      ],
      "metadata": {
        "id": "QklKad9uYvpQ"
      }
    }
  ]
}