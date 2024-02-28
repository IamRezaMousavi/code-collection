# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-02-24 12:25:54
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-07-25 17:29:39

def check(pos):
    for key in pos:
        for other in pos:
            if key == other:
                continue
            if pos[key] == pos[other]:
                print(key, other)

def main():
    import networkx as nx
    import matplotlib.pyplot as plt

    G = nx.DiGraph()
    pos = {}
    labels = {}
    
    basicLesson = []
    mainLesson = []
    electronicBasicLesson = []
    electronicMainLesson = []
    telecommBasicLesson = []
    telecommMainLesson = []
    labs = []
    
    # -------------
    G.add_edge(0, 1, weight=0.6)
    pos[0] = (0, 0)
    pos[1] = (pos[0][0]-1, pos[0][1])
    labels[0] = "Math 1"
    labels[1] = "Math 2"
    basicLesson.extend([0, 1])
    
    G.add_edge(1, 4, weight=0.6)
    pos[4] = (pos[1][0]-1, pos[1][1]+8)
    labels[4] = "Probability"
    basicLesson.append(4)
    
    G.add_edge(2, 3, weight=0.6)
    pos[2] = (pos[0][0], pos[0][1]-6)
    pos[3] = (pos[2][0]-1, pos[2][1])
    labels[2] = "Physics 1"
    labels[3] = "Physics 2"
    basicLesson.extend([2, 3])
    
    G.add_edge(2, 9, weight=0.3)
    pos[9] = (pos[2][0]-1, pos[2][1]-3)
    labels[9] = "Physics\nLab 1"
    labs.append(9)
    
    G.add_edge(3, 10, weight=0.3)
    pos[10] = (pos[3][0]-1, pos[3][1]-2)
    labels[10] = "Physics\nLab 2"
    labs.append(10)
    
    G.add_edge(7, 5, weight=0.6)
    G.add_edge(1, 5, weight=0.6)
    pos[7] = (pos[2][0], pos[2][1]-6)
    pos[5] = (pos[7][0]-2, pos[7][1])
    labels[7] = "Computer\nProgramming"
    labels[5] = "Numerical\nCalculations"
    basicLesson.extend([5, 7])
    
    G.add_edge(1, 6, weight=0.3)
    pos[6] = (pos[1][0]-1, pos[1][1]-2)
    labels[6] = "Differential\nEquations"
    basicLesson.append(6)
    
    G.add_node(8)
    pos[8] = (pos[7][0], pos[7][1]-6)
    labels[8] = "Workshop"
    basicLesson.append(8)
    
    # -------------
    
    G.add_node(11)
    pos[11] = (pos[8][0], pos[8][1]-3)
    labels[11] = "Engineering\nEconomics"
    mainLesson.append(11)
    
    G.add_edge(12, 13, weight=0.6)
    pos[12] = (pos[11][0], pos[11][1]-3)
    pos[13] = (pos[12][0]-1, pos[12][1])
    labels[12] = "English"
    labels[13] = "Language of\nElectricity"
    mainLesson.extend([12, 13])
    
    G.add_node(14)
    pos[14] = (pos[11][0]-1, pos[11][1])
    labels[14] = "Electrical\nDrawing"
    mainLesson.append(14)
    
    G.add_edge(8, 15, weight=0.6)
    pos[15] = (pos[8][0]-1, pos[8][1])
    labels[15] = "Electric\nWorkshop"
    mainLesson.append(15)
    
    G.add_edge(1, 16, weight=0.6)
    G.add_edge(6, 16, weight=0.6)
    pos[16] = (pos[1][0]-2, pos[1][1])
    labels[16] = "Engineering\nMathematics"
    mainLesson.append(16)
    
    G.add_node(17)
    pos[17] = (pos[14][0]-1, pos[14][1]-2)
    labels[17] = "Intro to Electrical\nEngineering"
    mainLesson.append(17)
    
    G.add_edge(3, 18, weight=0.3)
    G.add_edge(6, 18, weight=0.3)
    pos[18] = (pos[3][0]-2, pos[3][1]-7)
    labels[18] = "Electrical\nCircuits 1"
    mainLesson.append(18)
    
    G.add_edge(18, 19, weight=0.6)
    pos[19] = (pos[18][0]-1, pos[18][1]+2)
    labels[19] = "Electrical\nCircuits 2"
    mainLesson.append(19)
    
    G.add_edge(1, 20, weight=0.6)
    G.add_edge(3, 20, weight=0.6)
    pos[20] = (pos[1][0]-1, pos[1][1]+4)
    labels[20] = "Electromagnetism"
    mainLesson.append(20)
    
    G.add_edge(16, 21, weight=0.6)
    pos[21] = (pos[16][0]-1, pos[16][1])
    labels[21] = "Signals and\nSystems"
    mainLesson.append(21)
    
    G.add_edge(21, 22, weight=0.6)
    G.add_edge(19, 22, weight=0.6)
    pos[22] = (pos[21][0]-1, pos[21][1])
    labels[22] = "Linear Control\nSystems"
    mainLesson.append(22)
    
    G.add_edge(18, 23, weight=0.6)
    pos[23] = (pos[18][0]-1, pos[18][1]-4)
    labels[23] = "Electronic 1"
    mainLesson.append(23)
    
    G.add_edge(23, 24, weight=0.6)
    pos[24] = (pos[23][0]-1, pos[23][1])
    labels[24] = "Electronic 2"
    mainLesson.append(24)
    
    G.add_edge(18, 25, weight=0.6)
    pos[25] = (pos[18][0]-1, pos[18][1]-15)
    labels[25] = "Electric\nMachines 1"
    mainLesson.append(25)
    
    G.add_edge(25, 26, weight=0.6)
    pos[26] = (pos[25][0]-1, pos[25][1])
    labels[26] = "Electric\nMachines 2"
    mainLesson.append(26)
    
    G.add_edge(4, 27, weight=0.6)
    G.add_edge(21, 27, weight=0.6)
    pos[27] = (pos[21][0]-1, pos[21][1]+8)
    labels[27] = "Principles of\nTelecommunication\nSystems"
    mainLesson.append(27)
    
    G.add_edge(26, 28, weight=0.6)
    pos[28] = (pos[26][0]-2, pos[26][1]-1)
    labels[28] = "Analysis of\nEnergy Systems"
    mainLesson.append(28)
    
    G.add_edge(23, 29, weight=0.3)
    pos[29] = (pos[23][0]-1, pos[23][1]+6)
    labels[29] = "Digital\nSystems 1"
    mainLesson.append(29)
    
    G.add_edge(29, 30, weight=0.6)
    pos[30] = (pos[29][0]-2, pos[29][1])
    labels[30] = "Digital\nSystems 2"
    mainLesson.append(30)
    
    G.add_edge(18, 31, weight=0.6)
    pos[31] = (pos[18][0]-1, pos[18][1]-0.5)
    labels[31] = "Electrical Circuits\nand Measurements Lab"
    labs.append(31)
    
    G.add_edge(25, 32, weight=0.6)
    pos[32] = (pos[25][0]-1, pos[25][1]-2)
    labels[32] = "Electric\nMachines Lab"
    labs.append(32)
    
    G.add_edge(24, 33, weight=0.3)
    pos[33] = (pos[24][0]-2, pos[24][1]-4)
    labels[33] = "Electronic Lab"
    labs.append(33)
    
    G.add_edge(22, 34, weight=0.6)
    pos[34] = (pos[22][0]-2, pos[22][1])
    labels[34] = "Linear Control\nSystems Lab"
    labs.append(34)
    
    G.add_edge(29, 35, weight=0.3)
    pos[35] = (pos[29][0]-2, pos[29][1]+3)
    labels[35] = "Digital\nSystems 1 Lab"
    labs.append(35)
    
    G.add_edge(35, 36, weight=0.6)
    G.add_edge(30, 36, weight=0.3)
    pos[36] = (pos[35][0]-1, pos[35][1])
    labels[36] = "Digital\nSystems 2 Lab"
    labs.append(36)
    
    # ---------------------
    G.add_nodes_from([37, 38])
    pos[37], pos[38] = (pos[12][0], pos[12][1]-3), (pos[12][0]-1, pos[12][1]-3)
    labels[37], labels[38] = "Bachelor Project", "Internship"
    mainLesson.extend([37, 38])
    
    G.add_edge(27, 39, weight=0.6)
    G.add_edge(24, 39, weight=0.6)
    pos[39] = (pos[27][0]-2, pos[27][1]-2)
    labels[39] = "Communication\nCircuits"
    electronicBasicLesson.append(39)
    
    G.add_edge(24, 40, weight=0.6)
    pos[40] = (pos[24][0]-2, pos[24][1])
    labels[40] = "Electronic 3"
    electronicBasicLesson.append(40)
    
    G.add_edge(30, 41, weight=0.6)
    pos[41] = (pos[30][0]-1, pos[30][1])
    labels[41] = "Microprocessor\nSystems Design"
    electronicBasicLesson.append(41)
    
    G.add_edge(23, 42, weight=0.3)
    pos[42] = (pos[23][0]-1, pos[23][1]-6)
    labels[42] = "Pulse and\nCurrent Circuits"
    electronicBasicLesson.append(42)
    
    G.add_edge(23, 43, weight=0.3)
    pos[43] = (pos[23][0]-1, pos[23][1]-8)
    labels[43] = "Electronic\nPhysics"
    electronicBasicLesson.append(43)
    
    G.add_edge(40, 44, weight=0.3)
    pos[44] = (pos[40][0]-1, pos[40][1])
    labels[44] = "Electronic 3 Lab"
    labs.append(44)
    
    G.add_edge(42, 45, weight=0.3)
    G.add_edge(33, 45, weight=0.6)
    pos[45] = (pos[42][0]-3, pos[42][1])
    labels[45] = "Pulse and Current\nCircuits Lab"
    labs.append(45)
    
    G.add_edge(39, 46, weight=0.3)
    pos[46] = (pos[39][0]-1, pos[39][1])
    labels[46] = "Communication\nCircuits Lab"
    labs.append(46)
    
    # -------------------
    G.add_edge(24, 48, weight=0.6)
    G.add_edge(26, 48, weight=0.3)
    pos[48] = (pos[24][0]-2, pos[24][1]-9)
    labels[48] = "Industrial\nElectronics"
    electronicMainLesson.append(48)
    
    G.add_edge(48, 47, weight=0.3)
    pos[47] = (pos[48][0]-1, pos[48][1])
    labels[47] = "Industrial\nElectronics Lab"
    labs.append(47)
    
    
    G.add_edge(21, 49, weight=0.6)
    G.add_edge(24, 49, weight=0.6)
    pos[49] = (pos[21][0]-3, pos[21][1]-6)
    labels[49] = "Filters and\nSynthesis"
    electronicMainLesson.append(49)
    
    G.add_edge(27, 50, weight=0.6)
    pos[50] = (pos[27][0]-2, pos[27][1]+3)
    labels[50] = "Telecommunication\nNetworks"
    electronicMainLesson.append(50)
    
    G.add_edge(24, 51, weight=0.6)
    pos[51] = (pos[24][0]-2, pos[24][1]-2)
    labels[51] = "Integrative\nCircuits CMOS"
    electronicMainLesson.append(51)
    
    G.add_edge(21, 52, weight=0.6)
    pos[52] = (pos[21][0]-3, pos[21][1]-3)
    labels[52] = "Digital Signal\nProcessing"
    electronicMainLesson.append(52)
    
    G.add_edge(30, 53, weight=0.6)
    pos[53] = (pos[30][0]-2, pos[30][1])
    labels[53] = "Digital\nSystems Design"
    electronicMainLesson.append(53)
    
    G.add_edge(3, 54, weight=0.6)
    G.add_edge(16, 54, weight=0.6)
    pos[54] = (pos[16][0]-1, pos[16][1]-4)
    labels[54] = "Modern\nPhysics"
    electronicMainLesson.append(54)
    
    # -----------------
    # G.add_nodes_from([37, 38])
    # pos[37], pos[38] = (pos[12][0], pos[12][1]-3), (pos[12][0]-1, pos[12][1]-3)
    # labels[37], labels[38] = "Bachelor Project", "Internship"
    
    # G.add_edge(27, 39, weight=0.6)
    # G.add_edge(24, 39, weight=0.6)
    # pos[39] = (pos[27][0]-2, pos[27][1]-2)
    # labels[39] = "Communication\nCircuits"
    telecommBasicLesson.append(39)
    
    G.add_edge(20, 57, weight=0.6)
    pos[57] = (pos[20][0]-1, pos[20][1]+8)
    labels[57] = "Fields\nand Waves"
    telecommBasicLesson.append(57)
    
    G.add_edge(57, 56, weight=0.6)
    pos[56] = (pos[57][0]-1, pos[57][1])
    labels[56] = "Microwave\nand Antenna"
    telecommBasicLesson.append(56)
    
    G.add_edge(27, 58, weight=0.6)
    pos[58] = (pos[27][0]-2, pos[27][1]+6)
    labels[58] = "Digital\nTelecommunications"
    telecommBasicLesson.append(58)
    
    # G.add_edge(21, 52, weight=0.6)
    # pos[52] = (pos[21][0]-3, pos[21][1]-3)
    # labels[52] = "Digital Signal\nProcessing"
    telecommBasicLesson.append(52)
    
    G.add_edge(58, 60, weight=0.3)
    pos[60] = (pos[58][0]-1, pos[58][1]+1)
    labels[60] = "Digital\nTelecommunications Lab"
    labs.append(60)
    
    # G.add_edge(39, 46, weight=0.3)
    # pos[46] = (pos[39][0]-1, pos[39][1])
    # labels[46] = "Communication\nCircuits Lab"
    # labs.append(46)
    
    G.add_edge(52, 62, weight=0.3)
    pos[62] = (pos[52][0]-1, pos[52][1])
    labels[62] = "Digital Signal\nProcessing Lab"
    labs.append(62)
    
    G.add_edge(56, 63, weight=0.3)
    pos[63] = (pos[56][0]-1, pos[56][1])
    labels[63] = "Microwave and\nAntenna Lab"
    labs.append(63)
    
    # -----------------
    # G.add_edge(21, 49, weight=0.6)
    # G.add_edge(24, 49, weight=0.6)
    # pos[49] = (pos[21][0]-3, pos[21][1]-6)
    # labels[49] = "Filters and\nSynthesis"
    telecommMainLesson.append(49)
    
    # G.add_edge(27, 50, weight=0.6)
    # pos[50] = (pos[27][0]-2, pos[27][1]+3)
    # labels[50] = "Telecommunication\nNetworks"
    telecommMainLesson.append(50)
    
    G.add_edge(24, 64, weight=0.6)
    pos[64] = (pos[24][0]-2, pos[24][1]+3)
    labels[64] = "Analog\nElectronic"
    telecommMainLesson.append(64)
    
    G.add_edge(27, 65, weight=0.6)
    G.add_edge(57, 65, weight=0.6)
    pos[65] = (pos[57][0]-4, pos[57][1]+5)
    labels[65] = "Otpical\nTelecommunication Systems"
    telecommMainLesson.append(65)
    
    G.add_edge(27, 66, weight=0.6)
    pos[66] = (pos[27][0]-2, pos[27][1]+1)
    labels[66] = "Wireless\nTelecommunications"
    telecommMainLesson.append(66)
    
    G.add_edge(7, 67, weight=0.6)
    pos[67] = (pos[7][0]-1, pos[7][1]-2)
    labels[67] = "Advanced\nProgramming"
    telecommMainLesson.append(67)
    
    G.add_edge(1, 68, weight=0.6)
    pos[68] = (pos[1][0]-1, pos[1][1]+12)
    labels[68] = "Linear\nAlgebra"
    telecommMainLesson.append(68)
    # -----------------
    check(pos)
    
    plt.figure(figsize=(22, 8))
    
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]
    
    nx.draw_networkx_nodes(G, pos, nodelist=labs, node_color="#00d9ff", node_size=200)
    nx.draw_networkx_nodes(G, pos, nodelist=basicLesson, node_color="#d54f4f", node_size=400)
    nx.draw_networkx_nodes(G, pos, nodelist=mainLesson, node_color="#ff0000", node_size=400)
    nx.draw_networkx_nodes(G, pos, nodelist=telecommBasicLesson, node_color="#ffff00", node_size=400)
    nx.draw_networkx_nodes(G, pos, nodelist=telecommMainLesson, node_color="#ff9500", node_size=400)
    nx.draw_networkx_nodes(G, pos, nodelist=electronicBasicLesson, node_color="#ff00ff", node_size=400)
    nx.draw_networkx_nodes(G, pos, nodelist=electronicMainLesson, node_color="#b22eff", node_size=400)
    
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=1, alpha=0.75, edge_color="#ff2525", arrowsize=15, node_size=400)
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=1, alpha=0.5, edge_color="blue", style="dashed", arrowsize=15, node_size=400
    )
    
    nx.draw_networkx_labels(G, pos, labels, font_size=6, font_family="sans-serif")
    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("graph-v2.1.2.png")
    plt.show()


if __name__ == "__main__":
    main()
