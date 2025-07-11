VP = 70
VN = 50
FP = 10
FN = 20

# Cálculo das métricas
acuracia = (VP + VN) / (VP + VN + FP + FN)
precisao = VP / (VP + FP)
recall = VP / (VP + FN)
especificidade = VN / (VN + FP)
f_score = 2 * (precisao * recall) / (precisao + recall)

# Exibição dos resultados
print(f"Acurácia: {acuracia:.2f}")
print(f"Precisão: {precisao:.2f}")
print(f"Recall (Sensibilidade): {recall:.2f}")
print(f"Especificidade: {especificidade:.2f}")
print(f"F-score: {f_score:.2f}")