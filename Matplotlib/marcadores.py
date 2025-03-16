"""
Marcadores
Você pode usar o argumento de palavra-chave marker para enfatizar cada ponto com um marcador especificado:
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

"""
Referência do marcador
Você pode escolher qualquer um destes marcadores:

Marker	Description
'o'	Circle	
'*'	Star	
'.'	Point	
','	Pixel	
'x'	X	
'X'	X (filled)	
'+'	Plus	
'P'	Plus (filled)	
's'	Square	
'D'	Diamond	
'd'	Diamond (thin)	
'p'	Pentagon	
'H'	Hexagon	
'h'	Hexagon	
'v'	Triangle Down	
'^'	Triangle Up	
'<'	Triangle Left	
'>'	Triangle Right	
'1'	Tri Down	
'2'	Tri Up	
'3'	Tri Left	
'4'	Tri Right	
'|'	Vline	
'_'	Hline
"""



"""
Formatar sequências de caracteresfmt
Você também pode usar o parâmetro de notação de string de atalho para especificar o marcador.
Este parâmetro também é chamado fmte é escrito com esta sintaxe:

marker|line|color
"""
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o:r')
plt.show()


"""
Line Syntax	Description
'-'	    Solid line	
':'	    Dotted line	
'--'	Dashed line	
'-.'	Dashed/dotted line
"""




"""
Referência de cor
Color Syntax	Description
'r'	            Red	
'g'	            Green	
'b'          	Blue	
'c'         	Cyan	
'm'	            Magenta	
'y'	            Yellow	
'k'	            Black	
'w'	            White
"""



"""
Tamanho do marcador
Você pode usar o argumento de palavra-chave markersizeou a versão mais curta ms para definir o tamanho dos marcadores:
"""
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()



"""
Cor do marcador
Você pode usar o argumento de palavra-chave markeredgecolorou o shorter mec para definir a cor da borda dos marcadores:
"""
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()



"""
Você pode usar o argumento de palavra-chave markerfacecolorou o shorter mfcpara definir a cor dentro da borda dos marcadores:
"""
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()